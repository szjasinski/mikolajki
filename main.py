# mikołajki
import base64

import streamlit as st
import pandas as pd
from numpy import random
import numpy as np


def get_mikolajkowy_df(givers_list=None, not_together_list=None):

    if not_together_list:
        separation = not_together_list + [(y, x) for x, y in not_together_list]
    indexes = np.array([n for n in range(len(givers_list))])
    pairs = [()]

    i = 0
    for _ in range(1000):
        i += 1
        random.shuffle(indexes)
        receivers = [givers_list[i] for i in indexes]
        pairs = [(giver, receiver) for giver, receiver in zip(givers_list, receivers)]

        t = 0
        for pair in pairs:
            if not_together_list:
                if pair in separation:
                    t += 1
            if pair[0] == pair[1]:
                t += 1
        if t == 0:
            break

    if i == 1000:
        pairs = [(":(", ":(") for x, y in zip(givers_list, receivers)]
        return pd.DataFrame(pairs, columns=['Daje prezent', 'Otrzymuje prezent'])

    df = pd.DataFrame(pairs, columns=['Daje prezent', 'Otrzymuje prezent'])
    return df


st.title('Mikołajki :))))')

colA1, colA2 = st.columns(2)

names_value = "Sławek\nAxel\nKacper\nKuba\nMaciek\nMagda\nMania\nKuczaj\nPiotrula\nSzymon\nWera\nŁukasz\nSylwia\nArtur"
not_together_value = "Kuczaj,Magda\nMaciek,Mania\nKuba,Wera\nSylwia,Artur"

with colA1:
    names_input = st.text_area("Osoby", value=names_value, height=400)

with colA2:
    not_together_input = st.text_area("Oni sie nie wylosuja", value=not_together_value, height=400)


if st.button("ZATWIERDZ OSOBY I PARY"):

    if len(names_input) > 0:
        textsplit = names_input.splitlines()
        st.session_state.names = textsplit

    if len(not_together_input) > 0:
        try:
            not_together_list = [(pair.split(',')[0], pair.split(',')[1]) for pair in not_together_input.splitlines()]
            st.session_state.not_together_list = not_together_list
        except IndexError:
            st.write("Wpisz osoby oddzielone przecinkami")
    else:
        st.session_state.not_together_list = None


if st.button("LOSUJ"):
    if 'names' in st.session_state and 'not_together_list' in st.session_state:
        if 'randomized_df' not in st.session_state:
            st.session_state.randomized_df = get_mikolajkowy_df(givers_list=st.session_state.names, not_together_list=st.session_state.not_together_list)

        df = st.session_state.randomized_df
        st.dataframe(df, use_container_width=True, height=len(df)*35 + 35)

