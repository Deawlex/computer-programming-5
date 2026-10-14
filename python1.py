item_name = input('Item name :')
price = int(input('Price :'))
quantity = int(input('Quantity :'))

before_discount_subtotal = subtotal = price * quantity

#Customer information
name = input('Customer name :')
is_member = input('Is member?(yes/no):')
total_previous_purchases = int(input('Amount :'))

#Discounts
#Member discount
if is_member == 'yes':
    subtotal = subtotal - subtotal*0.1
print(subtotal, 'with member discount')
#Bulk discount
if quantity > 5:
    subtotal = subtotal - subtotal*0.05
print(subtotal, 'with bulk discount')
#Loyalty discount
if total_previous_purchases >= 1000000:
    subtotal = after_discount = subtotal - subtotal*0.03
print(subtotal, 'with loyalty discount')

#Tax
subtotal = subtotal + subtotal*0.12
print(subtotal, 'with tax')
#Shipping
if subtotal < 500000:
    subtotal = subtotal + 25000

print('Customer name', name, ', His membership status :', is_member)
print('Bought :', item_name, ', how many :', quantity, ", price for each :", price)
print('Subtotal before discounts :', before_discount_subtotal)
if is_member == 'yes':
    print('Member discount : True')
elif is_member == 'no':
    print('Member discount : False')
if quantity > 5:
    print('Bulk discount : True')
else:
    print('Bulk discount : False')
if  total_previous_purchases >= 1000000:
    print('Loyalty discount : True')
else:
    print('Loyalty discount : False')
print('Total discounts applied :', before_discount_subtotal - after_discount)