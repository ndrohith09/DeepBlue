# DeepBlue
![Screenshot from 2022-10-22 23-13-14](https://user-images.githubusercontent.com/73429989/197387717-dcf5d6a3-39c3-4768-8df5-ae6ae077f7cd.png)

## Abstract 
Our project "DeepBlue" is an user friendly application that focuses on providing children the knowledge about marine life. Users can upload or paste the image URL of which they want to identify and that image will be given to our ML modal to classify and the result will be given back with an image preview. We use Twilio SMS API to send an SMS to the user's mobile with extra resources about the sea object, so that they can learn much more than they expected. 

## Inspiration
Kids enjoy art and cartoons and at the same time, parents want them to observe and learn whatever they see. So we came up with **DeepBlue**, an user friendly tool that can classify marine objects based on the image provided.

## What it does
Kids may learn more about marine life with the aid of DeepBlue. When the user uploads the image in the input field, the AlexNet models classifies it as either a dolphin, jellyfish, etc. The output is sent as response by FastAPI to the client . After clicking the microphone icon, a computer-generated voice will speak out the results that corresponds to the input picture. The user may later get additional information about that specific marine species by pressing "more information" and entering their mobile number.

![Screenshot from 2022-10-22 21-27-44](https://user-images.githubusercontent.com/73429989/197387719-7b3ba724-e900-4a13-bb80-ac559650fb45.png)
![Screenshot from 2022-10-22 22-42-36](https://user-images.githubusercontent.com/73429989/197387721-88c62535-73db-4544-a57f-50b022cbdba5.png)
![Screenshot from 2022-10-22 22-43-46](https://user-images.githubusercontent.com/73429989/197387724-6e517bb5-96fc-4f11-ae76-14ff66a4d711.png)


## How we built it
Our project was divided into 3 phases.
- The initial step was brainstorming, during which we looked at several publications, research papers, and actual instances. We learned about it from there.
- The second step is planning, during which we choose the tech stack for the project's front end, back end, dataset, and neural network model.
- The third phase is implementation, during which we used React JS to build our GUI, Fastapi for our API, and Pytorch to train our deep learning model on a deep fictitious dataset.

## Architecture of DeepBlue
![architecture](https://user-images.githubusercontent.com/73429989/197374896-a9467f9c-3639-4ea9-be95-d9a3ceabc710.png)

## Deep Learning Model Phase 
![Screenshot from 2022-10-22 23-25-48](https://user-images.githubusercontent.com/73429989/197375635-98fdda97-e81a-4b0d-81fd-fd0428437007.png)

## AlexNet :
![architecture](https://production-media.paperswithcode.com/models/alexnet_deornOM.png)
 
Paper : [https://arxiv.org/pdf/1404.5997v2.pdf](https://arxiv.org/pdf/1404.5997v2.pdf)

## Challenges we ran into
Some of the AlexNet capabilities have to be modified to fit our product. Developing an API for the Deep Learning Model using the FastAPI framework and utilising the React Axios framework to make API requests were some areas were we spent a lot of time. The model responds to the requested request in a shorter amount of time with the help of FastAPI & Axios framework.

## Accomplishments that we're proud of
Using AlexNet model for identifying sea creatures. Customizing the AlexNet model according to our project . Adjust parameters to bring a better accuracy for the model. Building an API using Fastapi to handle request response cycle. Using Twilio API to communicate more information about the sea creature.

## What we learned
Using pretrained Neural Network models with different datset. Customizing the pretrained neural network according to our needs.  Usage of FastAPI. Creating UI/UX using React JS .

## What's next for DeepBlue
Implement DeepBlue as a mobile application . Introduce as browser extension such that kids can find the information of sea creatures within single click. Improving accuracy of the Deep Learning model by tuning the parameters.
