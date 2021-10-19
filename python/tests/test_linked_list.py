import pytest

from linked_list.linked_list import Node,LinkedList



def test_new_linked_list_is_empty():
  expected = None
  ll = LinkedList()
  actual = ll.head
  assert actual == expected

def test_linked_list_insert():
  expected = 1
  ll = LinkedList()
  ll.insert(1)
  actual = ll.head.data
  assert actual == expected

def test_first_node():
    expected = "last"
    ll = LinkedList()
    ll.insert("first")
    ll.insert("last")
    actual = ll.head.data

    assert actual == expected

def test_linked_list_insert_multiple_nodes():
  expected = None
  ll = LinkedList()
  ll.insert(0)
  ll.insert(1)
  first_node=ll.insert(0)
  second_node=ll.insert(1)
  actual = first_node and second_node
  assert actual == expected

def test_linked_have_value():
    expected = True

    ll = LinkedList()
    ll.insert(1)
    actual = ll.includes(1)

    assert actual == expected

def test_linked_have_not_value():
    expected = False

    ll = LinkedList()
    ll.insert(2)
    actual = ll.includes(3)

    assert actual == expected

def test_to_string():
    expected = '{0}->{2}->NULL'
    ll = LinkedList()
    ll.insert(2)
    ll.insert(0)
    actual= ll.to_string()
    assert actual == expected

########## 06 ##########
def test_append_one_node():

    expected ="{0}->{2}->NULL"
    ll = LinkedList()
    ll.insert(0)
    ll.append(2)
    actual= ll.to_string()
    assert actual == expected

def test_append_multiple_nodes():

  expected ="{0}->{2}->{4}->NULL"
  ll = LinkedList()
  ll.insert(0)
  ll.append(2)
  ll.append(4)
  actual= ll.to_string()
  assert actual == expected

def test_insert_before_middle_node():
  expected ="{0}->{2}->{4}->NULL"
  ll = LinkedList()
  ll.insert(4)
  ll.insert(0)
  ll.insert_before(4,2)
  actual= ll.to_string()
  assert actual == expected

def test_insert_before_first_node():
  expected ="{0}->{2}->{4}->NULL"
  ll = LinkedList()
  ll.insert(4)
  ll.insert(0)
  ll.insert_before(4,2)
  actual= ll.to_string()
  assert actual == expected

# def test_insert_after_middle():
    
#     expected = "{0}->{2}->{4}->{6}->NULL"
#     ll = LinkedList()
#     ll.append(0)
#     ll.append(2)
#     ll.insert_after(2,3)
#     ll.append(6)
#     actual = ll.to_string()
#     assert actual == expected

def test_insert_after_last():
    
    expected = "{0}->{2}->{4}->NULL"
    ll = LinkedList()
    ll.insert(2)
    ll.insert(0)
    ll.append(4)
    actual = ll.to_string()
    assert actual == expected

############# 07 ############

def test_k_larger():

    expected = 'k is larger than the list range'
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.append(7)
    actual = ll.kth_from_end(5)
    assert actual == expected

def test_k_equal_list_length():

    expected = 'k and the list have the same length'
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.append(7)
    actual = ll.kth_from_end(3)
    assert actual == expected

def test_k_negative():

    expected = 'k is a negative number'
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.append(7)
    actual = ll.kth_from_end(-5)
    assert actual == expected

def test_k_size_1():

    expected = 0
    ll = LinkedList()
    ll.insert(0)
    actual = ll.kth_from_end(0)
    assert actual == expected

def test_k_middle():

    expected = 2
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    actual = ll.kth_from_end(2)
    assert actual == expected

########## 08 ###########


def test_list_empty():

    excepted="{ 5 } -> { 3 } -> { 2 } -> NULL"
    ll_1=LinkedList()
    ll_2 =LinkedList()
    ll_1.insert(5)
    ll_1.insert(3)
    ll_1.insert(2)
    actual = ll_1.zipLists(ll_1)
    
    assert excepted==actual