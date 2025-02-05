FROM node:19-alpine
WORKDIR /cache/

# NODEJS DEPENDENCIES
COPY --chown=node:node ./frontend/package*.json .
RUN apk update \
    && apk add --no-cache --virtual .build-deps python3 make g++ git \
    && npm install \
    && apk del .build-deps

WORKDIR /frontend/
ENV PATH /frontend/node_modules/.bin:$PATH

# CONTAINER ENTRYPOINT: WAITS FOR THE DATABASE TO BE READY
# Note: Entrypoint commands are run before every commands run in the container
COPY --chown=node:node docker/development/frontend/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Note: Container is run with default user of node image (user 'node')
ENTRYPOINT ["entrypoint.sh"]
CMD ["npm", "run", "development"]