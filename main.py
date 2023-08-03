import streamlit as st
import numpy as np

st.header("Streamlit demo")

b = st.button('Click me')

if b:
    st.text(f'{np.random.rand(1)}')
