#BUBBLE_SORTING
list_2 = [3,8,1,9,4]
print(list_2)
def bubble_sorting(list_2):
    length2 = len(list_2)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,length2):
            if list_2[i] > list_2[i+1]:
                sorted = False
                list_2[i], list_2[i+1] = list_2[i+1], list_2[i]
                print(list_2) #step_by_step
    return list_2

print(f'the sorted list is{bubble_sorting(list_2)}')       