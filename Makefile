# The following are needed to make sure that running:
#  $ make -f <path>/Makefile
# will work with this Makefile.
MAKEFILE_PATH = $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR = $(dir $(MAKEFILE_PATH))
PRJ_PATH=$(realpath ${MAKEFILE_DIR} )
PRJ_SLUG=$(notdir ${PRJ_PATH})

docker-build:
	docker build -t ${PRJ_SLUG} .

docker-tests:
	docker run --rm -v ${PRJ_PATH}:/template ${PRJ_SLUG}
