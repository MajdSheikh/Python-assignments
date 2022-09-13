for x in range(0,151,1): 
    print(x)

for y in range(5,1001,1):
    if y % 5 == 0:
     print(y)



for z in range(1,101,1):
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
       print (z)


sum = 0
for i in range(0,10, 1):
    if i % 2 == 1:
        sum = sum + i
print(sum)
#or
sum = 0
for i in range(1, 500001, 2):
    if 1 % 2 == 1:
        sum = sum + i
print(sum)
    


for i in range(2018, 0, -4):
    print(i)



def multiples(lowNum, highNum, mult):
    for i in range (lowNum, highNum, 1):
        if i % mult == 0:
            print(i)

multiples(2, 10, 3)