S=input()
lenS=len(S)

def state(i):
    if(lenS==i):
        return True

    if(S[i:i+7]=="dreamer"):
        j=state(i+7)
        if(j==True):
            return True
    if(S[i:i+5]=="dream"):
        j=state(i+5)
        if(j==True):
            return True
    if(S[i:i+6]=="eraser"):
        j=state(i+6)
        if(j==True):
            return True      
    if(S[i:i+5]=="erase"):
        j=state(i+5)  
        if(j==True):
            return True
    return False
i=0
if(state(i)):
    print("YES")
else:
    print("NO")





