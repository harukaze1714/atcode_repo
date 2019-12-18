S=input()
L=list(["SAT","FRI","THU","WED","TUE","MON","SUN"])

for i in range(len(L)):
    if(L[i]==S):
        print(i+1)