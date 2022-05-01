import streamlit as st
import pandas as pd


#st.title("Whats trending in Denver?")
#st.write("We used the spotify api to get the top unique songs in Denver over the span of the last few months.")
#
#
#st.write("This is a graph of the top songs in Denver over the last few months.")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
