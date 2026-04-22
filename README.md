# NLP Models API

FastAPI застосунок з інтеграцією Detoxify та Hugging Face моделей для аналізу тексту.

## Можливості

| Endpoint | Модель | Опис |
|---|---|---|
| `POST /api/original` | Detoxify original | Аналіз токсичності (англійська, Wikipedia коментарі) |
| `POST /api/unbiased` | Detoxify unbiased | Аналіз токсичності без упередженості до груп |
| `POST /api/multilingual` | Detoxify multilingual | Аналіз токсичності (багато мов, включаючи українську) |
| `POST /api/sentiment` | Hugging Face | Аналіз емоцій тексту (позитивне / негативне) |

## Категорії токсичності (Detoxify)

| Поле | Опис |
|---|---|
| `toxicity` | Загальна токсичність |
| `severe_toxicity` | Дуже груба токсичність |
| `obscene` | Непристойний контент |
| `threat` | Погрози |
| `insult` | Образи |
| `identity_attack` | Атаки на групи людей |

## Запуск

```bash
# Активація віртуального середовища (Windows)
.venv\Scripts\activate

# Запуск сервера
uvicorn app.main:app --reload
```

Сервер доступний на `http://127.0.0.1:8000`

