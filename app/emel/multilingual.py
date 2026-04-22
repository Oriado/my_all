"""
Викликання файлу:

```bash
python -m app.emel.multilingual
```
"""
from detoxify import Detoxify

multilingual_model = Detoxify("multilingual")


def pred_multilingual(text: str) -> dict:
    """Аналізує токсичність тексту за допомогою багатомовної моделі"""
    result = multilingual_model.predict(text)
    return {key: float(val) for key, val in result.items()}
