def largest_num():
    num = [2,5,6,8,1,9]
    largest=num[0]

    for i in range(1,len(num)):
        if num[i]>largest:
            largest=num[i]
    print(largest)

largest_num()