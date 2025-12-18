import zeinebviz
import numpy as np

# ---- 1. Line ----
zeinebviz.styled_line(
    x=[1, 2, 3, 4],
    y=[2, 5, 3, 6],
    title="Line Plot",
    color="#e74c3c"  # rouge vif
)

# ---- 2. Bar ----
zeinebviz.styled_bar(
    x=["A", "B", "C", "D"],
    y=[5, 3, 7, 2],
    title="Bar Plot",
    color="#3498db"  # bleu
)

# ---- 3. Scatter ----
zeinebviz.styled_scatter(
    x=[1, 2, 3, 4],
    y=[4, 1, 3, 5],
    title="Scatter Plot",
    color="#2ecc71"  # vert
)

# ---- 4. Histogram ----
data = np.random.randn(100)
zeinebviz.styled_hist(
    data,
    title="Histogram Plot",
    color="#9b59b6"  # violet
)

# ---- 5. Boxplot ----
data2 = np.random.randn(20)
zeinebviz.styled_box(
    data2,
    title="Boxplot",
    color="#f1c40f"  # jaune
)
