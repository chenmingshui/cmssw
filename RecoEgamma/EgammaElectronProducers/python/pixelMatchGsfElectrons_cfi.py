import FWCore.ParameterSet.Config as cms

# module to produce gsf electrons
#
pixelMatchGsfElectrons = cms.EDProducer("GsfElectronProducer",

    # input collections
    barrelSuperClusters = cms.InputTag("correctedHybridSuperClusters","electronPixelSeeds"),
    endcapSuperClusters = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower","electronPixelSeeds"),
    tracks = cms.InputTag("pixelMatchGsfFit"),
    ctfTracks = cms.InputTag("generalTracks"),
    hcalRecHits = cms.InputTag("hbhereco"),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    # steering
    applyEtaCorrection = cms.bool(False),
    applyAmbResolution = cms.bool(True),    
    # preselection parameters
    minEOverPBarrel = cms.double(0.0),
    maxEOverPBarrel = cms.double(10000.0),
    minEOverPEndcaps = cms.double(0.0),
    maxEOverPEndcaps = cms.double(10000.0),
    maxDeltaEta = cms.double(0.02),
    maxDeltaPhi = cms.double(0.1),
    # electron algo
    ElectronType = cms.string(''),
    # nested parameter set for TransientInitialStateEstimator
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    )

)


