from pydantic import BaseModel


class ToxicityRequest(BaseModel):
    text: str


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    label: str
    score: float
    text: str


class ToxicityResponse(BaseModel):
    toxicity: float
    severe_toxicity: float
    obscene: float
    threat: float
    insult: float
    identity_attack: float
