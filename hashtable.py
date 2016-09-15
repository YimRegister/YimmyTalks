#hash table with collisions
hash_table = [""] * 10

def hash_function(thing_to_be_hashed):
    #add up the ascii values of the string and mod length of table (takes care of overflow)
    print(sum([ord(char) for char in thing_to_be_hashed]))
    return sum([ord(char) for char in thing_to_be_hashed])%len(hash_table)

def insert(table,thing_to_be_hashed):
    hash_table[hash_function(thing_to_be_hashed)]=thing_to_be_hashed

insert(hash_table,"Jon Snow")
#insert(hash_table,"Andria")
#insert(hash_table,"Adrian")
print(hash_table)

#hash table that uses chaining

chained_hash_table= [[]for j in range(5)]

#this time we add to a list at that index, so we don't overwrite
def chained_insert(table,thing_to_be_hashed):
    chained_hash_table[hash_function(thing_to_be_hashed)].append(thing_to_be_hashed)

chained_insert(chained_hash_table,"Adrian")
chained_insert(chained_hash_table,"Andria")
chained_insert(chained_hash_table,"Ardian")
print(chained_hash_table)

#this will tell you where to start looking, but still sucks
def get(table,thing_to_get):
    index = hash_function(thing_to_get)
    print(str(thing_to_get) + " is located at index: " +str(index))
    return index
get(chained_hash_table,"Adrian")
get(chained_hash_table,"Andria")

def get4real(table,thing_to_get):
    start = get(table,thing_to_get)
    i=0
    while table[start][i]!=thing_to_get:
        i+=1
    return (start,i)
print(get4real(chained_hash_table,"Ardian"))
