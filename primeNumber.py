for i in range(2,10):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print i
print "==========="
num=7
for i in range(2,num):
    if (num % i) == 0 :
        print(num,"is not a prime number")
        break
else:
    print "Not a prime Number"
