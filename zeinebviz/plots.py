import matplotlib.pyplot as plt

# ---- STYLE GLOBAL ----
def _apply_style():
    plt.rcParams.update({
        "figure.figsize": (7, 4),
        "axes.facecolor": "#f2f2f2",
        "axes.edgecolor": "#333333",
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
        "lines.linewidth": 2,
        "font.size": 11
    })

# ---- 1. LINE ----
def styled_line(x, y, title="", color="#2980b9"):
    _apply_style()
    plt.plot(x, y, marker="o", color=color)
    plt.title(title)
    plt.show()

# ---- 2. BAR ----
def styled_bar(x, y, title="", color="#ff7f0e"):
    _apply_style()
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.show()

# ---- 3. SCATTER ----
def styled_scatter(x, y, title="", color="#2ca02c"):
    _apply_style()
    plt.scatter(x, y, color=color)
    plt.title(title)
    plt.show()

# ---- 4. HIST ----
def styled_hist(data, title="", color="#9467bd"):
    _apply_style()
    plt.hist(data, bins=10, color=color)
    plt.title(title)
    plt.show()

# ---- 5. BOX ----
def styled_box(data, title="", color="#f39c12"):
    _apply_style()
    plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor=color))
    plt.title(title)
    plt.show()
import matplotlib.pyplot as plt

# ---- STYLE GLOBAL ----
def _apply_style():
    plt.rcParams.update({
        "figure.figsize": (7, 4),
        "axes.facecolor": "#f2f2f2",
        "axes.edgecolor": "#333333",
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
        "lines.linewidth": 2,
        "font.size": 11
    })

# ---- 1. LINE ----
def styled_line(x, y, title="", color="#2980b9"):
    _apply_style()
    plt.plot(x, y, marker="o", color=color)
    plt.title(title)
    plt.show()

# ---- 2. BAR ----
def styled_bar(x, y, title="", color="#ff7f0e"):
    _apply_style()
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.show()

# ---- 3. SCATTER ----
def styled_scatter(x, y, title="", color="#2ca02c"):
    _apply_style()
    plt.scatter(x, y, color=color)
    plt.title(title)
    plt.show()

# ---- 4. HIST ----
def styled_hist(data, title="", color="#9467bd"):
    _apply_style()
    plt.hist(data, bins=10, color=color)
    plt.title(title)
    plt.show()

# ---- 5. BOX ----
def styled_box(data, title="", color="#f39c12"):
    _apply_style()
    plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor=color))
    plt.title(title)
    plt.show()
