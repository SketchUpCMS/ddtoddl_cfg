
## ddtoddl_cfg

This repo contains a simple [Python configuration](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAboutPythonConfigFile) of [CMSSW](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCMSSWFramework) for creating a big XML file of the CMS detector geometry that you can use for [SketchUpCMS](https://github.com/SketchUpCMS/SketchUpCMS).


### An example usage:

#### Check out CMSSW and enter the CMSSW environment
```bash
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSSW_9_0_0_pre5
cd CMSSW_9_0_0_pre5/src
cmsenv
```

#### Apply a patch to fix the chimney hole on the magnet
```bash
git cms-init
git cms-merge-topic -u SketchUpCMS:fix_chimney_hole_9_0_X
```

You can read about the disccussion of this patch:
 * https://github.com/cms-sw/cmssw/pull/835
 * https://github.com/cms-sw/cmssw/pull/836
 * https://github.com/cms-sw/cmssw/pull/857

The patch hasn't been merged to CMSSW. But this is necesary for SketchUp.

#### Compile
```bash
scram b -j 9
```

#### Check out this repo
```bash
git clone git@github.com:SketchUpCMS/ddtoddl_cfg.git
```

#### Create a big XML file
```bash
cmsRun ddtoddl_cfg/run_OutputDDToDDL_cfg.py
```
By default, it uses the geometry config file [`Configuration.Geometry.GeometryExtended2016_cff`](https://github.com/cms-sw/cmssw/blob/CMSSW_9_0_0_pre5/Configuration/Geometry/python/GeometryExtended2016_cff.py) and create the big XML file `GeometryExtended2016.xml`.

The file `GeometryExtended2016.xml` can be used as an input to [SketchUpCMS](https://github.com/SketchUpCMS/SketchUpCMS).

You can specify the geometry config and the output XML filename as arguments to `cmsRun`. For example
```bash
cmsRun ddtoddl_cfg/run_OutputDDToDDL_cfg.py geometryConfig=Configuration.Geometry.GeometryExtended2023D11_cff outFilename=GeometryExtended2023D11.xml
```
will use one of the Phase 2 upgrade geometry config [`Configuration.Geometry.GeometryExtended2023D11_cff`](https://github.com/cms-sw/cmssw/blob/CMSSW_9_0_0_pre5/Configuration/Geometry/python/GeometryExtended2023D11_cff.py) and create a big XML file  with the filename `GeometryExtended2023D11.xml`.


