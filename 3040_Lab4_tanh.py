# File: SD23040_Lab4_tanh.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Tanh Activation Function")

# Tanh
def tanh(x):
    return np.tanh(x)

# Input
x = np.linspace(-10, 10, 400)
y = tanh(x)

# Plot
plt.plot(x, y, label='Tanh', color='green')
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
st.pyplot(plt)