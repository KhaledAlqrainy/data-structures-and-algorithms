import pytest

from linked_list.linked_list import Node,LinkedList


###########
def test_new_linked_list_is_empty():
  expected = None
  ll = LinkedList()
  actual = ll.head
  assert actual == expected

def test_linked_list_insert():
  expected = 1
  ll = LinkedList()
  actual = ll.insert(2)
  assert actual == expected

def test_first_node():
    expected = "last"
    ll = LinkedList()
    ll.insert("first")
    ll.insert("last")
    actual = ll.head.value

    assert actual == expected

def test_linked_list_insert_multiple_nodes():
  expected = 3
  ll = LinkedList()
  first_node=ll.insert(1)
  second_node=ll.insert(2)
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
    expected = "{ b } -> { c } -> NULL"
    ll = LinkedList()
    ll.insert("c")
    ll.insert("b")
    actual= ll.to_string()
    assert actual == expected