new_dict = {}
new_dict['name'] = 'Mahatma Gandhi'
new_dict[2] = 'India'
new_dict[3.14] = 'chakras'
new_dict['number'] = 108
new_dict['one'] = 1
for i in new_dict.keys():
    print(i)
for i in new_dict.values():
    print(i)
for i in new_dict.items():
    print(i)
new_dict.pop('name')
for i in new_dict.items():
    print(i)
