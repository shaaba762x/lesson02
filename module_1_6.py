my_dict = {'hobbit' : 111, 'higt_elf' : 2021, 'dwarf': 464, 'human' : 18}
print(my_dict)
print('Human:', my_dict.get('human'))
print('Orc -', my_dict.get('orc', 'В увольнительной'))
my_dict.update({'varg' : 5,
               'pony' : 3})
print(my_dict)
del my_dict['hobbit']
print(my_dict)
# задание 3
my_set = {2, 12, 85, '07', 2, 85, 2, 'frombolla', 7, 2}
print(my_set)
my_set.add(5)
my_set.add(14)
print(my_set)
my_set.discard('frombolla')
print(my_set)