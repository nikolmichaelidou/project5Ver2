import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("#### Quick Project Summary")
    st.write(
        f"This dataset contains 2104 images."
        f"We compared all of those images to determine an average healthy leaf and a leaf with mildew.")
    st.write("#### What does the client want?")
    st.write(
        f"The client is"
        f"interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew and in predicting if a cherry tree is healthy or contains powdery mildew."
    )    
    st.write("#### What is mildew?")
    st.write(
        f"Mildew is a form of fungus. It is distinguished from its closely related counterpart, mould, largely by its colour: moulds appear in shades of black, blue, red, and green, whereas mildew is white. It appears as a thin, superficial growth consisting of minute hyphae (fungal filaments) produced especially on living plants or organic matter such as wood, paper or leather")
