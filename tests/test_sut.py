from actions.sut import StringParser


def test_find_uppercase_word():
    parser = StringParser()
    counter = parser.count_uppercase_words("ABC")
    assert counter == 1


def test_find_multiple_uppercase_words():
    parser = StringParser()
    counter = parser.count_uppercase_words("ABC DEF")
    assert counter == 2


def test_not_find_uppercase_word():
    parser = StringParser()
    counter = parser.count_uppercase_words("abc")
    assert counter == 0