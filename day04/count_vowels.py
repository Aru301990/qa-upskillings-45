def count_vowels():
    string="automation"
    count=0

    for i in string:
        if i in "aeiou":
            count +=1
    print(count)
count_vowels()