from turtle import right
from xmlrpc.client import Boolean

count = 0

def binarySearch(list, target, left, right):
    global count
    count = count + 1
    if left <= right:
        mid = (left+right)//2
        print(f'Middle number is {list[mid]} : Left -> {left} right -> {right} middle -> {mid} ')
    
        if target == list[mid]:
            print(f'The Target number ({target}) is found is index number {mid} and loop count {count}')
            
        if target > list[mid]:
            binarySearch(list, target, mid+1, right)
        
        if target < list[mid]:
            binarySearch(list, target, left, mid-1)
    
    else:
        print('The number is not found in list')
        
numbers = [9,12,6,4,38,46,36,16,45,12,17,2,4,25,12,14,22,20]
sorted_numbers = sorted(numbers)
print(f'Sorted numbers are {sorted_numbers} ')
left = 0
right = len(sorted_numbers)-1
target = 4
binarySearch(sorted_numbers, target, left, right)

        

