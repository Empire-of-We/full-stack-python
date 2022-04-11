name = 'Kim'
shit = [42, 'tank', 3.14]

name2 = 'tank'

name3 = 'kevin'

print(name,name2,name3)
print(shit)
print(shit[0])
print(shit[1])
print(shit[2])

print(len(shit))

print(type(shit))

print(shit[-3])

print(shit[1:3])

print(shit[1:])

if 52 in shit:
    print('tank is in shit')
else:
    print('item is not in this list')

shit[0] = 99
print(shit)

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