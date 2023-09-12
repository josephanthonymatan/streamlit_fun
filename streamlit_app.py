import streamlit
import pandas as pd

streamlit.title("HELLO, WORLD!")
streamlit.header("This is a header...")

streamlit.text("...and this is text.")

streamlit.text("And this is more text")

streamlit.text("We can add emojis which is funny 🥣 🥗 🐔 🥑🍞")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)

streamlit.text("Let's put a pick list here so they can pick the fruit they want to include")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)




