import random


def binary_search(num_list, num):
    count = 0
    i = 0
    j = len(num_list) - 1
    while i <= j:
        count += 1
        index = (i + j) // 2
        if num_list[index] == num:
            return index, count
        elif num_list[index] > num:
            j = index - 1
        elif num_list[index] < num:
            i = index + 1
    return -1, count


def sub_recursive_binary_search(num_list, num, count, i, j):
    count += 1
    if i > j:
        return -1, count
    index = (i + j) // 2
    if num_list[index] == num:
        return index, count
    elif num_list[index] > num:
        return sub_recursive_binary_search(num_list, num, count, i, index-1)
    elif num_list[index] < num:
        return sub_recursive_binary_search(num_list, num, count, index+1, j)


def recursive_binary_search(num_list, num):
    return sub_recursive_binary_search(num_list, num, 0, 0, len(num_list)-1)


def test():
    loop_total_count = 0
    recursive_total_count = 0
    num_list = sorted(random.sample(range(-100, 100), 100))
    for round in range(100):
        num = num_list[random.randint(0,99)]
        print(num , "___", num_list)
        loop_total_count += binary_search(num_list, num)[1]
        print(binary_search(num_list, num))
        recursive_total_count += recursive_binary_search(num_list, num)[1]
        print(recursive_binary_search(num_list, num))
    print(loop_total_count/100, recursive_total_count/100)


test()
