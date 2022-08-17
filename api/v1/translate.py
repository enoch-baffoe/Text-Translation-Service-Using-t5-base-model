from fastapi import APIRouter, status
from transformers import T5ForConditionalGeneration, T5Tokenizer

from schemes.translate import Languages

translation_router = APIRouter(tags=["Translate"])


@translation_router.on_event("startup")
def load_model():
    """
    This loads the tokenizer and model on startup.
    The model and tokenizer loaded here is the one saved in the models folder
    """
    global model
    global tokenizer
    model = T5ForConditionalGeneration.from_pretrained("./models")
    tokenizer = T5Tokenizer.from_pretrained("./models")


@translation_router.post("/translate", status_code=status.HTTP_200_OK)
async def translate(
    source_language: Languages,
    destination_language: Languages,
    input_text: str,
):
    """
    Translates text among 4 different languages namely:
    English, French Romanian, German

    - Inputs:
        - source_language: the language your text is in
        - destination_language: the language you want to translate the text to
        - Input_text: the text you want to translate


    - Output:
        - success: boolean to show if text was successfully translated
        - translated_text: the translated text from the algorithm
    """
    token_input = (
        "translate "
        + source_language.value
        + " to "
        + destination_language.value
        + ": "
        + input_text
    )
    input_ids = tokenizer(token_input, return_tensors="pt").input_ids  # type: ignore[name-defined]

    outputs = model.generate(input_ids)  # type: ignore[name-defined]

    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)  # type: ignore[name-defined]
    if translated_text:
        return {"success": True, "translated_text": translated_text}
    return {"success": False, "translated_text": None}
