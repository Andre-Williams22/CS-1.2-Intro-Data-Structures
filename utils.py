import time
import re

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 1000) + ' ms')
        return result

    return wrapper


def good_words(source_file):
    """
    Takes text file as a paramater and returns a list of all the words with all characters except for A-Z removed
    Keeps spaces and newline characters
    Params:
        source_file: file - A .txt file to read words from
    Returns:
        List of words from a text file
    Raises:
        File Not Found if source file does not exist
    """

    with open(source_file, 'r') as f:
        words_file = f.read().lower()
        clean_words = re.sub(r'[^a-zA-Z\s]', '', words_file)
        return clean_words.split()