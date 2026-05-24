import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))

    sns.histplot(df[column], kde=True)

    plt.title(f"{column} Distribution")

    plt.show()


def plot_countplot(df, column):
    plt.figure(figsize=(8, 5))

    sns.countplot(x=df[column])

    plt.title(f"{column} Count Plot")

    plt.xticks(rotation=45)

    plt.show()


def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    plt.figure(figsize=(14, 10))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.show()