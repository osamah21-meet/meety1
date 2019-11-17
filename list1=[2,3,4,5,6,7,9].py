list1=[2,3,4,5,6,7,9,11]
list2=[55,22,33,43,3,4,11]
list3=[]
def matching_finder(list1,list2):
	t=len(list1)
	d=len(list2)
	i=0
	c=0
	for i in range(t) :
		for c in range (d):
			if list1[i]==list2[c]:
				print (list1[i])
				list3.append(list1[i])

		c+=1
	i+=1
	c=0

matching_finder(list1,list2)
print (list3)

b=0
sum=0
k=len(list3)
for b in range (k):
	sum=sum+list3[b]
	b+=1
print (sum)