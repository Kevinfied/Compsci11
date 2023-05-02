
def subtract(list1, list2):
    list3 = []
    for q in list1:
        if q not in list2:
            list3.append(q)
    return list3


