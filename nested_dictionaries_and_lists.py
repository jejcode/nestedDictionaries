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

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]. - DONE
x[1][0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant' - DONE
students[0]['last_name'] = 'Bryant'
print(students)
# In the sports_directory, change 'Messi' to 'Andres' - DONE
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
# Change the value 20 in z to 30 - DONE
z[0]['y'] = 30
print(z)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(sourceList): # get key, value pairs from a given dictionary
    for dictionary in sourceList:
        output = []
        for key, value in dictionary.items():
            output.append(key + ' - ' + value)
        print(', '.join(output))
        # bonus to get them to appear exactly as below!)
        # first_name - Michael, last_name - Jordan
        # first_name - John, last_name - Rosales
        # first_name - Mark, last_name - Guillen
        # first_name - KB, last_name - Tonel
iterate_dictionary(students) 

# given a list of dictionaries and a key name, the function prints the value
# stored in that key for each dictionary
def iterate_dictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in dojo.keys():
        print('--------------')
        print(str(len(dojo[key])) + ' ' + key.upper()) # include the number of entries in the list
        for value in dojo[key]: #print each entry in the list
            print(value)
printInfo(dojo)
