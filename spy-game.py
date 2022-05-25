'''
SPY GAME: Given a list of integers and returns True if it contains 007 in order

 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False

'''

def spy_game(nums):
    # iterating upto length - 2 positions only
    for i in range(len(nums) - 2):
        # checking conditions
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False




