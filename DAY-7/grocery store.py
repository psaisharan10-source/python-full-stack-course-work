

'''
# Grocery store data
products = [
    "Rice","Wheat Flour","Sugar","Milk","Eggs (12 pcs)",
    "Cooking Oil","Tea Powder","Salt","Bread","Soap"
]

prices = [60,45,40,25,70,130,90,20,30,25]

print("------ Welcome to Grocery Store ------")
print("Here are the available products:\n")

print("Index   Product           Price (Rs.)")

for i in range(len(products)):
    print(i+1,"   ",products[i]," "*(15-len(products[i])),prices[i])

print("\nEnter the product indexes you want to buy (you can repeat indexes)")
indexes = list(map(int,input("Enter indexes (e.g. 1 2 2 5): ").split()))

print(indexes)

print("\n--------- Your Bill ---------")
print("Product        Qty    Price    Total")

grand_total = 0

for i in set(indexes):
    qty = indexes.count(i)
    price = prices[i-1]
    total = qty * price
    grand_total += total
    
    print(products[i-1]," "*(12-len(products[i-1])),qty,"     ",price,"     ",total)

print("\nGrand Total:",grand_total)

'''


'''
list
'''
'''
products = ['rice','sugar','weat flour','milk','eggs',
            'cooking oil','tea powder','salt','bread','soap']

price = [60,30,40,20,70,80,110,35,45,65]

print("------Welcome to Grocery store------")
print("Here are the available products:\n")

print('Index'.ljust(6,' '),'products'.ljust(15,' '),'price'.ljust(6,' '))

for i in range(10):
    print(str(i+1).ljust(6,' '),products[i].ljust(15,' '),str(price[i]).ljust(6,' '))


items = list(map(int,input("Enter the indexes:").split()))

print("Selected items:")

total_amount = 0
for item in items:
    print(products[item-1],price[item-1])
    total_amount+=price[item-1]

'''



