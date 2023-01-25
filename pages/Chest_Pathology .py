# Include PIL, load_image before main()
from PIL import Image
import streamlit as st
import torchxrayvision as xrv
import skimage, torch, torchvision
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import cv2

import plotly.express as px

st.sidebar.success("Please do select an option to do your customized analysis.")

st.sidebar.title('Developers Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                    '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                    '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)')



st.title("Chest X-Ray - Basic Interpretation")
st.write("The chest x-ray is the most frequently requested radiologic examination. In fact every radiologst should be an expert in chest film reading. The interpretation of a chest film requires the understanding of basic principles.")


def plot_sample_with_masks(sample, df):
    
    if "semantic_masks" in sample:
        width = len(sample["semantic_masks"])
        fig, axs = plt.subplots(1, max(2,1+width), sharey=True, figsize=(3+3*width,3))
        axs[0].imshow(sample["img"][0], cmap="Greys_r");
        axs[0].set_title("idx:" + str(sample["idx"]))
    
        for i, patho in enumerate(sample["semantic_masks"].keys()):
            axs[i+1].imshow(sample["img"][0], cmap="Greys_r");
            axs[i+1].imshow(sample["semantic_masks"][patho][0]+1, alpha=0.5);
            axs[i+1].set_title(patho)
        plt.show()
        
    if "pathology_masks" in sample:
        width = len(sample["pathology_masks"])
        fig, axs = plt.subplots(1, max(2,1+width), sharey=True, figsize=(3+3*width,3))
        axs[0].imshow(sample["img"][0], cmap="Greys_r");
        axs[0].set_title("idx:" + str(sample["idx"]))
        for i, patho in enumerate(sample["pathology_masks"].keys()):
            axs[i+1].imshow(sample["img"][0], cmap="Greys_r");
            axs[i+1].imshow(sample["pathology_masks"][patho][0]+1, alpha=0.5);
            axs[i+1].set_title(df.pathologies[patho])
        plt.show()
    pd.DataFrame(sample["lab"], index=df.pathologies)




def load_image(image_file):
	img = Image.open(image_file)
	return img

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:
    file_details = {"filename":image_file.name, "filetype":image_file.type,
        "filesize":image_file.size}
    st.caption("File Details: ")
    st.write(file_details)
    st.image(load_image(image_file),width=350)

    print(image_file)

    # Prepare the image:
    img = skimage.io.imread(image_file)

    print(img.shape)
    if len(img.shape) !=3 or (len(img.shape==3 and img.shape[2]!=3)):
        img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    print(img.shape)
    
    img = xrv.datasets.normalize(img, 255) # convert 8-bit image to [-1024, 1024] range
    img = img.mean(2)[None, ...] # Make single color channel

    transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop(),xrv.datasets.XRayResizer(224)])

    img = transform(img)
    img = torch.from_numpy(img)
    

    # Load model and process image
    model = xrv.models.DenseNet(weights="densenet121-res224-all")
    outputs = model(img[None,...]) # or model.features(img[None,...]) 

    data1 = dict(zip(model.pathologies,outputs[0].detach().numpy()))
    Values = [float(i) for i in data1.values()]
    Keys = list(data1.keys())

    data = {
        "Attributes" : Keys,
        "Probability Scores" : Values
    }

    fig = px.bar(data, x='Attributes', y='Probability Scores', 
    color_discrete_sequence=["light blue"])

    

    st.plotly_chart(fig, use_container_width=True)

    Keymax = max(data1, key=data1.get)

    print(data)


    st.write(f"The attribute with max probability score is {Keymax}")

    st.json(dict(zip(model.pathologies,outputs[0].detach().numpy())))



