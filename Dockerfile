# 1. Createa a base Image

FROM python:3.12

# 2. Specify the working directory for docker

WORKDIR /shop-kipa-app

# 3. Copy the needed files for the shop-kipa project to workdir

COPY requirements.txt /shop-kipa-app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /shop-kipa-app/

EXPOSE 8000

CMD [ "python", "manage.py", "makemigrations", "migrate", "runserver", "0.0.0.0:8000"]