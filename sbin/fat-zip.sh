#!/bin/bash -e

BASEDIR=`pwd`/`dirname $0`/..
BUILD_ZIP=${BASEDIR}/build/build.zip

source "${BASEDIR}/sbin/var-env.sh"

mkdir -p "${BASEDIR}/dist"
mkdir -p "${BASEDIR}/target"
mkdir -p "${BASEDIR}/build"

rm -Rf ${BUILD_ZIP}

echo "Download ..."
"$BASEDIR/env/bin/python" -m pip install --upgrade -t ./target/ .

echo "Add dependencies to zip:"
(cd ${BASEDIR}/target;zip -r ${BUILD_ZIP} .)
for P in $PACKAGES; do
    echo "Add source: ${P}"
    (cd ${P}; zip -ur ${BUILD_ZIP} .)
done

mv ${BUILD_ZIP} ${BASEDIR}/dist/fat-build.zip