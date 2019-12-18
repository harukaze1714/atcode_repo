N=int(input())
l=len(str(N))

def calc(st):
    st=str(st)
    if(len(st)>l):return 0
    t=calc(st+"3")
    f=calc(st+"5")
    s=calc(st+"7")
    o=0
    if(st.find("7")>=0 and st.find("5")>=0 and st.find("3")>=0 and int(st)<=N):
        o=1
    return (t+f+s+o)

print(calc(str()))





