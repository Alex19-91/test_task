import os

files_ext = dict()

while True:
    folder = input("Please enter dir path (example: '/'Users/test/Desktop/dir'): ")
    if os.path.exists(folder) == False:
        print("Sorry, folder does not exist")
        continue
    else:
        break

for root, dirs, files in os.walk(folder, topdown=True, onerror=None, followlinks=False):  
    for filename in files:
        file_extension = filename.rsplit('.', 1)[-1]
        if file_extension not in files_ext:
            files_ext[file_extension] = 1;
        else:
            files_ext[file_extension] = files_ext[file_extension] + 1;
        

for elem in sorted(files_ext.items() , reverse=True, key=lambda x: x[1]):
    print(elem[0], elem[1]) 

