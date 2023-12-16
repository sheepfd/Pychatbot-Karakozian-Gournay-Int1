from functions1 import *
question = "Comment une nation peut-elle prendre soin du climat ?" #input("Write your question : ")
question += question + " "
name_of_files = real_list_of_file("./Speeches")
mat_of_dict=Tf_idf("cleaned")
#append the tf_idf of the question in a dicsionary with the ones of all the corpus so we don't have problem of random index for each word
mat_of_dict.append(TF_IDF_question_dico(question))

#creation of a matrix with tf idf of the corpus and the qestion in the end of it
mat_corpus_question=[]
for i in range(len(mat_of_dict)):
    row=[]
    for key,val in mat_of_dict[len(mat_of_dict)-1].items():
        if key in mat_of_dict[i]:
            row.append(mat_of_dict[i][key])
        else:
            row.append(0)
    mat_corpus_question.append(row)

mostrevelentdoc = most_relevant_document(mat_corpus_question)
print(mostrevelentdoc)
print(TF_IDF_question_dico(question))
maxi_tf_idf_question= highest_tf_idf(TF_IDF_question_dico(question))
print(maxi_tf_idf_question)
"""for key,value in dico_text_ini('Speeches').items():
    for a in value:
        if maxi_tf_idf_question in a:
            print(a)
    break
"""
"""print(type(mostrevelentdoc))
print(text_ini(mostrevelentdoc))"""

answer=[]
for a in text_ini(mostrevelentdoc):
    if maxi_tf_idf_question in a:
        answer.append(a)

print(answer[0])
