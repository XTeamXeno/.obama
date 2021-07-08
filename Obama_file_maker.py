import pickle

# determin vars
print("What do you want to turn into a .obama file?")
save = input()
print("What do you want to name this file?")
name = input()
name = name + ".obama"
print("Your save data is,", save, "and your name is,", name, "ENTER to continue")
input() 

# picker script
with open(name,"wb") as obama_pickler:
    pickle.dump(save,obama_pickler, 5)
print("Done! (Press enter to exit)")
input()
exit("Done")