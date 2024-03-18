
Create the env:
```
python3 -m venv lamma
```

Activate the env:
```
source lamma/bin/activate
```
Install the requirements:

```
pip install -r requirements.txt
```

mapping
```gunicorn -w 4 -b 0.0.0.0:8200 app:app```
