from xmlrpc.client import Boolean

numbers = [2,12,14,6,45,3,4,9,23]
have = Boolean
sorted_numbers = sorted(numbers)
find = 9

middle_len = int(len(numbers)/2)
print('middle number',sorted_numbers[middle_len])

print(middle_len)
print(sorted_numbers)

if sorted_numbers[middle_len] == find:
    have = True;
    print('Number was in middle')

if sorted_numbers[middle_len] > find:
    print('in smaller')
    for value in range(middle_len, 0, -1):
        print(value)
        if sorted_numbers[value] == find:
            have = True
            print('Number was smaller than middle')
            break

if sorted_numbers[middle_len] < find:
    print('in Greater')
    for value in range(middle_len, len(sorted_numbers), 1):
        print(value)
        if sorted_numbers[value] == find:
            have = True
            print('Number was greater than middle')
            break
if have == True:
    print(find, ' < this number have in numbers list')
else:
    print(find, ' < Cant find this number')

        

