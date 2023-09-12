import streamlit
import pandas as pd

streamlit.title("HELLO, WORLD!")
streamlit.header("This is a header...")

streamlit.text("...and this is text.")

streamlit.text("And this is more text")

streamlit.text("We can add emojis which is funny 🥣 🥗 🐔 🥑🍞")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

