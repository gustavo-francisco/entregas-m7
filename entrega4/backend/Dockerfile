FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libgomp1

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
