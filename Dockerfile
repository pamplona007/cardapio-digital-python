FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN python -m venv .venv
RUN source .venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ]
