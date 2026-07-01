import streamlit as st
pg=st.navigation([st.Page("task.py"),st.Page("task1.py"),st.Page("task2.py")])
pg.run()