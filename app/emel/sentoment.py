"""
Викликання файлу:

```bash
python -m app.emel.sentoment
```
"""
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")


def pred_santiment(text: str) -> dict:
    """Визначає емоційне забарвлення тексту"""
    result = sentiment_pipeline([text])[0]
    return {
        "label": result["label"],
        "score": result["score"]
    }
