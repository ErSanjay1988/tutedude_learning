val=input("Enter text to write to the file:")
file=open('Assignment4/Output.txt','w')
file.write(val+'\n')
file.close()
print("Data successfully written to output.txt")

appendVal=input("Enter additional text to append:")
file=open('Assignment4/Output.txt','a')
file.write(appendVal+'\n')
file.close()
print("Data successfully appended.")

print("Final content of output.txt")
with open('Assignment4/Output.txt','r') as file:
  for line in file:
   print(line)
file.close()
