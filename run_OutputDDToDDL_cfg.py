import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing('analysis')
options.inputFiles = 'file:dummry.root',
options.outputFile = 'dummy.root'
options.maxEvents = -1
options.register('geometryConfig',
                 'Configuration.Geometry.GeometryExtended2017_cff', # default
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 'the geometry config to be loaded')
options.register('outFilename',
                 'GeometryExtended2017.xml', # default
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 'output XML filename')
options.parseArguments()

##____________________________________________________________________________||
process = cms.Process("GEOM")

##____________________________________________________________________________||
process.load(options.geometryConfig)

##____________________________________________________________________________||
process.BigXMLWriter = cms.EDAnalyzer(
    "OutputDDToDDL",
    rotNumSeed = cms.int32(0),
    fileName = cms.untracked.string(options.outFilename)
    )

##____________________________________________________________________________||
process.pAStd = cms.EDAnalyzer(
    "PerfectGeometryAnalyzer",
    dumpPosInfo = cms.untracked.bool(False),
    label = cms.untracked.string(""),
    isMagField = cms.untracked.bool(False),
    dumpSpecs = cms.untracked.bool(False),
    dumpGeoHistory = cms.untracked.bool(False),
    outFileName = cms.untracked.string("STD"),
    numNodesToDump = cms.untracked.uint32(0),
    fromDB = cms.untracked.bool(False),
    ddRootNodeName = cms.untracked.string("cms:OCMS")
    )

##____________________________________________________________________________||
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

##____________________________________________________________________________||
process.source = cms.Source(
    "EmptyIOVSource",
    lastValue = cms.uint64(1),
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    interval = cms.uint64(1)
    )

##____________________________________________________________________________||
process.p1 = cms.Path(
    process.pAStd *
    process.BigXMLWriter
    )

##____________________________________________________________________________||
