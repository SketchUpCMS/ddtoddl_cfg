import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--geometry-config', default = 'Configuration.Geometry.GeometryExtended2016_cff', help = 'the geometry config to be loaded')
parser.add_argument('-o', '--out', default = 'GeometryExtended2016.xml', help = 'output XML filename')
parser.add_argument('unused', nargs = argparse.REMAINDER, help = '')
args = parser.parse_args()

##____________________________________________________________________________||
process = cms.Process("GEOM")

##____________________________________________________________________________||
process.load(args.geometry_config)

##____________________________________________________________________________||
process.BigXMLWriter = cms.EDAnalyzer(
    "OutputDDToDDL",
    rotNumSeed = cms.int32(0),
    fileName = cms.untracked.string(args.out)
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
