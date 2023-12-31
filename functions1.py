"""
name of the project : Pychatbot-Karakozian-Gournay-Int1
authors : Paul Gournay, Vrej Karakozian
role this file : Create every necessary function for our chatbot in
comment :  here we stocked every funtions that we created and that we will use for our porject in main. All the functions are well described inside the file itself.
"""




import os
import math
from collections import defaultdict

def real_list_of_file(directory): # give a list of file  of the directory : input string return  list 1d of files
    files_names = []
    for filename in os.listdir(directory):
        files_names.append(filename)
    return files_names
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


def Cleanedfile(file_name): #this function is used for take all files of a directory change the content without punctuation and caps into a new directory which is 'Cleaned' : file_name is a string parameter is here to take the filename of the files of the directory, then change it direclty so no need to return anything.
    contentV1 = ""  # Initialisation of content V1 because we have to change all upper letter by lower letter
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()  # Here it's all the text of the speech store in the variable content
    for i in content:
        if ord(i) > 64 and ord(i) < 91:  # It's the interval of the upper letter in ASCII
            contentV1 = contentV1 + chr(ord(i) + 32)  # +32 in order to change upper letter into lower letter
        elif i == 'É':
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


def lower_letter(string): #this function converts a given string to lowercase and removes punctuation : so it takes a string and return a string 
    new_string = ""
    for i in string:
        if ord(i) > 64 and ord(i) < 91:  # It's the interval of the upper letter in ASCII
            new_string = new_string + chr(ord(i) + 32)  # +32 in order to change upper letter into lower letter
        elif i == 'É':
            new_string = new_string + "é"
        elif i == "-" or i == "'" or i == "." or i == "\n" or i in ";:!?'" or i in '"':
            new_string = new_string + " "
        elif ord(i) > 95 and ord(i) < 123 or ord(i) == 32 or i in "ùàéèôûîâêçŒœ" and not (i in ";:!?'"):
            new_string = new_string + i
        else:
            new_string = new_string + i
    new_string = list(new_string.split(" "))
    len_string = len(new_string)
    count = 0
    for i in range(0, len_string):
        if new_string[i - count] == "":
            new_string.remove("")
            count += 1
    return new_string

def tf(string): #Calculates the frequency of each word in a given string and returns a dictionary: The input string and the return A dictionary where keys are words and values are their respective frequencies
    dictionary = dict()
    string = list(string.split(" "))
    key_word = set(string)  # use a set to have only one time each word
    for i in key_word:
        count = 0
        for j in string:
            if j == i:
                count += 1
            dictionary[i] = count
    del dictionary[""]  # delete element with keys nothing (little bug corrected)

    return dictionary


def idf(directory): #compute the score idf for every words in a directory : input a string (name of the directory) return a dictionary with key unique word of all the corpus (str) and as value the idf score (float)
    num_files = 8  # like the number of files is constant let's initialise it now
    all_speeches = ""
    dico_score = defaultdict(
        int)  # use of "collection" module to be able to inisialize integer in the dictionarie to then be able to increment
    for filename in os.listdir(directory):
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
            speech = f.read()
        all_speeches += speech
    words = set(
        tf(all_speeches).keys())  # use a set of all speeches getting the words of them calling the tf function to be able to use them as keys for the dico score
    for filename in os.listdir(directory):
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:  # loop to read the content of one file by one
            speech = f.read()
        speech = tf(speech).keys()  # get all the word in the file using keys of the tf function
        for a in words:
            if a in speech:  # read all words in a file calling the keys of tf function to check if a word in all words in the folder is in the document
                dico_score[a] += 1
    for key, value in dico_score.items():  # create the dictionary associating the IDF score with each word
        dico_score[key] = round(math.log10(num_files / value), 5)
    return dico_score


def Tf_idf(directory): # compute the tf_idf score in a given file for every unique word : input a string (name of the directory) so return a list 2d  of dictionaries where each row represent the tf_idf score for each word of each document of the folder
    score_tf_idf = dict()
    list_of_dict_tf_idf = []
    count = 0
    all_speeches = ""
    list_score = []
    TF_IDF_matrix = []
    idf_score = idf(directory)
    for filename in os.listdir(directory):
        score_tf_idf = dict()
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
            speech = f.read()
            all_speeches += speech
        speech = tf(speech)  # create a set of all
        for key, value in speech.items():
            score_tf_idf[key] = value * idf_score[key]  # computation of the td_idf score
        list_of_dict_tf_idf.append(
            score_tf_idf)  
    return (list_of_dict_tf_idf)


def TF_IDF_matrix(directory):  #compute the tf_idf score in a given file for every unique word : input a string (name of the directory) so return a list 2d  where list each row represents a word and each column represents a document
    all_speeches = ""
    TF_IDF_matrix = []
    TF_IDF_matrix_inverted = []
    for filename in os.listdir(directory):
        score_tf_idf = dict()
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
            speech = f.read()
            all_speeches += speech
    words = set(
        tf(all_speeches).keys())  # set of all words to be able to know all the words in all documents and then use them as key to create the TF_IDF_matrix
    list_of_dict_tf_idf = Tf_idf("Cleaned")
    for a in words:
        row = []
        for i in range(len(list_of_dict_tf_idf)):
            if a in list_of_dict_tf_idf[i].keys():
                row.append(list_of_dict_tf_idf[i][a])
            else:
                row.append(0)  # add 0 if the word isn't in the document so each row has exactly 8 columns
        TF_IDF_matrix.append(row)
    return (TF_IDF_matrix)


# Part 2
def all_speech(directory): #all the content in str of each files of a directory : so input directory abd return all the content in one string
    all_speeches = ""
    for filename in os.listdir(directory):
        score_tf_idf = dict()
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
            speech = f.read()
            all_speeches += speech
    return all_speeches

def TF_IDF_question_dico(question): #Compute the Tf-Idf of the question and put it in a dictionary :take as input a string which is the question for creating and return a dictionary as key all words and as value tf idf score of each word of the question
    set_question = set(list(question.split(" ")))
    set_all_speeches = set(list(all_speech("Cleaned").split(" ")))
    intersection = set_question & set_all_speeches # we create two set one of the words of the question and one of the all string content of files in order to take their intersection
    if '' in intersection: # just for being sure that there is no '' our set
        intersection.remove('')
    tf_idf_question = dict()
    score_idf = idf('Cleaned')
    tf_question = tf(question)
    for key, value in score_idf.items():
        if key in intersection:
            tf_idf_question[key] = value * (tf_question[key]/len(tf_question))
        else:
            tf_idf_question[key] = 0
    return tf_idf_question

def TF_IDF_question_mat(question): #Compute the Tf-Idf of the question and put it in a matrix :take as input a string which is the question for creating and return a dictionary as key all words and as value tf idf score of each word
    set_question = set(list(question.split(" ")))
    set_all_speeches = set(list(all_speech("Cleaned").split(" ")))
    intersection = set_question & set_all_speeches
    if '' in intersection:
        intersection.remove('')
    tf_idf_question = dict()
    score_idf = idf('Cleaned')
    tf_question = tf(question)
    for key, value in score_idf.items():
        if key in intersection:
            tf_idf_question[key] = value * (tf_question[key]/len(tf_question))
        else:
            tf_idf_question[key] = 0
    mat_tf_idf=[]
    for val in tf_idf_question.values():
        mat_tf_idf.append(val)
    return mat_tf_idf

def scalar_product(vectorsA,vectorsB): #compute the scalar product between 2 list 1D : input 2 list 1D return the result of the saclar product (int)
    result = 0
    for i in range(len(vectorsA)):
        result += vectorsA[i] * vectorsB[i]
    return result

def calculate_norm(vectorsA): #compute the norm of a 1d list : input list 1d thus return a int

    norm = math.sqrt(sum(x ** 2 for x in vectorsA))# Calculate the Euclidean norm of the vector A
    if norm == 0 : # because in the computation of simlarity we use the norm as a denominator so it can't be equal to 0
        print("Sorry we can't answer your question")
        exit(0)
    return norm

def similarity(vectorsA,vectorsB): # just aply the formula given in the pdf wetween 2 list 1D in order to know the similarity a score : input : 2 1d list return a score(int)

    score=(scalar_product(vectorsA,vectorsB))/(calculate_norm(vectorsA)*calculate_norm(vectorsB))

    return score

def most_relevant_document(mat): #it'll search for the more similar file in the directory by using the using the previous score of similarity : input:matrix 2d list and return a string the name of the most similar file
    name_of_files = real_list_of_file("./Speeches")
    max=similarity(mat[0],mat[len(mat)-1])
    for i in range(len(mat)-1):
        similar=similarity(mat[i],mat[len(mat)-1])

        if max<similar:
            max=similar

            max_index=i
    return name_of_files[max_index]


def highest_tf_idf (dict): #it'll be use for computing the highest_tf_idf score of a dict, and be use in our main script to compute the highest_tf_idf score of the question : input a dict and as return it'll be the word whith the highest value
    max =0
    word = ""
    for key,value in dict.items():
        if value > max :
            max = value
            word = key
    return word

def text_ini(filename): # Get the content in str of one of the file in the directory Speeches : input: file name of one in 'Speeches'(str) return the content so also a string
    content =""
    directory= 'Speeches'
    with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
        content = f.read()
        content = content.replace("\n","").split(".")
    return content

