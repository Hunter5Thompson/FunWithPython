import numpy as np
import pandas as pd

bestand = pd.read_html('https://de.m.wikipedia.org/wiki/Lockheed_A-12')
len(bestand)
print(len(bestand))
print(bestand[1])


pd.read_csv