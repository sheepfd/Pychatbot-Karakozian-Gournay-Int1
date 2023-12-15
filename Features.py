from functions1 import *
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

