def hasnumbers(cnum):
    return cnum.isdigit()
def check_len(length):
    if length >= 13 and length <= 16 :
        return True
    return False

def startwith(cnum):
    f=int(cnum[0])
    if f==4 or f==5 or f==6:
        return True
    elif f==3:
        s=int(cnum[1])
        if s==7 or s==4 or s==5:
            return True
        else:
            return False
    return False

def luhn_check(cnum):
    halflen=len(cnum)-2
    tsum=0
    for i in range(halflen,-1,-2):
        n=int(cnum[i])
        n=n*2
        if n>9:
            n=n%10
            n=n+1
        cnum=cnum[:i]+str(n)+cnum[i+1:]
        tsum+=n
    for i in range(len(cnum)-1,-1,-2):
        tsum+=int(cnum[i])
    if tsum%10==0:
        return True
    return False

    
def main():    
    cnumber=str(input("Enter a credit card number"))
    if hasnumbers(cnumber):
        if check_len(len(cnumber)):
            if startwith(cnumber):
                if luhn_check(cnumber):
                    print("Valid:A Valid Number")
                else:
                    print("Invalid:Invalid Number")
            else:
                print("Invalid:Check starting number ")
        else:
            print("Invalid:Check Number Length")
    else:
        print("Invalid:Contains alphabets or special characters")

    print("THANK YOU")
    
