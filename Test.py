from functions1 import *

a = list_of_files("./Speeches","txt")
for filename in os.listdir("Speeches"):
    lower_letter(f'Speeches/{filename}')