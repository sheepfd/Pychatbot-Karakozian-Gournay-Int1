from functions1 import *
question = "bonjour je m'appelle jean je ta si ok non si france " #input("Write your question : ")
name_of_files = real_list_of_file("./Speeches")
mat_of_dict=Tf_idf("cleaned")
mat_of_dict.append(TF_IDF_question_dico(question))
print(mat_of_dict)

mat=[]
for i in range(len(mat_of_dict)):
    row=[]
    for key,val in mat_of_dict[len(mat_of_dict)-1].items():
        if key in mat_of_dict[i]:
            row.append(mat_of_dict[i][key])
        else:
            row.append(0)
    mat.append(row)

