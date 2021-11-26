def capitalize_title(title):
    """
    Change a string to title-case.

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)

    Function that takes a string (title) as an argument and returns that same
    string in title case.
    """

    return title.title()


def check_sentence_ending(sentence):
    """
    Check if string ends in a period.

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.

    Function that takes a string (sentence) as an argument and returns a bool
    verifying whether or not that string ends in a period.
    """
    if sentence[-1] == ".":
        return True
    return False


def clean_up_spacing(sentence):
    """
    Strips leading and trailing whitespace.

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.

    Function that takes a string (sentence) as an argument and returns a string
    with any trailing and leading whitespace removed.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """
    Replaces any occurence of a given word with its given synonym.

    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words

    Function that takes three strings (sentence, old_word, new_word) as
    arguments and replaces every instance of old_word within sentence with
    new_word.
    """

    return sentence.replace(old_word, new_word)
