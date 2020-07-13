#QUICK_SORTING
list1 = [36,28,2,6,1,18,9]
print(list1)

def quick_sorting(list1):
    length = len(list1)
    if length <= 1:
        return list1
    else:
        key = list1.pop()
        items_lower = []
        items_higher = []
        for item in list1:
            if item <= key:
                items_lower.append(item)
            else:
                items_higher.append(item)
        return quick_sorting(items_lower) + [key] + quick_sorting(items_higher)


print(f'the sorted list is {quick_sorting(list1)}')


 



