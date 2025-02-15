#############
# Base image
#############
FROM python:3.11-buster

ENV HOME=/home/pytest
ENV USERNAME=pytest
ENV PACKAGE_ROOT ${HOME}/package

# Create user USERNAME
RUN mkdir -p ${HOME} && \
    useradd --home-dir ${HOME} ${USERNAME} && \
    chown ${USERNAME} ${HOME}

############################################################
# Switch to the user that we just created
#===========================================================
# n.b.: we're not running as root because root's ability
#       to write to read-only temp files (!) can break tests
#       that check for proper I/O exceptions, for example
############################################################
USER ${USERNAME}
WORKDIR ${HOME}

##################################################
# Create a virtual env and install poetry into it
##################################################
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=0
ENV POETRY_CACHE_DIR=/tmp/poetry_cache
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install poetry

################################################################
# Copy and install Poetry dependencies (but not the actual 
# application, which will get installed by the entry_point 
# script when we start the container).  Clear the cache after
# to lighten the container.
################################################################
COPY pyproject.toml poetry.lock .
RUN . venv/bin/activate && \
    poetry install --no-root --compile && \
    rm -rf ${POETRY_CACHE_DIR} && \
    rm pyproject.toml

#################################################3
# Make a copy of the lock file so we can check for
# changes in the entry script (below).
#################################################3
RUN mv poetry.lock ${HOME}/poetry.lock.image

##########################
# Set-up the entry script
##########################
RUN touch entry_script.sh
RUN chmod a+rx entry_script.sh
RUN echo \
'#!/bin/bash \n\
# Check that the container was run with a defined PACKAGE_ROOT\n\
if ! test -d ${PACKAGE_ROOT} ; then\n\
  echo "The project directory has not been mounted properly.  Please run the container with: docker run -v $""PWD:"${PACKAGE_ROOT}" etc."\n\
  exit 1\n\
fi\n\
# Check that the lock file hasn't changed since the container was built\n\
# (if it has, then the container should be rebuilt)\n\
if ! cmp -s ${HOME}/poetry.lock.image ${PACKAGE_ROOT}/poetry.lock ; then\n\
  echo poetry.lock has been updated since the image was built.  Please rebuild it and try again.\n\
  exit 1\n\
fi\n\
# Activate the virtual env\n\
cd ${HOME}\n\
. venv/bin/activate\n\
# Install the version of the package that is on disk when the container is run\n\
cd ${PACKAGE_ROOT}\n\
poetry install --only-root\n\
echo\n\
# Run pytest\n\
pytest' \
>> entry_script.sh
