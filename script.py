# switch case of every possibility because why the fuck not
list = ["1. Find The Zeroes", "2. Show that lim f(x) exists", "3. Find lim f(x)", "4. Find inf. lim f(x)", "5. Find horiz. asymptotes", "6. Find vertical Asymptotes", "7. Find domain", "8. Find the normal line to f(x) at (a,b)", "9. Show that there exists a c in [a,b] such that f(c)=n", "10. find f'(x) by the limit definition", "11. Average rate of change given f'(x)"]
todo = ["y=0, solve", "-lim and +lim are equal", "Table[Ask] or uhhhhhh", "table ask 999999999 or big/small=DNE, small/big=DNE, big/small=0, equal/equal=coeffecients", "pos and neg inf. limits", "you're cooked", "Domain=(inf,-inf), find denominators(not 0), sqrt(non negative) log or ln, real world stuff)", "slope is negative reciprocal", "IVT, confirm f(x) is continuous and show f(a)<n<f(b)", "f'(x)=lim_h->0 (f(x+h)-f(x))/h \n or f'(x)=lim_x->a (f(x)-f(a))/x-a", "f'(x)=m"]
index = 0
while True:
    print("What do you see?")
    if index!=0:
        print("0. previous page")
    print(list[index]+"\n"+list[index+1])
    if index+1!=len(list)-1:
        print(".. next page")
    choice = input()
    if choice=="0" and index!=0:
        index = index-1
    elif choice=="." and index+1!=len(list)-1:
        index = index+1
    else:
        break
print(todo[int(choice)-1])