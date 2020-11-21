'''This will be a Python script that functions as a grocery calculator. It will take in key-value pairs for items
and their prices, and return the subtotal and total, and can print out the list for you for when you're ready to
take it to the store!'''

'''Algorithm:
1. User enters key-value pairs that are added into a dict.
2. Users tells script to return total, subtotal, and key-value pairs in a nicely formatted list.'''

#Object = GroceryList
#Methods = addToList, Total, Subtotal, returnList

# Grocery calculator
class GroceryList(dict):
    def __init__(self):
        self = {}
    def addToList(self, item, price):
        self.update({item:price})
    def Total(self):
        total = 0
        for items in self:
            total += (self[items])*.07 + (self[items])
        return total
    def Subtotal(self):
        subtotal = 0
        for items in self:
            subtotal += self[items]
        return subtotal
    def returnList(self):
        return self

List1 = GroceryList()
List1.addToList("milk",4)
List1.addToList("eggs", 3)
List1.addToList("kombucha", 3)
print(List1.Total())        # Total = 10.70
print(List1.Subtotal())     # Subtotal = 10
print(List1.returnList())   # returnList = {"milk":4, "eggs":3, "kombucha":3}
