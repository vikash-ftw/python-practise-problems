'''
Just for fun, not a real problem :)
PRINT BIG: Given a single letter, return a 5x5 representation of that letter (up-to 'E' is sufficient)

print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *

'''

def print_big(letter):
    # dict of star patterns associated with number
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    # dict of alphabet having combination of number 
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}

    # matching alphabet and getting value from patterns dict
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('b')

