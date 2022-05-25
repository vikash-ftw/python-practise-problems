'''
SPY GAME: Given a list of integers and returns True if it contains 007 in order

 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False

'''


def spy_game(nums):
    # a list having spy code with extra char to avoid out of index issue while comparing @line:17
    spy_code = [0, 0, 7, 'x']

    for num in nums:
        # comparing
        if num == spy_code[0]:
            spy_code.pop(0)

    return len(spy_code) == 1
