#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    indexes = []

    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for j in range(length):
        result = hash_table_retrieve(ht, limit-weights[j])
        if result != None:
            indexes.append(result)

    if indexes and indexes[0] != indexes[1]:
        return indexes
    elif indexes and indexes[0] == indexes[1]:
        return [indexes[1], 0]
    else: 
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
