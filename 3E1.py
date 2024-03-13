word = input("Give me a word:")
hline = "+"
line = "|"
for char in word:
    hline += "---+"
    line += "{:^3}|".format(char)
print(hline+"\n"+line+"\n"+hline)
