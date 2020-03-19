from enum import Enum
from typing import List

from pydantic import BaseModel, BaseConfig


class EntityType(str, Enum):
    PERSON = "PERSON"
    NORP = "NORP"
    FAC = "FAC"
    ORG = "ORG"
    GPE = "GPE"
    LOC = "LOC"
    PRODUCT = "PRODUCT"
    EVENT = "EVENT"
    WORK_OF_ART = "WORK_OF_ART"
    LAW = "LAW"
    LANGUAGE = "LANGUAGE"
    DATE = "DATE"
    TIME = "TIME"
    PERCENT = "PERCENT"
    MONEY = "MONEY"
    QUANTITY = "QUANTITY"
    ORDINAL = "ORDINAL"
    CARDINA = "CARDINA"


class NamedEntity(BaseModel):
    entity: str
    entity_type: EntityType


class Sentence(BaseModel):
    sentence: str


class ProcessedSentence(BaseModel):
    named_entities: List[NamedEntity] = []
