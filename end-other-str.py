'''
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
end_other('abcXYZ', 'abcDEF') → False
end_other('Hiabc', 'abcd') → False
'''


def end_other(a, b):
    # checking the small string out of both
    if len(a) > len(b):
        # using endwith() function to check condition
        return a.lower().endswith(b.lower())
    return b.lower().endswith(a.lower())
