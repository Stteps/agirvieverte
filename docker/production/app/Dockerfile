# STATIC FILES BUILD (FRONTEND)
FROM node:19-alpine as static-build
WORKDIR /code/
COPY frontend/ frontend/

# INSTALLING NODEJS DEPENDENCIES
WORKDIR /code/frontend/
RUN apk update \
    && apk add --no-cache --virtual .build-deps python3 make g++ git \
    && npm install \
    && apk del .build-deps

# RUNNING BUILD SCRIPT (WEBPACK)
RUN ["npm", "run", "production"]


# WEB APP (BACKEND)
FROM python:3.10-slim

# ENVIRONMENT VARIABLES
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# CREATING GROUP AND USER FOR SETTING APPROPRIATE PERMISSIONS OVER THE APP
# Note: Some programs require home dir write access, so we create a home dir for the user
RUN addgroup --system --gid 1000 app  \
    && adduser --system --ingroup app --uid 1000 --home=/home/app app

# INSTALLING OS-LEVEL DEPENDENCIES
# Note: We install dependencies then clean the install to reduce image size
# Note: build-essential is used for building python packages
# Note: libpq-dev includes Postgre's client (psycopg2) dependencies
# Note: procps is used for celery
# Note: psycopg2 is Postgre's python client
RUN apt-get update && apt-get install -y -q --no-install-recommends \
  build-essential \
  libpq-dev \
  git \
  gettext \
  procps \
  && pip install --no-cache-dir psycopg2 \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# SOURCE CODE DIRECTORY AND BASE PATH
WORKDIR /code/
COPY --chown=app:app app/ app/
COPY --chown=app:app config/ config/
COPY --chown=app:app assets/locales/ assets/locales/
COPY --chown=app:app manage.py manage.py
COPY --chown=app:app setup.py setup.py
COPY --from=static-build --chown=app:app /code/frontend/build /code/frontend/build
COPY --from=static-build --chown=app:app /code/frontend/templates /code/frontend/templates
COPY --from=static-build --chown=app:app /code/frontend/webpack-stats.json /code/frontend/webpack-stats.json

# WE CREATE A MEDIA FOLDER FOR MEDIA FILES (STATIC FILES ARE SERVED SEPARATLY IN DEV)
RUN mkdir -p /var/www/static/ && chown -R app:app /var/www/static/
RUN mkdir -p /var/www/media/ && chown -R app:app /var/www/media/

# INSTALLING PYTHON DEPENDENCIES
COPY --chown=app:app requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/base.txt

# INSTALLING NLTK PACKAGES
RUN ["python", "-m", "spacy", "download", "en_core_web_md"]
RUN ["python", "-m", "spacy", "download", "fr_core_news_md"]
RUN ["python", "-m", "spacy", "download", "es_core_news_md"]
RUN ["python", "-m", "spacy", "download", "de_core_news_md"]
RUN ["python", "-m", "spacy", "download", "it_core_news_md"]
RUN ["python", "-m", "spacy", "download", "pt_core_news_md"]
#TO DO: CHECK IF PUNKT PACKAGE IS NOT NEEDED?
RUN ["python", "-c", "import nltk; nltk.download('stopwords', download_dir='/usr/local/nltk_data')" ]

# PREPARE PRODUCTION SCRIPT: APPLY MIGRATIONS AND COLLECT STATIC FILES
COPY --chown=app:app docker/production/app/prepare-production.sh /usr/local/bin/prepare-production.sh
RUN chmod +x /usr/local/bin/prepare-production.sh
# PYTHON WSGI SERVER COMMAND SCRIPT
COPY --chown=app:app docker/production/app/start-gunicorn-server.sh /usr/local/bin/start-gunicorn-server.sh
RUN chmod +x /usr/local/bin/start-gunicorn-server.sh
# PYTHON ASGI SERVER COMMAND SCRIPT
COPY --chown=app:app docker/production/app/start-daphne-server.sh /usr/local/bin/start-daphne-server.sh
RUN chmod +x /usr/local/bin/start-daphne-server.sh
# CELERY WORKER COMMAND SCRIPT
COPY --chown=app:app docker/production/app/start-celery-worker.sh /usr/local/bin/start-celery-worker.sh
RUN chmod +x /usr/local/bin/start-celery-worker.sh

# WORKAROUND: NEED PERMISSIONS FOR COMPILATION OF CYTHON FILES
RUN chown -R app:app /code/

# WE LAUNCH THE PREPARE PRODUCTION SCRIPT AS USER 'app'
USER app
CMD ["prepare-production.sh"]