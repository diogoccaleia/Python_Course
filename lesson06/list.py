users = ['Diogo', 'Joana', 'Miguel']

data = ['Diogo', 25, True]

emptylist = []

print("Diogo" in data)

print(users[0])
print(users[-2])
print(users.index('Joana'))

print(users[0:2])
print(users[:])

print(len(users))

users.append('Inês')
# print(users)

users += ['Beru']
# print(users)

users.extend(['Roberta', 'Joaquim'])
# print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Laura')
# print(users)

users[2:2] = ['Eduardo', 'Alex'] # adds to the list
# print(users)

users[1:3] = ['Roberto', 'JPJ'] # replace values 1 and 2
# print(users)

users.remove('Laura')
# print(users)

print(users.pop()) # last place
# print(users)

del users[0]
# print(users)

# del data
data.clear()
# print(data)

users[1:2] = ['diogo']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Diogo',25,True))

anothertuple = (1,4,2,8)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Macamba')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)