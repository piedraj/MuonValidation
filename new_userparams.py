#! /usr/bin/env python

import os
import shutil
import sys
import fileinput
import string


#-------------------------------------------------------------------------------
#
# Input parameters
#
#-------------------------------------------------------------------------------
Submit           = True
Publish          = True
Publish_rootfile = False
WebRepository    = '/afs/cern.ch/cms/Physics/muon/CMSSW/Performance/RecoMuon/Validation/val'
User             = 'piedra'


#-------------------------------------------------------------------------------
#
# For FastSim   HLT and DQM  are set automatically to False
# For HeavyIons HLT and RECO are set automatically to False
#
#-------------------------------------------------------------------------------
ValidateHLT  = True
ValidateRECO = True
ValidateISO  = True
ValidateDQM  = True


#-------------------------------------------------------------------------------
#
# Information about the TARGET release
#
#-------------------------------------------------------------------------------
NewParams = dict(

    Type='New',
    
    Release='CMSSW_10_2_2',

    Condition='102X_upgrade2018_realistic_v11',

    PileUp='no',
    #PileUp='25ns',
    #PileUp='25ns',
    #PileUp='',  # for HeavyIons

    Version='v1',

    Format='DQMIO',

    FastSim=False,

    HeavyIons=False,

    # Needed if you copy any root file from the DQM GUI.
    # See GetLabel function for more details
    Label='',

    # Where to get the root file from. Possible values
    #    WEB: Take root files from the MuonPOG Validation repo on the web
    #    GUI: Copy root files from the DQM GUI server
    #    EOS: copy root files from Muon POG users area
    # By default, if the root files are already in the local area,
    # they won't be overwritten
    GetFilesFrom='GUI',

    DqmGuiBaseRepo='https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/',

    EOSBaseRepository='/eos/cms/store/group/phys_muon/abbiendi/RelVal/'
)


#-------------------------------------------------------------------------------
#
# Information about the REFERENCE release
# You only need to set the variables than are different from the target release
#
#-------------------------------------------------------------------------------
RefParams = dict(

    Type='Ref',

    Release='CMSSW_10_2_0',

    Condition='102X_upgrade2018_realistic_v9_gcc7',

    #PileUp='25ns',

    Version='v1'
)


#-------------------------------------------------------------------------------
#
# Samples for validation
#
#-------------------------------------------------------------------------------

# FullSim PU25ns
#samples = ['RelValZMM_13', 'RelValTTbar_13']

# FullSim noPU
samples = ['RelValZMM_13', 'RelValTTbar_13', 'RelValSingleMuPt10', 'RelValSingleMuPt100',
           'RelValSingleMuPt1000', 'RelValWM_13', 'RelValJpsiMuMu_Pt-8', 'RelValZpMM_13',
           'RelValWpM_13', 'RelValDisplacedSUSY_stopToBottom_M_300_1000mm_13']

# FastSim PU25ns
#samples = ['RelValZMM_13', 'RelValTTbar_13']
          
# FastSim noPU
#samples = ['RelValZMM_13', 'RelValTTbar_13', 'RelValSingleMuPt10_UP15', 'RelValSingleMuPt100_UP15']

# FullSim HeavyIons
#samples = ['RelValZEEMM_13_HI']
