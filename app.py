# -*- coding:utf-8 -*-

import streamlit as st 
import seaborn as sns 

@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df

def main():
    st.title("Hello World on Streamlit.io")
    iris = load_data()
    st.table(iris)

if __name__ == "__main__":
    main()

#배포할 때 파이썬 버전은 3.11로