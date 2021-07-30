# increments some_property by 1
from contextlib import contextmanager


@contextmanager
def simple_content_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1


class Some_obj(object):
    def __init__(self, arg):
        self.some_property = arg


obj = Some_obj(5)
print(obj.some_property)

with simple_content_manager(obj):
    print(obj.some_property)

print(obj.some_property)

