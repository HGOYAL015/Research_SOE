
issue_id=set()
component=set()
link=dict()
edge=[]

file=input()
issue_id1=set()
component1=set()
link1=dict()
ans1=dict()
edge1=[]
file_handle=open(file,'r')
file_handle.readline()
for line in file_handle:
    a,b,c=line.split(",")
    issue_id.add(a)
    issue_id.add(b)
    component.add(c)
    edge.append([a,c])
    edge.append([b,c])
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

    if(a in link.keys()):
        if(b in link[a].keys()):
            
            link[a][b].add(c)
        else:
            link[a][b]=set()
            link[a][b].add(c)


    else:
        link[a]=dict()
        link[a][b]=set()
        link[a][b].add(c)
    if(b in link.keys()):
        if(a in link[b].keys()):
            link[b][a].add(c)
        else:
            link[b][a]=set()
            link[b][a].add(c)            
    else:
        link[b]=dict()
        link[b][a]=set()
        link[b][a].add(c)


      
for i in link:
    
    ans1[i]=dict()
    for j in link[i]:
        ans1[i][j]=len (link[i][j])

        
file =input()
file_handle=open(file,'r')
file_handle.readline()
for line in file_handle:
    a,b=line.split(",")
    b=b[:-1]
    
    issue_id1.add(a)
    component1.add(b)
    edge1.append([b,a])
    
    if(a in link1.keys()):
        link1[a].add(b)
    else:
        link1[a]=set()
        link1[a].add(b)

ans2=dict()

for i in issue_id1:
    for j in issue_id1:
        if i!=j:
            check=len(link1[i].intersection(link1[j]))
            if check:
                if i in ans2.keys():                    
                    ans2[i][j]=int(check)
                else:
                    ans2[i]=dict()
                    ans2[i][j]=int(check)
                # print(i+"\t"+j+"\t"+str(check))
                
                



# issue_id,issue_id1=issue_id1,issue_id
# ans1,ans2=ans1,ans2
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
        
                



        


