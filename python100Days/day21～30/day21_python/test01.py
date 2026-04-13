import json
if __name__ == '__main__':
    my_dict = {
        'name': '段世超',
        'age': 40,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BMW', 'max_speed': 240},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 280}
        ]
    }
    print(json.dumps(my_dict))