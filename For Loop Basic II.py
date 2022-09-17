#Biggie Size
list = [-1, 3, 5, -5]
def BiggieSize(list):
    for i in range(0, len(list), 1):
        if list[i] > 0:
            list[i] = "big"
    print(list)
print(BiggieSize(list))    



#Count Positives
list = [-1,1,1,1]
def countPositives(list):
    count = 0
    for i in range (len(list)):
        if list[i] > 0:
            count += 1
            list[-1] = count
    print(list)
countPositives(list)


#Sum Total
x = [1,2,3,4]
def sumTotal(x):
    sum = 0
    for i in range (0, len(x), 1):
        sum += x[i]
    print(sum)
sumTotal(x)



#Average
y = [1,2,3,4]
def average(y):
    sum = 0
    for i in range (len(y)):
        sum += y[i]
        avg = sum / len(y)
    print(avg)
average(y)


#Length
q = [37,2,1,-9]
def length(q):
    count = 0
    for i in range(0,len(q), 1):
        count = count + 1
    print(count)
length(q)



#Minimum
w = [37,2,1,-9]
def minimum(w):
    if len(w) == 0:
        print("False")
    else:
        min = w[0]
        for i in range (len(w)):
            if w[i] < min:
                min = w[i]
        print(min)
minimum(w)



#Maximum
e = [37,2,1,-9]
def maximum(e):
    if len(e) == 0:
        print("False")
    else:
        max = e[0]
        for i in range (len(e)):
            if e[i] > max:
                max = e[i]
        print(max)
maximum(e)



#Ultimate Analysis
list = [37,2,1,-9]
def ultimateAnalysis(list):
    dictionary = {'sumTotal': 0, 'average': 0, 'minimum': list[0], 'maximum': list[0], 'length': len(list)}
    for i in range(len(list)):
        len(list) == len(list)
        dictionary['sumTotal'] += list[i]
        dictionary['average'] = dictionary['sumTotal'] / len(list)
        if list[i] > dictionary['maximum']:
            dictionary['maximum'] = list[i]
        elif list[i] < dictionary['minimum']:
            dictionary['minimum'] = list[i]  
    return dictionary   
print(ultimateAnalysis(list))



#Reverse List
list = [37,2,1,-9]
newList = []
def reverse(list):
    for i in range(len(list)-1, -1, -1):
        newList.append(list[i]) 
    print(newList)
reverse(list)
