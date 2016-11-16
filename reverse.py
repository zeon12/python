def reverse(text):
    list1 = list(text)
    list2 = list()
    while len(list1) > 0:
        list2.append(list1[-1])
        del list1[-1]

    return ''.join(list2)
