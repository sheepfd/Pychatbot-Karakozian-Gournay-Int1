"""
name of the project : Pychatbot-Karakozian-Gournay-Int1
authors : Paul Gournay, Vrej Karakozian
role this file : Use for the chatbot + features
comment :  Here you can see the menu where you have to choice between the option 1 by inputing 1 or the option 2 byinputing 2. If you select option 1, 
you gain access to the seven available features. Alternatively, if you choose option 2, you can interact with the chatbot and freely ask it any questions you may have.
"""


from functions1 import *

Menu="////////////////////Menu//////////////////// \n-Type 1 if you want to access the Features \n-Type 2 to Access Chatbot mode"
print(Menu)
choice=int(input("Enter your choicec here:"))

#//////////////////////////////////////////////////features//////////////////////////////////////////////////
if choice==1:
    print("////////////////////Features Mode////////////////////")
    feature = int(input("Enter the number of the feature: "))
    #1.
    if feature==1:
        count= 0
        a = Tf_idf("Cleaned")
        least_important = []
        for i in a :
            for key,value in i.items():
                if value == 0:
                    least_important.append(key)
        least_important = set(least_important)
        least_important = list(least_important)
        print(least_important) #['mesdames', 'se', 'aux', 'messieurs', 'il', 'faire', 'j', 'france', 'histoire', 'mais', 'son', 'par', 'peuple']"""
    #2.
    elif feature==2:
        a = Tf_idf("Cleaned")
        word=tuple()
        max = 0
        for i in a:
            for key,value in i.items():
                if value > max:
                    max = value
                    word= (key,value)
        print(word) # in the output('la', 81.0)"""

    #3.
    elif feature==3:
        max = 0
        word = ()
        with open("Cleaned/Nomination_Chirac1","r",encoding = 'utf-8') as f:
            speech1 = f.read()
        with open("Cleaned/Nomination_Chirac2","r",encoding = 'utf-8') as f:
            speech2 = f.read()
        speech = tf(speech1 +speech2)
        for key,value in speech.items():
            if value > max:
                max = value
                word= (key,value)
            if value == max: #in order to verify if there no other value which equal to the gratest one
                print(value)
        print(word) #output ('de', 97)

    #4
    elif feature==4:
        max=0
        count = 0
        president = ()
        for filename in os.listdir("Cleaned"):
            with open(f"Cleaned/{filename}", "r", encoding="utf-8") as f:
                speech = f.read()
            speech = tf(speech)
            for key,value in speech.items():
                if key == "nation":
                    print(filename.split("_")[1]) # Output: Nomination_Chirac1, Nomination_Chirac2, Nomination_Hollande, Nomination_Macron, Nomination_Mitterrand2
                    if max < value:
                        max = value
                        president = (max,filename)
        print(president) # Output : (4, 'Nomination_Chirac2')  like it's Chirac no need to sum his 2 speeches because he is already the one who say it the more


    #5.
    elif feature==5:
        for filename in os.listdir("Cleaned"):
            with open(f"Cleaned/{filename}", "r", encoding="utf-8") as f:
                speech = f.read()
            speech = tf(speech)
            for key in speech.keys():
                if key == "climat" or key == "écologie":
                    print(filename.split("_")[1]) # Output: Nomination_Macron he is the only one thus he is at same the time the first one """
    #6
    elif feature==6:
        list_word_all_president_mention=[]
        idf_score=idf("Cleaned")
        word_in_all_doc=[]
        for key,val in idf_score.items():
            if val==0:
                word_in_all_doc.append(key)
        a = Tf_idf("Cleaned")
        least_important = []
        for i in a:
            for key, value in i.items():
                if value == 0:
                    least_important.append(key)
        least_important = list(set(least_important))
        for word in word_in_all_doc:
            if word not in least_important:
                list_word_all_president_mention.append(word)
        print(list_word_all_president_mention)

    else:
        print("this feature does not exist")

elif choice==2:
    print("////////////////////Super Chatbot Mode////////////////////")
    question = input("Write your question : ")  # This variable will take the user's question
    question += question + " "  # The porpuse of this space at the end is to make sure taht the last character/word is well undestand by out script

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

    maxi_tf_idf_question= highest_tf_idf(TF_IDF_question_dico(question)) # store the word with highest score tf idf of the question



    answer=[] #store the answer in a list because there many answer and like we want the first one we just have to print answer[0]
    for a in text_ini(mostrevelentdoc):
        if maxi_tf_idf_question in a:
            answer.append(a)

    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!",
        "Quand": "À ce moment-là, ",
        "Où": "À cet endroit, ",
        "Qui": "La personne en question est ",
        "Quoi": "En termes simples, ",
        "Combien": "Le nombre exact est ",
        "S'il te plaît": "Bien sûr, ",
        "Pourrais-tu": "Si cela vous convient, ",
        "Merci": "Je vous en prie!",
        "Excuse-moi": "Pas de problème, ",
        "Désolé": "Je m'excuse pour ",
        "Bonjour": "Bonjour! Comment puis-je vous aider aujourd'hui?",
        "Bonsoir": "Bonsoir! Comment puis-je vous assister?",
        "Au revoir": "Au plaisir de vous revoir bientôt!",
        "S'il vous plaît": "Veuillez ",
        "Merci beaucoup": "Merci infiniment!",
        "Je vous en prie": "De rien, ",
        "Excusez-moi": "Excusez-moi pour ",
        "Pouvez-vous": "Oui, je peux ",
        "Je ne peux pas": "Malheureusement, je ne peux pas ",
        "Je ne sais pas": "Je suis désolé, je ne sais pas ",
        "C'est possible": "Oui, c'est possible ",
        "Je ne suis pas sûr": "Je ne suis pas sûr, ",
        "Peux-tu m'aider": "Bien sûr, je peux vous aider à ",
        "Fais-tu cela": "Oui, je fais cela ",
    }
    final_answer=""

    for key,val in question_starters.items():
        if key in question :
            final_answer+=val+" "

    final_answer=final_answer+answer[0]+"."

    print(final_answer)
print("programmed by Vrej KARAKOZIAN and Paul GOURNAY")
