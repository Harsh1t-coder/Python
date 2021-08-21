inp = input("Enter a phrase ")
text = inp.split()
a = ""
for i in text:
    a  = a + str(i[0]).upper()
print(a)