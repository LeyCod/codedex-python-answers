books = ['Zero to One',
'The Lean Startup',
'The Mom Test',
'Made to Stick',
'Life in Code']

print(books)

#TODO add one more book to the list using a list method 

books.append('Zero to Sold')

print('list: ', books, 'new book added: ', books[-1])

#TODO use the .remove() & .pop() method to remove this two books: 'Zero to One' and 'The Lean Startup'.

books.remove('Zero to One')
print('"Zero to One" was removed using .remove()', books)

books.pop(0)
print('"The Lean Startup" was removed using .pop()', books)