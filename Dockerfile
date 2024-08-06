#############
# Base image
#############
FROM python:3.11-buster

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

ENV TEST_ROOT /test_template
ENV TEMPLATE_ROOT /template

WORKDIR ${TEST_ROOT}

################################################################
# Copy and install Poetry dependencies (but not the actual 
# application, which will get installed by the entry_point 
# script when we start the container)
################################################################
COPY pyproject.toml poetry.lock .
RUN poetry install --no-root && \
    rm -rf ${POETRY_CACHE_DIR} && \
    rm pyproject.toml && \
    mv poetry.lock poetry.lock.image

##########################
# Set-up the entry point
##########################
RUN touch entry_script.sh
RUN chmod a+rx ${TEST_ROOT}/entry_script.sh
RUN echo '\n\
set -e \n\
\n\
_term() {\n\
  echo "Caught SIGTERM signal!"\n\
  kill -TERM "$child" 2>/dev/null\n\
}\n\
\n\
# trap _term SIGTERM\n\
\n\
if ! test -d ${TEMPLATE_ROOT} ; then \n\
  echo The project directory has not been mounted.  Please run the container with e.g. 'docker run -v \$PWD:${TEMPLATE_ROOT}' \n\
  exit 1 \n\
fi \n\
if ! cmp -s ${TEST_ROOT}/poetry.lock.image ${TEMPLATE_ROOT}/poetry.lock ; then \n\
  echo poetry.lock has been updated since the image was built.  Please rebuild it and try again. \n\
  exit 1 \n\
fi \n\
cd ${TEMPLATE_ROOT} \n\
poetry install --only-root \n\
pytest' >> ${TEST_ROOT}/entry_script.sh
ENTRYPOINT ["sh", "-c", "${TEST_ROOT}/entry_script.sh"]
