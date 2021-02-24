n=int(input("n="))
L=2**(n+1)-1
j=0
i=0
b=0
#start para
para=[]
para.append(((L//2)+1)/2)
paracount=1
while paracount<(n-1)//2:
    para.append((L//(2**(len(para)+1))+1)/2+para[len(para)-1])
    paracount+=1
#fin para
count=1
print(para[0],para[0])
#first line
for x in range(L):
    print("#",end="")
j+=1
print("")
#main loop
while j<L-1:
    i=0
    while i<(L-1):
#1 condition
        if i==0:
            print("#",end="")
            i+=1
            continue
        for b in range(len(para)):
            if abs(i-L+1)+j==2*(para[b]+1)+L//(2**(b+2))-1 and n//2>b+1 and n>3 and j>para[b] and  j<=para[b]+L//(2**(b+2)) and i>=para[b]+L//(2**(b+2)) and i <para[b]+L//(2**(b+1))-1 :
                print("#",end="")
                i+=1
                break
            elif abs(i-L+1)+abs(j-L+1)==2*(para[b]+1)+L//(2**(b+2))-1 and n//2>b+1 and n>3 and j>=para[b]+L//(2**(b+2)) and j<para[b]+L//(2**(b+1))-1 and i>=para[b]+L//(2**(b+2)) and i <para[b]+L//(2**(b+1))-1:
                print("#",end="")
                i+=1
                break
            elif i+abs(j-L+1)==2*(para[b]+1)+L//(2**(b+2))-1 and n//2>b+1 and n>3 and i>para[b] and i<=para[b]+L//(2**(b+2)) and j>=para[b]+L//(2**(b+2)) and j<para[b]+L//(2**(b+1))-1:
                print("#",end="")
                i+=1
                break
            elif i+j==2*(para[b]+1)+L//(2**(b+2))-1 and n//2>b+1 and n>3 and i>para[b] and i <=para[b]+L//(2**(b+2)) and j>para[b] and j <=para[b]+L//(2**(b+2)):
                print("#",end="")
                i+=1
                break
            elif abs(i-L+1)+j==L//2+1 and n>1:
                print("#",end="")
                i+=1
                break
            elif abs(i-L+1)+abs(j-L+1)==L//2+1 and n>1:
                print("#",end="")
                i+=1
                break
            elif i+abs(j-L+1)==L//2+1 and n>1:
                print("#",end="")
                i+=1
                break
            elif i+j==L//2+1 and n>1:
                print("#",end="")
                i+=1
                break

#2,3 conditions
            elif (j==para[b] or j==para[b]+L//(2**(b+1))-1)  and i>para[b] and i<para[b]+L//(2**(b+1))-1 and n>2:
                while (j==para[b] or j==para[b]+L//(2**(b+1))-1)  and i>para[b] and i<para[b]+L//(2**(b+1))-1 and n>2:
                    print("#",end="")
                    i+=1
                break
            elif (i==para[b] or i==para[b]+L//(2**(b+1))-1)  and j>para[b] and j<para[b]+L//(2**(b+1))-1 and n>2:
                print("#",end="")
                i+=1
                break
            elif b==max(range(len(para))):
                print(".",end="")
                i+=1
                break
                
    print("#")
    j+=1
for x in range(L):
    print("#",end="")
            

