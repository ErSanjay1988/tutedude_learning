#List 
org_list=[]
dup_list=[]
for i in range(1,11):
 org_list.append(i)
print("Original List:",org_list)
print("Extracted first five element:", org_list[0:5])
dup_list=org_list[0:5].copy()
print("Reversed Extracted Elements:",dup_list[::-1])