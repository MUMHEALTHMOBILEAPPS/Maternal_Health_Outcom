import re


def is_found(txt, pattern):
    if re.match(pattern, txt) is not None:
        return 1
    else:
        return 0


def remove_special_chars(txt):
    special_chars = '(){}\n\'.'
    return ''.join(c for c in txt if c not in special_chars)

