FROM python:3.11.4
WORKDIR /app
COPY frontback/ /app/
COPY database/models.py /app/
COPY frontback/requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
