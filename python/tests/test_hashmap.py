from linked_list.hashmap import HashTable
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

    hashtable.add('Forza','Milan')
    assert hashtable.contains('Forza')


