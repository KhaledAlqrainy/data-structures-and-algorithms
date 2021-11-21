from Data_Structure.hashTable.hashmap import HashTable
import pytest

@pytest.fixture
def hashtable():
    
	return HashTable()

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected

def test_add(hashtable):

    expected = "Milan"
    hashtable.add("Forza","Milan")
    actual = hashtable.get("Forza")
    assert actual == expected

def test_not_exist_key(hashtable):

    expected = None
    actual = hashtable.get("anything")
    assert actual == expected

def test_collision(hashtable):

    expected = "ilrossoneri"
    hashtable.add("Forza","Milan")
    hashtable.add("Forza","ilrossoneri")
    actual = hashtable.get("Forza")
    assert actual == expected
