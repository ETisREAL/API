FROM python:3.9.16

WORKDIR /usr/src/app

COPY requiremets.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]