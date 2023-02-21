FROM python:3

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Обновляем пакетный менеджер
RUN apt-get update -y && apt-get upgrade -y

# Ставим зависимости GDAL, PROJ
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

COPY ./requirements.txt .

RUN  pip install --upgrade pip && pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

COPY . .

RUN apt install -y netcat

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

## RUN python3 manage.py migrate
