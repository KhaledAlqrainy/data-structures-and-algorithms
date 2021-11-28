from Data_Structure.hashTable.hashmap import *
# from linked_list.hashTable import __version__
import pytest

@pytest.fixture
def hashtable():
    test_hash = HashTable()
    test_hash.add('yahya', '23')
    test_hash.add('there', 95)
    test_hash.add('there', 127)
    return test_hash

def test_hash(hashtable):
    assert hashtable.__buckets[hashtable.__hash('yahya')].head.value == '23'
    assert hashtable.__hash('united') == 389


def test_add(hashtable):
    assert hashtable.add('go','play football')
    assert hashtable.__buckets[hashtable.__hash('go')].head.value == 'play football'

def test_contains(hashtable):
    assert hashtable.contains('yahya') == True
    assert hashtable.contains('anything') == False

def test_get(hashtable):
    assert hashtable.get('yahya') == '23'

def test_collision(hashtable):
    assert hashtable.__buckets[hashtable.__hash('there')].head.value == 127
    assert hashtable.__buckets[hashtable.__hash('there')].head.next.value == 95
    assert hashtable.get('there') == 127
