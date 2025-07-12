data = {
    1: {'name': 'Rice', 'price': 60},
    2: {'name': 'Wheat Flour', 'price': 45},
    3: {'name': 'Sugar', 'price': 40},
    4: {'name': 'Milk', 'price': 25},
    5: {'name': 'Eggs (12 pcs)', 'price': 70},
    6: {'name': 'Cooking Oil', 'price': 130},
    7: {'name': 'Tea Powder', 'price': 90},
    8: {'name': 'Salt', 'price': 20},
    9: {'name': 'Bread', 'price': 30},
    10: {'name':'Soap','price':50}}

for i in range(1,11):
    print(f'{i} {data[i]["name"].ljust(15," ")}:{data[i]["price"]}')
items=list(map(int,input("Enter the item indexes: ").split()))
print(items)

total=0
ids=set()
for i in items:
    if i not in ids:
        co=items.count(i)
        total+=(data[i]['price']*co)
        print(f'{data[i]["name"]}-{co}*{data[i]["price"]}={data[i]["price"]*co}')
        ids.add(i)
print(f"Total Bill: {total}")
