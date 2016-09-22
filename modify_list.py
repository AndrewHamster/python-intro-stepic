def modify_list(l):
    for i in l:
        if i % 2 == 1:
            del l[l.index(i)]
    for i in range(len(l)):
         l[i] //= 2



lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
