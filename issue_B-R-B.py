issue_id=set()
component=set()
link=dict()
ans=dict()
edge=[]
file =input()
file_handle=open(file,'r')
file_handle.readline()
for line in file_handle:
    a,b,c=line.split(",")
    issue_id.add(a)
    issue_id.add(b)
    component.add(c)
    edge.append([a,c])
    edge.append([b,c])
    # if( a in link.keys()):
    #     if(c in link[a].keys()):
    #         link[a][c].append(b)
    #     else:
    #         link[a][c]=[]
    #         link[a][c].append(b)
    # else:
    #     link[a]=dict()
    #     link[a][c]=[]
    #     link[a][c].append(b)
    # if( b in link.keys()):
    #     if(c in link[b].keys()):
    #         link[b][c].append(a)
    #     else:
    #         link[b][c]=[]
    #         link[b][c].append(a)
    # else:
    #     link[b]=dict()
    #     link[b][c]=[]
    #     link[b][c].append(a)

    if(a in link.keys()):
        if(b in link[a].keys()):
            link[a][b]+=1
        else:
            link[a][b]=1
    else:
        link[a]=dict()
        link[a][b]=1
    if(b in link.keys()):
        if(a in link[b].keys()):
            link[b][a]+=1
        else:
            link[b][a]=1
    else:
        link[b]=dict()
        link[b][a]=1


      
for i in link:
    
    
    for j in link[i]:
        print(i+"\t"+j+"\t"+str(link[i][j]))
        
        
        
    print("---------------------------------------------------------")

