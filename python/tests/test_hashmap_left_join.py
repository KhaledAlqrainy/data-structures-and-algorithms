from code_challenges.hashmap_left_join.hashmap_left_join import hashmap_left_join

def test_left_join():
    actual = hashmap_left_join(
        key={
        'first': 'Forza',
        'second': 'Amunt',
        'third': 'Go',
        'fourth': 'viva',
    }, key2={
        'first': 'Milan',
        'second': 'Valencia',
        'third': 'Hilal',
        'seven': 'algeria',
    })
    excepted = [['first', 'Forza', 'Milan'], ['second', 'Amunt', 'Valencia'], ['third', 'Go', 'Hilal'], ['fourth', 'viva', 'None']]
    assert actual == excepted