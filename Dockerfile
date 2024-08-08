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
RUN poetry install --no-root --compile && \
    rm -rf ${POETRY_CACHE_DIR} && \
    rm pyproject.toml && \
    mv poetry.lock poetry.lock.image

##########################
# Set-up the entry script
##########################
RUN touch entry_script.sh
RUN chmod a+rx entry_script.sh
RUN echo \
'#!/bin/bash \n\
if ! test -d ${TEMPLATE_ROOT} ; then\n\
  echo "The project directory has not been mounted properly.  Please run the container with: docker run -v $""PWD:"${TEMPLATE_ROOT}" etc."\n\
  exit 1\n\
fi\n\
if ! cmp -s ${TEST_ROOT}/poetry.lock.image ${TEMPLATE_ROOT}/poetry.lock ; then\n\
  echo poetry.lock has been updated since the image was built.  Please rebuild it and try again.\n\
  exit 1\n\
fi\n\
cd ${TEMPLATE_ROOT}\n\
\n\
poetry install --only-root\n\
echo\n\
pytest' \
>> entry_script.sh
