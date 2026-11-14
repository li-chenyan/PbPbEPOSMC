import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("ReggeGribovPartonMCGeneratorFilter",
    # impact parameter min in fm
    bmin = cms.double(9),
    # impact parameter max in fm
    bmax = cms.double(30),
    # file with more parameters specific to crmc interface
    paramFileName = cms.untracked.string("Configuration/Generator/data/ReggeGribovPartonMC.param"),
    # in HI collisions nuclear fragments with pt=0 can be in the hep event. to skip those activate this option
    skipNuclFrag = cms.bool(True),
	beammomentum = cms.double(2680),
	targetmomentum = cms.double(-2680),
    beamid = cms.int32(208),
    targetid = cms.int32(208),
    model = cms.int32(0),
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/ReggeGribovPartonMC_EposLHC_PbPb_MinimumBias_cfi.py,v $'),
    annotation = cms.untracked.string('ReggeGribovMC generator')
)

particlefilter = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.5,2.5),
    Status = cms.untracked.vint32(1,1),
    MinEta = cms.untracked.vdouble(-2.5,-2.5),
    MinPt = cms.untracked.vdouble(0.75,0.75),
    ParticleID = cms.untracked.vint32(3122,-3122)
)

ProductionFilterSequence = cms.Sequence(generator+particlefilter)