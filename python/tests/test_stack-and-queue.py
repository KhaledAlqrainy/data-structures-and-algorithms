from stack_and_queue.stack_and_queue import Node,Stack,Queue
import pytest


stack=Stack()

def test_push_stack():
    stack.push('5')
    actual = stack.top.data
    expect = '5'
    assert actual == expect


def test_push_multiple_values():
    stack.push('Milano')
    actual = stack.__str__()
    expect = 'Milano\n5'
    assert actual == expect

def test_pop_stack():
    assert stack.pop() == 'Milano'
    actual = stack.__str__()
    expect = '5'
    assert actual == expect

def test_empty_multiple_pops():
    stack.push('khaled')
    stack.push('qrainy')
    assert stack.__str__() == 'qrainy\nkhaled\n5'
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.__str__() == ''

def test_peek():
    stack.push('khaled')
    stack.push('qrainy')
    assert stack.peek() == 'qrainy'

def test_instantiate_empty_stack():
    stack2 = Stack()
    assert stack2.__str__() == ''

def test_pop_and_peek_empty_stack():
    stack3 = Stack()
    assert stack3.pop() == 'Stack is Empty'
    assert stack3.peek() == 'Stack is Empty'

########## QUEUE ########

queue = Queue()

def test_enqueue_queue():
    queue.enqueue('khaled')
    assert queue.__str__() == 'khaled'

def test_enqueue_multiple_values():
    queue.enqueue('qrainy')
    assert queue.__str__() == 'khaled\nqrainy'

def test_dequeue_queue():

    assert queue.dequeue() == 'khaled'
    assert queue.__str__() == 'qrainy'

def test_peek_queue():
    queue.enqueue('khaled')
    queue.enqueue('f')
    queue.enqueue('r')

    assert queue.peek() == ('qrainy')

def test_empty_multiple_dequeue():
    assert queue.__str__() == 'qrainy\nkhaled\nf\nr'
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    assert queue.__str__() == ''

def test_instantiate_empty_queue():
    queue2 = Queue()
    assert queue2.__str__() == ''

def test_peek_empty_queue():
    empty_queue = Queue()
    assert empty_queue.__str__() == ''
    assert empty_queue.peek() == 'Queue is Empty'