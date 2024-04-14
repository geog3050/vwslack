mylist = [int(x) for x in input('Enter a list of numbers separated by spaces: ').split()]

contains_duplicates = any(mylist.count(x) > 1 for x in mylist)

if contains_duplicates:
    print('The list provided contains duplicate values.')
else:
    print('The list provided does not contain duplicate values.')

remove_duplicates = input('Do you want to remove duplicates from the list? ')

if remove_duplicates == 'yes':
    mylist = list(set(mylist))
    print('List after removing duplicates:', mylist)
else:
    print('Original list:', mylist)
