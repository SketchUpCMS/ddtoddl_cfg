#!/bin/bash

set -ex
shopt -s expand_aliases
export BUILD_DIR=${PWD}
set +u && source ${CMS_PATH}/cmsset_default.sh; set -u
cmsrel ${CMSSW_RELEASE}
cd ${CMSSW_RELEASE}/src
git init
git remote add fix_chimney_hole_9_0_X https://github.com/SketchUpCMS/cmssw.git
git remote update
scram b -j 9
