"""
Викликання файлу:

```bash
python -m app.emel.unbiased
```
"""
from detoxify import Detoxify

unbiased_model = Detoxify("unbiased")


def pred_unbiased(text: str) -> dict:
    """Аналізує токсичність текстів"""
    result = unbiased_model.predict(text)
    return {key: float(val) for key, val in result.items()}
