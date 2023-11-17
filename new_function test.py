import os


def list_of_files2(directory, extension):

    files_names = []
    alldigits=[1,2,3,4,5,6,7,8,9,0]
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename.split("_")[1].split(".")[0])
    for i in range (len(files_names)):
        if files_names[i][-1] in alldigits:
            files_names[i]=files_names[i][-1]

    return files_names