# задание 1

list = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']
print( { key: [ i for i in range(j, len(list)) if key == list[i] ] for j, key in enumerate(list) if list.index(key) >= j} )

# задание 2

def JaccardSimilarity(setFirst: set, setSecond: set):
    count = 0
    for elem in setFirst:
         if (elem in setSecond):
             count += 1
    return count / (len(setFirst) + len(setSecond) - count)

print( JaccardSimilarity( {1, 2, 3, 5},{1, 4, 3, 5} ) )
print( JaccardSimilarity( {'This', 'set'}, {'This', 'set', 'too'} ) )
