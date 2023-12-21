from functions1 import *
test_number=int(input("enter the demo number"))

if test_number==2:
    print(Tf_idf("Cleaned"))
    print(len(Tf_idf("Cleaned")))
    print(TF_IDF_matrix("Cleaned"))
    print(len(TF_IDF_matrix("Cleaned")))