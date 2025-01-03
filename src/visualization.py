import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def plot_data(df, x_col, y_col, plot_type):
    plt.figure(figsize=(10, 6))
    plt.clf()  # Clear the previous plot to avoid overlap

    if plot_type == "Box Plot":
        sns.boxplot(y=df[y_col], color="#d175ff", orient="v")
    elif plot_type == "Violin Plot":
        sns.violinplot(y=df[y_col], color="#d175ff", orient="v")
    elif plot_type == "Bar":
        sns.countplot(y=y_col, data=df, color="#d175ff")
    elif plot_type == "Scatter Plot":
        sns.scatterplot(x=df[x_col], y=df[y_col], color="#d175ff")

    st.pyplot(plt)
