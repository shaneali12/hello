import streamlit as st
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEVeex8M9FQ_Kk0rwMBDW0DDISwAw5uk2imQ&s")
st.title("Chai Wala")
st.subheader("Best Chai In World")
st.text("choose your chai")
chai = st.selectbox("your fav chai: ", ["Masala Chai", "Adrak Chai", "Garam Chai"]) 
add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("masala added to your chai")
add_lemon = st.checkbox("Add lemon")

if add_lemon:
    st.write("lemon added to your chai")

add_ginger = st.checkbox("Add ginger")

if add_ginger:
    st.write("ginger added to your chai")
tea_base = st.radio("pick your chai base", ["Milk", "Water", "Almond Milk"])
if tea_base:
    st.write(f"selected base {tea_base}")
cups  = st.number_input("How Many Cups", min_value=1, max_value=10, step=1)
if cups:
    st.write(f"selected {cups} cups")
sugar = st.slider("sugar level", 0, 5, 2)
name = st.sidebar.text_input("enter your name: ")
if name:
    st.sidebar.write("welcome")
dob = st.sidebar.date_input("enter your date of birth: ")
if dob:
    st.sidebar.success(f"your date of birth is {dob}, thanks for registring")





if st.button("make chai"):
    st.write(f"you choose {chai}. exellent choice")
