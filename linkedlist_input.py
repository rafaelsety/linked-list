from linkedlist_git import Node
from linkedlist_git import LinkedList

#linked list declaration
ll = LinkedList()

#linked list input
class InputProgram:
    def input_list(self):
        #insert values
        num =int(input("Masukan banyak data: "))
        value = []
        for itr in range(0,num):
            insert_list = input("Masukan data: ")
            value.append(insert_list)
        ll.insert_values(value)
        print("Linkedlist: ")
        ll.print()

    def input_begin(self):
        #insert at begining
        insert_begin = input("Masukan data: ")
        ll.insert_at_begining(insert_begin)
        ll.print()

    def input_end(self):
        #insert at end
        insert_end = input("Masukan data: ")
        ll.insert_at_end(insert_end)
        ll.print()

    def input_at(self):
        #insert at (index, data)
        insert_at_index = int(input("Masukan index: "))
        insert_at_data = input("Masukan data: ")
        ll.insert_at(insert_at_index, insert_at_data)
        ll.print()

    def input_after(self):
        #insert after value (data, data)
        insert_after = input("Masukan data sebelumnya: ")
        insert_data = input("Masukan data: ")
        ll.insert_after_value(insert_after, insert_data)
        ll.print()

    def drop_at(self):
        #remove at
        remove_index = int(input("Masukan index: "))
        ll.remove_at(remove_index)
        ll.print()

    def drop_values(self):
        #remove by value
        remove_value = input("Hapus data: ")
        ll.remove_by_value(remove_value)
        ll.print()

    def got_long(self):
        #get length
        print("Panjang data: ",ll.get_length())

    def default_list(self):
        print("Linkedlist: ")
        ll.insert_values(['a','i','u','e','o'])
        ll.print()
