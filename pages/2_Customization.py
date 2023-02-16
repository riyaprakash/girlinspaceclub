import requests
import streamlit as st
import csv
import pandas as pd
from csv import writer
from PIL import Image
from streamlit.components.v1 import html
##from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import get_pages

##Adds balloons on screen when order is added to cart
def balloons():
    st.balloons()

##allows users to navigate through pages using buttons instead of sidebar
def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")
    
image = Image.open('flightsuit.jpg')

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide", initial_sidebar_state="collapsed")

# Hide streamlit branding
hide_streamlit_style = """
  <style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  </style>
  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("Flight Suit Customization")
st.write("---")

leftcol,rightcol = st.columns([8,7], gap="large");

##flight suit model on left side of the screen
with leftcol:
    st.write("##")
    st.image(image)

##tabs on right side of the screen
with rightcol:
    # ---- SIZING PREFERENCE ----
    tab1, tab2, tab3 = st.tabs(["Sizing", "Suit Color", "Patches"])
    with tab1:
        ##create 2 columns
        with st.container():
            ##Print size questions 
            st.header("Sizing Preference")
            st.write("##")

            ##prints size chart in expander
            size_chart=pd.read_csv('Sizing_Chart.csv')
            with st.expander("Size Chart"):
                st.write(size_chart.head(7))

            ##dropdown that appears before custom or standard options
            choice = st.selectbox("Do you want to purchase a space suit with custom measurements or with standard sizing?", ["-", "Custom", "Standard"])
            
            ##If user chooses custom measurements
            if 'Custom' in choice:
                 with st.form("custom", clear_on_submit=True):
                    
                    ##unit of measurement
                    add_col1 = st.selectbox('What is your preferred unit of measurement?',('cm', 'in'))

                    add_col2 = st.number_input('Enter Height',0,500)
                    add_col3 = st.number_input('Enter Chest',0,500)
                    add_col4 = st.number_input('Enter Waist',0,500)
                    add_col5 = st.number_input('Enter Total Arm Length',0,500)
                    add_col6 = st.number_input('Enter Inseam',0,500)
                    add_col7 = st.number_input('Enter Body Length',0,500)
                    st.form_submit_button("Save")

            ##if user chooses standard slizes
            if 'Standard' in choice:
                with st.form("standard"):
                    ##If user chooses standard sizing
                    add_col1 = st.selectbox("Which size suit do you want to purchase?",("XXS", "XS", "S", "M", "L", "XL"))
                    st.form_submit_button("Save")


    # ---- SUIT COLOR ----
    with tab2:
        st.write("---")
        colors = st.form("color")
        with colors:
            ##Print color questions
            st.header("Suit Color")
            st.write("##")
            st.selectbox("What color do you want your suit to be?", ("Black", "Blue"))
            st.write("##")
            colors.form_submit_button("Save")

    # ---- PATCHES ----
    with tab3:
        st.write("---")
        patches = st.form("patches")
        with patches:
            ##Print color questions
            st.header("Patches")
            st.write("##")
            st.selectbox("Would you like the Girl in Space Club Embroidery on the back?", ("Yes", "No"))
            st.write("We are currently unable to provide custom patches. However, if you would like to get your own, you have the option of including three blank patch spaces for the following dimensions:")
            st.checkbox("2 circular patches (diameter 3.75': right chest, left arm")
            st.checkbox("1 rectangular patch (2 x 4): left chest")
             #display balloons on button click
            patches.form_submit_button("Save")
 
 
    # ---- FINISH ORDERING ----
    st.text_input(" ", placeholder="Name your Order")
    addtocart = st.button("Add to Cart", disabled = True, on_click= balloons)

    
    # ---- VIEW CART ----
    st.write("---")
    if st.button("View Cart"):
        switch_page("Cart")

    # ---- BACK TO HOME ----
    if st.button("Return to home"):
        switch_page("Home")