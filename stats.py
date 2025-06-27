def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def num_char(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def get_count(dictionary):
    return dictionary["num"]

def sorted_char(char_count):
    result = []
    for key, value in char_count.items():
        result.append({"char": key, "num": value})
    result.sort(reverse=True, key=get_count)
    return result 