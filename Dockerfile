FROM python:3

WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 8000

CMD [ "gunicorn", "-b 0.0.0.0:8000", "wsgi:app" ]