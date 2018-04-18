#lists
the_count = {0,1,2,3,4,5}
shopping_list = ["noodles" , "eggrolls","milk" , "rice","soda"]

print(shopping_list[0])

print(len(shopping_list))
for item in shopping_list:
# going through a list
    print (item)

print(len(the_count))
for numbers in the_count:
      print(numbers)

len(shopping_list)    #gives me the langth of the list
range(3)  #gives a list of numbers 0 throggh 2
range(len(shopping_list))   #A list of every index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("the item at index %d is %s" % (num, item))

#turn thngs into list
str1 = "hello class!"
listone = list(str1)
print(listone)
listone[11] = '.'
print(listone)
print("".join(listone))

shopping_list.append("cereal")
print(shopping_list)

#removing things from list
shopping_list.remove("soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

#the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

#dealing with string
strTwo = "ThIs iS a VeRY oDd sEnTenCE"
lowercase = strTwo.lower()
print(lowercase)

# dictionaries - made up of key: value pairs
dictionaries = {'name': 'lance', 'age': 23, 'height': 5 * 12 + 5}

# accessing dictionaries
print(dictionaries['name'])
print(dictionaries['age'])
print(dictionaries['height'])

# adding to a dictionary

large_dictionary = {
    'ca': 'california',
    'fl': 'Florida',
    'OH': 'Ohio'
}
print(large_dictionary['fl'])

larger_dictionary = {
    'ca': [
        'Fresno',
        'sacramento',
        'Los angeles',
    ],
    'fl': [
        "tampa",
        "orlando",
        "miami",
    ],
    'OH': [
        "Cleavland",
        "cincinnati",
    ]
}




print(larger_dictionary['OH'])
print(larger_dictionary["OH"][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}
current_node = largest_dictionary["CA"]
print(current_node)
print(current_node["POPULATION"])
print(current_node["NAME"])
