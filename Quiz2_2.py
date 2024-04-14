mylist = [int(x) for x in input('Enter a list of numbers separated by spaces: ').split()]

mylist.sort()

if len(mylist) >=2:
    max_num = max(mylist)
    mylist.remove(max_num)

    second_max_num = max(mylist)
    
    print('The second largest number is:', second_max_num)
else:
    print('The list should have at least two numbers')
