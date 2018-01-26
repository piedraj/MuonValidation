# 0. Do not go anywhere without this

Subscribe to the following CMS HyperNews forums.

    hn-cms-alca@cern.ch
    hn-cms-muon-object-validation@cern.ch
    hn-cms-physics-validation@cern.ch
    hn-cms-relval@cern.ch

# 1. Muon Validation documentation

Here you can find the files produced for validation.

    https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/

Distributions produced in different validations.

    https://cmsdoc.cern.ch/cms/Physics/muon/CMSSW/Performance/RecoMuon/Validation/val/

Validation database.

    https://cms-pdmv.cern.ch/valdb/

Old (2013) validation description.

    https://twiki.cern.ch/twiki/bin/view/CMS/RecoMuonValidationSuite

Automatic Relmon validations.

    http://cms-service-reldqm.web.cern.ch/cms-service-reldqm/cgi-bin/RelMon.py

Code.

    https://github.com/cms-sw/cmssw/tree/master/Validation/RecoMuon
    https://github.com/cms-sw/cmssw/tree/master/Validation/MuonIsolation
    https://github.com/cms-sw/cmssw/tree/master/Validation/MuonIdentification


# 2. How to produce the muon validation plots

As usual, first login to lxplus and go to your CMSSW releases area.

    ssh -Y piedra@lxplus.cern.ch -o ServerAliveInterval=240
    bash -l
    cd work/CMSSW_projects/

Once there you need to setup the CMSSW release.

    export SCRAM_ARCH=slc6_amd64_gcc530
    cmsrel CMSSW_9_3_0_pre1
    cd CMSSW_9_3_0_pre1/src/
    cmsenv

Here comes the validation part. Get the package from the official repository, and then copy the modified files from rocio's public area.

    git cms-addpkg Validation/RecoMuon

    cd Validation/RecoMuon/test

    git clone https://github.com/piedraj/MuonValidation

    cp MuonValidation/muonReleaseSummaryValidation.py .
    cp MuonValidation/userparams.py .
    cp MuonValidation/macro/* macro/.

In principle you are all set. It is time to run the muon validation.

    cd Validation/RecoMuon/test
    export X509_USER_PROXY=/tmp/x509up_u23679
    export X509_CERT_DIR=/etc/grid-security/certificates/
    voms-proxy-init -voms cms
    python muonReleaseSummaryValidation.py

Now you can start doing the real work. You should modify the **userparams.py** file with the information that you will find in [RelMon](https://cms-pdmv.cern.ch/relmon/), at the crossing of the **Muon** and **TTbar** lines.

    emacs -nw RecoMuon/test/userparams.py

    NewParams
      Type='New',
      Release='CMSSW_10_0_0_pre3_GEANT4',
      Release_c='CMSSW_10_0_0_pre3_GEANT4',  # Name of the output folder
      Condition='100X_upgrade2018',
      PileUp='no',
      FastSim=False,
      Label='realistic_v4_mahiON',
      Version='v1'

    RefParams
      Type='Ref',
      Release='CMSSW_10_0_0_pre3',
      Release_c='CMSSW_10_0_0_pre3',  # Name of the output folder
      Condition='100X_upgrade2018',
      PileUp='no',
      FastSim=False,
      Label='realistic_v4_mahiON',
      Version='v1'

# 3. Things to do

* Update the output to a more web friendly format, from pdf pages to png figures.
* Check which validation distributions should be removed.
* Improve (if possible) the information available in the titles of the histograms.
* Check / update the Kolmogorov-Smirnov (KS) test threshold.
* Check the horizontal and vertical ranges.
