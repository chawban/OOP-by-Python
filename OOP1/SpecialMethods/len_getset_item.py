#len_getitem.py

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index, value):
        self.items[index] = value
        
    def __getitem__(self, index):
        return self.items[index]
    
           
my_list = MyList([10, 20, 30, 40])
print(len(my_list))  # Output: 4

my_list[2] = 99  #Set
print(my_list[2])  # Get Output: 99
print(my_list.items)  # Output: [10, 99, 30]
