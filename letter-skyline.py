'''
SKYLINE: Given a string and return a matching string matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.


to_skyline('Anthropomorphism') -> aNtHrOpOmOrPhIsM
                                       or
                                  AnThRoPoMoRpHiSm

'''


def to_skyline(s):
    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(s[i].upper())
        else:
            result.append(s[i].lower())
    return ''.join(result)


print(to_skyline('Anthropomorphism'))
