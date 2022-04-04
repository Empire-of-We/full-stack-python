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
