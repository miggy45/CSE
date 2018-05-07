World_map = {
    'WESTHOUSE': {
        'NAME': "WEST OF HOUSE",
        "DESCRIPTION": "YOU ARE WEST OF WHITE HOUSE",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE',
        }
    },
    'NORTHHOUSE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': "INSERT DESCRIPTION HERE",
        'PATH': {
            'SOUTH': 'WESTHOUSE'
        }
    }
}
current_node = World_map['WESTHOUSE']
directions = ['','','',]


print(current_node)
while True:
    print(current_node['name'])
    print(current_node['description'])
    command = input('>_')
    if command =='quit':
        quit(0)
if command in delattr:
    name_of8_node = current_node['paths'][command]
        print('command not recognized')

