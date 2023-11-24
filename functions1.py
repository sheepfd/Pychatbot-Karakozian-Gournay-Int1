import os
import math
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
    contentV1 ="" #Initialisation of content V1 because we have to change all upper letter by lower letter
    with open(file_name,"r",encoding="utf-8") as f:
        content = f.read() #Here it's all the text of the speech store in the variable content
    for i in content:
        if ord(i)>64 and ord(i) <91 : # It's the interval of the upper letter in ASCII
            contentV1 = contentV1 + chr(ord(i)+ 32) # +32 in order to change upper letter into lower letter
        else:
            contentV1 =  contentV1 + i
    with open(f"Cleaned/{file_name.split('.')[0].split('/')[-1]}","w",encoding="utf-8") as f: #Create a New file with the New content
        f.write(contentV1)
    contentV2 = "" #let's initialize a new variable in oder to change again and only have lower letter and nothing else
    for  i in contentV1:
        if i == "-" or  i == "'" or i == "." or i == "\n" :
            contentV2= contentV2 + " "
        elif ord(i) >95 and ord(i)<122 or ord(i) == 32   or i in "ùàéèôûîÉâêçŒœ" and not(i in ";:!?'") :
            contentV2 = contentV2 + i

    with open(f"Cleaned/{file_name.split('.')[0].split('/')[-1]}",
              "w",encoding="utf-8") as f:  # change the file with the New content
        f.write(contentV2)

def tf(string):
    dictionary = dict()
    string = list(string.split(" "))
    key_word=set(string)
    for i in key_word:
        count = 0
        for j in string:
            if j == i:
                count+=1
            dictionary[i]=count
    del dictionary[""]

    return dictionary

def idf_score(directory):
    num_words=0 # create a variable in order to keep all number of words for after
    num_files=8 # like the number of files is constatn let's initialaze now
    all_speeches =""
    dico_score =dict()
    occuracy = 0
    i= 0
    for filename in os.listdir(directory):

        with open(f"{directory}/{filename}","r", encoding="utf-8") as f:
            speech = f.read()
        all_speeches += speech
        words = set(tf(all_speeches).keys())
        for a in words:
            if a in tf(speech).keys():
                occuracy+=1
            dico_score[a]= occuracy
        print(i)
        i+=1


















