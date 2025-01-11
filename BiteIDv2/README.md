# BiteIDv2
#### Application demo: https://huggingface.co/spaces/AaronJHugging/BiteIDv2

### <ins>Description<ins>

BiteIDv2 is a machine-learning application with the purpose of detecting a food item within an image and classifying it as one of the 80 food classes it is trained on. You can see the list of the food groups here: [List](https://docs.google.com/document/d/1j61PGjhg-tqbFXat96Tdesn7f5Ez0loxbZTJ6ZFo0OQ/edit?usp=sharing). 

This application runs on two convolutional neural networks (CNN) - specifically efficientnet_b2. The first model that the image goes through is a binary feature extractor. Its goal is to determine if the image contains food or not. Once the image goes through the first model 
