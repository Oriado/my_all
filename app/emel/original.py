"""
Викликання файлу:

```bash
python -m app.emel.original
```
"""
from detoxify import Detoxify

original_model = Detoxify("original")


def pred_original(text: str) -> dict:
    """Аналізує токсичність тексту"""
    result = original_model.predict(text)
    return {key: float(val) for key, val in result.items()}
