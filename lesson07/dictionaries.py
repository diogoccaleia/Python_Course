# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JP"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bruno"
print(band)

print(band.popitem()) # tuple
print(band)

# delete and clear items

band["drums"] = "Bruno"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# #  bad example, creates a reference not a copy
# band2 = band # creates a reference
# print("Bad copy")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)
# #########

band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)

# or use the constructor function
band3 = dict(band)
print("Good copy")
print(band3)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "guitar"
}
member2 = {
    "name": "Plant",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

# Sets
nums = {1, 2, 3, 4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates allowed

nums = {1, 2, 2, 3} # ignores repetitions
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 3, 0}
print(nums)

# but you acannot refer to an elemente in a the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6 , 7}
nums.update(morenums)
print(nums)

# u can use update with lists, tuples, and dictionaries, too.

# merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# everuthing except duplicates
one.symmetric_difference_update(two)
print(one)