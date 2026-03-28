class box:
    def open(self, port:int):
        """Open a given port"""
        raise NotImplementedError
    def close(self, port:int):
        """Close a given port"""
        raise NotImplementedError
    def put(self, source:str, destination:str):
        """Load a local file (source) into the box (at destination)"""
        raise NotImplementedError
    def dir(self, path:str="/", recurse:bool=False):
        """List the box's file contents, with root as the default file path, recursively only if specified"""
        raise NotImplementedError
    def run(self, command:str, path:str="/"):
        """Run a command on the box, from the root path by default"""
        raise NotImplementedError
    @classmethod
    def docker(cls, image:str):
        """Create a box from a named docker image"""
        raise NotImplementedError
    @classmethod
    def dockerfile(cls, filepath:str):
        """Create a box from a local dockerfile"""
        raise NotImplementedError
