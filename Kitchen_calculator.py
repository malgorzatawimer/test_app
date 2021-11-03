# sum
# 1 gallon is 3.79 liters
# 1 pint is 0.57 liters
# 1 cap is 0.24 liters
# 1 ounce is 28.35 grams
# 1 pound is 453.59 grams
# 1 tablespoon is 14.30 grams
# 1 teaspoon is 5.69 grams
def gallon(a):
    g = float(a * 3.79)
    return g


def pint(a):
    p = float(a * 0.57)
    return p


def cap(a):
    c = float(a * 0.24)
    return c


def ounce(a):
    o = float(a * 28.35)
    return o


def pound(a):
    p = float(a * 453.59)
    return p


def tablespoon(a):
    tbls = float(a * 14.3)
    return tbls


def teaspoon(a):
    tea = float(a * 5.69)
    return tea


import streamlit as st
import base64

main_bg = "images/cookies.png"
main_bg_ext = "png"
side_bg = "images/bg-sidebar.jpeg"
side_bg_ext = "jpeg"

# file = open(main_bg)

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

template = """<div style = "background-color:beige; padding: 1px;">
                 <h2 style = "color:black; text-align:center"> Ingredients calculator</h2>
                 </div>"""
st.markdown(template, unsafe_allow_html=True)


st.sidebar.title("Select your measure type")
dropdown = st.sidebar.selectbox(" ", ["dropdown to select", "Liquids", "Non-liquids"])
if dropdown == "Liquids":
    radio_button = st.sidebar.radio("select your choice", ["Gallon", "Pint", "Cap"])
    x = st.number_input("Enter the amount")
    # Gallon
    if radio_button == "Gallon":
        result_gallon = gallon(x)
        if st.button("Get result"):
            st.success("The given measure of gallons amounts to {} in liters".format(result_gallon))
            st.balloons()
    if radio_button == "Pint":
        result_pint = pint(x)
        if st.button("Get result"):
            st.success("The given measure of pints amounts to {} in liters".format(result_pint))
            st.balloons()
    if radio_button == "Cap":
        result_cap = cap(x)
        if st.button("Get result"):
            st.success("The given measure of caps amounts to {} in liters".format(result_cap))
            st.balloons()
if dropdown == "Non-liquids":
    radio_button = st.sidebar.radio("select your choice", ["Ounce", "Pound", "Tablespoon", "Teaspoon"])
    x = st.number_input("Please enter your measure")
    # Ounce
    if radio_button == "Ounce":
        result_ounce = ounce(x)
        if st.button("Get result"):
            st.success("The given measure of ounces amounts to {} in grams".format(result_ounce))
            st.balloons()
    if radio_button == "Pound":
        result_pound = pound(x)
        if st.button("Get result"):
            st.success("The given measure of pounds amounts to {} in grams".format(result_pound))
            st.balloons()
    if radio_button == "Tablespoon":
        result_tablespoon = tablespoon(x)
        if st.button("Get result"):
            st.success("The given measure of tablespoons amounts to {} in grams".format(result_tablespoon))
            st.balloons()
    if radio_button == "Teaspoon":
        result_teaspoon = teaspoon(x)
        if st.button("Get result"):
            st.success("The given measure of teaspoons amounts to {} in grams".format(result_teaspoon))
            st.balloons()
