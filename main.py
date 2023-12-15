from functions1 import *
question = input("Write your question : ")
question = set(question)

set_all_speeches = set(list(all_speech("Cleaned").split(" ")))
print(question - set_all_speeches)


