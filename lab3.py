#Lab 3

#Task 1: Working with strings
food = "Lasagna"

print(food[0:3])
print(food[-3:])

first_last = food[0] + food[-1]

print(food.split())

print(''.join(food))

#Task 2: Working with lists
number_list = [5, 10, 15, 20, 25, 30]

number_list.append(35)

number_list.insert(3, 18)

number_list.pop()

number_list.remove(10)
print(number_list[0:3])
print(number_list[-3:])

#Task 3: Working with dictionaries
books = {'Charles Dickens': 'Oliver Twist', 'Jane Austen': 'Pride and Prejudice', 'Stephen King': 'The Shining', 'J. K.  Rowling': 'Harry Potter'}
print(books.keys())
print(books.values())
print(books.get('Charles Dickens'))
books.pop('Stephen King')
print(books)
del books['Charles Dickens']
print(books)

for x in books:
    print(x)