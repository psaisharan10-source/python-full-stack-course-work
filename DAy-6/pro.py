
'''
i = 0
while i<=30:
    if i==25:
        pass
    print(i)
    i+=1
'''
'''
bullets = 10
while bullets > 0:
    print("{bullets} bullets are left, you can shoot! ")
    bullets-=1
else:
    print("game over")

'''



'''
moves = 32
winning_point = 24
while moves >0:
    if moves == winning_point:
        print("you win the game")
        break
    print(f" {moves}moves are left,you can play!! ")
    
    moves-=1
else:
    print("game over")
'''



'''
data = {}
n = int(input("enter no of students:"))
for i in range(n):
    name = input("enter the name:")
    data[name]=False
print(data)

'''




'''
data = {}
n = int(input("enter no of students:"))
for i in range(n):
    name = input("enter the name:")
    data[name]=False
for name in data:
    print(name)
    status = int(input(f"Enter the {name} status (0-absent,1-present):"))
    data[name] = bool(status)
print(data)

'''



