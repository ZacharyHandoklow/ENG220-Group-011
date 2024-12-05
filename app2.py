import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Gun Violence for Counties App")

# Use the file path from Colab
file_path = 'Gun Violence for Counties.csv'

# Check if the file exists
try:
    # Read the CSV file
    data = pd.read_csv(file_path)
    st.write("### Data Preview")
    st.dataframe(data)

    # Dropdown for selecting columns
    columns = data.columns.tolist()
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    # Dropdown for graph type
    graph_type = st.selectbox(
        "Select Graph Type",
        ["Line", "Scatter", "Bar", "Pie"]
    )

    # Plot button
    if st.button("Plot Graph"):
        fig, ax = plt.subplots()

        if graph_type == "Line":
            ax.plot(data[x_column], data[y_column], marker='o')
            ax.set_title(f"{y_column} vs {x_column} (Line Plot)")

        elif graph_type == "Scatter":
            ax.scatter(data[x_column], data[y_column])
            ax.set_title(f"{y_column} vs {x_column} (Scatter Plot)")

        elif graph_type == "Bar":
            ax.bar(data[x_column], data[y_column])
            ax.set_title(f"{y_column} vs {x_column} (Bar Chart)")
            plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

        elif graph_type == "Pie":
            # Pie chart only makes sense for single-column data
            if len(data[x_column].unique()) <= 10:  # Limit to 10 unique categories for readability
                plt.pie(
                    data[y_column],
                    labels=data[x_column],
                    autopct='%1.1f%%',
                    startangle=90,
                )
                plt.title(f"{y_column} (Pie Chart)")
            else:
                st.error("Pie chart requires fewer unique categories in the X-axis.")

        if graph_type != "Pie":
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            st.pyplot(fig)
        else:
            st.pyplot(plt)

    st.write("Tip: Ensure the selected columns are numeric for meaningful plots.")

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please ensure the file is available in the Colab environment.")
