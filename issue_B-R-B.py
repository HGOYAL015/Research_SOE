issue_id=set()
component=set()
link=dict()
ans=dict()
edge=[]
file_handle=open("issue_B-R-B.csv",'r')
file_handle.readline()
for line in file_handle:
    a,b,c=line.split(",")
    c=c[:-1]
    issue_id.add(a)
    issue_id.add(b)
    component.add(c)
    edge.append([a,c])
    edge.append([b,c])
    if( a in link.keys()):
        if(c in link[a].keys()):
            link[a][c].append(b)
        else:
            link[a][c]=[]
            link[a][c].append(b)
    else:
        link[a]=dict()
        link[a][c]=[]
        link[a][c].append(b)
    if( b in link.keys()):
        if(c in link[b].keys()):
            link[b][c].append(a)
        else:
            link[b][c]=[]
            link[b][c].append(a)
    else:
        link[b]=dict()
        link[b][c]=[]
        link[b][c].append(a)
      
for i in link:
    print(i)
    
    for j in link[i]:
        print("\t"+j)
        
        for k in link[i][j]:
            print("\t\t"+k)
    print("---------------------------------------------------------")

