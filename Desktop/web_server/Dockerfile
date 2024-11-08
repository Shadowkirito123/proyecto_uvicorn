FROM python:3.10-slim
WORKDIR /docker_app
COPY requirements.txt /docker_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /docker_app/requirements.txt

COPY . /docker_app/

# CMD bash -c "while true; do sleep 1; done"
CMD [ "uvicorn", "proyecto_web.asgi:application", "--host", "0.0.0.0", "--port", "80" ]