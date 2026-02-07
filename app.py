import streamlit as st

st.title("Proposal App")
st.components.v1.html(open("proposal (1).html").read(), height=800)
