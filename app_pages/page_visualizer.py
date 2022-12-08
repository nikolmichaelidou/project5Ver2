import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_visualizer_body():
    st.write("### Leaves Visualizer")
    st.info(
        f"* The client is interested in having a study that visually "
        f"differentiates a healthy leaf from a leaf with mildew")
    
    version = 'v1'
    if st.checkbox("Diffrence betwwen healthyleaf and one with mildew"):
        
      avg_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
