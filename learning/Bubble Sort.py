oldlist = [10, 75, 43, 15, 25, -4, 27]


def bubble_sort(lst):
    last_item = len(lst) - 1
    for j in range(last_item):
        for i in range(last_item - j):
            print(lst)
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


new_list = bubble_sort(oldlist)
print(new_list)
print(oldlist)
