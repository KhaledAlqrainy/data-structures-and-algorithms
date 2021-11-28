from code_challenges.repeated_word.repeated_word import repeated_word

def test_repeated_words():

    actual = repeated_word("Once upon a time, I used to have a good sleep...")
    excpected = "a"
    assert actual == excpected

def test_repeated_words1():

    actual = repeated_word("Amunt Valencia always, Amunt forever...")
    excpected = "amunt"
    assert actual == excpected

def test_repeated_words2():

    actual = repeated_word("Life was very good before coding, coding sucks...")
    excpected = "coding"
    assert actual == excpected

def test_repeated_words2():

    actual = repeated_word("Life was very good before coding, coding sucks...")
    excpected = "coding"
    assert actual == excpected

