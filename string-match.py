'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
string_match('he', 'hello') → 1
string_match('iaxxai', 'aaxxaaxx') → 3
'''


def string_match(a, b):
    count = 0
    # to check the smaller string
    if len(a) < len(b):
        # to iterate till second last char of string
        for i in range(len(a) - 1):
            # matching
            if a[i] == b[i] and a[i+1] == b[i+1]:
                count += 1
        return count
    else:
        for i in range(len(b) - 1):
            if a[i] == b[i] and a[i+1] == b[i+1]:
                count += 1
        return count
