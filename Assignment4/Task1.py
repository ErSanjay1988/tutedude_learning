# to verify and read existing text file.
try:
 with open(f'Assignment4/Sample.txt','r') as file:
        print("Reading file content")
        for line_number, line_content in enumerate(file, 1): 
            print(f"Line {line_number}: {line_content.strip()}") 
 file.close() 
except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found.") 

        