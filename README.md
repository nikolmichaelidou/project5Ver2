# Cherry Leaf Mildew Detector Prototype

## Dataset Content

This dataset contains 2104 images of cherry leaves. The photos show healthy leaves and leaves with mildew.
<hr>

## Requirements

The client is the head of IT and Innovation at Farmy & Foods, a company in the agricultural sector that produces and harvests different types of food. is requesting a dataset that:

* Visualize the difference between a healthy leaf from a leaf that contains powdery mildew.
* Also, that predicts if a cherry tree leaf is healthy or has powdery mildew.

### How to validate?

In order to differentiate between a healthy leaf and a leaf with mildew can be done with a simple image study.

## Dashboard Design (Streamlit UI)

### Page 1: Summary

* General information:
  * Powdery mildew, is a fungal disease that affects a wide range of plants.
The company is concerned about supplying the market with a product of compromised quality.
Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree. To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a tree leaf image, if it is healthy or has powdery mildew.
* Project Dataset:
The available dataset contains 2104 images of cherry leaves
* Business Requirements
The client is:
  * is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  * is interested in predicting if a cherry tree is healthy or contains powdery mildew.

### Page 2: Leaf Visualizer

* The client we will be able to see the average difference between a healthy leaf and a leaf with mildew cell. Also, the client will be able to generate a gallery of images of either healthy leaves of leaves with mildew by simply pressing the "Generate Montage" button.

### Page 3: Mildew Detector

* Here the client can upload pictures of cherry tree leaves and the Detector will detect if it is a healthy leaf or if it has mildew.

<hr>

## Credit

* This project was created by following a walk-through provided by Code Institute: Walk-through Project 01 Data Analysis & Machine Learning Toolkit.
* Data used for this project was retrieved from Kaggle. https://www.kaggle.com/datasets/codeinstitute/cherry-leaves
