from python_on_whales import DockerClient, docker
from python_on_whales.client_config import ClientNotFoundError
import uuid

# Agnostic client
try:
    _client = DockerClient(client_call=["docker"])
except ClientNotFoundError:
    _client = DockerClient(client_call=["podman"])

class box:
    def __init__(self):
        self.container = None
        self._ports = set()

    def open(self, port: int | list[int]):
        '''Open given port(s)'''
        if not self.container:
            raise ValueError("No container; use box.docker()")
        ports = [port] if isinstance(port, int) else port
        self._ports.update(ports)
        # Dynamic bind requires restart; tracked for now

    def close(self, port: int | list[int]):
        '''Close given port(s)'''
        if not self.container:
            raise ValueError("No container; use box.docker()")
        ports = [port] if isinstance(port, int) else port
        self._ports.difference_update(ports)
        # Dynamic unbind requires restart; tracked for now

    def ports(self) -> list[int]:
        '''Return the currently open ports on the box (query Docker live)'''
        raise NotImplemenetedError

    def run(self, command: str, path: str = '/', background: bool = False) -> str:
        '''Returns the output from running a given command'''
        return self.container(
            command = command,
            detach = True if background else False,
            workdir = path,
        )

    def ps(self):
        '''Return the processes currently running on the box'''
        return self.run("ps aux")

    def put(self, source: str, destination: str):
        '''Place a local file from source to destination in the box'''
        docker.copy(source, (self.container.name, destination))

    def get(self, source: str, destination: str):
        '''Retrieve a file from inside the box to a local destination'''
        docker.copy((self.container.name, source), destination)
        
    def dir(self, path: str = '/', recurse: bool = False) -> list[str]:
        '''List the contents at path'''
        if not self.container:
            raise ValueError("No container; use box.docker()")
        cmd = "find" if recurse else "ls"
        cmd_args = [cmd, path]
        res = docker.container.exec(self.container.name, *cmd_args)
        return [line.strip() for line in res.stdout.decode().splitlines() if line.strip()]
        
    @classmethod
    def docker(cls, image: str):
        '''Create a box from a named docker image'''
        instance = cls()
        name = f"box-{uuid.uuid4().hex[:8]}"
        instance.container = _client.run(image, detach=True, name=name, remove=False)
        return instance

    @classmethod
    def dockerfile(cls, filepath: str):
        '''Create a box from a local dockerfile'''
        instance = cls()
        name = f"box-{uuid.uuid4().hex[:8]}"
        context = '/'.join(filepath.split('/')[:-1]) or '.'
        build_res = _client.build(path=context, dockerfile=filepath)
        image_id = build_res.id
        instance.container = _client.run(image_id, detach=True, name=name, remove=False)
        return instance

    def __del__(self):
        raise self.container.remove()
