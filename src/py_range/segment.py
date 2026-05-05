from python_on_whales import docker
from .utils import random_name
from .box import box

class segment:
    def __init__(
        self,
        name: str = "",
    ):
        self.name = name if name else random_name()

        if not docker.network.exists(name):
            self.network = docker.network.create(self.name)
        else:
            # TODO - this is gross logic
            self.network = docker.network.inspect(name)

    @classmethod
    def attach(cls, name:str):
        if not docker.network.exists(name):
            raise Exception(f"Could not find network '{name}'")
        return cls(name)

    def add(self, box: box):
        if not box.ready():
            raise Exception(f"box '{box.name}' is not ready")
        docker.network.connect(self.network, box.name)

    def __iadd__(self, box: box):
        self.add(box)
        return self

    def containers(self) -> box:
        containers = self.network.containers
        names = [containers[c].name for c in containers]
        boxes = [box.attach(name) for name in names]
        return boxes

    def __iter__(self):
        return iter(self.containers())

    def __len__(self):
        return len(self.containers())
    
    def __getitem__(self, key):
        return self.containers()[key]
    
    def __reversed__(self):
        return reversed(self.containers())

    def remove(self, box: box, force: bool = True):
        docker.network.disconnect(self.network, box.name, force=force)

    def __isub__(self, box: box):
        self.remove(box)
        return self

    def __del__(self):
        self.network.remove()