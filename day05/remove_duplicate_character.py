def remove_duplicate_character():
    text="automation"
    res=""
    for i in text:
        if i not in res:
            res+=i
    print(res)

remove_duplicate_character()

