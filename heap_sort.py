#HEAP_SORT_ALGORITHM

def heapify(list1,n,i):
    largest = i
    l = (2*i)
    r = (2*i)+1
    if l<=n and list1[l-1] > list1[largest-1]:
        largest = l
    
    if r<=n and list1[r-1] > list1[largest-1]:
        largest = r
    
    if largest != i:
        list1[largest-1],list1[i-1] = list1[i-1],list1[largest-1]
        heapify(list1,n,largest)

def heap_sort(list1,n):
    for i in range(n//2,0,-1):
        heapify(list1,n,i)
        print(list1)
    for i in range(n,0,-1):
        list1[0],list1[i-1] = list1[i-1],list1[0]
        n = n-1
        print("swap")
        print(list1)            #check step by step
        
        heapify(list1,n,1)
        
        print("arrange")        #check step by step
        print(list1)
        



list1 = [14,53,6,13,7,2,40]
n = len(list1)
print(n)
print(list1)
heap_sort(list1,n)
print("The sorted list: \n")
print(list1)
