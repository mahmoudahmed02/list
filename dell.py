def remove_many(args,*vartuple):
    list = args
    new_value = 0
    for value in vartuple:
        print(value - new_value)
        print(list)
        del list[value - new_value]
        new_value +=1
        print('----------')

    print(list)
remove_many([1,2,3,1,2,1] ,0,3,5)
