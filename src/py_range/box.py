import signal
import sys

from python_on_whales import docker

from .utils import random_name


class box:
    def __init__(
        self, 
        name: str = "",
        image: str = "alpine", 
        command: str = "sleep infinity",
        ports: list[int] = [],
        start: bool = True,
    ):
        self.image = image
        self.command = command.split()
        self.name = name if name else random_name()
        self.ports = ports
        self.container = None

        if start:
            self.start()

    @classmethod
    def attach(cls, name:str):
        names = [c.name for c in docker.container.list()]
        if name not in names:
            raise Exception(f"Could not find container '{name}'")
        box = cls(name=name, start=False)
        box.container = docker.container.inspect(name)
        return box

    def start(self):
        # restarts
        if self.container:
            self.container.remove(force=True)
        
        # start afresh
        self.container = docker.run(
            self.image, 
            self.command, 
            detach=True, 
            name=self.name, 
            remove=False,
        )

    def ready(self) -> bool:
        """Check if container is running and can accept commands"""
        if not self.container:
            return False
        info = docker.container.inspect(self.container.name)
        return info.state.running

    def run(
        self,
        command: str,
        path: str = "/",
        interactive: bool = False,
        timeout: int = -1,
    ) -> str:
        """Returns the output from running a given command"""
        cmd = command.split()

        if interactive:
            return docker.execute(
                self.container,
                cmd,
                interactive=interactive,
                tty=sys.stdin.isatty(),
                workdir=path,
            )
        
        # non-interactive
        if timeout > 0:
            def handler(signum, frame):
                raise TimeoutError(f"Command timed out after {timeout}s")

            old_handler = signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)
            try:
                result = docker.execute(self.container, cmd, workdir=path)
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
        else:
            result = docker.execute(self.container, cmd, workdir=path)
        return result


    def ps(self):
        """Return the processes currently running on the box"""
        return self.run("ps aux")

    def put(self, source: str, destination: str):
        """Place a file from local source to destination in the box"""
        docker.copy(source, (self.container.name, destination))

    def get(self, source: str, destination: str):
        """Retrieve a file from inside the box to a local destination"""
        docker.copy((self.container.name, source), destination)

    def dir(self, path: str = "/", recurse: bool = False) -> list[str]:
        """List the contents at path"""
        results = self.run(f"{'find' if recurse else 'ls'} {path}")
        return results.split("\n")
        
    def __del__(self):
        if self.container:
            self.container.remove(force=True)

    # [name for name in self.container.network_settings.networks][:-1]