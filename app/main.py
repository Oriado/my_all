import fastapi
from contextlib import asynccontextmanager
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.db import create_db_and_tables
from pathlib import Path
from app.emel.original import pred_original
from app.emel.unbiased import pred_unbiased
from app.emel.multilingual import pred_multilingual
from app.emel.sentoment import pred_santiment
from app.validation import ToxicityRequest, ToxicityResponse, SentimentRequest, SentimentResponse

BASE_DIR = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    create_db_and_tables()
    yield


app = fastapi.FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
def home(request: fastapi.Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"title": "Головна сторінка"})

@app.get("/register")
def register(request: fastapi.Request):
    return templates.TemplateResponse(request=request, name="register.html", context={"title": "Реєстрація"})

@app.get("/login")
def login(request: fastapi.Request):
    return templates.TemplateResponse(request=request, name="login.html", context={"title": "Вхід"})

@app.get("/dashboard")
def dashboard(request: fastapi.Request):
    return templates.TemplateResponse(request=request, name="dashboard.html", context={"title": "Дашборд", "name": "Марія"})

@app.get("/logout")
def logout(request: fastapi.Request):
    return templates.TemplateResponse(request=request, name="logout.html", context={"title": "Вихід"})

@app.get("/ping")
def ping():
    return "pong"

@app.get("/models")
def models(request: fastapi.Request):
    return templates.TemplateResponse(request=request, name="models.html", context={"title": "Моделі"})

@app.post("/api/sentiment", response_model=SentimentResponse)
def api_sentiment(payload: SentimentRequest):
    result = pred_santiment(payload.text)
    return SentimentResponse(
        label=result["label"],
        score=result["score"],
        text=payload.text
    )

@app.post("/api/original", response_model=ToxicityResponse)
def api_original(payload: ToxicityRequest):
    result = pred_original(payload.text)
    return ToxicityResponse(**result)

@app.post("/api/unbiased", response_model=ToxicityResponse)
def api_unbiased(payload: ToxicityRequest):
    result = pred_unbiased(payload.text)
    return ToxicityResponse(**result)

@app.post("/api/multilingual", response_model=ToxicityResponse)
def api_multilingual(payload: ToxicityRequest):
    result = pred_multilingual(payload.text)
    return ToxicityResponse(**result)

