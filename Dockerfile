FROM tensorflow/tensorflow

RUN mkdir /app

WORKDIR /app

ADD . /app

COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 

# EXPOSE 8000

# CMD python manage.py runserver 0:8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "Chatbot_Site.wsgi:application"]

CMD gunicorn AssistantsWeb.wsgi:application --bind 0.0.0.0:$PORT
