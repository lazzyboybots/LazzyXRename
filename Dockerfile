FROM python:3.13.2
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]
