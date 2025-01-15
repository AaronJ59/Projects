# BiteIDv2
#### Application demo: https://huggingface.co/spaces/AaronJHugging/BiteIDv2

### <ins>Description<ins>


![Screenshot 2025-01-14 212216](https://github.com/user-attachments/assets/013df751-8258-416f-ad98-9e38c86f31b6)


BiteIDv2 is a machine-learning application with the purpose of detecting a food item within an image and classifying it as one of the 80 food classes it is trained on. You can see the list of the food groups here: [List](https://docs.google.com/document/d/1j61PGjhg-tqbFXat96Tdesn7f5Ez0loxbZTJ6ZFo0OQ/edit?usp=sharing). 

This application runs on two convolutional neural networks (CNN) - specifically efficientnet_b2. The first model that the image goes through is a binary feature extractor. Its goal is to determine if the image contains food or not. Once the image goes through the first model and it outputs
'tensor([1])' (which means the image has food), the image is then passed into a multiclass feature extractor. This model decides which of the 80 food groups the image is best reflected in/belongs to. The final output of this pipeline is shown through the gradio interface in a user-friendly way and is hosted on HuggingFace.
