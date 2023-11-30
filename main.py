# mikołajki
import streamlit as st
import pandas as pd
from numpy import random
import numpy as np

givers = ["osoba" + str(n) for n in range(1, 5)]
conflicted_people = [("osoba1", "osoba2"), ("osoba3", "osoba4")]
conflict = conflicted_people + [(y, x) for x, y in conflicted_people]

indeksy = np.array([n for n in range(len(givers))])

pairs = [()]
for _ in range(1000):
    random.shuffle(indeksy)
    print(indeksy)

    receivers = [givers[i] for i in indeksy]
    pairs = [(giver, receiver) for giver, receiver in zip(givers, receivers)]

    t = 0
    for pair in pairs:
        if pair in conflict:
            t += 1
        if pair[0] == pair[1]:
            t += 1
    if t == 0:
        print("Udało się:)")
        print(pairs)
        break
    else:
        print("Próbujemy dalej:)")
        print("Konflikty... ", pairs)

df = pd.DataFrame(pairs, columns=['Daje prezent', 'Otrzymuje prezent'])

st.write(df)