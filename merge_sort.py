#MERGE_SORTING
def merge_sorting(list_3):
    if len(list_3) > 1:
        mid = len(list_3)//2
        left_list = list_3[:mid]    #partitioning
        right_list = list_3[mid:]   #partitioning
        merge_sorting(left_list)
        merge_sorting(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list_3[k] = left_list[i]
                i = i+1
                k = k+1
            else:
                list_3[k] = right_list[j]
                j = j+1
                k = k+1
        
        while i < len(left_list):
            list_3[k] = left_list[i]
            i = i+1
            k = k+1

        while j < len(right_list):
            list_3[k] = right_list[j]
            j = j+1
            k = k+1
        print(list_3)
    return (list_3)

list_3 = [1,10,6,2,9]
print(list_3)
print(f' The sorted list is {merge_sorting(list_3)}')