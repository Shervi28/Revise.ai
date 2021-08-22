import streamlit as st
from multiapp import MultiApp
from apps import dashboard, about

app = MultiApp()

st.image('reviselogo2.png')

st.subheader("""
 Navigation
""")


app.add_app("Dashboard", dashboard.app)
app.add_app("About", about.app)


app.run() 