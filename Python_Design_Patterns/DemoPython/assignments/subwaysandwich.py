print('Select any 3 Toppings from the below : ')
print('Onions \nLettuce \nTomato \nOlives \nPeppers \nPickle')

t1=input('Enter First Choice of Toppings')
t2=input('Enter Second Choice of Toppings')
t3=input('Enter Third Choice of Toppings')

quantities = int(input('Tippi Top How many you want ? '))

total = quantities*5;

print('Total Price for {0} Sandwiches, Is {1}'.format(quantities,total))
