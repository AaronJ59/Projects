# BiteID

#### Application demo: https://huggingface.co/spaces/AaronJHugging/BiteID

### <ins>Description<ins>

![Screenshot 2025-01-16 193405](https://github.com/user-attachments/assets/70c4d9e9-9d2b-4d69-8ebe-1ce31e3fd5bc)

This app was created as a way to gain experience on a simpler task before starting on BiteIDv2.

BiteID is a machine-learning application that detects and classifies food within an image if the image contains pizza, hamburger, lasagna, sushi, or steak.

This application runs on two convolutional neural networks (CNN) - specifically **efficientnet_b2**. The first model that the image goes through is a binary feature extractor. Its goal is to determine if the image contains food or not. Once the image pases through the first model and it outputs
'tensor([1])' (which means the image has food), the image is then passed into a multiclass feature extractor. This model decides which of the 5 food classes the image is best reflected in/belongs to. The final output of this pipeline is shown through the gradio interface in a user-friendly way and is hosted on HuggingFace
