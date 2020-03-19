import spacy
from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.models.sentence import NamedEntity, ProcessedSentence, Sentence

router = APIRouter()

nlp = spacy.load("en_core_web_sm")


@router.post("/process", response_model=ProcessedSentence)
def extract_name(sentence: Sentence):
    """
    This endpoint returns a processed sentence
    """
    doc = nlp(sentence.sentence)
    named_entities = [
        NamedEntity(entity=ent.text, entity_type=ent.label_) for ent in doc.ents
    ]
    return ProcessedSentence(named_entities=named_entities)
