from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn
from PIL import Image
import torch.nn.functional as F 
import torch
from torchvision import transforms as T  
from torchvision.models import alexnet
from torch import nn 
import requests 
from twilio.rest import Client
import wikipedia


app = FastAPI() 

origins = [
    "http://localhost",
    "http://localhost:3000",
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# setting CPU to make predictions
device = torch.device("cpu")

# load pretrained model
model = alexnet(pretrained=True) 
model.classifier[6] = nn.Linear(in_features=4096,out_features = 19, bias=True) 
model.load_state_dict(torch.load('./ocean_alex_25.pt'))
model.to(device) 

# labels
class_map = ['Corals',
 'Crabs',
 'Dolphin',
 'Eel',
 'Jelly Fish',
 'Lobster',
 'Nudibranchs',
 'Octopus',
 'Penguin',
 'Puffers',
 'Sea Rays',
 'Sea Urchins', 
 'Seahorse',
 'Seal',
 'Sharks',
 'Squid',
 'Starfish',
 'Turtle_Tortoise',
 'Whale']

# prediction function
def predict_img(image): 

    INPUT_DIM = 224 
    preprocess = T.Compose([
            T.Resize(INPUT_DIM ),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )]) 
    

    im = Image.open(image).convert('RGB')
    im_preprocessed = preprocess(im) 
    batch_img_tensor = torch.unsqueeze(im_preprocessed, 0)
    output = model(batch_img_tensor) 
    confidence = F.softmax(output, dim=1)[0] * 100 
    _, indices = torch.sort(output, descending=True) 
    return [(class_map[idx], confidence[idx].item()) for idx in indices[0][:1]]

# prediction function
def predict_img_url(url): 

    INPUT_DIM = 224 
    preprocess = T.Compose([
            T.Resize(INPUT_DIM ),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )]) 
    

    im = Image.open(requests.get(url, stream=True).raw).convert('RGB')
    im_preprocessed = preprocess(im) 
    batch_img_tensor = torch.unsqueeze(im_preprocessed, 0)
    output = model(batch_img_tensor) 
    confidence = F.softmax(output, dim=1)[0] * 100 
    _, indices = torch.sort(output, descending=True) 
    return [(class_map[idx], confidence[idx].item()) for idx in indices[0][:1]]


@app.get("/")
async def root():
    return {"message": "Sea Animals prediction"} 

@app.post("/url/")
async def create_url( url : str):       
    # send file to prediction function 
    prediction = predict_img_url(url)
    print(prediction[0]) 
    animal = prediction[0][0] 
    confidence = prediction[0][1]
    return {
        "animal": animal, 
        "confidence": confidence
    }


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):       
    print(file)
    # send file to prediction function 
    prediction = predict_img(file.file) 
    print(prediction[0]) 
    animal = prediction[0][0] 
    confidence = prediction[0][1]
    return {
        "animal": animal, 
        "confidence": confidence
    }

account_sid = '****' 
auth_token = "****"

@app.post("/twilio")
async def twilio(url: str , mobile : str): 
    wiki = wikipedia.summary(url , sentences = 3)
    print(wiki) 
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Info: "+wiki,
    from_='+19896822464',
    to='+91'+mobile
    )
    print(message.sid)
    return {"message": "Message sent successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
