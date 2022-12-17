import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_visualizer import page_visualizer_body
from app_pages.mildew_detector import page_detector_body


app = MultiPage(app_name="Cherry Mildew Detector")


app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaf visualizer", page_visualizer_body)
app.add_page("Mildew Detector", page_detector_body)


app.run()
