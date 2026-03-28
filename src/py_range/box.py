class box:
    def open(self, port: int | list[int]):
        '''Open given port(s)'''
        raise NotImplementedError

    def close(self, port: int | list[int]):
        '''Close given port(s)'''
        raise NotImplementedError

    def ports(self) -> list[int]:
        '''Return the currently open ports on the box (query Docker live)'''
        raise NotImplementedError

    def ps(self):
        '''Return the processes currently running on the box'''
        raise NotImplementedError

    def put(self, source: str, destination: str):
        '''Place a local file from source to destination in the box'''
        raise NotImplementedError
        
    def dir(self, path: str = '/', recurse: bool = False) -> list[str]:
        '''List the contents at path'''
        raise NotImplementedError
        
    def run(self, command: str, background: bool = False) -> str:
        '''Returns the output from running a given command'''
        raise NotImplementedError

    @classmethod
    def docker(cls, image: str):
        '''Create a box from a named docker image'''
        raise NotImplementedError

    @classmethod
    def dockerfile(cls, filepath: str):
        '''Create a box from a local dockerfile'''
        raise NotImplementedError
