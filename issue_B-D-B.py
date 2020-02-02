
issue_id=set()
component=set()
link=dict()
ans=dict()
edge=[]
file_handle=open("issue_B-D-B.csv",'r')
file_handle.readline()
for line in file_handle:
    a,b=line.split(",")
    b=b[:-1]
    
    issue_id.add(a)
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
    print("------------------ ")

