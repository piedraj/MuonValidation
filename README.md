# Known issues or features

**2020/03/12, Muon validation changes from CMSSW_11_1_0_pre2.** The following distributions were introduced in the Muon validation from the CMSSW_11_1_0_pre2 release:

    displacedGlobalMuons
    displacedStandAloneMuons
    displacedTrks
    pfMuonTrks
    recoMuonTrks
    tunepMuonTrks

In a similar fashion, the following distributions were removed from the Muon validation from the CMSSW_11_1_0_pre2 release:

    probeTrks_MABH_vs_TABH  
    DQMData           
    PDF                
    RecoMuonV             
    seedsOfSTAMuons
    standAloneMuons
    probeTrks_TkAsso

**2019/12/20, CMS geometries.** This [README](https://github.com/cms-sw/cmssw/blob/master/Configuration/Geometry/README.md) contains short descriptions of the different CMS Run 3 and Phase2 geometries.

**2018/02/26, FullSim.** The MuonAssociatorByHits (MABH) is used for all the plots made by the MuonTrackValidator and by the RecoMuonValidator. Giovanni Abbiendi introduced a comparison with the associator used by the TrackingPOG (TABH) (which can run *only* on inner tracks) to keep under control the comparison of results obtained with our code and theirs (on inner tracks with pt > 4 GeV). This serves to avoid that low level changes in the tracking simulation/validation could go unnoticed by us. Only large discrepancies between them should be alarming, not the small differences that we see on the fake rates (while on the efficiencies they are in perfect agreement).

**2018/02/22, FastSim.** The fake rates cannot be compared with and without pmx. There aren't tracking particles with pmx, and this implies a much higher fake rate. On the other hand, the efficiencies can be compared.


# Do not go anywhere without this

Subscribe to the following CMS HyperNews forums and e-groups.

    hn-cms-alca@cern.ch
    hn-cms-muon-object-validation@cern.ch
    hn-cms-physics-validation@cern.ch
    hn-cms-relval@cern.ch
    cms-PPD-PdmV-val-admin-pdmv@cern.ch
    
# Never travel without a Grid certificate

To connect to the CMS VOMS server you need to setup a Grid certificate at your lxplus `/home/.globus` area. All the necessary information to get a new Grid User certificate, copy it to lxplus and import it to a web browser, can be found in the [Chapter 5.1](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid) of the CMS WorkBook. The Grid certificate will be needed in your web browser to access pages such as RelVal and the Muon POG Validation web page.


# Muon Validation documentation

Here you can find all the ROOT files centrally produced for validation.

    https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/

Distributions (discontinued after CMSSW_10_3_0_pre3) produced for different validations.

    https://cmsdoc.cern.ch/cms/Physics/muon/CMSSW/Performance/RecoMuon/Validation/val/

Validation database.

    https://cms-pdmv.cern.ch/valdb/

Old (2013) validation description.

    https://twiki.cern.ch/twiki/bin/view/CMS/RecoMuonValidationSuite

Automatic RelMon validations.

    https://cms-pdmv.cern.ch/relmon/

Code.

    https://github.com/cms-sw/cmssw/tree/master/Validation/RecoMuon
    https://github.com/cms-sw/cmssw/tree/master/Validation/MuonIsolation
    https://github.com/cms-sw/cmssw/tree/master/Validation/MuonIdentification
    
CMSSW release schedule.

    https://twiki.cern.ch/twiki/bin/view/CMS/ReleaseSchedule


# How to produce the muon validation plots

As usual, first login to lxplus and go to your CMSSW releases area.

    ssh -Y piedra@lxplus.cern.ch -o ServerAliveInterval=240
    bash -l
    cd work/CMSSW_projects/

Once there you need to setup the CMSSW release.

    cmsrel CMSSW_11_1_0_pre2
    cd CMSSW_11_1_0_pre2/src/
    cmsenv

If you have never used Git then you will have to follow the [First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) instructions. The following commands are the bare minimum set-up needed.

    git config --global user.name   "John Doe"
    git config --global user.email  johndoe@example.com
    git config --global user.github <your github username>

Get the muon validation package and compile it. 

    git cms-addpkg Validation/RecoMuon
    scram b -j 8
    cd Validation/RecoMuon/test

Open `new_userparams.py` and replace `User='cprieels'` by `User='piedra'`. Now click on the little green pie at the crossing of the **Muons** row and the **RelValTTbar_13** column in the [RelMon](https://cms-pdmv.cern.ch/relmon/) pie matrix. There you will find the precise names of the target and reference CMSSW releases. Use these release names in the [RelVal repository](https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/) to find the target and reference files, for example for **RelValTTbar_13**. At this point you have all the needed information to complete the `new_userparams.py` validation configuration. Do not forget to follow the syntax below.

    DQM_V0001_R000000001__RelValTTbar_13__CMSSW_9_4_4-PU25ns_94X_mc2017_realistic_v10For2017G_v2-v1__DQMIO.root
    DQM_V0001_R000000001__{samples}__{Release}-PU{PileUp}_{Condition}-{Version}__{Format}.root

You should be all set. It is time to run the muon validation.
    
    export X509_CERT_DIR=/etc/grid-security/certificates/
    voms-proxy-init -voms cms
    export X509_USER_PROXY=$(voms-proxy-info -p)
    
    python new_muonReleaseSummary.py
        
Once the validations are done you should copy (or move) them to the muon validation eos repository. The example below corresponds to the `CMSSW_10_6_0` release.

    cp -r CMSSW_10_6_0 /eos/user/c/cmsmupog/www/Validation/.
    cd /eos/user/c/cmsmupog/www/Validation/CMSSW_10_6_0
    cp ../index.php .
    find . -type d -exec cp index.php {} \;
    
Now you are left with checking the produced histograms, which will be available at the [Muon POG Validation web page](https://cms-muonpog.web.cern.ch/cms-muonpog/Validation/).


# Manual download

To manually download a file you only need to know the URL or web address.

    /usr/bin/curl -k -O -L --capath $X509_CERT_DIR --key $X509_USER_PROXY --cert $X509_USER_PROXY -w "%{http_code}" + url
    
For example.

    /usr/bin/curl -k -O -L --capath $X509_CERT_DIR --key $X509_USER_PROXY --cert $X509_USER_PROXY -w "%{http_code}" https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/CMSSW_11_0_x/DQM_V0001_R000000001__RelValZMM_14__CMSSW_11_0_0-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1__DQMIO.root
    /usr/bin/curl -k -O -L --capath $X509_CERT_DIR --key $X509_USER_PROXY --cert $X509_USER_PROXY -w "%{http_code}" https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/CMSSW_11_1_x/DQM_V0001_R000000001__RelValZMM_14__CMSSW_11_1_1-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200_raw1100-v1__DQMIO.root


# How to use DQM RelVal

To make more exhaustive validation studies it is recommended to use DQM RelVal, following the steps below.

0. Go to [DQM RelVal](https://cmsweb.cern.ch/dqm/relval/).
1. Click on **Run #**.
2. Enter the release (10_0_0) in the **Search** box.
3. Check the option **Vary By** Any.
4. Find a target dataset.
   * /RelValTTbar_13/CMSSW_10_0_0-PUpmx25ns_100X_upgrade2018_realistic_v6-v1/DQMIO
5. Find a reference dataset.
   * /RelValTTbar_13/CMSSW_10_0_0-PU25ns_100X_upgrade2018_realistic_v6_mahiOFF-v1/DQMIO
6. Click on **10_0_0(1)** in the target dataset.
7. Click on the CMS icon.
   * Paste the reference dataset in the first **Dataset** box.
   * Choose **Show reference:** For all.
   * Choose **Position:** Overlay+ratio.
   * Click again on the CMS icon.
8. Click on **Workspace**.
9. Click on **Everything**.
10. Click on **Muons**.

And you are ready to validate!
