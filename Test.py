from functions1 import *

"""with open('Cleaned/Nomination_Chirac1',"r",encoding="utf-8") as f :
    speech = f.read()"""
idf_score("Cleaned")
a = list_of_files("./Speeches","txt")
for filename in os.listdir("Speeches"):
    lower_letter(f'Speeches/{filename}') # in order to fill completly the folder Cleaned

"""with open("Speeches/Nomination_Chirac.txt","r") as f:
    content= f.read()
    print(content)"""