from general import list_of_chars_to_string

def get_lowercase_alphabet():

    alphabet = [chr(ascii_num) for ascii_num in range(ord('a'), ord('z') + 1)]
    return list_of_chars_to_string(alphabet)

