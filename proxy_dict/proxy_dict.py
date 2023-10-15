from collections import UserDict
from collections.abc import Mapping


class ProxyDict(UserDict):
    def __init__(self, source_dict: dict):
        if not isinstance(source_dict, dict):
            raise TypeError
        super().__init__()
        self.data = source_dict

    def __setitem__(self, key, value):
        raise TypeError

    def __delitem__(self, key):
        raise TypeError

    def __eq__(self, other):
        # return id(self) == id(other)
        if not isinstance(other, list):
            return False
        if not isinstance(other, Mapping):
            raise TypeError
        return self.items() == other.items()

    def __repr__(self):
        return f"ProxyDict({self.data})"


if __name__ == "__main__":
    user_data = {"name": "Trey Hunner", "active": False}
    proxy_data = ProxyDict(user_data)
    print(f"proxy_data: {proxy_data}")
    user_data["active"] = True
    print(f"proxy_data: {proxy_data}")
    assert proxy_data["active"] is True

    assert len(proxy_data) == 2
    print(f"len(proxy_data): {len(proxy_data)}")
    print(f"proxy_data.items(): {proxy_data.items()}")
    print(f"proxy_data.keys(): {proxy_data.keys()}")
    # dict_items([('name', 'Trey Hunner'), ('active', False)])
    print(f"proxy_data.values(): {proxy_data.values()}")
    # dict_values(['Trey Hunner', False])
    assert proxy_data.get("name") == "Trey Hunner"
    assert proxy_data.get("shoe_size", 0) == 0

    for key in proxy_data:
        print(key)

    print(proxy_data)

    p1 = ProxyDict(user_data)
    p2 = ProxyDict(user_data.copy())
    print(f"p1 == p2: {p1 == p2}")
    print(f"p2 == user_data: {p2 == user_data}")
    print(f"id(user_data): {id(user_data)}")
    print(f"id(p1): {id(p1)}")
    print(f"id(p2): {id(p2)}")
    print(f"user_data: {user_data}")
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    assert p1 == p2
    assert p2 == user_data
