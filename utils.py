import json


def export_price() -> int:
    with open("price.json", "r") as file:
        data = json.load(file)
        return int(data)
