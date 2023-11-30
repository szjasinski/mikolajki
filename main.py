# mikołajki
import streamlit as st
import pandas as pd
from numpy import random
import numpy as np


def get_mikolajkowy_df():
    givers = ["Weronika", "Kuba", "Marta", "Szymon", "Emilka", "Filip", "Kacper", "Sławek", "Asia", "Sylwia", "Artur",
              "Axel", "Maciek", "Łukasz", "Kuczaj", "Helenka"]
    not_together = [("Weronika", "Kuba"), ("Marta", "Szymon"), ("Emilka", "Filip"), ("Sławek", "Asia"),
                         ("Sylwia", "Artur")]
    separation = not_together + [(y, x) for x, y in not_together]
    indexes = np.array([n for n in range(len(givers))])
    pairs = [()]

    for _ in range(1000):
        random.shuffle(indexes)
        receivers = [givers[i] for i in indexes]
        pairs = [(giver, receiver) for giver, receiver in zip(givers, receivers)]

        t = 0
        for pair in pairs:
            if pair in separation:
                t += 1
            if pair[0] == pair[1]:
                t += 1
        if t == 0:
            break

    df = pd.DataFrame(pairs, columns=['Daje prezent', 'Otrzymuje prezent'])
    return df


st.title('Mikołajki :))))')
if st.button("LOSUJ"):
    df = get_mikolajkowy_df()
    st.dataframe(df, use_container_width=True, height=600)





