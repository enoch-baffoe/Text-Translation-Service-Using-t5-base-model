import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from transformers import T5ForConditionalGeneration, T5Tokenizer

from api.v1.translate import translation_router
from core.config import settings

app = FastAPI(title=settings.title, version=settings.version)


def save_model():
    """Function to load tokenizer and model from online
    and then save it to the folder named models
    """
    tokenizer_online = T5Tokenizer.from_pretrained(
        "t5-base", model_max_length=512, force_download=True
    )
    model_online = T5ForConditionalGeneration.from_pretrained(
        "t5-base", return_dict=True
    )

    model_online.save_pretrained("./models/")
    tokenizer_online.save_pretrained("./models")


@app.on_event("startup")
def initialize_models():
    """Function runs on start up and checks if the models do not exist
    locally. It downloads the models using the load_model function
    """
    if not os.path.isdir("models"):
        os.mkdir("models")
    if len(os.listdir("./models")) == 0:
        save_model()


@app.get("/", include_in_schema=False)
async def index():
    """Redirects user to /docs"""
    return RedirectResponse(url="/docs")


# adding traslation routes from api/v1/translate
app.include_router(translation_router, prefix=settings.api_prefix)
