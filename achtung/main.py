from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from io import StringIO
import requests
import random

from .settings import ENV, TEMPLATES


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def index(request: Request):
    return TEMPLATES.TemplateResponse("pages/index.html", {"request": request})


@app.get("/coming")
async def coming(request: Request):
    return TEMPLATES.TemplateResponse("pages/heart.html", {"request": request})


@app.post("/test_trigger")
async def test_trigger():
    print("TRIGGER!")


greetings = ["Hello", "Hi", "Hey", "Greetings", "Howdy", "Salutations"]
pet_names = [
    "My love",
    "My lord",
    "King",
    "Baby",
    "The greatest lover of all time",
    "Soon to be Millionaire",
    "Master of the moustache",
    "Daddy",
    '9" wonder',
]
message = [
    "I was eating a baby bell cheese when I saw your picture and I thought I would eat you instead.",
    "I'm not a photographer, but I can picture me and you together, baby.",
    "Come live in my heart, and pay no rent.",
    "I can't stop thinking about you",
    "Do you have a map? I'm getting lost in your eyes.",
    "Are you a parking ticket? Because you've got fine written all over you.",
    "Are you a magician? Because whenever I look at you, everyone else disappears!",
    "I'm not a hoarder but I really want to keep you forever.",
    "Are you a camera? Because every time I look at you, I smile.",
    "Are you a bank loan? Because you have my interest.",
    "Are you a fruit, because Honeydew you know how fine you look right now?",
    "You're my chocolate chip cookie, I want to eat you up.",
    "You're so beautiful that you made me forget my pickup line.",
    "I'm a doctor. I can tell you how to get pregnant.",
    "I'm a pirate, and you're my booty.",
    "I'm a lawyer. I can get you off.",
]


@app.post("/trigger")
async def trigger():

    requests.post(
        "https://api.mynotifier.app",
        {
            "apiKey": ENV.API_KEY,
            "message": f"{random.choice(greetings)}, {random.choice(pet_names)}",
            "description": f"{random.choice(message)}\nPlease give me some attention <3",
            "type": "info",
        },
    )
