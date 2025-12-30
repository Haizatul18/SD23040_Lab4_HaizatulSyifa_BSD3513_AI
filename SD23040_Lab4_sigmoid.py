# File: SD23040_Lab4_sigmoid.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Sigmoid Activation Function")

# Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input
x = np.linspace(-10, 10, 400)
y = (x)

# Plot
plt.plot(x, y, label='sigmoid', color='pink')
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
st.pyplot(plt)