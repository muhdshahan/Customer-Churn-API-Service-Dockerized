# Dockerfile
FROM python:3.13

# Specifies the directory to work
WORKDIR /app 
# copies only requirements.txt file from local machine into container at /app/requirements.txt
# this copying is done first so as to avoid reinstalling dependencies when requirements file doesnt change
# copy format is COPY <source> <destination>
COPY requirements.txt .
# --no-cache-dir ensures pip doesn't keep cached package files, so reduces image size
RUN pip install --no-cache-dir -r requirements.txt
# copies actual application source code into container, where dependencies are already installed
COPY app app
COPY models models

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]