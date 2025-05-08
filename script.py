# switch case of every possibility because why the fuck not
list = ["1. Find The Zeroes", "2. Show that lim f(x) exists", "3. Find lim f(x)", "4. Find inf. lim f(x)", "5. Find horiz. asymptotes", "6. Find vertical Asymptotes", "7. Find domain", "8. Find the normal line to f(x) at (a,b)", "9. Show that there exists a c in [a,b] such that f(c)=n", "10. find f'(x) by the limit definition", "11. Average rate of change given f'(x)"]
todo = ["y=0, solve", "-lim and +lim are equal", "Table[Ask] or uhhhhhh", "table ask 999999999 or big/small=DNE, small/big=DNE, big/small=0, equal/equal=coeffecients", "pos and neg inf. limits", "you're cooked", "Domain=(inf,-inf), find denominators(not 0), sqrt(non negative) log or ln, real world stuff)", "slope is negative reciprocal", "IVT, confirm f(x) is continuous and show f(a)<n<f(b)", "f'(x)=lim_h->0 (f(x+h)-f(x))/h \n or f'(x)=lim_x->a (f(x)-f(a))/x-a", "f'(x)=m"]
trigder = ["sin(x)->cos(x)*x’", "cos(x)->-sin(x)*x’", "tan(x)->sec^2(x)*x’", "sec(x)->sec(x)tan(x)*x’", "csc(x)->-csc(x)cot(x)*x’", "cot(x)=-csc^2(x)*x’", "Arcsin(u) -> 1/sqrt(1-u^2) * u’", "Arctan(u) -> 1/(1+u)^2 * u’", "Arcsec(u) ->1/(|u| sqrt(u^2-1)) * u’"]
constantder = ["a^u->lna * u’", "e^u -> e^u * u’", "Log_a u->1/(ulna) * u’"]
trigint = ["∫ secx tanx dx = secx + C", "∫ cscxcotx dx = -cscx + C", "∫ tanx dx = ln |secx| + C", "∫ cotx dx = ln|sinx| + C", "∫ csc^2x dx = -cotx + C", "∫secx dx = ln|secx+tanx| + C", "∫cscx dx = ln|cscx-cotx| + C"]
def liist():
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
def trig():
    whar = input("1 Derivative \n 2 Integral")
    if whar=="1":
        whar=input("1 trig \n 2 constants")
        if whar=="1":
            for str in trigder:
                input(str)
        elif whar=="2":
            for str in constantder:
                input(str)
    elif whar=="2":
        for str in trigint:
            input(str)
whar=input("1. list thing \n 2. Trig+washer/disc method")
if whar == "1":
    liist()
elif whar == "2":
    trig()
