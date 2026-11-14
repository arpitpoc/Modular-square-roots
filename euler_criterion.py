

def euler_criterion(a,p):

    a=a%p
    if a==0:
        return "Zero is neither Quadratic Residue nor Non-Residue"
    temp=(p-1)//2
    result=pow(a,temp,p)

    if result==1:
        return "Quadratic Residue"
    elif result == p-1:
        return "Quadratic Non-Residue"

    else:
        return "Invalid Result"
       


