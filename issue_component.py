
issue_id=set()
component=set()
link=dict()
ans=dict()
edge=[]
file_handle=open("issue_component.csv",'r')
file_handle.readline()
for line in file_handle:
    a=""
    b=""
    for i in line:
        if i!=' ' :
            a+=i
        else:
            
            break
    flag=0
    issue_id.add(a)
    for i in line:
        if i=='\n':
            break
        if flag==1:
            b+=i
        if i==' ' :
            flag=1

    component.add(b)
    edge.append([b,a])
    
    if(b in link.keys()):
        link[b].append(a)
    else:
        link[b]=[]
        link[b].append(a)


for i in component:
    for j in link[i]:
        if(j in ans.keys()):
            ans[j]+=len(link[i])-1
        else:
            ans[j]=len(link[i])-1
        
for i in ans:
    print(str(i)+ " "+ str(ans[i]))
