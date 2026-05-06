from python_on_whales import docker

from .utils import random_name
from .box import box

class segment:
    def __init__(
        self,
        name: str = "",
    ):
        self.name = name if name else random_name()

        if docker.network.exists(self.name):
            self.network = docker.network.inspect(self.name)
        else:
            self.network = docker.network.create(self.name)            

    def add(self, *box: box):
        for b in box:
            if not b.ready():
                raise Exception(f"box '{b.name}' is not ready")
            docker.network.connect(self.network, b.name)

    def __iadd__(self, box: box):
        self.add(box)
        return self

    def containers(self) -> list[box]:
        containers = self.network.containers
        names = [containers[c].name for c in containers]
        boxes = [box(name) for name in names]
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Segment('{self.name}')"