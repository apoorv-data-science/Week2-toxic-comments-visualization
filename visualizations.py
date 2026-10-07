import matplotlib.pyplot as plt
import pandas as pd
from .config import TOXICITY_COLUMNS


def plot_toxicity_share(df: pd.DataFrame, output_path):
    """Create a donut chart for comments with at least one toxicity label."""
    flagged = df[TOXICITY_COLUMNS].sum(axis=1).gt(0)
    counts = [flagged.sum(), (~flagged).sum()]
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(counts, labels=["Toxic", "Non-toxic"], autopct="%1.1f%%", startangle=90,
           colors=["#d1495b", "#4f772d"], wedgeprops={"width": 0.42, "edgecolor": "white"})
    ax.set_title("Share of Comments Flagged as Toxic")
    fig.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_category_counts(df: pd.DataFrame, output_path):
    """Create a bar chart for toxicity-category frequency."""
    counts = df[TOXICITY_COLUMNS].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    counts.plot(kind="bar", ax=ax, color="#457b9d")
    ax.set_title("Toxicity Categories by Frequency")
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Comments")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
