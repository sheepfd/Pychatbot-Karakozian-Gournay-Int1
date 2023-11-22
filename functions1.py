import os

def list_of_files(directory, extension):

    files_names = []
    alldigits=["1","2","3","4","5","6","7","8","9","0"]
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename.split("_")[1].split(".")[0])
    for i in range (len(files_names)):
        if files_names[i][-1] in alldigits:
            files_names[i]= files_names[i][:-1]

    return list(set(files_names))
def lower_letter(file_name):
    contentV1 =""
    with open(file_name,"r") as f:
        content = f.read()
    for i in content:
        if ord(i)>64 and ord(i) <91:
            contentV1 = contentV1 + chr(ord(i)+ 32)
        else:
            contentV1 =  contentV1 + i
    with open(f"Cleaned/{file_name.split('.')[0].split('/')[-1]} Cleaned version ","a") as f:
        f.write(contentV1)
