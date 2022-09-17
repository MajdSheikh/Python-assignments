x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15
x[1][0] = 15
print(x)


#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0])


# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z[0]['y'])



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name - ", students[i]['first_name'], ", last_name - ", students[i]['last_name'])
iterateDictionary(students) 



#  iterateDictionary2('first_name', students)
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(students[i][key_name])
iterateDictionary2('first_name', students)

# iterateDictionary2('last_name', students)
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(students[i][key_name])
iterateDictionary2('last_name', students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    for i in range(len(dojo)):
        print(len(dojo['locations']), "locations")
        print(dojo['locations'])
        print(len(dojo['instructors']), "instructors")
        print(dojo['instructors'])
printInfo(dojo)

