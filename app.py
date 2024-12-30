import streamlit as st
import pandas as pd
import base64
from src.ai_insights import generate_insights
from src.visualization import plot_data


def set_background_image(image_file):
    with open(image_file, "rb") as f:
        img = f.read()
        b64 = base64.b64encode(img).decode()
        st.markdown(
             f"""  
             <style>  
             .stApp {{  
                 background-image: url(data:image/png;base64,{b64});  
                 background-size: cover;  
             }}  
             </style>  
             """,
             unsafe_allow_html=True
        )


set_background_image("assets/vector.png")

st.markdown(
    """
    <style>
        .stTextInput > label, .stMarkdown, .stText, .stTitle, .stHeader {
            color: #f5f5f5; /* Light gray text color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """  
    <div style="text-align: center;">
        <h1
            style='
                background: linear-gradient(to right, #ae00ff, #d175ff, #e3a4ff);
                -webkit-background-clip: text;
                color: transparent;
            '
        >
        DataSenseAI
        </h1>
        <p>Welcome to your AI-powered data insights app!</p>
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.markdown("### Dataset Preview")
    st.write(df.head())

    st.markdown("### Data Summary")
    summary = df.describe()
    st.write(summary)

    st.markdown("### Full Dataset")
    st.write(df)

    st.subheader("Select Columns to Visualize")
    columns = df.columns.tolist()
    # selected_columns = st.multiselect("Choose columns", columns)
    # Allow user to select x and y axes
    x_axis = st.selectbox("Select X-axis (optional)", ["None"] + columns)
    y_axis = st.selectbox("Select Y-axis", [None] + columns)

    if y_axis:
        st.write(f"### Visualize for: {y_axis}")

        if x_axis == "None":
            # Single column visualization
            if pd.api.types.is_numeric_dtype(df[y_axis]):
                # Numeric column: Box Plot or Violin Plot
                plot_type = st.selectbox(f"Select plot type for {y_axis}", ["Box Plot", "Violin Plot"])
                plot_data(df, x_axis, y_axis, plot_type)
            elif pd.api.types.is_string_dtype(df[y_axis]):
                # Categorical column: Bar Chart
                plot_data(df, x_axis, y_axis, "Bar")
            else:
                st.write(f"No visualization available for column: {y_axis}")
        else:
            # Two-column visualization
            if pd.api.types.is_numeric_dtype(df[x_axis]) and pd.api.types.is_numeric_dtype(df[y_axis]):
                # Numeric columns: Scatter Plot
                plot_data(df, x_axis, y_axis, "Scatter Plot")
            else:
                st.write("Both X and Y axes must be numeric for a Scatter Plot.")

    else:
        st.warning("You have to select the Y Axis first!", icon=":material/warning:")

    if st.button("Generate Insights"):
        insights = generate_insights(df)

        if insights == "Error generating insights.":
            st.error("Error generating insights please make sure you have a valid API key.", icon=":material/error:")
        else:
            st.markdown("### Insights")
            st.write(insights)
