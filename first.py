# задание 1

list = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']
print( { value: [ i for i in range(j, len(list)) if value == list[i] ] for j, value in enumerate(list) if list.index(value) >= j} )

# задание 2

def jaccardSimiliarity(setFirst: set, setSecond: set):
    count = 0
    for elem in setFirst:
         if (elem in setSecond):
             count += 1
    return count / (len(setFirst) + len(setSecond) - count)

print( jaccardSimiliarity( {1, 2, 3, 5},{1, 4, 3, 5} ) )
print( jaccardSimiliarity( {'This', 'set'}, {'This', 'set', 'too'} ) )