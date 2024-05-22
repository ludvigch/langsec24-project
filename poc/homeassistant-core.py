class Employee:
    def __init__(self) -> None:
        name = "default"


from collections.abc import Mapping
# core/homeassistant/components/google_assistant/helpers.py
def deep_update(target, source):
    """Update a nested dictionary with another nested dictionary."""
    for key, value in source.items():
        if isinstance(value, Mapping):
            target[key] = deep_update(target.get(key, {}), value)
        else:
            target[key] = value
    return target

a = {'a': 1, 'b': 2}
b = {'__init__': 3, 'd': 4}

print(a['values()'])
test = dict()
print(test)