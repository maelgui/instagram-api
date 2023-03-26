FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "instapi.main:app", "--host", "0.0.0.0" ]

EXPOSE 8000
