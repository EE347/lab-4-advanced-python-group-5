import csv

with open("task5.csv", "w",newline='') as csvfile:
    while 1 :
        name = str(input("What is your name?"))
        if name == "quit":
            break
        
        writer = csv.writer(csvfile)
        writer.writerow([name," "])

with open("task5.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
