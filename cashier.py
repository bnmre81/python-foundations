mylist = []

while True:
	item = input('Item (enter "done" when finished): ')
	if item == 'done':
		break
	price = input("Price: ")
	quantity = input("Quantity: ")
	my_dict = {}
	my_dict['name'] = item
	my_dict['price'] = price
	my_dict['quantity'] = quantity

	mylist.append(my_dict)
	

print('''
-------------------
receipt
-------------------
''')

for index in range(len(mylist)):
	item_price = int(mylist[index]['quantity']) * float(mylist[index]['price'])
	print('''
{} {} {}KD'''.format(mylist[index]['quantity'],mylist[index]['name'], item_price))


price_list = []
total_price = []

for index in range(len(mylist)):
	i_price = int(mylist[index]['quantity']) * float(mylist[index]['price'])
	price_list.append(i_price)
	total_price = sum(price_list)


print('''
-------------------
Total Price: {}'''.format(total_price))









    

	
	
    

	
