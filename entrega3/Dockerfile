FROM python:3.8-slim

WORKDIR /

COPY .  .

RUN apt-get update && apt-get install -y libgomp1

RUN pip install -r requirements.txt

CMD ["uvicorn", "minha_api:app", "--host", "0.0.0.0", "--port", "8000"]