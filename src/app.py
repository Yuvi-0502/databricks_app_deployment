import streamlit as st

def main():
    st.set_page_config(page_title="Databricks Hello World", page_icon="🚀")
    st.title("Hello World! 🚀")
    st.write("This Streamlit app is running on Databricks Apps.")
    st.write("It was deployed entirely locally using a `databricks.yml` file.")

if __name__ == "__main__":
    main()