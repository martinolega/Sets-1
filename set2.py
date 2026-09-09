#Trovo i gruppi da 3 che formano un certo numero

num = 15

mySet = {1, 2, 3, 4, 5, 6, 7, 10, 13}

setOfSets = set()

for x in mySet:
    for y in mySet:
        if(x != y):
            z = num - x - y
            if(z in mySet and z != x and z != y):
                setOfSets.add(frozenset({x, y, z}))

print(setOfSets)