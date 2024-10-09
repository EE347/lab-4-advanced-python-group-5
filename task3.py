name = input('What is your name?')
with open("task3.txt", "a") as myfile:
    myfile.write("\n"+name)
