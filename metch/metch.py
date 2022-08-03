class List(list):
    def __init__(self, data):
        super().__init__(data)

    def map(self, fn):
        return List(*(fn(x) for x in self))

    def filter(self, fn):
        return List(*(x for x in self if fn(x)))

    def dict(self):
        return Dict(self)

    def seq(self):
        return Seq(self)


class Seq:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def list(self):
        return List(self)

    def map(self, fn):
        return Seq(*(fn(x) for x in self))

    def filter(self, fn):
        return Seq(*(x for x in self if fn(x)))


class Dict(dict):
    def __init__(self, data):
        super().__init__(data)

    def keys(self):
        return Seq(self.keys())

    def values(self):
        return Seq(self.values())

    def items(self):
        return Seq(self.items())

def mlist(*args):
    return List(args)

def seq(*args):
    return Seq(args)

def mdict(**kwargs):
    return Dict(kwargs)
