def match(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list.append(word)
    print("first and last elements are same",list)
    return ctr 
count=match(['abc','cbc','def','1221'])
print("number of words with same first and last characters are",count)