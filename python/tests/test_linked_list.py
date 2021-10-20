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

def test_insert_after_middle():
    
    expected = "{0}->{2}->{4}->{6}->NULL"
    ll = LinkedList()
    ll.append(0)
    ll.append(2)
    ll.insert_after(2,3)
    ll.append(6)
    actual = ll.to_string()
    assert actual == expected

def test_insert_after_last():
    
    expected = "{0}->{2}->{4}->NULL"
    ll = LinkedList()
    ll.insert(2)
    ll.insert(0)
    ll.append(4)
    actual = ll.to_string()
    assert actual == expected

