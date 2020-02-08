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

##Print minimum element from list
numbers = [34,2,8,56,91,7,2,8,11,55,91]
final = []
while numbers:
    min = numbers[0]
    for i in numbers:
        if i < min:
           min = i
    final.append(min)
    numbers.remove(min)
print final

##Print Maximum element from list
numbers = [34,2,8,56,91,7,2,8,11,55,91]
final_mav = []
while numbers:
    max = numbers[0]
    for i in numbers:
        if i > max:
           max = i
    final_mav.append(max)
    numbers.remove(max)
print final_mav

#Reverse string
name = "Somanath Dange"
rev_str = ""
for i in name:
   rev_str = i + rev_str
print rev_str

#Reverse string word by word
name = "my name is shivansh"
str = name.split(" ")
name_str = str[::-1]
rev_str1 = ' '.join(name_str)
print rev_str1
