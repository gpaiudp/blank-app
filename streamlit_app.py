import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim((0, 2))
ax.set_ylim((-2, 2))
line, = ax.plot([], [], lw=2)

# Define the animation function
def animate(i):
    # Compute the x and y coordinates for the i-th frame
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    # Set the data for the line object
    line.set_data(x, y)
    return line,

# Create the animation object
# frames=100 specifies the number of frames
# interval=20 is the delay in milliseconds between frames
anim = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

# Show the plot
plt.show()





import streamlit as st

st.title("🎈 My new ganesha app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
