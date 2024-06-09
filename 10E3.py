import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ["Hydrogen", "Hellium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]
symbols = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]
weights = [1.008, 4.00, 6.94, 9.01, 10.81, 12.01, 14.01, 16.00, 19.00, 20.18]
elem = {"Name": names, "Symbol": symbols, "Weight": weights}
pt = pd.DataFrame(elem, index = range(1,len(names)+1))
print(pt)
