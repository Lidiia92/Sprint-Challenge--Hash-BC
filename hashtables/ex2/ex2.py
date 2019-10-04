#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


tickets = [
  Ticket("PIT", "ORD" ), 
  Ticket("XNA", "CID" ),
  Ticket("SFO", "BHM" ),
  Ticket("FLG", "XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX", "SFO" ),
  Ticket("CID", "SLC" ),
  Ticket("ORD", "NONE"),
  Ticket("SLC", "PIT" ),
  Ticket("BHM", "FLG" )
]

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    route[0] = hash_table_retrieve(hashtable, 'NONE')
    
    for j in range(1, length):
        route[j] = hash_table_retrieve(hashtable, route[j-1])

    return route

