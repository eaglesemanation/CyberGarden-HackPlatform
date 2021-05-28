FROM python:3.8-slim
ADD requirements.txt ./temp/requirements.txt
RUN pip3 install -r ./temp/requirements.txt
WORKDIR backend/
COPY . .
ENTRYPOINT ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "-k uvicorn.workers.UvicornWorker"]
