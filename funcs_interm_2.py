# 1.  change value of 10 in x to 15
# x = [ 
#     [5,2,3], 
#     [10,8,9] 
#     ] 
# x[1][0] = 15
# print(x)

# 2, change last name jordan to bryant
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name'] = 'Bryant'
# print(students)

# 3. sports from messit to andres
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# 4. 
# z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30
# print(z)

# ---------------------

# Iterate through a list of Dictionaries 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iterateDictionary(param): 
#     for dict in param: # this will loop through the 4 rows of key value pairs
#         show_str = ''
#         for key in dict.keys(): # this will loop through they keys in each row
#             show_str += f"{key} - {dict[key]}, " # this will show the first key value pair (first name: ___) then continue in the row to the next key (last name:) then go to the next row
#         show_str = show_str[:len(show_str) - 9] #at the end of the inner for-loop, this is slice notation https://stackoverflow.com/questions/509211/understanding-slice-notation
#         print(show_str)
# holder = iterateDictionary(students)

# -----------------------

# def iterateDictionary2(key_name, some_list):
#     for dict in some_list:
#         if key_name == "first_name":
#             print (dict['first_name'])
#         elif key_name == "last_name":
#             print(dict['last_name'])
# holder = iterateDictionary2('first_name', students)
# holder = iterateDictionary2('last_name', students)

# ------------------------

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(param):
    for key in param.keys():
        print (f"{len(param[key])} {key.upper()}")
        for idx in param[key]:
            print (idx)
        print('\n')
        
printInfo(dojo)