def rev_rec_print(num):
    if num < 0:
        return
    rev_rec_print(num-1)
    print(num)
    return

#rev_rec_print(5)

def rec_print(num):
    if num < 0:
        return
    print(num)
    rec_print(num-1)
    return

def rev_rec_print_arr(arr):
    if not len(arr):
        return
    rev_rec_print_arr(arr[1::])
    print(arr[0])
    return

#rev_rec_print_arr([1,2,3,4,5,6])

def rec_print_arr(arr):
    if not len(arr):
        return
    print(arr[0])
    rec_print_arr(arr[1::])
    return


#rec_print_arr([1,2,3,4,5,6])

import random
def rand_list(num, arr=[]):
    if len(arr) == num:
        return arr
    arr.append(random.randint(-num, num))
    return rand_list(num,arr)


print(rand_list(7))
