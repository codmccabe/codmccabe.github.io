import numpy as np
import matplotlib.pyplot as plt
import mplcursors

def plot_parabola(event):
    x = np.linspace(-5, 5, 400)
    y = x**2

    plt.figure()
    plt.plot(x, y)
    plt.title('Interactive Parabola')
    plt.xlabel('x')
    plt.ylabel('y = x^2')
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

    # Add interactive cursor to pick points
    mplcursors.cursor(hover=False).connect(
        "add", lambda sel: sel.annotation.set_text(f"({sel.target[0]:.2f}, {sel.target[1]:.2f})")
    )

    plt.show()

plot_parabola(None)
