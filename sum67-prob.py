'''
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) → 2
sum67([2, 2, 6, 7, 7]) → 11
'''

# function to calculate sum param: list of numbers


def sum67(nums):
    # var to store sum
    curr_sum = 0
    # list to store buffer items
    buffer_list = list()
    # counter to keep track of occurance of 6
    six_count = 0
    for i in nums:
        if i == 6:
            six_count += 1
            continue

        if i == 7:
            # checking if 6 appeared before then clearing buffer
            if six_count > 0:
                six_count = 0
                del buffer_list[:]
                continue

        # to store items in buffer those are followed after 6
        if six_count > 0:
            buffer_list.append(i)
            continue

        # maintaining current total sum
        curr_sum += i
    return curr_sum
