#Print elemets from triangular index from a given list
numbers = [34,2,8,56,91,7]
for i in range(1,len(numbers)):
    sum = 0
    for j in range(1,i):
        sum = sum + j
    if sum >= len(numbers):
       break
    print numbers[sum]
    
    output: 

34
2
56
 
##Get unique values from a list
numbers = [34,2,8,56,91,7,2,8,11,55,91]
uniq_list = []
for i in numbers:
    if i not in uniq_list:
       uniq_list.append(i)
print uniq_list
#Output = [34, 2, 8, 56, 91, 7, 11, 55]
