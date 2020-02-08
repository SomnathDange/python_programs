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
 
