import math
n = 2022
x = math.pi
word = "Python"
polish = "książka"
outfile = open("outfile.txt","w",encoding="utf-8")

outfile.write("{}\n{}\n{}\n{}".format(n,x,word,polish))
print("{}\n{}\n{}\n{}".format(n,x,word,polish))
