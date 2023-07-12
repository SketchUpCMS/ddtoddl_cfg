# ddtoddl_cfg

This repo contains a simple [Python configuration](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAboutPythonConfigFile) of [CMSSW](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCMSSWFramework) for creating a big XML file of the CMS detector geometry that you can use for [SketchUpCMS](https://github.com/SketchUpCMS/SketchUpCMS).


## Usage

### Check out CMSSW and enter the CMSSW environment

New CMSSW releases for now do not have the patch mentioned below. Regardless, this code will work 
on newer CMSSW releases (such as CMSSW_12_X) but will not have the fixes the patch addresses (for now).

Also, older releases of CMSSW such as CMSSW_9_X no longer can be run on an lxplus-like environment. So the 
solution is to run in a Docker container with CMSSW_9_X. 

Instructions for both are given below.

#### In an lxplus-like environment

```bash
export SCRAM_ARCH=slc7_amd64_gcc10
scram project CMSSW_12_3_4
cd CMSSW_12_3_4/src
cmsenv
```

#### In a Docker container

Create and run the Docker container:

```
docker run -it --rm gitlab-registry.cern.ch/cms-cloud/cmssw-docker/cmssw_9_2_1-slc7_amd64_gcc530:2020-08-25-a8685cef /bin/bash
```

This will start the container and you will be in the `CMSSW_9_2_1/src` dir:

```
Setting up CMSSW_9_2_1
WARNING: Developer's area is created for non-production architecture slc7_amd64_gcc530. Production architecture for this release is slc6_amd64_gcc530.
CMSSW should now be available.
[12:38:22] cmsusr@695b565ca016 ~/CMSSW_9_2_1/src $ cmsenv
```

Apply a patch to fix the chimney hole on the magnet

```bash
git cms-init
git cms-merge-topic -u SketchUpCMS:fix_chimney_hole_9_0_X
```

You can read about the disccussion of this patch:
 * https://github.com/cms-sw/cmssw/pull/835
 * https://github.com/cms-sw/cmssw/pull/836
 * https://github.com/cms-sw/cmssw/pull/857

The patch hasn't been merged to CMSSW. But this is necesary for SketchUp.

Compile: 

```bash
scram b -j 9
```

### Check out this repo
```bash
git clone git@github.com:SketchUpCMS/ddtoddl_cfg.git
```

Note: Unless you also mount your `.ssh` dir when you start the Docker container you will not have ssh access to
the git repo from within the container. In this case you can:

```bash
git clone https://github.com/SketchUpCMS/ddtoddl_cfg.git
```

### Create a big XML file
```bash
cmsRun ddtoddl_cfg/run_OutputDDToDDL_cfg.py
```
By default, it uses the geometry config file [`Configuration.Geometry.GeometryExtended2017_cff`](https://github.com/cms-sw/cmssw/blob/CMSSW_9_0_0_pre5/Configuration/Geometry/python/GeometryExtended2017_cff.py) and create the big XML file `GeometryExtended2017.xml`.

The file `GeometryExtended2017.xml` can be used as an input to [SketchUpCMS](https://github.com/SketchUpCMS/SketchUpCMS).

You can specify the geometry config and the output XML filename as arguments to `cmsRun`. For example
```bash
cmsRun ddtoddl_cfg/run_OutputDDToDDL_cfg.py geometryConfig=Configuration.Geometry.GeometryExtended2023D11_cff outFilename=GeometryExtended2023D11.xml
```
will use one of the Phase 2 upgrade geometry config [`Configuration.Geometry.GeometryExtended2023D11_cff`](https://github.com/cms-sw/cmssw/blob/CMSSW_9_0_0_pre5/Configuration/Geometry/python/GeometryExtended2023D11_cff.py) and create a big XML file  with the filename `GeometryExtended2023D11.xml`.


