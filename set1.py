set = {1, 2, 3, 4, 5, 6, "Test", "Hello", "Hello", 1, 2, 3}
print(set)

for x in set:
    print(f"{x} - {type(x)}")

print(set)

set.add(1)
print(set)

set.add(7)
print(set)

set.remove(1)
print(set)

set2 = {1, 2, 3, 4, 5, 6, 7, 8, "Hi", "Hello"}

set3 = set.union(set2)
print(set)
print(set2)
print(set3)

frozenset1 = frozenset({"1", "2", "3"})
print(f"{frozenset1} - {type(frozenset1)}")

print(len(frozenset1))
print(len(set3))