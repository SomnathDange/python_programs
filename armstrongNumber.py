n = 153
sum = 0
for i in str(n):
    sum = sum + (int(i)**3)
if n == sum:
    print "ArmStrong"
else:
    print "No ArmStrong"

#num = int(input("Please Enter Number"))
num=153
sum = 0
temp=num
while(temp>0):
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp/10
if num == sum:
    print "ArmStrong"
else:
    print "No ArmStrong"
