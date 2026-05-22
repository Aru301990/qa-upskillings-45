def first_non_repeating():
    s="automation"
    count=0
    for i in s:
        if s.count(i)==1:
            print(i)
            break
first_non_repeating()