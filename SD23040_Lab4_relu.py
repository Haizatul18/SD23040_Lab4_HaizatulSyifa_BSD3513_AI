# File: SD23040_Lab4_relu.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("ReLU Activation Function")

# Define ReLU
def relu(x):
    return np.maximum(0, x)

# Input
x = np.linspace(-10, 10, 400)
y = relu(x)

# Plot
plt.plot(x, y, label='ReLU', color='blue')
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
st.pyplot(plt)