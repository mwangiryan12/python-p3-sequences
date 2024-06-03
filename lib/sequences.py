def print_fibonacci(length):
    if length==1:
        print([0])
    elif length == 2:
        print([0,1])
    elif length>2:
        lst = [0,1]
     
        for i in range(2,length):
            third = lst[-1]+lst[-2]
           
            lst.append(third)
           
        print (lst)
    else:
        print([])

print_fibonacci(5)