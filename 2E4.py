hline = "+---+--------------------+------+----------+"
header = "|No.|Name (en)           |Symbol|Weight (u)|"
pt = [(1,"Hydrogen","H",1),(2,"Helium","He",4),(3,"Lithium","Li",7),(4,"Beryllium","Be",9),(5,"Boron","B",11),(6,"Carbon","C",12),(7,"Nitrogen","N",14),(8,"Oxygen","O",16),(9,"Fluorine","F",19),(10,"Neon","Ne",20)]
print(hline+"\n"+header+"\n"+hline)
for x in pt:
    line = "|{:>3}|{:<20}|{:^6}|{:>10}|".format(*x)
    print(line)
print(hline)
