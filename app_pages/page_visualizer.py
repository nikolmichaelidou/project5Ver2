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
    version = 'v1'
    if st.checkbox("Difference between healthy leaf and one with mildew"):
            avg_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
            avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")


