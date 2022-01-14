def strCountDis(string):
    c = 0
    for i in string:
        if i.isalpha():
            if string.count(i)==1:
                c = i
                break
    return c
