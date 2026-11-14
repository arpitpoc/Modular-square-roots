

def brute_force(a,p):
    roots=[]
    for x in range(p):
        if ((x*x)%p==a%p):
            roots.append(x)
            
    return roots

