# Stay tuned

Subscribe to the following CMS Talk categories and CERN e-groups.

* [ALCADB](https://cms-talk.web.cern.ch/c/ppd/alca/108)
* [Muon Objects Validation](https://cms-talk.web.cern.ch/c/muons/muon-object-validation/175)
* [PDMV](https://cms-talk.web.cern.ch/c/ppd/pdmv/107)
* [RelVal Samples and Release Testing](https://cms-talk.web.cern.ch/c/ppd/pdmv/relval/111)
* [cms-PPD-PdmV-MCval](https://e-groups.cern.ch/e-groups/Egroup.do?egroupName=cms-PPD-PdmV-MCval)
* [cms-PPD-PdmV-DATAval](https://e-groups.cern.ch/e-groups/Egroup.do?egroupName=cms-PPD-PdmV-DATAval)


# Access rights

* Ask the [Muon POG conveners](cms-muon-pog@cern.ch) to be included in the **cms-muon-pog-people** e-group, so you can access `/eos/user/c/cmsmupog`.
* Ask the [PdmV conveners](cms-PPD-conveners-PdmV@cern.ch) for **Muon data and MC** write access in [ValDB](https://cms-pdmv.cern.ch/valdb/).


# Never travel without a Grid certificate

To connect to the CMS VOMS server you need to setup a Grid certificate at your lxplus `/home/.globus` area. All the necessary information to get a new Grid User certificate, copy it to lxplus and import it to a web browser, can be found in the [Chapter 5.1](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid) of the CMS WorkBook. The Grid certificate will be needed in your web browser to access pages such as RelVal and the Muon POG Validation web page.


# Muon Validation documentation

* [CMSSW release schedule](https://twiki.cern.ch/twiki/bin/view/CMS/ReleaseSchedule) TWiki
* [PdmV release validation general instructions for validators](https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVRelValValidatorInstruction) TWiki
* [Offline Muon DQM plot description](https://twiki.cern.ch/twiki/bin/view/CMS/MuonsDQMPlots) TWiki
* [GitHub Validation/RecoMuon code](https://github.com/cms-sw/cmssw/tree/master/Validation/RecoMuon)
* [GitHub Validation/MuonIdentification code](https://github.com/cms-sw/cmssw/tree/master/Validation/MuonIdentification) 
* [GitHub Validation/MuonIsolation code](https://github.com/cms-sw/cmssw/tree/master/Validation/MuonIsolation)


# How to produce the muon validation plots

First of all, open the [2024 Muon Validation spreadsheet](https://docs.google.com/spreadsheets/d/1JrD1fEHujlLBdoDZtHuaWeM2SX5UTlgUMU9hTUxBjeY/edit#gid=829147341) and write down your name in the validation that you will perform. Then login to lxplus and go to your CMSSW releases area.

    ssh -Y <your lxplus username>@lxplus.cern.ch -o ServerAliveInterval=240
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

Open `new_userparams.py` and replace `cprieels` by your `$USER` name.

For each release validation go to the **FullSimReport** (and **FullSimReport_PU**) [RelMon](https://cms-pdmv.cern.ch/relmon/) Subcategory, scroll down until you find the pie matrix, and click on the green pie that corresponds to the crossing of the **Muons** row and the **RelValTTbar_14** column. There you will find the precise names of the target and reference CMSSW releases. If needed, use these release names to find the target and reference files in the [RelVal repository](https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/), for example for **RelValTTbar_14**. At this point you have all the needed information to complete the `new_userparams.py` validation configuration. Do not forget to follow the syntax below.

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


# Data validation

0. Go to [ValDB](https://cms-pdmv.cern.ch/valdb/) and click on one of the Data Campaigns, such as 13_3_0_Data.
1. Once inside the Data Campaign, click on the **Relmon** link.
2. Click on **DataReport** within the different RelMon Subcategories.
3. Once inside the **RelMon** DataReport you'll have to scroll down to the Summary Table (pie chart collection) and look for the columns that correspond to muon only datasets. In the 13_3_0_Data validation there are three RelVals:
   * Muon_133X_dataRun3_v3_Data_2022_RelVal_2022D_357735
   * SingleMuon_133X_dataRun3_v3_Data_2022_RelVal_2022B_355769
   * SingleMuon_133X_dataRun3_v3_Data_2022_RelVal_2022C_356381
4. For each RelVal go the row that corresponds to the **Muons** pie chart and click on it.
5. Next you will have to click on the **To the DQM gui...** link.
6. Once you are in the CMS DQM GUI, click first on the CMS icon on the top left corner. You will have to choose for the Reference histograms that the **Position** is Overlay+ratio
7. You are all set to validate, at least, the following **Muons** distributions:
   * **MuonRecoAnalyzer** folder
   * **Isolation** folder
   * **Tracking** -> innerTrack -> GeneralProperties folder
   * **RecoDisplacedMuonV** folder (MC only)

<!---
<details>
  <summary><h1>Deprecated</h1></summary>

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
 
</details>
-->
