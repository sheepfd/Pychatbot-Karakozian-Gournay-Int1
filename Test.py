from functions1 import *

"""with open('Cleaned/Nomination_Chirac1',"r",encoding="utf-8") as f :
    speech = f.read()"""
"""print(lower_letter("mlkqdsfjkmqslf lksqfdjmqdsflj mkqsfdlmsâdflj sdsf'mklfjrmmklaezjmeazkljmlkezr 'fdmslkjf qsdmfkjqdfsml O' ''' HJDOFH MDJoéklfm"))"""
a = list_of_files("./Speeches","txt")
for filename in os.listdir("Speeches"):
    Cleanedfile(f'Speeches/{filename}') # in order to fill completly the folder Cleaned
print(len(TF_IDF_matrix("Cleaned")))
"""with open("Speeches/Nomination_Chirac.txt","r") as f:
    content= f.read()
    print(content)"""
"""print(TF_IDF_question(""))"""
"""print(Tf_idf('Cleaned'))
print(TF_IDF_question(""))"""

print(dico_text_ini('Speeches'))
