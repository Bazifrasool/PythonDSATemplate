# unordered , unchangable and no duplicates
sample_set = {"A", "B", "C"}
print(sample_set, type(sample_set))
empty_set = set()
empty_set.add("ABMS")
empty_set.add("AABMS")
empty_set.add("AABMS")
print(len(empty_set))
# does not have index # print(empty_set[0])
for x in empty_set:
    print(x)
# for adding sets together i.e UNION
empty_set.update(sample_set)
list_temp = [x for x in range(0, 10)]
empty_set.update(list_temp)
# to remove item --- .remove() // discard() does not error if not found
# get union rets a new set
print(empty_set.union(sample_set))
print("_________________________________--")
# get intersection
print(empty_set.intersection(sample_set))

print(empty_set, type(empty_set))
# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
