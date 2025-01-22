# 1. Createa a base Image

FROM python:3.12

# 2. Specify the working directory for docker

WORKDIR /shop-kipa-app

# 3. Copy the needed files for the shop-kipa project to workdir

COPY . /shop-kipa-app/

RUN pip update pip && pip install -r requirments.txt

CMD [ "python", "manage.py", "makemigrations", "migrate", "runserver",]