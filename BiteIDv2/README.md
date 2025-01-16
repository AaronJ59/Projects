# BiteIDv2
#### Application demo: https://huggingface.co/spaces/AaronJHugging/BiteIDv2

### <ins>Description<ins>


![Screenshot 2025-01-14 212216](https://github.com/user-attachments/assets/013df751-8258-416f-ad98-9e38c86f31b6)


BiteIDv2 is a machine-learning application with the purpose of detecting a food item within an image and classifying it as one of the 80 food classes it is trained on. You can see the list of the food groups here: [List](https://docs.google.com/document/d/1j61PGjhg-tqbFXat96Tdesn7f5Ez0loxbZTJ6ZFo0OQ/edit?usp=sharing). 

This application runs on two convolutional neural networks (CNN) - specifically **efficientnet_b2**. The first model that the image goes through is a binary feature extractor. Its goal is to determine if the image contains food or not. Once the image goes through the first model and it outputs
'tensor([1])' (which means the image has food), the image is then passed into a multiclass feature extractor. This model decides which of the 80 food groups the image is best reflected in/belongs to. The final output of this pipeline is shown through the gradio interface in a user-friendly way and is hosted on HuggingFace.


### <ins>How it's Made<ins>

**Tech Used:** Python, PyTorch, Gradio, HuggingFace

1. **multiclass_data_creation_food80.ipynb**: I created a multiclass dataset of 80 food classes from the [Food101 dataset](https://pytorch.org/vision/main/generated/torchvision.datasets.Food101.html). Then, it was turned into a zip file and downloaded into my local computer.
   
2. **binary_data_creation_food80.ipynb**: Imported over my multiclass dataset since I used a sample of those images to create the 'food' part of this binary dataset. To get nonfood images, I downloaded them from this [Kaggle dataset](https://www.kaggle.com/datasets/nitchayj/images) and created the 'nonfood' part of the dataset. The train:test split was 1125 images: 375 images.
   
3. **model_experimentation.ipynb**: This is where all the testing/experimenting happened. I decided to leave it as it is for transparency. I have experimentation from BiteID in this notebook because it is what massively contributed to eventually doing BiteIDv2. To seethe experimentation for BiteIDv2, go to the bottom of this notebook.

   * To choose a model, I needed a lightweight one but it should be powerful enough to have a decent accuracy for object recognition. I experimented with mobilenetv2 and efficientnet_b2. After many trials with different dataset sizes, data augmentation, and epochs, efficinetnet_b2 had       slightly higher accuracy than mobilenetv2. Mobilenetv2 had a faster prediction time but both models predicted under a second.
   * I trained an instance of the efficientnet_b2 model on the food80 dataset and downloades its 'state_dict', effectively creating the multiclass feature extractor.
    
4. **effnetb2binaryclassifier_biteidv2.ipynb**: This notebook is where the binary feature extractor was trained. I trained another instance of efficientnet_b2 on the dataset created from "**binary_data_creation_food80.ipynb**" notebook.
   
5. **gradiointerface_biteidv2**: The state_dict for the multiclass and binary models are loaded in. I test the multiclass feature extractor to check if the state dict was loaded in properly. Once completed, implementing the Gradio interface was next. Both models are added into one function that streamlines the passage of the image from the binary feature extractor to the multiclass feature extractor. The Gradio app structure is formed and then downloaded into a zip file. On HuggingFace, I import the zipfile and successfully host the gradio interface.


