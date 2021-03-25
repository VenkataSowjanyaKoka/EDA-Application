import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title

header =  st.beta_container()
tools = st.beta_container()

with header:
    st.title("Web Application for Exploratory Data Analysis")
    st.markdown("Exploratory data analysis gives us an idea of all the details in the dataset, through which we can get a complete idea of what information we already have and need to have in order to perform further analysis or build a model.")
    st.markdown("---")

with tools:
    st.subheader("** How does it work? **")
    st.markdown("- Upload or drag and drop a csv file in the top left corner slider option")
    st.markdown("- You can also click on **Press to use Example Dataset** below to of example dataset")
    st.markdown("- Wait for few seconds to see your EDA report (_**Time taken to generate report depends on size of file**_)")
    st.markdown("---")

# Upload CSV data

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""[Example CSV input file](https://raw.githubusercontent.com/VenkataSowjanyaKoka/EDA-Application/main/grades%20(1).csv)""")
    st.markdown("---")

# Pandas Profiling Report

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
    st.markdown("---")

else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.read_csv("https://raw.githubusercontent.com/VenkataSowjanyaKoka/EDA-Application/main/grades%20(1).csv")
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
        st.markdown("---")

st.markdown("\n")
st.markdown(" _**Built using**_  `Python` + `Streamlit`  _**by**_  [Venkata Sowjanya Koka](https://www.linkedin.com/in/venkata-sowjanya-koka)</h5>", unsafe_allow_html=True)
st.markdown("---")
