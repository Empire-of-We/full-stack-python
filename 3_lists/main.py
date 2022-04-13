name = 'Kim'
my_list = [42, 'tank', 3.14]

name2 = 'tank'

name3 = 'kevin'

print(name,name2,name3)
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])

print(len(my_list))

print(type(my_list))

print(my_list[-3])

print(my_list[1:3])

print(my_list[1:])

if 52 in my_list:
    print('tank is in my_list')
else:
    print('item is not in this my_list')

my_list[0] = 99
print(my_list)

attack_test = ['max', 'min', 'geartax']
attack_test.sort()
print(attack_test)

attack_test = ['max', 'min', 'geartax']
attack_test.sort(reverse=True)
print(attack_test)

attack_test = [11, 75, 888, 43]
attack_test.reverse()
print(attack_test)

attack_test = [11, 75, 888, 43]
attack_test.sort(reverse=True)
print(attack_test)

attack_test = [11, 75, 888, 43]
attack_test_2 = attack_test.copy()
print(attack_test_2)

attack_test = [11, 75, 888, 43]
attack_test_2 = [12, 85, 788, 49]
attack_test.extend(attack_test_2)   
print(attack_test) 