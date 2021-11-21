from Data_Structure.repeated_word.repeated_word import repeated_word

def test_repeated_words():

    actual = repeated_word("Once upon a time, I used to have a good sleep...")
    excpected = "a"
    assert actual == excpected
