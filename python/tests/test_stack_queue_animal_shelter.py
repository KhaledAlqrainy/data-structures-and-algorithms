from stack_and_queue.stack_queue_animal_shelter import Cat,Dog,Animalshelter


def test_enqueue():

    animal = Animalshelter()
    animal.enqueue(Dog('Spaiky'))
    animal.enqueue(Cat('Luca'))
    animal.enqueue(Cat('Rich'))
    animal.enqueue(Dog('Luca'))

    assert animal.first.data == 'Spaiky'
    assert animal.first.next.data == 'Luca'
    assert animal.first.next.next.data=='Rich'
    assert animal.first.next.next.next.data=='Luca'

def test_dequeue_cat():

    animal = Animalshelter()
    animal.enqueue(Cat('Spaiky'))
    animal.enqueue(Dog('Luca'))

    assert animal.dequeue('cat')== None

def test_dequeue_dog():

    animal = Animalshelter()
    animal.enqueue(Cat('Rich'))
    animal.enqueue(Dog('Luca'))
    animal.enqueue(Dog('Luca2'))

    assert animal.dequeue('dog')== None


