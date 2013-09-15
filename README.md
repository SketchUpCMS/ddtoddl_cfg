
An example usage:

        cmsrel CMSSW_5_3_12
        cd CMSSW_5_3_12/src
        cmsenv
        git clone git@github.com:SketchUpCMS/ddtoddl_cfg.git
        cmsRun ddtoddl_cfg/run_OutputDDToDDL_cfg.py

This will create a file

        GeometryExtended.xml


This xml file can be used as an input to
[SketchUpCMS](https://github.com/SketchUpCMS/SketchUpCMS).

