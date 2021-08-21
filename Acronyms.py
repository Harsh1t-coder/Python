phrase= input("Enter a phrase: ")
text = phrase.split()
ac = ""
for i in text:
    ac = ac + str(i[0]).upper()
print(ac)
