def display(hash_table):
    for i in range(len(hash_table)):
        print(i, end = " ")

        for j in hash_table[i]:
            print("->", end = " ")
            print(j, end = " ")

        print()

def hash(key):
    return key % len(hash_table)

def insert(hash_table, key, value):
    hash_key = hash(key)
    hash_table[hash_key].append(value)

def find(hash_table, key):
    hash_key = hash(key)
    print(hash_table[hash_key])


hash_table = [[] for _ in range(10)]

insert(hash_table, 50, 'Apple')
insert(hash_table, 25, 'Orange')
insert(hash_table, 10, 'Banana')
insert(hash_table, 4, 'Kiwi')
insert(hash_table, 30, 'Raspberry')
insert(hash_table, 38, 'Blueberry')

display(hash_table)
find(hash_table, 10)
