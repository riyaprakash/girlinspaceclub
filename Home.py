import requests
import streamlit as st
from streamlit.components.v1 import html
from PIL import Image

##allows users to navigate through pages using buttons instead of sidebar
def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
# browser label
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide", initial_sidebar_state="collapsed")

# Hide streamlit branding
hide_streamlit_style = """
  <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
  </style>
  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

##image on home page
image = Image.open('sabrinaskates.jpg')

# ---- HEADER SECTION ----

left,right = st.columns([5,3])
##title, subtitle, and buttons
with left:
    st.title("Welcome to the Girl in Space Club Outfitter")
    st.subheader("Design Your Dream Flight Suit Here")
    st.write('***')
    ##left_column, right_column = st.columns(2)
    ##with left_column:
    if st.button("Create New Suit"):
            nav_page("Customization")
    ##with right_column:
    st.write('##')
    if st.button("View Cart"):
            nav_page("Cart")
    st.write('##')
    if st.button("Return to Old Cart"):
        nav_page("Cart")

##image
with right:
    st.image(image)

