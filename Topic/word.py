file = "stammed_input.txt"

file_handle=open(file,'r')

file_handle.readline()
print("issue_id,topic_ngram")
for line in file_handle:
    ngram=dict()
    list_word=[]
    a,temp=line.split('~',1)
    temp=temp[:-1]
    # print(temp)
    temp=temp.split(' ')
    temp=temp[:-1]
    # print(temp)
    list_word+=temp
    # print(list_word)

    n=len(list_word)
    k=0
    # print(a,end="~")
    for i in list_word:
        print(a+","+i)
    # print("\n")
    for i in range(2,min(8,n+1)):
        word=list_word[0]
        for j in range(1,i):
            word+="_"+list_word[j]
        ngram[i]=dict()
        ngram[i][word]=1
        ini=0
        for k in range(i,n):
            l=len(list_word[ini])+1
            word=word[l:]
            word+="_"+list_word[k]
            ini+=1
            if word in ngram[i].keys():
                ngram[i][word]+=1
            else:
                ngram[i][word]=1

        # for jj in ngram[i]:
        #     print(str(jj)+" "+str(ngram[i][jj]))
        # print("\n")
        # print(a,end="~")

        for jj in ngram[i]:
            print(a+","+str(jj))
        # print("\n")





        
    
    
        
    
    
    
    

    
        
        

