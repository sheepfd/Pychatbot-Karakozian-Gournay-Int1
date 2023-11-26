import os
import math
from collections import defaultdict


def list_of_files(directory, extension):
    files_names = []
    alldigits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename.split("_")[1].split(".")[0])
    for i in range(len(files_names)):
        if files_names[i][-1] in alldigits:
            files_names[i] = files_names[i][:-1]

    return list(set(files_names))


def lower_letter(file_name):
    contentV1 = ""  # Initialisation of content V1 because we have to change all upper letter by lower letter
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()  # Here it's all the text of the speech store in the variable content
    for i in content:
        if ord(i) > 64 and ord(i) < 91:  # It's the interval of the upper letter in ASCII
            contentV1 = contentV1 + chr(ord(i) + 32)  # +32 in order to change upper letter into lower letter
        elif i == 'É' :
            contentV1 = contentV1 + "é"
        else:
            contentV1 = contentV1 + i
    with open(f"Cleaned/{file_name.split('.')[0].split('/')[-1]}", "w",
              encoding="utf-8") as f:  # Create a New file with the New content
        f.write(contentV1)
    contentV2 = ""  # let's initialize a new variable in oder to change again and only have lower letter and nothing else
    for i in contentV1:
        if i == "-" or i == "'" or i == "." or i == "\n":
            contentV2 = contentV2 + " "
        elif ord(i) > 95 and ord(i) < 123 or ord(i) == 32 or i in "ùàéèôûîâêçŒœ" and not (i in ";:!?'"):
            contentV2 = contentV2 + i

    with open(f"Cleaned/{file_name.split('.')[0].split('/')[-1]}",
              "w", encoding="utf-8") as f:  # change the file with the New content
        f.write(contentV2)


def tf(string):
    dictionary = dict()
    string = list(string.split(" "))
    key_word = set(string) #use a set to have only one time each word
    for i in key_word:
        count = 0
        for j in string:
            if j == i:
                count += 1
            dictionary[i] = count
    del dictionary[""] # delete element with keys nothing (little bug corrected)

    return dictionary


def idf(directory):
    num_files = 8  # like the number of files is constant let's initialise it now
    all_speeches = ""
    dico_score = defaultdict(int) #use of "collection" module tu be able to inisialize integer in the dictionarie to then be able to increment 
    for filename in os.listdir(directory):
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
            speech = f.read()
        all_speeches += speech
    words = set(tf(all_speeches).keys()) # use a set of all speeches getting the words of them calling the tf function to be able to use them as keys for the dico score
    for filename in os.listdir(directory):
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f: # loop to read the content of one file by one
            speech = f.read()
        speech = tf(speech).keys() # get all the word in the file using keys of the tf function
        for a in words:
            if a in speech: #read all words in a file calling the keys of tf function to check if a word in all words in the folder is in the document
                dico_score[a] += 1
    for key, value in dico_score.items(): # create the dictionary associating the IDF score with each word
        dico_score[key] = round(math.log10(num_files / value) + 1, 5)
    return dico_score


def Tf_idf(directory):
    score_tf_idf = dict()
    list_of_dict_tf_idf=[]
    count=0
    all_speeches =""
    list_score = []
    TF_IDF_matrix=[]
    idf_score = idf(directory)
    for filename in os.listdir(directory):
        score_tf_idf = dict()
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
            speech = f.read()
            all_speeches += speech
        speech = tf(speech) # create a set of all
        for key, value in speech.items():
            score_tf_idf[key] = value * idf_score[key] # computation of the td_idf score
        list_of_dict_tf_idf.append(score_tf_idf) # create a list of dictionaries where each row represent the tf_idf score for each word of each document of the folder
    words = set(tf(all_speeches).keys()) # set of all words to be able to know all the words in all documents and then use them as key to create the TF_IDF_matrix
    for i in range(len(list_of_dict_tf_idf)):
        for a in words:
            if a in list_of_dict_tf_idf[i].keys():
                TF_IDF_matrix.append(list_of_dict_tf_idf[i][a])

    return(TF_IDF_matrix,list_of_dict_tf_idf)
    









