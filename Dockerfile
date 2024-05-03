FROM python:3.8
#FROM python:3.11-slim

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN python -m venv venv
RUN . venv/bin/activate

RUN pip install -r requirements.txt

COPY . .

RUN #chmod a+x docker/*.sh

WORKDIR src

#CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
#CMD python main.py
RUN #python -m uvicorn main:app --host 0.0.0.0 --port 80
