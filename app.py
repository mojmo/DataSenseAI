import streamlit as st
import pandas as pd
import base64
from src.ai_insights import generate_insights


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

    if st.button("Generate Insights"):
        insights = generate_insights(df)
        st.markdown("### Insights")
        st.write(insights)
