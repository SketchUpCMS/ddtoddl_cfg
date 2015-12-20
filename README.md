
An example usage:

```bash
cmsrel CMSSW_5_3_32
cd CMSSW_5_3_32/src
cmsenv
git cms-init
git cms-merge-topic -u SketchUpCMS:fix_chimney_hole
scram b -j 9
git clone git@github.com:SketchUpCMS/ddtoddl_cfg.git
cmsRun ddtoddl_cfg/run_OutputDDToDDL_cfg.py
```

This will create a file

```
GeometryExtended.xml
```

This xml file can be used as an input to
[SketchUpCMS](https://github.com/SketchUpCMS/SketchUpCMS).

