import pickle

print("What was the name of the .obama file that you want to open (w/o the .obama at the end)(eg 'savefile' instead of 'savefile.obama'")
import_name = input()
import_name = import_name + ".obama"
imported = pickle.load(open(import_name,"rb"))
print(imported)
input()