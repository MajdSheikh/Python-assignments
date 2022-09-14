def countdown(num):
    empty_list = []
    for num in range(num, 0, -1):
        empty_list.append(num)
    return empty_list
print(countdown(10))



list = [1,2]
def PrintAndReturn(list):
    print(list[0])
    return list[1]
print(PrintAndReturn(list))



list = [1,2,3,4,5]
def firstPlusLength(list):
    sum = list[0] + len(list)
    print(sum)
print(firstPlusLength(list))




list = [5,2,3,2,1,4]
def ValuesGreaterthanSecond(list):
    newList = []
    for i in range (0, len(list), 1):
        if list[i] > list[1]:
            newList.append(list[i])
    print(len(newList))
    return newList
print(ValuesGreaterthanSecond(list))




def thisLengthThatValue(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(thisLengthThatValue(4, 7))
