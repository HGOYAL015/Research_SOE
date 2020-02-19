
issue_id=set()
component=set()
link=dict()
edge=[]
file =input()
file_handle=open(file,'r')
file_handle.readline()
for line in file_handle:
    a,b=line.split(",")
    b=b[:-1]
    
    issue_id.add(a)
    component.add(b)
    edge.append([b,a])
    
    if(a in link.keys()):
        link[a].add(b)
    else:
        link[a]=set()
        link[a].add(b)

ans1=dict()

for i in issue_id:
    for j in issue_id:
        if i!=j:
            check=len(link[i].intersection(link[j]))
            if check:
                if i in ans1.keys():                    
                    ans1[i][j]=int(check)
                else:
                    ans1[i]=dict()
                    ans1[i][j]=int(check)
                # print(i+"\t"+j+"\t"+str(check))
                
                

issue_id1=set()
component1=set()
link1=dict()
ans2=dict()
edge1=[]
file1 =input()
file_handle=open(file1,'r')
file_handle.readline()
for line in file_handle:
    a,b,c=line.split(",")
    issue_id1.add(a)
    issue_id1.add(b)
    component1.add(c)
    edge1.append([a,c])
    edge1.append([b,c])
    # if( a in link1.keys()):
    #     if(c in link1[a].keys()):
    #         link1[a][c].append(b)
    #     else:
    #         link1[a][c]=[]
    #         link1[a][c].append(b)
    # else:
    #     link1[a]=dict()
    #     link1[a][c]=[]
    #     link1[a][c].append(b)
    # if( b in link1.keys()):
    #     if(c in link1[b].keys()):
    #         link1[b][c].append(a)
    #     else:
    #         link1[b][c]=[]
    #         link1[b][c].append(a)
    # else:
    #     link1[b]=dict()
    #     link1[b][c]=[]
    #     link1[b][c].append(a)

    if(a in link1.keys()):
        if(b in link1[a].keys()):
            
            link1[a][b].add(c)
        else:
            link1[a][b]=set()
            link1[a][b].add(c)


    else:
        link1[a]=dict()
        link1[a][b]=set()
        link1[a][b].add(c)
    if(b in link1.keys()):
        if(a in link1[b].keys()):
            link1[b][a].add(c)
        else:
            link1[b][a]=set()
            link1[b][a].add(c)            
    else:
        link1[b]=dict()
        link1[b][a]=set()
        link1[b][a].add(c)


      
for i in link1:
    
    ans2[i]=dict()
    for j in link1[i]:
        ans2[i][j]=int(len (link1[i][j]))

inter=issue_id.intersection(issue_id1)

for i in issue_id:
    for j in issue_id1:
        if i==j:
            continue
        sum=0
        for k in inter:
            if i==k or j == k :
                continue
            temp=0
            if i in ans1.keys():
                if k in ans1[i].keys() and ans2.keys():                
                    if j in ans2[k].keys():
                        a=ans1[i][k]
                        b=ans2[k][j]
                        temp=a*b
            sum = sum +temp

        print(i+"\t"+j+"\t"+str(sum))
        
                



        


