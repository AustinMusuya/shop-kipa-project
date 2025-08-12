# 1. Create a base Image

FROM python:3.12

# 2. Specify the working directory inside the Docker container.

WORKDIR /shop-kipa-app

# 3. Copy project requirements file for shop-kipa project to workdir

COPY requirements.txt /shop-kipa-app/

# 4. Run the required commands to update and install project dependencies

RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy all project files from host to workdir

COPY . /shop-kipa-app/

# 6. Expose the port that the container will listen on for incoming connections.

EXPOSE 8000

# 7. Copy setup script to workdir

COPY setup.sh /shop-kipa-app/

# 8. Make script executable

# RUN chmod +x /shop-kipa-app/setup.sh

# 9. Use the script to handle migrations and run the server

CMD [" python", "manage.py", "runserver", "0.0.0.0:8000"]