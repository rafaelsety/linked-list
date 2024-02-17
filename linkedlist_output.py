from linkedlist_git import LinkedList
from linkedlist_input import InputProgram

ll = LinkedList()
ip = InputProgram()

#linkedlist program wannabe
class ShowProgram:
    def menu(self):
        print(" 1. INPUT AT BEGIN \n 2. INPUT AT END \n 3. INPUT AT (INDEX, DATA) \n 4. INPUT AFTER \n 5. DROP AT (INDEX) \n 6. DROP VALUE \n 7. GET LENGTH")


    def oprator_def(self):
        while True:
            oprator = input("Ingin mengedit data (y/n)? ")
            if oprator == 'y':
                self.menu()
                pick = int(input("Pilih angka: "))
                if pick == 1:
                    ip.input_begin()
                elif pick == 2:
                    ip.input_end()
                elif pick == 3:
                    ip.input_at()
                elif pick == 4:
                    ip.input_after()
                elif pick == 5:
                    ip.drop_at()
                elif pick == 6:
                    ip.drop_values()
                elif pick == 7:
                    ip.got_long()
                else:
                    print("byee!!")
                    break
            else:
                print("byee")
                break

    def making(self):
        have = input("Ingin membuat list (y/n)? ")
        if have == 'y':
            ip.input_list()
            self.oprator_def()
        else:
            ip.default_list()
            self.oprator_def()
