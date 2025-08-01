# Converted PDF

Special Issue Reprint

Data Mining and Machine

Learning with Applications

Edited by

Wei Fang

mdpi.com/journal/mathematics

Data Mining and Machine Learning

with Applications

Data Mining and Machine Learning

with Applications

Editor

WeiFang

Basel•Beijing•Wuhan•Barcelona•Belgrade•NoviSad•Cluj•Manchester

Editor

WeiFang

NanjingUniversityofInformation

Science&Technology

Nanjing,China

EditorialOffice

MDPI

St.Alban-Anlage66

4052Basel,Switzerland

This is a reprint of articles from the Special Issue published online in the open access journal

Mathematics(ISSN2227-7390) (availableat:https://www.mdpi.com/si/mathematics/DataMining

MachLearn).

Forcitationpurposes,citeeacharticleindependentlyasindicatedonthearticlepageonlineandas

indicatedbelow:

Lastname,A.A.;Lastname,B.B.ArticleTitle.JournalNameYear,VolumeNumber,PageRange.

ISBN978-3-0365-9807-9(Hbk)

ISBN978-3-0365-9818-5(PDF)

doi.org/10.3390/books978-3-0365-9818-5

© 2024 by the authors. Articles in this book are Open Access and distributed under the Creative

CommonsAttribution(CCBY)license.ThebookasawholeisdistributedbyMDPIundertheterms

and conditions of the Creative Commons Attribution-NonCommercial-NoDerivs (CC BY-NC-ND)

license.

Contents

AbouttheEditor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . vii

JingLu,HongjunChaiandRuchunJia

AGeneralFrameworkforFlightManeuversAutomaticRecognition

Reprintedfrom:Mathematics2022,10,1196,doi:10.3390/math10071196 . . . . . . . . . . . . . . . 1

WeiFang,YuShaandVictorS.Sheng

SurveyontheApplicationofArtificialIntelligenceinENSOForecasting

Reprintedfrom:Mathematics2022,10,3793,doi:10.3390/math10203793 . . . . . . . . . . . . . . . 17

YousefAlmaghthawi,IftikharAhmadandFawazE.Alsaadi

PerformanceAnalysisofFeatureSubsetSelectionTechniquesforIntrusionDetection

Reprintedfrom:Mathematics2022,10,4745,doi:10.3390/math10244745 . . . . . . . . . . . . . . . 39

PanZheng,WenqinZhao,YaqiongLv,LuQianandYifanLi

HealthStatus-BasedPredictiveMaintenanceDecision-MakingviaLSTMandMarkovDecision

Process

Reprintedfrom:Mathematics2023,11,109,doi:10.3390/math11010109. . . . . . . . . . . . . . . . 65

AdelA.Ahmed,SharafJ.Malebary,WaleedAliandAhmedA.Alzahrani

A Provable Secure Cybersecurity Mechanism Based on Combination of Lightweight

CryptographyandAuthenticationforInternetofThings

Reprintedfrom:Mathematics2023,11,220,doi:10.3390/math11010220. . . . . . . . . . . . . . . . 79

Ali Raza, Sharjeel Adnan, Muhammad Ishaq, Hyung Seok Kim, Rizwan Ali Naqvi and

Seung-WonLee

AssistingGlaucomaScreeningProcessUsingFeatureExcitationandInformationAggregation

TechniquesinRetinalFundusImages

Reprintedfrom:Mathematics2023,11,257,doi:10.3390/math11020257. . . . . . . . . . . . . . . . 103

Gaeithry Manoharam, Mohd Shareduwan Mohd Kasihmuddin, Siti Noor Farwina

MohamadAnwarAntony,NurulAtiqahRomli,Nur‘AfifahRusdi,etal.

Log-Linear-BasedLogicMiningwithMulti-DiscreteHopfieldNeuralNetwork

Reprintedfrom:Mathematics2023,11,2121,doi:10.3390/math11092121 . . . . . . . . . . . . . . . 123

TariqAhamedAhanger,UsmanTariq,FadlDahan,ShafiqueA.ChaudhryandYasirMalik

SecuringIoTDevicesRunningPureOSfromRansomwareAttacks:LeveragingHybridMachine

LearningTechniques

Reprintedfrom:Mathematics2023,11,2481,doi:10.3390/math11112481 . . . . . . . . . . . . . . . 153

JuanLaborda,SoniaRuanoandIgnacioZamanillo

Multi-CountryandMulti-HorizonGDPForecastingUsingTemporalFusionTransformers

Reprintedfrom:Mathematics2023,11,2625,doi:10.3390/math11122625 . . . . . . . . . . . . . . . 177

YifenLiandYuanyangChen

NSNet: AnN-ShapedConvolutionalNeuralNetworkwithMulti-ScaleInformationforImage

Denoising

Reprintedfrom:Mathematics2023,11,2772,doi:10.3390/math11122772 . . . . . . . . . . . . . . . 203

Sebastia´n Va´zquez-Ram´ırez, Miguel Torres-Ruiz, Rolando Quintero, Kwok Tai Chui and

CarlosGuzma´nSa´nchez-Mejorada

AnAnalysisofClimateChangeBasedonMachineLearningandanEndoreversibleModel

Reprintedfrom:Mathematics2023,11,3060,doi:10.3390/math11143060 . . . . . . . . . . . . . . . 223

v

JamolbekMattiev,MonteDavityanandBrankoKavsek

ACMKC: A Compact Associative Classification Model Using K-Modes Clustering with Rule

RepresentationsbyCoverage

Reprintedfrom:Mathematics2023,11,3978,doi:10.3390/math11183978 . . . . . . . . . . . . . . . 249

vi

About the Editor

WeiFang

WeiFangisaProfessorintheSchoolofComputerScienceatNanjingUniversityofInformation

Science&Technology,China,andDirectoroftheInstituteofArtificialIntelligenceandMeteorological

BigData(AIMB).HewasavisitingscholarattheUniversityofFloridafrom2015to2016.Currently,

Prof. FangalsoservesasaseniormemberoftheChinaComputerFederation(CCF),anexecutive

member of the Committee of Computer Applications of CCF, a member of the Chinese Artificial

Intelligence Society, a Program Reviewer of the National Natural Science Foundation of China,

a Program Reviewer of the Ministry of Science and Technology, and a Dissertation Reviewer

of the Ministry of Education Expert, a Reviewer of the National Postdoctoral Innovation and

EntrepreneurshipCompetition, andamemberoftheJiangSuAssociationofArtificialIntelligence.

Prof. Fanghaspresidedoveronetop-levelprojectoftheNationalNaturalScienceFoundationof

China,fourprovincialandministerialprojects,andthreemunicipalprojects,andhasparticipatedin

ninenational,provincialandministerialresearchprojects. Hehaspublishedmorethan30academic

papersindexedinSCIandEI,authorized12nationalinventionpatents,andbeengranted10software

copyrights. He has served as the chair of ICAIS International Conference Workshops, TURCAIS

2019,aTPCMemberoftheMLAI2022InternationalConference,aguesteditorofmanySCIjournals,

andareviewerofnumerousinternationalacademicjournals.

vii

mathematics

Article

A General Framework for Flight Maneuvers Automatic Recognition

JingLu1,2,*,HongjunChai2andRuchunJia3

1 CollegeofComputerScienceandTechnology,NanjingUniversityofAeronauticsandAstronautics,

Nanjing211106,China

2 CollegeofComputerScience,CivilAviationFlightUniversityofChina,Guanghan618307,China;

chaihongjun@cafuc.edu.cn

3 WangjiangCampus,SichuanUniversity,Chengdu610065,China;ruchunjia@zaibei.org.cn

* Correspondence:lujing_cafuc@nuaa.edu.cn

Abstract: FlightManeuverRecognition(FMR)referstotheautomaticrecognitionofaseriesof

aircraftflightpatternsandisakeytechnologyinmanyfields. Thechaoticnatureofitsinput

dataandtheprofessionalcomplexityoftheidentificationprocessmakeitdifficultandexpensive

toidentify,andnoneoftheexistingmodelshavegeneralgeneralizationcapabilities. Ageneral

frameworkisproposedinthispaper,whichcanbeusedforallkindsofflighttasks,independent

oftheaircrafttype. Wefirstpreprocessedtherawdatawithunsupervisedclusteringmethod,

segmenteditintomaneuversequences,thenreconstructedthesequencesinphasespace,calculated

theirapproximateentropy,quantitativelycharacterizedthesequencecomplexity,anddistinguished

theflightmaneuvers.Experimentsonarealflighttrainingdatasethaveshownthattheframework

canquicklyandcorrectlyidentifyvariousflightmaneuversformultipleaircrafttypeswithminimal

humanintervention.

Keywords:FlightManeuverRecognition(FMR);unsupervisedclustering;phasespacereconstruction

Citation:Lu,J.;Chai,H.;Jia,R.A 1.Introduction

GeneralFrameworkforFlight

FlightManeuver,accordingtothestandarddefinitiongivenbytheFederalAviation

ManeuversAutomaticRecognition.

Administration(FAA)[1],referstoaseriesofflightpatternsofanaircraftunderthecontrol

Mathematics2022,10,1196.

ofthepilot.FMRasakeytechnologyforautomaticevaluationofflighttechnologyisthe

https://doi.org/10.3390/

math10071196 focusofresearchontheapplicationofartificialintelligenceinthefieldofflighttraining.

Inthe1970s,forone-on-one,air-to-aircombattraining,NASAdevelopedanadaptive

AcademicEditor:PaoloCrippa

maneuveringlogiccomputerprogram(AML)[2,3],whichprovidesanvirtualcompetitor

Received:3March2022 forhumanpilotsatNASALangleyResearchCenter’s(LRC)DifferentialManeuvering

Accepted:1April2022 Simulator(DMS).AsAI,AMLrecognizesthemaneuversandintentionsoftheopponent

Published:6April2022 andmakestherightdecisionstodrivethenextmaneuvers.Inaddition,thestudyofflight

maneuvers’aircraftloadsisanimportantissueinthefieldofflightsafetyinvolvingaircraft

Publisher’sNote:MDPIstaysneutral

design,flightcertification,andaccidentinvestigation,andFMRisthebasictechnology

withregardtojurisdictionalclaimsin

forthisstudy.BarndtG.[4]examinedhowtheNavycouldprocessrawparameterdata

publishedmapsandinstitutionalaffil-

generated by HUMS to identify the maneuvers flown so as to support the structural

iations.

monitoringfunctionin2007.Manystudiesinthisareahavebeengeneratedsincethen.

AlthoughthereisalsoawidedemandforFMRinthefieldofUAVandaircombat

research,duetothelimitationofdatasourcesandauthor’sconcentration,thispaperonly

Copyright: © 2022 by the authors. focusesonmannedfixed-wingcivilaviationtrainingflight.

Licensee MDPI, Basel, Switzerland. TherawdataofFMRismultivariatetime-seriesdatageneratedfromnonlinearaircraft

Thisarticleisanopenaccessarticle powersystem,whichhastypicalchaoticcharacteristicsandcannotbedirectlyapplied

distributed under the terms and tocommontimeseriesanalysismethods. Asanartificialmechanicaloperatingsystem,

conditionsoftheCreativeCommons thedataperformanceofthesameflightmaneuverofdifferentpilotsofdifferenttypesof

Attribution(CCBY)license(https:// aircraftisverydifferent,nottomentiontheinfluenceofenvironmentalfactorssuchas

creativecommons.org/licenses/by/ weathervariation.

4.0/).

Mathematics2022,10,1196.https://doi.org/10.3390/math10071196 https://www.mdpi.com/journal/mathematics

1

Mathematics2022,10,1196

Essentially,FMRisamultiplenonlineartime-seriespattern-recognitionproblem[5].

Pattern-recognitionproblemsmainlyincludeclassificationandclustering.

Classification-basedFMR

Inthetime-seriesclassificationproblem,featurevolumeconstructionandclassifier

designarethecoreproblems.Time-seriesclassificationaimstotakethewholetimeseries

asinputtoassignadiscretelabel.InFMR,differentmaneuversoftenhavedifferentlengths

duetodifferencesinaircrafttypes,andthesamemaneuvershavedifferentlengthsdue

todifferencesinpilotoperatinghabits.Itismoredifficultthanthegeneralclassification

problemowingtotheinequationallengthoftheclassifiedtime-seriesdata,whichmakesit

impossibletoapplythegeneralclassificationalgorithmdirectly.

Inordertosolvethesedifficulties,thereareusuallytwoapproaches.First,definethe

appropriatedistancedegreeusingadistance-basedpattern-recognitionmethod,suchas

DynamicTimeWarping(DTW)distance[6–8],LocalitySensitiveHash(LSH)distance[9],

andApproximateEntropy[10].Theadvantagesofthesemethodsarethattheyconformto

thebasicprinciplesofpatternrecognition;themoresimilarthepatternsare,thesmaller

theirdistancesare;andthealgorithmsaresimpleandeasytoimplement,donotlimit

the length of the time series between patterns, and can analyze nonlinear time series.

Thesignificantdisadvantagesareexpensivecalculationandinabilitytoidentifysubtle

differencesbetweenpatterns.

Second,usingknowledgerulesorcontext-dependentmodeling,eachsequenceisrep-

resentedbyanequal-lengthandsame-dimensionfeaturevectorofmodelparametersand

thentrainedandclassifiedbyaconventionalclassificationalgorithm,whichisadomain-

relatedapproachcalledthemodel-basedmethod.Ingeneral,model-basedFMRmethods

canbedividedintofourcategories:(1)featureextraction-based[11–14],(2)expertknowl-

edgerule-based[15–27],(3)probabilisticgraphicalmodel-based[28–31],and(4)neural

network-based[32–36].

(1)ThemainmethodsforfeatureextractionareSVDandSVMmethods,combined

withleastsquaresorhierarchicalclassificationmethods,whichreducethecomputational

effortbyreducingthenumberofdimensionsandcompressingthedata.Themodelsare

simpleandeasytotrainbutarenotcomplete,andtheyaresensitivetotemporallengthand

requiremanualpriorknowledge.(2)Theexpertknowledgerulemodelmethodneedsto

establishtheartificialruleknowledgedatabasefirst,thenusethepattern-matchingquery

methodtoachieverecognition.TheknowledgeruleextractionmethodincludesNatural

LanguageProcessing,GeneticAlgorithm,andSwarmOptimization.Thistypeofmethod

isverywidelyused,withhighrecognitionefficiencyandcorrectrate,buttheunavoidable

disadvantagesarehighlaborcost;thefactthatacertainmodelonlycorrespondstoacertain

typeofaircrafttypeorflighttask;andtheinabilityofthemethodbegeneralized.(3)The

probabilisticgraphicalmodel-basedmainlyuseshiddenMarkovmodel(HMM),Kalman

filtering,anddynamicBayesianmethods,whichcannotonlyidentifybutalsopredict

andonlyneedafewparameterstoformacompletemodelbutcannothandlenonlinear

time series. (4) The model based on neural network work uses deep neural network

withfullysupervisedtrainingmethodtoconstitutethemodel,withhighrecognitionrate

andgoodmodelmaturitybutalsowithhighcostofintegrationwithlabeleddataand

computationalcomplexity.Differentaircrafttypescorrespondtodifferentmodelsandneed

tobecompletelyretrained.

Naturally,hybridmethodscombiningmultiplemethodshavealsobeenproposed[37,38];

thesemethodshavebetterrecognitionperformancebutstilldonothavetheabilitytogeneralize.

Clustering-basedFMR

Inaddition,somescholarshavealsoconductedFMRfromtheperspectiveofcluster-

ing[39–42].Thesemethodsdonotrequirepriorknowledgewiththeabilitytogeneralize.

However,theclusteringresultsrelyheavilyongoodtemporalsegmentation,andmost

ofthepapersappearingnowusemanualsegmentationwithoutautomaticsegmentation

capability,andtheclusteredresultsstillneedtobeinterpretedbyhumanexpertsand

cannotcorrespondautomatically.

2

Mathematics2022,10,1196

Insummary,itcanbefoundthattheexistingliteraturemethodsallperformFMRfora

certaintaskofacertainaircraftmodelandgenerallyhavethesignificantdisadvantagesof

relyingonmanualexpertknowledge,beingunabletoautomaticallysegment,andbeing

difficulttogeneralize.

Tothebestofourknowledge,thereisnogeneralframeworkthatcanautomaticallysegment

sequencesandquicklydiscriminatebetweenmaneuverswithminimalhumanintervention.

Thispaperproposesanewgeneralframework;thegeneralideaistointegratethe

automaticsegmentationcapabilityofunsupervisedclusteringandtheabilityofinformation

entropytodistinguishsequencecomplexity.

Thispaperisorganizedasfollows.Section2introducestheautomaticsegmentation

method of flight maneuver sequence. Section 3 introduces the automatic recognition

methodofmaneuversegments.Section4completelyelaboratestheoverallframeworkof

automaticFMRprocessing.Section5coverstheexperimentalprocessandexperimental

results,andtheconclusionisgiveninSection6.

2.SequenceSegmentation

2.1.TheTrendFragmentationAlgorithm

Inthispaper,akeyparameterisselectedfortrendidentification,andtheindexof

alltrendsegmentsisobtainedusingtheslopemethodcombinedwithaheightchange

threshold,usingaslidingmodelwithadoublewindow.

Theslopemethodisbasedontheleastsquaremethod,wherethesequencetobe

segmentedisfittedtoastraightline,andthemaintrendofthesequenceisdeterminedby

comparingtheslopeofthelinewithathresholdsize.

SetD=(y1,y2,···,ym )Tisasampleset,X=(x1,x2,···,xm )Tisthetimesequence

set,D isasubsetofthesamples,i=(1,2,···,L),andListhenumberoftrendsegments.

i

ThemodelparametersareobtainedbyfittingtheleastsquaresmethodasinEquation(1).

(cid:2) (cid:3)

ω =(k,b)T = DTD

−1

DT·X, i=(1,2,···,L) (1)

i i i i i i i

Theheight-changethresholdisusedtodeterminelong,slow-climbing,orcircling

maneuversinflight,whichhavesmallslopesandlongdurationsandcanbemisjudged

basedontheslopealone.ThealgorithmisdescribedinAlgorithm1.

ThecoreofAlgorithm1istousetheslidingdoublewindowmethodtofittheslopeto

theoriginaldataanddeterminetheflightattitudeasascending,leveling,ordescending

atthattimebasedontheslopeandusethechangeinattitudeasthesignalforautomatic

sequencesegmentation.Theksisslopethreshold,Δ sisheight-changethreshold,ωisfitting

matrix,Fisthefixedwindow,Sistheslidingwindow,O istheoutputsubsequence,f is

j

theflagbit,andtakesvaluesintherange{‘U’,‘L’,‘D’}.

2.2.TheClusteringAlgorithm

WithAlgorithm1,weobtainthetrendsegments,andthissectionwillusethedynamic

clusteringmethodISODATA(IterativeSelfOrganizingDataAnalysisTechniquesAlgo-

rithm)tocompletethesegmentclassification.ISODATAalgorithmautomaticallyselectsa

numberofsamplesasclustercentersandadjuststheclasscentersbysamplemeaniteration

insubsEquationuentcalculationsandrealizestheadjustmentofclustercenterdataby

mergingandsplittingofpatterns.However,theinputdataaretimeseries,sothealgorithm

cannotbeuseddirectly;therefore,thispaperimprovesthealgorithmtoTS-ISODATA,and

thealgorithmisdescribedasfo⎡llowsAlgorithm2.⎤

x11 ··· x1n

⎢ ⎥

ForinputrawdataX = ⎣ . . . ... . . . ⎦, nparameters, mdatapointsofthe

xm1 ··· xmn

fragment,normalizedas

x −x

x ij = x ij − j x ,min −0.5 (2)

j,max j,min

3

Mathematics2022,10,1196

calculateitsstatisticsas

(cid:10)

(cid:11) (cid:12)

x i = m 1 ∑m j=1 x ij , s i = m 1 ∑m j=1 x ij −x i 2(i=1,2,···,n) (3)

Algorithm1TheTrendFragmentationAlgorithm.

Input: samplesetD=(y1,y2,···,ym )T; timesequencesetX=(x1,x2,···,xm )T;

1. Setslopethresholdksandheight-changethresholdΔ s;

2. Initialvalueoffittingparameterω=(k,b)T;

(cid:11) (cid:12)

3. InitializethefixedwindowF= x (cid:11)Fstart ,x2,···,xFend T (cid:12) , Fstart =1, Fend =h;

5 4 . . I I n n i i t t i i a a l l i i z z e e t t h h e e o sl u id tp in u g ts w e i q n u d e o n w ce (cid:11) S O = j = x ( S x st F ar s t ta , rt x , 2 x , F · (cid:12)e · nd · , , f x ) S ; end T, Sstart =1, Send =h;

7 6 . . L R e e a a s d t a sq s u a a m re p s le fi s t s ti u n b g se m t o D d i e = lto y o S b st t a a rt i , n ·· p · a , r y a S m en e d te T r ; s t : im ω i e ; sequencesetXi =S;

8. Ifk≥ks,identifiesXiasanupwardtrend,setf=‘U’;

9. Otherwise,if−ks <k<ksidentifiesXiasaleveltrend,setf=‘L’;

10. Otherwise,identifiesXiasadownwardtrend,setf=‘D’;

11. IfXiisnotaleveltrend,andk’ssignsareunchanged,set

Fstart =Fstart, Fend =Fend +1, Sstart =Sstart +1, Send =Send +1;

12. O Fs t t h ar e t r = wi S s s e t , ar if t, k’ F s en s d ig = ns F a st r a e rt c + ha h n , g S ed st , ar s t e = tO S j st = art ( + xFs 1 ta , rt S ,x en F d end= ,f S ), end +1;

1 1 3 4 . . I L f e X as i t is sq a u l a e r v e e s l fi tr t e ti n n d g , m se o t d Fs e t l ar t t o = ob F t s a t i a n rt, pa F r en a d m = ete F r e s n : d ω + l 1 = , S (cid:11)s D ta l r T t D = l (cid:12) S − st 1 a D rt l + T· 1 X , l; Send =Send +1;

15. CalculatefixedwindowheightchangeΔ=|kl ·(Fend −Fstart )|;

16. I F f st | a k r l t | = > S k s s t , ar s t e , t F f en = d ‘L = ’, F s s e t t ar O t + j = h, ( S xF st st a a r rt t , = xFe S nd s , ta f r ) t , +1, Send =Send +1;

17. I

F

f

st

|

a

k

r

l

t

|

=

<

S

k

s

s

t

,

ar

a

t,

nd

Fe

Δ

nd

>

=

Δ

F

s

st

,

a

s

r

e

t

t

+

f

h

=

,

‘

S

U

s

’

ta

(

r

k

t

l

=

>

S

0

s

)

ta

o

rt

r

+

‘D

1

’

,

(k

S

l

en

<

d =

0),

S

s

e

e

n

t

d

O

+

j

1

=

;

(xFstart ,xFend ,f),

18. Otherwise,if|kl |<ks, andΔ<Δ s,set

Fstart =Fstart, Fend =Fend +1, Sstart =Sstart +1, Send =Send +1;

19. IfSend ≥m,enditerations;otherwise,gobackto7.

Output: O.

Algorithm2TS-ISODATAAlgorithm.

Input: X,trendsequenceO;

1. Normalizedprocessingxij;

2. Statisticscalculationxi,si;

3. Constructfeaturevectorsy=(x1,s1,x2,s2,···,xn,sn )T; (cid:13) (cid:14)

4. Randomlyselectk0samplesasinitialclusteringcentersC= c1,c2,···,ck0 ;

5. Calculatethedistancefromeachsamplexitotheclustercenterofthek0clustercentersand

assignittotheclasswiththemindistance;

6. DeterminewhetherthenumberofelementsineachclassaboveislessthanNmin.Ifso,

discardtheclass,makek=k−1,andreassignthesamplestotheclasswiththemin

distance;

7. Foreachcategoryci,recalculatetheclusteringcentersci = |c 1

i

| ∑ x∈xi x;

8. Ifthecurrentk≤ 1

2

k0,splitoperation;

9. Ifthecurrentk≥2k0,mergeoperation;

10. Terminateifthemaximumnumberofiterationsisreached;otherwise,gobackto2.

Output:Clusteringresults

4

Mathematics2022,10,1196

3.FlightManeuverRecognition

Algorithm2assignsthefragmenttoaspecificclasswithoutknowingwhichflight

maneuversitis.Inthissection,thealgorithmwillusephasereconstructiontoreconstruct

thefeaturespaceandidentifyspecificclassesofflightmaneuversbasedontheprinciple

thatdifferentmaneuvershavedifferentapproximateentropy.

3.1.PhaseSpaceReconstruction

DuetothesuperiorityofPSR(phasespacereconstruction)forchaotictime-series

computation[43], thispaperadoptsamultivariatedatafusionreconstructionmethod

basedonBayesianestimationtheory,andthemaincalculationstepsareasfollows.

3.1.1.ReconstructionParameters

Thephasespacereconstructiontechniquehastwokeyparameters:thedimensionof

theembeddingmandthedelaytimeτ,whicharedeterminedhereusingtheC-Cmethod.

1. Definethecorrelationintegralcorrespondingtoeachpointyoftheembeddedtime

seriesinthereconstructedphasespaceasinEquation(4).

(cid:11) (cid:12)

C(m,N,r,t)= M(M 2 −1)

1≤i

∑

≤j≤m

θ r−d ij (4)

(cid:15)

d ij =(cid:5)Y i −Y j (cid:5) ∞, θ(z)= 1 0 , , z z< > 0 0 (5)

where Y is the reconstructed phase space vector, M is the number of vectors

i

M=N−(m−1)τ, mistheembeddingdimension, N isthenumberofpointsof

theoriginaltimeseries,tistime,andθ(z)istheassociativeintegral,acumulative

distributionfunctionthatexpressestheprobabilitythatthedistancebetweenanytwo

pointsinthephasespaceislessthantheradiusr.Here,thedistancebetweenpointsis

expressedasaninfinitenumberofparametersofthedifferenceofvectors.

2. SplitthegiventimeseriesintotequationualanddisjointsubsequencesasEquation(6),

wheretisthereconstructiontimedelay.

x1={x1,xt+1,···,xN−t+1 },x2={x1,xt+2,···,xN−t+2 },···,xt={x1,x2t,···,xN } (6)

3. Calculatetheoriginalsequence’sS1andeachsequence’sS2:

S1 (m,N,r,t)=C(m,N,r,t)−Cm(1,N,r,t) (7)

S2 (m,r,t)= 1

t s

∑

=

t

1

[Cs (m,N,r,t)−C

s

m(1,r,t)] (8)

4. SelectthetworadiusesrwiththemaxandminvaluesanddefinetheincrementsΔS2:

(cid:13) (cid:11) (cid:12)(cid:14) (cid:13) (cid:11) (cid:12)(cid:14)

ΔS2 (m,t)=max S2 m,r

j

,t −min S2 m,r

j

,t (9)

5. Calculatethestatistics:

S2 (t)=

1

1

6 m

∑

=

5

2j

∑

=

4

1

S2 (cid:11) m,r

j

,t (cid:12) (10)

ΔS(t)= 1 ∑ 5 ΔS(m,t) (11)

4 m=2

S2cor (t)=ΔS2 (m,t)+|S2 (m,r,t)| (12)

6. TakethevaluecorrespondingtothefirstzeropointofS2 (t)orthefirstminimalvalue

ofΔS(t)astheoptimaltimedelayτ.

5

Mathematics2022,10,1196

7. LetthetcorrespondingtotheglobalminimumofS2cor (t)bethelengthofthetime

serieswindowandtheembeddingdimensionm.

3.1.2.FusionPhase

Aspreviouslystated,thesinglevariabledelaytimeisτ,andtheembeddingdimen-

sion is m. To ensure that the multivariate is fully expanded in the same phase space

withoutdistortion,eachvariable’sτ=min(τ),andm=max(m),(i=1,2,···,r).Each

i i

reconstructedsequenceexpressionX asinEquation(13).

i

⎡ ⎤

x i,1 x i,1+τ ... x i,1+(m−1)τ

⎢ ⎥

X i = ⎢ ⎢ ⎣ x i . . ,2 x i,2 . . +τ .. . . . x i,2+( . . m−1)τ ⎥ ⎥ ⎦ , i=1,2,···,r (13)

. . . .

x i,M x i,M+τ ... x i,M+(m−1)τ

Extracttherreconstructedsequencesofthesamepositionkoutofphasepointsin

Equation(13)toformthefusionsetD

k

=[x1,x2,···,xr ].Thespecificexpressionisgiven

inEquation(14). ⎧ (cid:20) (cid:21)

⎪⎪⎪⎨

x

x1

2

=

=

(cid:20) x

x

1

2

,

,

k

k

x

x

1

2

,

,

k

k

+

+

τ

τ

.

.

.

.

.

.

x

x

1

2

,

,

k

k

+

+

(

(

m

m

−

−

1

1

)

)

τ

τ

(cid:21)

⎪⎪⎪⎩

(cid:20)

. .

. (cid:21)

(14)

xr = x r,k x r,k+τ ... x r,k+(m−1)τ

Lettheexpressionofthephasepointatpositionkafterfusionbez ,andtheoptimal

k

fusionphasepointatkisobtainedaccordingtoEquation(15).

p(z k |x1,x2,···,xr )= p( p x ( 1 x , 1 x , 2 x , 2 · , · · · ·· ,x , r x | r z ) k ) ·p(z k ) (15)

Let p(z

k

|x1,x2,···,xr ) obey a normal distribution with mean z and variance δ2.

Accordingto(16)and(17),thecalculationgives(18).

⎧

⎪⎪⎨

1 = ∑

r

1 + 1

⎪⎪⎩ σ

z

2

=

i

∑

= r 1 σ

x

i

i

2

+

σ

z

0

0

2 (16)

σ2 i=1 σ i 2 σ 0 2

(cid:22) (cid:23) (cid:22) (cid:23) (cid:24) (cid:23) (cid:25)

γexp[−1 ∑ r x i −z k 2 −1 z k −z0 2 ]= √1 exp[−1 z k −z 2 (17)

2 i=1 σ i 2 σ 0 2πσ 2 σ

z= ∑r i=1σ x i i 2 + σ z 0 0 2 (18)

∑r 1 + 1

i=1σ2 σ2

i 0

ThefinalBayesianestimateoftheoptimalfusionphasepointatpositionkisobtained

asinEquation(19),wheretheupperandlowerlimitsofωarethemaximumandminimum

values of the phase point, and the PSR can be completed after finding all M position

phasepoints.

(cid:26) (cid:22) (cid:27)

zˆ = z √1 exp[−1 z k −z)2 dz , ∀k=1,2,···,M (19)

k ω k 2πσ 2 σ k

3.2.RecursionGraphsandApproximateEntropy

Recursiongraphs(RP)isaneffectivemethodforqualitativeanalysisofnonlinear

dynamicalsystems,whichcanrevealtheinternalstateevolutionprocessofthesystemby

usingtheimage-changepattern.ItisgenerallyimplementedusingtheHeavisidefunction.

6

Mathematics2022,10,1196

TheblackdotsintheRPdiagramindicatethattheattractortrajectoriesreachthesame

regionoftheorbitatdifferentmomentsandviceversaforthewhitedots.

Approximateentropycanquantitativelyanalyzethestructuralcomplexityofnonlin-

earsystems[44]asdefinedinEquation(20). Differentflightmaneuversgenerallyhave

differentcomplexityandhavedifferentapproximateentropy.Bycalculatingtheapprox-

imateentropyandcombiningwiththemaneuversentropylibrary,wecanknowwhich

maneuveritis.

ApEn(m,r)= N l → im ∞ (cid:28) Φm(r)−Φm+1(r) (cid:29) ,Φm(r)= N− 1 m+1 N− i ∑ = m 1 +1 lnC i m(r) (20)

(cid:13) (cid:20) (cid:21) (cid:14)

C i m(r)= N− 1 m d X i ,X j <r (21)

(cid:20) (cid:21) (cid:30) (cid:30) (cid:30) (cid:30)

d X i ,X j = k=0, m 1,· a ·· x ,m−1 (cid:30)x i+k −x j+k (cid:30) (22)

wherei=(1,2,···,N−m+1), j=(1,2,···,N−m+1), andi(cid:9)=j.

4.TheFMRGeneralFramework

Thegeneralideaofthegenericframeworkproposedinthispaperistointegratethe

automaticsegmentationcapabilityofunsupervisedclusteringandtheinformationentropy

capabilityofdistinguishingsequencecomplexity.

First,theoriginalinputdataareprocessedusingadynamicclusteringmethodsuch

asISODATA,andthealgorithmoutputsthesegmented,unknownkindsofmaneuver

sequences.Second,themultivariatephasespacereconstructioncalculationisappliedto

establishthecompletephasespaceofthedynamicalsystem.Then,therecurrencemapand

approximateentropyarecalculatedinthenewphasespacetoanalyzethecomplexityof

thesequencesqualitativelyandquantitatively.Finally,accordingtotheprinciplethatthe

complexityofdifferentkindsofmaneuversequencesisdifferent,thespecifickindofthe

sequenceisdeterminedbasedonthecalculationresultssoastocompletetheFMR.The

specificflowchartisshowninFigure1.

Intheflowchart,therawflightdataarefirstpreprocessedtoextractsomeofthe

parametercolumns. Thespeed,altitude,rollangle,andpitchangleformaparameter

matrix,whichisinvolvedintheunsupervisedclusteringcalculation. Usingthedouble-

windowalgorithm,thetrendidentificationiscompletedbyusingthenormalloadasthe

slopeprimitive,andthetrendisusedtosegmentthewholerawsequenceintosubseries

andoutputtheindexvalues.Basedontheindexvaluesofsubsequencesintheprevious

step,parameterfragmentsareextractedforeachofthefourparametersequences. The

extractedfourparameterfragmentsarefedintotheC-Calgorithm,andthephasespace

reconstructionisperformedaccordingtothecalculatedminimumdelaytimeandmaximum

embeddingdimension,respectively,andthephasepointsatthesamepositioninthesefour

spacesarefusedtoextracttheactionfragments. Afteracomprehensiveanalysisofthe

qualitativevaluesoftherecurrencemapandthequantitativevaluesoftheapproximate

entropy,theactionrecognitionresultsarefinallyobtained.

7

Mathematics2022,10,1196

Flight Raw Data

Normal Overload Speed Height Roll Yaw

Slope Primitives Eigenvector

Dual sliding window trend

Unsupervised Clustering

recognition

Index of trend segments

Extracting Speed Extracting Height Extracting Roll Extracting Yaw

segments segments segments segments

C-C Algorithm

Delay Time Embedded Dimension

(cid:68)(cid:349)(cid:374) (cid:68)(cid:258)(cid:454)

PSR1 PSR2 PSR3 PSR4

Phase Points of Four Phase Space

Fusion of the same position in the same phase space

Extracting maneuver segments

Qualitatively analyze by RP Qualitatively analyze by ApEn

The complexity of RP The value of ApEn

Comprehensive analysis

The result of FMR

Figure1.AgeneralframeworkforFMR.

5.Experiments

TheexperimentalenvironmentisWindows10operatingsystem,Anacondadevelop-

mentenvironment,pythonlanguage,andMatlab7.1simulationplatform.Thevisualization

toolisthethree-dimensionalflightpathrecoverysystem(3D-FPRS)developedbytheau-

thor’steam.Thesystemisbasedontheopen-sourceCesiumJSplatformandimplemented

usingWebGL,HTML5technology,whichcanreducetheinputflightrawdatainto3D

dynamicvisualizationofflighttrajectory.

TheexperimentalrawdatawereobtainedfromCAFUCrealflighttrainingrecords:the

aircrafttypeisC172R,filename1log_210721ZUCK,5724lines;filename2log_210316ZUUU,

6445lines.Duetotheproblemofdataaccuracy,1104rowsofdatainlog_210721ZUCKand

8

Mathematics2022,10,1196

4626rowsofdatainlog_210316ZUUUwereusedduringtheexperiment,withsixcolumns

ofdataineachrow,totaling34,380piecesofdata. Thetotallengthoftheexperimental

sequencewas5730.ThewholerawflightdataarevisualizedasFigure2.

Figure2.Thevisualizationofwholerawflightdata(file1andfile2).

Thespeed,sideslipangle,altitude,pitchangle,rollangle,andnormaloverloadare

consideredaskeydataduringtheexperiment,withothermulti-columnflightparameter

dataparticipatinginthefeaturedataprocessing.

TS-ISODATAmodelhassixclusteringparameters,andK=7,L=1,andI=100were

selectedintheexperiment,andthegeneticalgorithmwasusedtofindθ n,θ S,θ C.Thefinal

optimalparametersettingvaluesobtainedareθ

n

=1, θ

S

=0.0373, andθ

C

=0.0043,and

theevaluationresultusingthissetofparametervaluesis6.3823.Theinputrawsequence

issegmentedinto96maneuversegments.Thesegmentationcalculationprocesstakesan

averageof76s.

Theindexoftheextractedmotorizedfragmentforaparticularexperimentwas(0,54,

108,162,216,270,378,432,486,540,594,648,702,756,810,864,918,972,1026,1080,1134,

1188,1242,1296,1350,1404,1458,1512,1566,1674,1728,1782,1836,1890,1944,1998,2052,

2160,2214,2268,2322,2376,2430,2484,2538,2592,2646,2700,2754,2808,2862,2916,3024,

3078,3132,3186,3240,3294,3348,3402,3456,3510,3564,3618,3672,3726,3780,3834,3888,

3942,3996,4050,4104,4158,4212,4266,4320,4374,4428,4482,4536,4590,4644,4698,4752,

4806,4860,4914,4968,5022,5076,5130,5184,5238,5292,5346,5368),whereeachindex

numberrepresentsthespecificmomentwhenthefilewasimported,

The feature vector extracted according to this was (1:{−0.131, 0.108, 0.203, 0.090,

−0.039,0.057,0.176,0.099,0.203,0.101,0.472,0.017},2:{0.018,0.096,−0.042,0.091,0.034,

0.029,0.074,0.050,−0.094,0.109,0.164,0.055},...,96:{0.018,0.096,−0.042,0.091,0.034,

0.029,0.074,0.050,−0.094,0.109,0.164,0.055}).TheresultofclusteringisshowninTable1.

Theclusteringcalculationprocesstakesanaverageof121s.

Table1.TS-ISODATAclusteringresults.

Categories CorrespondingManeuverSegments

1 8,9,16,18,23,24,31,34,35,42,45,48,52,55,60,63,67,74,77,82,19,28,37,40,49,58,69,79

2 1,87,92,94

3 3,5,12,14,15,20,27,33,36,39,41,51,54,57,62,81,84,88,95,96,11,25,38,43,65,68,71,72,

4 4,6,22,53,50,66,73,89,91,2,7,10,13,17,21,26,29,30,44,47,32,46,56,59,61,64,70,75,83,85,76,78,80,86,90,93

9

Mathematics2022,10,1196

Afterpreliminaryexpertanalysis,category4arealltransitional-levelflightsbetween

complexmaneuvers,whicharenotsignificant,sothispaperusesPSRmethodtostudythe

recurrencegraphandapproximateentropyofcategory1,2,and3.TheApEnresultsare

giveninTable2.

Table2.TheApEnvalueforcategories1–3.

Categories 1 2 3 4 5 6 7 8 9 10 Average

1 0.3937 0.3148 0.4985 0.3512 0.2881 0.4112 0.3309 0.2490 0.3989 0.4117 0.3648

2 0.3166 0.3594 0.4252 0.0870 0.2491 0.0408 0.0870 0.0741 0.1295 0.1922 0.1961

3 0.1346 0.0941 0.2007 0.1178 0.0953 0.1457 0.1178 0.0953 0.1419 0.0344 0.1177

Experimental results show that the dataset as a multivariate time series does fit

thechaoticnonlineardynamicalsystemcharacteristics.Similarmaneuversshowsimilar

characteristicsontherecurrencegraph,withclosevaluesofapproximateentropy(ApEn),

whiledifferentmaneuversvarywidely.Thus,thephasespacereconstructionrecognition

methodbasedonapproximateentropycandistinguishtherecognitionofflightmaneuvers,

especiallycomplexmaneuvers.

Threesamplesofthetracerecoveryvisualizationandrecurrencemapexperimentare

giveninFigures3–5.

(a) (b)

Figure3.(a)Category1maneuvervisualizationreduction;(b)themaneuver’sRPandApEnvalue.

(a) (b)

Figure4.(a)Category2maneuvervisualizationreduction;(b)themaneuver’sRPandApEnvalue.

10

Mathematics2022,10,1196

(a) (b)

Figure5.(a)Category3maneuvervisualizationreduction;(b)themaneuver’sRPandApEnvalue.

Inordertostudywhatexactlythesethreecategoriesofmaneuversare,thispaper

usestherecurrencediagramsofthesethreecategoriesofmaneuversinconjunctionwith

thevisualflightpathrecoverysystemtobeabletoclearlydistinguishthecategoriesof

maneuvers.AsshowninFigures3a,4aand5a,category1isEightmaneuver,category2is

RectangularCoursemaneuver,andcategory3isSpinmaneuver.Notonlydothesethree

categoriesofmaneuvershavedifferentApEnvalue,buttheirRPsalsohavesignificant

differences,whichperfectlymatchthecomplexitylevelgivenbyflightexpertsasshownin

Figures3b,4band5b.TheRPandApEncalculationprocesstakesanaverageof88s.

TheoverallaveragetimeofthewholeframeworkautomaticFMRcalculationprocess

is285swith5730rawinputdata.

In order to verify that the framework can be applied to multiple aircraft types,

weselectedtwootherdatasetstocompletethevalidationexperiments,whicharealso

from CAFUC real flight training records: aircraft types SR20 and DA42, file 3 name

log_210521_ZHCC(13,750lines),andfile4namelog_210531_ZUUU(13,018lines);theraw

flightdataarevisualizedasFigure6.

(a) (b)

Figure6.(a)File1visualization;(b)file2visualization.

Inaddition,inordertodocomparisonexperiments,theprojectteamdevelopedan

expertvalidationaidtool(EVAT)asshowninFigure7.

ThesystemisalsobasedontheCesiumJSplatform,whichcannotonlybereducedto

3Ddynamicvisualizationofflighttrajectorybutalsocandisplayeachsecondoftemporal

parametersandmarktheminsequence,helpingflightexpertstojudgeflightmovements

withthenakedeye.

Withthistool,threeflightexpertsmadeflightmaneuversjudgmentsontheabovetwo

experimentalfilesandtwovalidationfiles,framebyframe,respectively,andthecomplete

comparisonresultsareshowninTable3below.

11

Mathematics2022,10,1196

Figure7.Expertvalidationaidtool(EVAT).

Table3.Theoverallexperimentalresults.

File1+File2 File3 File4

Categories Average

C172,5730Lines SR20,13,750Lines DA32,13,018Lines

Number FMR Expert Accuracy(%) FMR Expert Accuracy(%) FMR Expert Accuracy(%) Accuracy

1 28 26 92.3 6 5 80 49 50 98.2 90.2

2 4 4 100 20 24 83.3 7 5 60 81.1

3 28 26 92.3 10 8 75 15 17 88.2 85.2

Ratio Ratio Ratio Ratio

Time(seconds)

285 15,675 55 382 17,569 45.9 349 21,638 62 54.3

TheexperimentalresultsinTable3showthatthemethodinthispapercanperform

FMRforthreetypesofaircraftanddifferentfilelengths,withthehighestaccuracyrate

forcategory1(Eightmaneuver),andthelowestaccuracyrateforcategory2(Rectangular-

Coursemaneuver),withanoverallaverageaccuracyrateof85.5%. Thereasonwhythe

Eightmaneuveraccuracyisthehighestisbecausethemaneuverissignificantlydifferent

fromothers, andtheRectangularCoursemaneuveraccuracyisthelowestbecausethe

maneuverisgenerallytime-consuming,whichisaccompaniedbyahalf-spinmaneuver,

andthenumberofsuchmaneuversissmall,sotherecognitionisnoteffective.

In terms of time consumption, the consumption time is related to the document

length,andoverall,therecognitionspeedofthispaperis54.3timesfasterthanhuman

flightexperts.

Thecomparisonexperimentsweredifficulttodesignandimplementbecausenone

oftheotherpapersdisclosedthedatasetsused,andsomeofthepaperscorrespondedto

aircrafttypesthatwerefighterjetsorUAVs,whichdifferedgreatlyfromthetemporal

natureofthispaper;neitherdidanyoftheothermethodscovertemporalsegmentation

andautomaticrecognition.However,westillcompletedtherecognitionexperimentsusing

thesamedatasetsprovidedinthispaper,files1and2,andtheexperimentalresultsare

showninthefollowingTable4.

Table4.Thecomparisonexperimentsresults.

Methods DTW[4] RF-SVM[10] ExpertSystem[15] DBM[29] CNN-LSTM[33] Ours

Accuracy(%) 79.6 61 89.6 77 71 85.5

Time(Seconds) 314 276 656 295 489 285

Fromtheresults,wecanseethatunderthesameflight-typecondition,theaccuracyof

thispaper’smethodissecondonlytotheexpertsystem,andthespeedissecondonlyto

SVM,whichisbetterthanothermethodsinthecomprehensiveevaluation.Moreimpor-

tantly,ifwewanttofollowtheaircraftmodel,exceptforthispaper,allothermethodshave

12

Mathematics2022,10,1196

toretrainthemodelorredesigntheknowledgerules,whichdoesnothavegeneralization

abilityinpracticalapplicationscenarios.

6.Conclusions

Inthispaper,ageneralframeworkwasconstructedforthefirsttimeforautomated

FMRbasedondynamicclusteringandphasespacereconstruction.Theframeworkdecom-

posestheFMRtaskintotwoparts,whichareautomaticmaneuversequencesegmentation

andautomaticmaneuverclassidentification.Theautomaticmaneuversequencesegmenta-

tionwasimplementedbytheimproveddynamicclusteringmethodTS-ISODATA,which

solvestheproblemofself-organizediterativeclusteringofmultivariatetimeseriesandsuc-

cessfullysegmentstheinputdataintomultiplesegmentsandautomaticallyclustersthem

intofourclasses.Duetothechaoticnatureoftheflightdynamicssystem,theautomatic

recognitionofmaneuvercategoriespartiallyreconstructsthephasespaceofmultivariate

fusion,transformstherepresentationaldimensionalchangepatternsofflightmaneuvers

thataredifficulttoorganizeintoattractivesubsequencesthatareeasytoidentify,and

generatesrecursivegraphsfromthemtocalculateApEnvaluesthatcancharacterizethe

complexityofmaneuvers.Withthehelpofavisual3Dflight-trackreductionsystem,the

flightmaneuvercategoriesareeasilyidentified.Withaninputsequenceof5000s,theentire

frameworkcomputationprocesstakesanaverageof285s,whichis54timesfasterthan

humanexpertrecognition,withanoverallaccuracyrateof85.5%.

Inthenextstep,theentropycorrespondingtodifferentflightactionscanbesolidified

soastoformanautomaticidentificationlibraryforfastandautomaticclassificationoutput.

Thissteprequirescollectingalargenumberofsamplesofaparticularflightmaneuver

andderivingareasonablerangeofapproximateentropyvaluesthroughalargenumber

ofexperiments, andtherangeofvaluesamongthemaneuversshouldnotoverlapto

avoidduality. Accordingtodifferententropyvaluerangescorrespondingtodifferent

aircraftmaneuverscategories,automaticidentificationruleswereestablishedtorealize

thefinalautomaticoutputofflightmaneuvers. Formaneuverswithcloseapproximate

entropyvaluesandlittledifference, thecomplexityoftherecurrencegraphshouldbe

considered,andthedifferenceenhancementofinformationentropyshouldbedesignedto

furtherstrengthenthedifferencebetweenmaneuvers.Inaddition,asapattern-recognition

category,althoughthemethodinthispaperhasbettergeneralizationabilityanddoesnot

requirepre-training,itiscomputationallyintensiveandtime-consumingandcannotrealize

onlinereal-timerecognition. Atthisstage,itcanonlybeusedforpost-flightanalysisto

supportthenextapplication,suchasflighttechnologyscoringbasedonaspecificflight

maneuverandpost-accidentinvestigationafteraflightaccident.Inthefuture,theprinciple

ofthemethodcanbeexploredindepthtosimplifythecomputationprocess.

AuthorContributions:Conceptualization,J.L.;methodology,J.L.;software,J.L.andH.C.;formal

analysis,J.L.;investigation,J.L.andH.C.;resources,J.L.,H.C.andR.J.;datacuration,J.L.;writing—

originaldraftpreparation,J.L.;writing—reviewandediting,J.L.andR.J.;visualization,J.L.andH.C.;

supervision,J.L.;projectadministration,J.L.;fundingacquisition,J.L.Allauthorshavereadand

agreedtothepublishedversionofthemanuscript.

Funding:ThisresearchwasfundedbytheCivilAviationFlightTechnologyandFlightSafetyKey

LaboratoryofChinaresearchprojects,NO:FZ2020ZZ02;TheCAFUCResearchProject,NO:CJ2021-

01;NationalNaturalScienceFoundationofChina,NO:U2033213;SichuanScienceandTechnology

Program,NO:2022YFG0027.

InstitutionalReviewBoardStatement:Notapplicable.

InformedConsentStatement:Notapplicable.

DataAvailabilityStatement:Notapplicable.

Acknowledgments:TheauthorswouldliketothankXiaodongLiuandgraduatestudentsZheCao

andLuPangfortheircontributions.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

13

Mathematics2022,10,1196

References

1. The United States Department of Transportation; Federal Aviation Administration; Airman Testing Standards Branch.

Pilot’sHandbookofAeronauticalKnowledge;TheUnitedStatesDepartmentofTransportation:OklahomaCity,AK,USA,2016.

2. Burgin,G.H.;Owens,A.J.AnAdaptiveManeuveringLogicComputerProgramfortheSimulationofOne-to-OneAir-to-AirCombat.

NASAContractorReport(CR),Volume2:ProgramDescription;NASA:SanDiego,CA,USA,1975.

3. Burgin,G.H.ImprovementstotheAdaptiveManeuveringLogicProgram.1986.Availableonline:https://ntrs.nasa.gov/404?

original=%2Fcitations%2F19880002266(accessedon2March2022).

4. Barndt,G.;Sarkar,S.;Miller,C.ManeuverregimerecognitiondevelopmentandverificationforH-60structuralmonitoring.In

ProceedingsoftheAnnualForumProceedings-AmericanHelicopterSociety,VirginiaBeach,VA,USA,1–3May2007;American

HelicopterSociety,Inc.:Fairfax,VA,USA,2007;Volume63,p.317.

5. Zhang,J.Y.TimeSeriesAnalysisMethodofFlightDataandItsApplication;NationalDefenseIndustryPress:Beijing,China,2013.

6. Li,Z.-X.;Zhang,F.-M.;Li,K.-W.AmultivariatetimeseriesindexingstructuresupportingDTWdistance. J.Softw. 2014,25,

560–575.

7. Li,H.;Shan,Z.;Guo,H.MDTW-basedflightactionrecognitionalgorithm.Comput.Eng.Appl.2015,51,267–270.

8. Shen,Y.;Ni,S.;Zhang,P.Asimilarsubsequencequerymethodforflightdata.J.AirForceEng.Univ.2019,20,7–12.

9. Tang,C.;Dong,J.LSH-basedtimesubsequencequeryalgorithm.J.Comput.Sci.2012,35,2228–2236.

10. Qu,J.;Lv,M.;Yang,Y.FlightMotionRecognitionMethodBasedonMultivariatePhaseSpaceReconstructionandApproximate

Entropy.InProceedingsofthe202140thChineseControlConference(CCC),Shanghai,China,26–28July2021;IEEE:Piscataway,

NJ,USA,2021;pp.7247–7253.

11. Mao, H.; Zhang, F.; Feng, H. Research on flight maneuver evaluation method based on singular value decomposition.

Comput.Eng.Appl.2008,44,240–242.

12. Mao,H.;Zhang,F.;Feng,H.Similarpatternqueryformultivariateflightdata.Comput.Eng.Appl.2011,47,151–155.

13. Yang,J.;Duan,C.;Xie,S.Fuzzyleastsquaressupportvectormachinebasedaircraftflightmaneuverrecognition.J.Ballist.Arrow

Guid.2004,S6,395–398.

14. Jia,Z.;Fan,X.;Xue,M.Onlineidentificationmethodfortacticalmaneuversofenemyaircraftbasedonmaneuverelements.

J.BeijingUniv.Technol.2018,38,820–827.

15. Kendrick,J.D.;Maybeck,P.S.;Reid,J.G.Estimationofaircrafttargetmotionusingorientationmeasurements.IEEETrans.Aerosp.

Electron.Syst.1981,2,254–260.[CrossRef]

16. Kou,Y.;Jiang,L.;Wang,D.High-orderreconstructionofthedecisionprocessofcloseaircom-batmaneuver.J.Syst.Simul.2019,

31,2085.

17. Molkenthin,J.DeterminationandVerificationofOperationalManeuverParametersandTimeHistories.LoadsRequir.Mil.Aircr.

1997,6,3–11.

18. Wang,Y.;Dong,J.;Liu,X.Identificationandstandardizationofmaneuversbaseduponoperationalflightdata.Chin.J.Aeronaut.

2015,28,133–140.[CrossRef]

19. Xie,C.;Ni,S.;Zhang,Z.Aknowledge-basedmethodforfastrecognitionofaerobaticmaneuvers.Comput.Eng.2004,30,116–118.

20. Ni,S.;Shi,Z.;Xie,C.Establishmentofaknowledgebaseformaneuveringflightmaneuversrecognitionofmilitarywarplanes.

Comput.Simul.2005,22,23–26.[CrossRef]

21. Travert,J.H.FlightRegimeandManeuverRecognitionforComplexManeuvers.Master’sThesis,Embry-RiddleAeronautical

University,DaytonaBeach,FL,USA,2009.

22. Chunmei,G.;Lili,Z.;Yu,B.RecognitionofFlightOperationActionBasedonExpertSystemInferenceEngine.InProceedingsof

the201911thInternationalConferenceonIntelligentHuman-MachineSystemsandCybernetics(IHMSC),Hangzhou,China,

24–25August2019;IEEE:Piscataway,NJ,USA,2019;Volume1,pp.17–20.

23. Tian,H.;Xie,S.;Wang,L.Flighttrajectoryidentificationbasedonroughsettheory.FirepowerCommandControl2015,40,29–33.

24. Zhou,D.Y.;Li,F.Geneticalgorithm-basedtacticalflightmaneuverdecisionforaircraft.J.Northwest.Polytech.Univ.2002,20,

109–112.

25. Wei,Z.;Ding,D.;Zhou,H.Aflightmaneuverrecognitionmethodbasedonmulti-strategyaffinecanonicaltimewarping.Appl.

SoftComput.2020,95,106527.[CrossRef]

26. Wang,L.;Huang,C.Q.;Wei,Z.L.AutomaticextractionofflightactionrulesbasedonSSAalgorithm.Comput.Eng.Appl.2019,14,

203–208.

27. Wang,Y.W.;Gao,Y.Aflightactionrecognitionruleextractionmethodbasedonwhaleoptimizationalgorithm.J.Nav.Aviat.Eng.

Coll.2019,33,447–451.

28. He,D.;Wu,S.;Bechhoefer,E.DevelopmentofRegimeRecognitionToolsforUsageMonitoring.InProceedingsofthe2007IEEE

AerospaceConference,BigSky,MT,USA,3–10March2007;IEEE:Piscataway,NJ,USA,2007;pp.1–11.

29. He,D.;Wu,S.;Bechhoefer,E.ARegimeRecognitionAlgorithmforHelicopterUsageMonitoring.Aerosp.Technol.Adv.2010,

391–404.Availableonline:https://books.google.co.jp/books?hl=en&lr=&id=bQWQDwAAQBAJ&oi=fnd&pg=PA391&dq=A+

regime+recognition+algorithm+for+helicopter+usage+monitoring.+&ots=4Kgn_R61wO&sig=I6atHzxhI1AC8YqD9Tw1cNbI_

ZQ&redir_esc=y#v=onepage&q=A%20regime%20recognition%20algorithm%20for%20helicopter%20usage%20monitoring.

&f=false(accessedon2March2022).

14

Mathematics2022,10,1196

30. Rajnicek,R.E.ApplicationofKalmanFilteringtoReal-TimeFlightRegimeRecognitionAlgorithmsinaHelicopterHealthand

UsageMonitoringSystem.Master’sThesis,Embry-RiddleAeronauticalUniversity,DaytonaBeach,FL,USA,2008.

31. Meng,G.-L.;Zhang,H.-M.;Park,H.-Y.Maneuverrecognitionofwarplanesinautomatedflighttrainingevaluation.J.Beijing

Univ.Aeronaut.Astronaut.2020,46,1267–1274.

32. Li,Y.F.;Ni,S.H.;Zhang,Z.L.AfuzzyKohonennetwork-basedintelligentprocessingmethodforflightdata.Syst.Eng.Electron.

Technol.2002,24,53–55.

33. Xu,W.Afuzzyneuralnetwork-basedapproachforshipboardaircraftlandingmaneuversrecognition.Appl.Sci.Technol.2013,2,

26–29.

34. Hanyang,F.;Hongming,F.;Ruiyuan,G.ResearchonairtargetmaneuverrecognitionbasedonLSTMnetwork.InProceedings

ofthe2020InternationalWorkshoponElectronicCommunicationandArtificialIntelligence(IWECAI),Shanghai, China,

12–14June2020;IEEE:Piscataway,NJ,USA,2020;pp.6–10.

35. Fang,W.;Wang,Y.;Yan,W.J.;Gong,Y.Flightactionrecognitionbasedondifferentialideasandconvolutionalneuralnet-works.

J.Chin.Acad.Electron.Sci.2021,16,347–353.

36. Fang,W.;Wang,Y.;Yan,W.;Lin,C.Symbolicflightactionrecognitionbasedonneuralnetworks.Syst.Eng.Electron.2021,1,13.

37. Zhang,Y.Y.;Wang,Y.Y.;Wang,C.H.X.Analysisofparametriccorrelationandtemporalfeaturesforflightactionrecognition

method.Comput.Eng.Appl.2016,52,246–249.

38. Shen,Y.;Ni,S.;Zhang,P.ABayesiannetwork-basedapproachforflightactionrecognition.Comput.Eng.Appl.2017,53,161–167.

39. Zhang,X.;Yin,Z.;Liu,F.;Huang,Q.Dataminingmethodforaircraftmaneuveringdivision. J.Northwest. Polytech. Univ.

2016,34,33–40.

40. Zhang,L.Anon-supervisedautomaticmethodofaircraftmaneuverpartition.J.Comput.MethodsSci.Eng.2021,21,383–395.

[CrossRef]

41. Kang,Z.;Shang,J.;Feng,Y.Adeepsequence-to-sequencemethodforaccuratelonglandingpredictionbasedonflightdata.IET

Intell.Transp.Syst.2021,15,1028–1042.[CrossRef]

42. Li,X.;Shang,J.;Zheng,L.CurveCluster+:CurveClusteringforHardLandingPatternRecognitionandRiskEvalua-tionBased

onFlightData.IEEETrans.Intell.Transp.Syst.2021.[CrossRef]

43. Tou,J.T.;Gonzalez,R.C.PatternRecognitionPrinciples;Addison-WesleyPublishingCompany:Reading,MA,USA,1974.

44. Pincus,S.M.Approximateentropyasameasureofsystemcomplexity.Proc.Natl.Acad.Sci.USA1991,88,2297–2301.[CrossRef]

[PubMed]

15

mathematics

Review

Survey on the Application of Artificial Intelligence in ENSO

Forecasting

WeiFang1,2,3,*,YuSha1andVictorS.Sheng4

1 SchoolofComputerandSoftware,EngineeringResearchCenterofDigitalForensics,MinistryofEducation,

NanjingUniversityofInformationScienceandTechnology,Nanjing210044,China

2 StateKeyLaboratoryofSevereWeather,ChineseAcademyofMeteorologicalSciences,Beijing100081,China

3 JiangsuCollaborativeInnovationCenterofAtmosphericEnvironmentandEquipment

Technology(CICAEET),NanjingUniversityofInformationScienceandTechnology,Nanjing210044,China

4 DepartmentofComputer,TexasTechUniversity,Lubbock,TX79409,USA

* Correspondence:hsfangwei@sina.comorfangwei@nuist.edu.cn

Abstract:Climatedisasterssuchasfloodsanddroughtsoftenbringheavylossestohumanlife,na-

tionaleconomy,andpublicsafety.ElNiño/SouthernOscillation(ENSO)isoneofthemostimportant

inter-annualclimatesignalsinthetropicsandhasaglobalimpactonatmosphericcirculationand

precipitation.Toaddresstheimpactofclimatechange,accurateENSOforecastscanhelpprevent

relatedclimatedisasters. Traditionalpredictionmethodsmainlyincludestatisticalmethodsand

dynamicmethods.However,duetothevariabilityanddiversityofthetemporalandspatialevolution

ofENSO,traditionalmethodsstillhavegreatuncertaintyinpredictingENSO.Inrecentyears,with

therapiddevelopmentofartificialintelligencetechnology,ithasgraduallypenetratedintoallaspects

ofpeople’slives,andtheclimatefieldhasalsobenefited.Forexample,deeplearningmethodsin

artificialintelligencecanautomaticallylearnandtrainfromalargeamountofsampledata,obtain

excellentfeaturerepresentation,andeffectivelyimprovetheperformanceofvariouslearningtasks.

Itiswidelyusedincomputervision,naturallanguageprocessing,andotherfields.In2019,Ham

Citation:Fang,W.;Sha,Y.;Sheng,

etal.usedaconvolutionalneuralnetwork(CNN)modelinENSOforecasting18monthsinadvance,

V.S.SurveyontheApplicationof

ArtificialIntelligenceinENSO andthewinterENSOforecastingskillcouldreach0.64,farexceedingthedynamicmodelwitha

Forecasting.Mathematics2022,10, forecastingskillof0.5.Theresearchresultswereregardedasthepioneeringworkofdeeplearningin

3793. https://doi.org/10.3390/ thefieldofweatherforecasting.ThispaperintroducesthetraditionalENSOforecastingmethodsand

math10203793 focusesonsummarizingthevariouslatestartificialintelligencemethodsandtheirforecastingeffects

forENSOforecasting,soastoprovideusefulreferenceforfutureresearchbyresearchers.

AcademicEditors:Jonathan

Blackledge,ChristopheGuyeuxand

Keywords:climatedisasters;ENSOforecasting;artificialintelligence;machinelearning;deeplearning

JakubNalepa

Received:15August2022 MSC:68-xx;68-11

Accepted:11October2022

Published:14October2022

Publisher’sNote:MDPIstaysneutral

withregardtojurisdictionalclaimsin 1.Introduction

publishedmapsandinstitutionalaffil- Climatechangeisadifficultproblemfacingtheworldtoday,anditaffectspeople’s

iations. productionandlifetoalargeextent. ThemostprominentElNiño-SouthernOscillation

(ENSO)phenomenonisthemostimportantinterannualsignalofshort-termclimatechange

on the earth [1]. It will have a great impact on the climate, environment, and socio-

economicsonaglobalscale.

Copyright: © 2022 by the authors.

ENSOiswindandseasurfacetemperatureoscillationsthatoccurintheequatorial

Licensee MDPI, Basel, Switzerland.

easternPacific.In1969,Bjerknes[2]proposedthatElNiñoandtheSouthernOscillationare

Thisarticleisanopenaccessarticle

twodifferentmanifestationsofthesamephysicalphenomenoninnature,whichisreflected

distributed under the terms and

intheoceanastheElNiñophenomenonandintheatmosphereastheSouthernOscillation

conditionsoftheCreativeCommons

phenomenon.ElNiñoreferstothephenomenonofabnormalwarmingoftheoceanevery

Attribution(CCBY)license(https://

twotosevenyears(everyfouryearsonaverage)intheequatorialeasternPacificOcean,

creativecommons.org/licenses/by/

4.0/). andtheoppositecoldphenomenoniscalledLaNiña[3].TheSouthernOscillationrefers

Mathematics2022,10,3793.https://doi.org/10.3390/math10203793 https://www.mdpi.com/journal/mathematics

17

Mathematics2022,10,3793

tothemutualmovementoftheatmospherebetweentheeasterntropicalPacificandthe

westerntropicalPacific,andthecycleisalsoapproximatelyfouryears. ElNiñoandLa

NiñaarecloselyrelatedtotheSouthernOscillation.WhentheSouthernOscillationindex

hasapersistentnegativevalue,anElNiñophenomenonwilloccurinthatyear,andonthe

contrary,aLaNiñaphenomenonwilloccurinthatyear.

SinceENSOisaglobalocean–atmosphereinteraction,ithasahugeimpactoncrop

yields,temperature,andrainfallonEarth. In1997-1998,firestriggeredbyanunusual

droughtcausedbyENSOdestroyedlargeswathesoftropicalrainforestworldwide[4].Hur-

ricanescausedconsiderabledamageintheUnitedStatesfrom1925-1997,withanaverage

annuallossof$5.2billion[5].InENSOyears,floodriskanomaliesexistinbasinsspanning

almosthalfoftheEarth’ssurface[6].TheWorldHealthOrganizationestimatesthatover

thepast30years,anthropogenicwarmingandprecipitationhaveclaimed150,000lives

eachyear[7]. Inordertodealwiththethreatofsuchclimatedisasters, knowingand

understandingthelawsofclimatechangeandmakingeffectiveclimatepredictionsin

advancearecrucialtoreducingdisasterlossesaroundtheworld.

ENSOpredictionisoneofthemostimportantissuesinclimatescience,affectingboth

interannualclimatepredictionsanddecadalpredictionsofnear-termglobalclimatechange.

Sincethe1980s,scientistsfromallovertheworldhavebeenworkingonENSOprediction

research[8].SincetherelevanttimescaleofSSTvariabilityinmostofthetropicalPacific

Oceanisabout1year,theENSOeventdominatestheSSTvariability[9],andtheoccurrence

ofENSOisreflectedbytheseasurfacetemperatureanomaly(SSTA);therefore,ENSOis

predicted.ThephenomenonisequivalenttopredictingSSTA.Inaddition,amongallthe

indices,Niño3.4isthemostcommonlyusedindextomeasureENSOphenomena,andthe

◦ ◦ ◦ ◦

Niño3.4indexisthemeanseatemperatureintherangeof5 N~5 S170 W~120 W.

ENSOprojectionsarebyfarthemostsuccessfulofshort-termclimatepredictions.

TraditionalENSOpredictionmodelsaremainlydividedintotwocategories: statistical

modelsanddynamicmodels. StatisticalmodelsanalyzeandpredictENSOthrougha

seriesofstatisticalmethods,suchasthelineartransposemodel(LIM),nonlinearcanonical

correlationanalysis(NLCCA),singularspectrumanalysis(SSA),etc. Essentially,thisis

accidental,theydonottakefulladvantageofthelawsofphysics. Thedynamicmodels

aremainlybasedonthedynamictheoryofatmosphere–oceaninteraction,suchasthe

intermediatecoupledmodel(ICM),thehybridcoupledmodel(HCM),andthecoupled

circulation model (CGCM) [10]. It is successful in short-term prediction, but it does

not make full use of the large amount of existing real historical data. For long-term

prediction,thepuredynamicmethodisdifficulttowork. Practicehasshownthatboth

dynamicmethodsandstatisticalmethodshaveacertainaccuracy,andbothcanreflect

someofthelawsofatmosphericmotion[11–13],butduetothevariabilityanddiversityof

ENSOspatiotemporalevolution,traditionalmethodsofpredictingENSOstillhavegreat

deficiencies,especiallyinthe21stcentury;theintensifiedinfluenceoftheextratropical

atmosphereonthetropicsmakesENSOmorecomplexandunpredictable.

TheconceptofartificialintelligencefirstcamefromtheDartmouthConferenceon

Computersin1956,anditsessenceistohopethatmachinescanthinkandrespondsimilarly

tohumanbrains.Machinelearningisanimportantwaytorealizeartificialintelligence.As

themostimportantbranchofmachinelearning,deeplearninghasdevelopedrapidlyin

recentyearsandisnowwidelyusedinimagerecognition,naturallanguageprocessing,

andotherfields.

Theconceptofdeeplearning,whichreferstothemachinelearningprocessofobtaining

adeepnetworkstructurecontainingmultiplelevelsthroughacertaintrainingmethod

basedonsampledata,wasfirstproposedbyHintonetal.[14]attheUniversityofToronto

in2006. Figure1showstherelationshipamongartificialintelligence,machinelearning,

artificialneuralnetworksanddeeplearning.Unlikemachinelearning,thedeeplearning

featureextractionprocessisperformedautomaticallythroughdeepneuralnetworks.The

featuresintheneuralnetworkareobtainedthroughlearning.Undernormalcircumstances,

whenthenetworklayerisshallow,theextractedfeaturesarelessrepresentativeofthe

18

Mathematics2022,10,3793

originaldata.Whenthenumberofnetworklayersisdeep,thefeaturesextractedbythe

modelwillbemorerepresentative. Whenthetasktobesolvedismorecomplex, the

parameterrequirementsofthemodelarealsohigher,andthenumberofnetworklayersat

thistimeisoftendeeper,whichmeansthatmorecomplextaskscanbesolved.Therefore,

itcanbeconsideredthatthedeeperthenetworklayer,thestrongerthefeatureextraction

ability.Currently,thecommonlyuseddeepneuralnetworkmodelsmainlyincludeCNN,

recurrentneuralnetwork(RNN),deepbeliefnetwork(DBN),andthedeepautoencoder

andgenerativeadversarialnetwork(GAN).

Figure1.Therelationshipbetweenartificialintelligence,machinelearning,artificialneuralnetworks,

anddeeplearning.

Withthewideapplicationofmachinelearninganddeeplearninginvariousfieldsin

recentyears,somescholarshavebeguntousemachinelearningordeeplearningtechnology

topredictmeteorologicalelements(windspeed,temperature,etc.)orclimatephenomena,

suchasENSO,andhaveobtainedbetterresults.Thispaperwillsummarizetheprevious

researchresultsandmakeamorecompletesummaryofENSOpredictionscombinedwith

deeplearning.

Thispaperisorganizedasfollows:Section1outlinesthemainlearningknowledgeand

developmentstatusinENSOforecasting;Section2focusesontraditionalENSOforecasting

methods;Section3isthekeypartofthispaper,introducingtherelatedmodelsandtheories

ofdeeplearninginartificialintelligenceandtheexistingENSOpredictionmethodsand

applicationsofdeeplearninginartificialintelligence;Section4summarizestheENSO

forecastingmethodsintabularformanddiscussestheexistingdeficienciesandfuture

developmentdirectionsofENSOpredictions;finally,Section5providesasummaryofthe

fulltext.

2.TraditionalMethods

Inthissection,wewillfocusontheexistingtheoriesorconclusionsoftraditionalENSO

forecastingmethods. TherearegenerallytwomethodsfortraditionalENSOprediction,

namely,thestatisticalmodelandthedynamicmodel.Thefollowingwilllistthecurrently

commonlyusedENSOforecastmethodsandrelatedENSOforecastknowledge.

2.1.ClimateDynamicsMethods

Thedynamicmethodusesdynamicequationstomodeltheocean,atmosphere,land,

andotherspheresandtheirinteractionsandusesthecomputertograduallyintegrate

tosimulatetheevolutionoftheatmosphere. SincethefirstcoupledENSOmodelwas

developed[15,16],varioustypesofcoupledmodelshavebeendesignedandusedforENSO

simulationandprediction.Thecouplingmodelsmainlyincludethesimplecoupledmodel

19

Mathematics2022,10,3793

(SCM)[17],intermediatecoupledmodel(ICM)[16],hybridcoupledmodel(HCM)[18],

andfullycoupledcirculationmodels(GCMs)[19]. Dynamicalmodelshavebecomethe

main tool for studying the mechanism, simulation, and prediction of ENSO, and the

predictiontimereaches6–12months. Ref.[17]identifiedseveralfreeequatorialmodes

forsimplecoupledocean–atmospheremodelsandfoundthattheyincludedunstableand

dampedmodesatlargeregionalscalesandlongperiods,systematicallyexploringthe

effectsofoceanthermodynamicsonthebehaviorofunstablemodes.Ref.[16]developed

anatmosphere–oceancoupledmodeltostudytheENSOphenomenon. Intheabsence

ofanomalousexternalforcing,thecoupledmodelreproducessomekeyfeaturesofthe

observedphenomenon. Theresultsshowthatthemeanseasurfacetemperature,wind,

andoceancurrentfielddeterminethecharacteristicspatialstructureoftheENSOanomaly.

Ref.[18]conductedaseriesofhindcastandpredictionexperimentsusingtheHCMofthe

tropicalocean–atmospheresystem.Itshowsrealskillsinforecastingfall/wintertropical

PacificSSTupto18monthsinadvance. Ref.[19]usedanintegratedocean–atmosphere

circulationmodel(OAGCM)forclimateprediction. Bothmodelperformanceanddata

assimilationschemesforclimatesimulationswereimprovedtoyieldbetterforecastingskills.

MostOAGCMscannowproficientlypredicttheIndianOceanDipole(IOD)1–2seasonsin

advance,withENSOsupto6–9monthsahead.

In recent years, many forecasting systems have been put into use. The National

ClimateCenterofChinaMeteorologicalAdministration(BCC/CMA)developedtheENSO

Monitoring,AnalysisandPredictionSystem(SEMAP2)[20].Thesystemconsistsoffive

subsystems:real-timemonitoringoftropicalatmosphereandocean,dynamicdiagnosis,

physical-basedstatisticalprediction,modelensembleprediction,andsimulation-based

modelprediction[21]correction,whichcanrealizethefeedbackprocessofENSOchanges

anddynamicsintherecentyearreal-timemonitoringandcanprovideuserswithforecasts

oftheENSOindexandrelatedmainvariableprocessesinthecomingyear.Sincethespring

of2013,SEMAP2hasbeenappliedtoENSObusinessmeetingsorganizedbytheNational

ClimateCenterseveralconsecutivetimesandgivenforecastopinions,withgoodresults

andwasadoptedbyforecastersmanytimes.Especiallyinthespringof2014,theprediction

oftheevolutiontrendofElNiñoinsummerandautumnwasbasicallyinlinewithreality

andmoreaccuratelypredictedtheweakcentralEINinoeventinthewinterof2014/15and

accuratelypredictedthedevelopmentofElNiñosincethespringof2015.TrendsandType

Conversions.Theforecastingsystemisstillinusetothisday.Thefifth-generationseasonal

forecastsystemSEAS5wasputintouseinNovember2017bytheEuropeanCentrefor

Medium-RangeWeatherForecasts.Itisacoupleddynamicalmodelthatincludeshigher

resolutionmodelsoftheatmosphere, ocean, andseaice. Animportantimprovement

inSEAS5istheweakeningofthecoldtonguebiasintheequatorialPacific, whilethe

amplitudeofElNiñoisclosertotheactualvalueandimprovesthepredictionabilityofEl

NiñointhecentralandwesternPacific,makingitshowparticularadvantagesinENSO

predictions.Whentheforecastperiodis9months,thecorrelationcoefficientofSEAS5to

ENSOforecastreachesmorethan0.7[22].

If the starting time of the prediction model is advanced by more than 6 months,

the prediction ability of the traditional method model will be greatly reduced due to

thephenomenonofthespringpredictabilitybarrier(SPB)[1].TheSPBphenomenonwas

discoveredbyWebsteretal.[23]inthedynamicpredictionmodel.Wangetal.[24]proposed

thatthelargestverticaltemperaturegradientandtheweakesteast–westthermaldifference

inspringareconducivetothegrowthofthecoupledsystemdisturbance,whichinturn

makesthespringsea-aircouplingthemostunstable,whichisconducivetothegeneration

oftheSPBphenomenon.Chenetal.[25]proposedanovelENSOpredictionmodel(EPM)

that combines tropical states and extratropical ocean–atmosphere interactions, which

cansignificantlyimproveENSOforecastingskillsbeyondthespring-predictablebarriers.

Althoughdynamicalmodelsaresuccessfulinshort-termpredictions, puredynamical

methodsareineffectiveforlong-termpredictions.

20

Mathematics2022,10,3793

2.2.MathematicalStatisticalMethods

ThestatisticalENSOpredictionmethodistorealizetheanalysisandpredictionof

ENSOphenomenonbysorting,summarizing,andanalyzinghistoricalENSOindicators.

Statisticalmodelsincludelinearstatisticalmodelsandnonlinearstatisticalmodels. The

formerisconstructedusinglinearmethodssuchasmultiplelinearregression,canonical

correlation, and Markov chains, while the latter is mainly constructed using machine

learningmethodssuchasBayesianandneuralnetworks.

2.2.1.TraditionalLinearStatisticalMethods

Amongthetraditionallinearstatisticalmethods,therearetwooutstandingclassi-

calmethods,HoltWinters(HW)methodandautoregressiveintegratedmovingaverage

(ARIMA)method.TheHWmethodisashort-termstatisticalmethod[26]thatproposesa

forecastingexpressionforexponentiallyweightedmovingaveragesforforecastingtime

serieswithseasonalpatternsandrepeatingforms,usingatechniquecalled“exponential

smoothing”,reducingthevolatilityoftime-seriesdata,allowingforaclearerunderstanding

ofitsrationale[27]. In2014,Mikeetal. usedtheHWmodeltopredicttheSSTindexin

theNiño3regionfrom1933to2012by1monthand12monthsinadvance,witharoot

meansquareerrorof0.303and1.309.ToaddresstheshortcomingthattheHWmodelis

notsuitableforperiodicallystationarytimeseries,theyproposedanimprovedHWmodel

calledthedynamicseasonalmodel(DSM).Experimentsshowthatthismodelpredicts

monthlyNino3insampleanalysisArea, andisbetterthanthedeterministicseasonal

modelandHWmodelintermsofseasurfacetemperatureindexandintradaystockreturn

changes[28].

ARIMA,alsoknownastheintegratedmovingaverageautoregressivemodel,isone

ofthetimeseriesforecastinganalysismethods.In2011,Matthieuetal.[29]developeda

time-seriesanalysismethodusingARIMAtoinvestigatethetemporalcorrelationbetween

monthly P. falciparum case numbers and ENSO measured by SOI at Cayenne General

Hospitalfrom1996to2009.ResultsshowedthatanElNiñolagof3monthshadapositive

effectonP.falciparumcases(p<0.001),andaddingSOIdatatotheARIMAmodelreduced

the Akaike information criterion (AIC) [30] by 4%. However, ARIMA cannot return

estimatesofseasonalcomponents[31].Inaddition,Penlandetal.[32]proposedtorepresent

theIndo-PacificSSTAsasastablelinearprocessdrivenbyspatiallycoherentstochastic

forcing, obtain the relevant parameters that best fit the stable linear process through

observations,andthenmakeassumptionsaboutstabilityandlinearity.Theexperimental

resultsshowthattheoptimalmodelcanachieveasamplecorrelationof67%between

twotimeseriespredicted7monthsinadvance. Themultiplelinearregressionmodel

proposedbyTsengetal.[33]onlyreliesonfiveevolutionsofthermoclinedepthanomalies

andzonalsurfacewindmodulationovera25-dayperiod. Itsuccessfullypost-reported

allENSOsexceptthe2000/01LaNiña.Xueetal.[34]establishedaforecastmodelusing

thelinearMarkovmodel,usingseasurfacetemperature,sealevelheight,andwindstress

aspredictors.Whentheforecastperiodis6months,itsforecast-relatedskillreaches0.8.

Kondrashov et al. [35] obtained the stochastic forcing model of ENSO by polynomial

regression analysis. When the forecast period is 6 months, the correlation coefficient

exceeds0.6.

TheENSOphenomenonisahighlycomplexanddynamicpatternwhosetrendover

timeisnonlinear.Traditionalstatisticalmethodshavepoorfittingeffectonnonlineardata

sets,andarenotidealforcomplexpatternrecognitionandknowledgediscovery.

2.2.2.MachineLearningMethods

TheML-basedENSOpredictionmethodisrealizedbylearningandmininghistorical

ENSOindexfeaturesandestablishinganENSOpredictionmodel.In1998,Tangangetal.[36]

andJiangGuorongetal.[37]foundthatthecombinationoftheneuralnetworkalgorithm

andempiricalorthogonalfunctionanalysismethodcanhaveunexpectedeffectsonENSO

forecasting.In2009,SilvestreandWilliam[38]proposedtwononlinearregressionmodels,

21

Mathematics2022,10,3793

Bayesianneuralnetwork(BNN)andsupportvectorregression(SVR).Temperaturecanbe

usedasapredictorofSSTanomaliesinthetropicalPacificfor3–15months.Theresults

showthattheBNNmodelhasbetteroverallpredictionperformancethantheSVRmodel.

LiuKefengetal.[39]alsofoundthatthemulti-stephierarchicalpredictionmethodbased

onthecombinationofsupportvectormachineandwaveletdecompositionmethodcan

effectivelypredictthetimeseriesofseatemperatureanomalies.Fengetal.[40]proposed

atoolbox“climatelearn”,combinedwithsomemachinelearningmethods,topredictthe

occurrenceofElNiñoandNiño3.4indices. In2016,intermsofENSOforecasting,the

zero-meanrandomerrormodelofICMwasproposed[41], calledtheensemble-mean

model, whichshowedbetterresultsthanthedeterministicICMonENSOforecasting.

PeterDetal.[42]combinedtheclassicautoregressivesyntheticmovingaveragetechnique

withanartificialneuralnetworktopredicttheENSOindex.Inaddition,LiChentongused

thedecisiontreealgorithmtoestablishamulti-modalENSOpredictionresultintelligent

consultationsystem.Heusedfourdecisiontreemodelmethods(boosting-basedGBDT,

XGBoost,lightGBM,andbagging-basedRF),respectively,andestablishedamulti-modal

ENSOforecastingresultintelligentconsultationsystemaccordingtodifferentadvance

forecastingtimes.

ML-basedmethods,especiallythosebasedondeepnetworks,tendtobemorecomplex,

takelongertocompute,andhavepoorpredictiveabilityforverylongsequencesofENSO

indices. Inaddition,forthelong-timeseriesNiño3.4indexandSOIdata,theynotonly

haveapproximatelyperiodicinterannualvariationcharacteristicsbutalsohavealarge

amountofhigh-frequencyrandomnoiseduetoseasonalvariation,whichseriouslyreduces

thepredictiveabilityofnumericalsimulationmodels. Therefore,ENSOeventsarestill

difficulttopredictwithaleadtimeofmorethanoneyear.

3.DeepLearningMethods

Withtherapiddevelopmentofbigdataanddeeplearningmethodsinrecentyears,

predictionmethodsbasedondeeplearninghavebeenwidelyusedinvariousfields,and

somescholarshavebeguntousedeeplearningtoimproveENSOforecastingskills.This

sectionmainlyintroducestherelatedmodelsandtheoriesofspatiotemporalsequencesin

deeplearningandtheapplicationofdeeplearninginENSOprediction,includingshallow

neuralnetworks,CNNs,RNNs,andgraphneuralnetworks(GNN).

3.1.ShallowNeuralNetworks

In1986,RumelharandHinton[43]proposedtheback-propagationalgorithm,which

solvedthecomplexcalculationproblemofthetwo-layerneuralnetwork,whichledtothe

researchupsurgeofthetwo-layerneuralnetworkintheindustry.Inadditiontoaninput

layerandanoutputlayer,atwo-layerneuralnetworkalsoincludesanintermediatelayer,

whereboththeintermediatelayerandtheoutputlayerarecomputationallayers.Itsmatrix

changeformulais: (cid:2) (cid:3)

W (1)∗a (1) =a (2)

(cid:2) (cid:3)

g W (2)∗a (2) =z (1)

Ineachlayeroftheneuralnetwork,exceptfortheoutputlayer,therewillbeabias

unit.Asinlinearregressionmodelsandlogisticregressionmodels.Thematrixoperation

oftheneuralnetworkafterconsideringthebiasisasfollows:

(cid:2) (cid:3)

g W (1)∗a (1)+b (1) =a (2)

(cid:2) (cid:3)

g W (2)∗a (2)+b (2) =z (2)

Differentfromthesingle-layerneuralnetwork,itistheoreticallyproventhatthetwo-

layerneuralnetworkcanapproximateanycontinuousfunctioninfinitely,thatistosay,

22

Mathematics2022,10,3793

inthefaceofcomplexnonlinearclassificationtasks,thetwo-layerneuralnetworkcan

betterclassify.

Themulti-layerneuralnetworkcontinuestoaddlayersaftertheoutputlayerofthe

two-layerneuralnetwork.Itsadvantageisthatitcanrepresentfeaturesinadeeperwayand

hasastrongerabilitytosimulatefunctions.TheBPneuralnetworkisaconceptproposed

byscientistsheadedbyRumelhartandMcClellandin1986.Itisamulti-layerfeedforward

neuralnetworktrainedaccordingtotheerrorback-propagationalgorithm.Inotherwords,

itisafeedforwardmulti-layerperceptron(MLP)trainedusingtheBPalgorithm. The

BPneuralnetworkiswidelyusedinmeteorologicalforecasting. TheclassicBPneural

networkisgenerallydividedintothreelayers,namely,theinputlayer,thehiddenlayer,

andtheoutputlayer.Themainideaofitstrainingis:inputdata,usetheback-propagation

algorithmtocontinuouslyadjustandtraintheweightsandthresholdsofthenetwork,

adjusttheweightsandthresholdsaccordingtothepredictionerror,andoutputtheresults

thatareclosetotheexpectationsuntilthepredictedresultscanreachtheexpectations.The

topologyoftheBPneuralnetworkisshowninFigure2.

Figure2.BPneuralnetworktopologydiagram.

WhentheBPneuralnetworkprocessesdata,thenetworkshouldbeinitializedfirst

andthenetworkparametersshouldbeset;Thesecondstepistocalculatetheoutputof

thehiddenlayer,theoutputformulaisshowninFormula(3),whereXrepresentsthe

inputvariable,ω ,aaretheinputconnectionweightofthelayerandthehiddenlayer

ij

andthethresholdofthehiddenlayer,listhenumberofnodesinthehiddenlayer, f is

theactivationfunctionofthehiddenlayer;thentheoutputlayeriscalculated,andthe

predictedoutputY oftheBPnetworkisshowninformula(4),Amongthem, H isthe

outputofthehiddenlayer,ω ,baretheconnectionweightsandthresholds,respectively;

ij

Theformulaforcalculatingtheerrorisshownin(5),whereY isthepredictedvalueofthe

k

network,O istheactualexpectedvalue;Weupdatetheweightsandupdatethenetwork

k

connectionweightsω ,ω throughthepredictionerrore. Theformulaisshownin(6),

ij jk

andηisthelearningrate;thenetworkthresholdsaandbareupdatedaccordingtothe

predictionerrore,andtheformulaisshownin(7);Finally,determinewhethertheiteration

canend. Ifthealgorithmiterationdoesnotend,wereturntothesecondstepuntilthe

algorithmends. (cid:24) (cid:31)

n

H = f ∑ω x +a , j=1,2,...,l (3)

j ij i j

i=1

l

Y = ∑ Hω +b , k=1,2,...,m (4)

k j jk k

j=1

e =Y −O , k=1,2,...,m (5)

k k k

(cid:11) (cid:12)

m

ω =ω +ηH 1−H x ∑ ω e , i=1,2,...,n;j=1,2,...,l

ij ij j j i k=1 jk k (6)

ω =ω +ηHe , j=1,...,l;k=1,...,m

jk jk j k

23

Mathematics2022,10,3793

m

a =a +ηH(1−H)x ∑ ω e , j=1,...,l

j j j i k=1 jk k (7)

b =b +ηe , k=1,...,m

k k k

ManyresearchersinitiallytriedtoapplyshallowneuralnetworkstoENSOprediction

and achieved good results. Jiang Guorong et al. [37] used the back-propagation (BP)

algorithmforENSOforecasting,whichcouldbetterpredictthechangingtrendofSSTin

keyareas.However,forecastskillassessmentdependsonforecasttime,whichisinversely

proportional. Baawainetal.[44]designedathree-layermulti-layerperceptronmodel,

andthehiddenlayerandoutputlayerweretrainedusingalogicalactivationfunction

throughanerrorback-propagationalgorithm.Ravietal.[45]usedtheANNmodeltoselect

theNiño1+2,Niño3,Niño3.4,andNiño4indicesasthepredictorsoftheIndiansummer

monsoonrainfallindex(ISMRI)forprediction.Theresultsshowthattheneuralnetwork

modelhasbetterpredictivepowerthanalllinearregressionmodels.Mekaniketal.[46]

foundthroughexperimentsthatusingthelaggedENSO-DMIindexcombinedwithANN

topredictspringrainfallcanachievea96.96%correlation. Thismethodcanbeusedin

areasoftheworldwherethereisarelationshipbetweenrainfallandlarge-scaleclimate

patternsthatcannotbeestablishedbylinearmethods. PetersikandDijkstraetal.[47]

usedanensembleofGaussiandensityneuralnetworksandquantileregressionneural

networkstotrainENSOindicesandoceanheatcontentwithasmallamountofdatato

predictENSO.For1963–2017assessments,thesemodelsarehighlycorrelatedwithlonger

leadtimes.However,theshallowneuralnetworkhaslimitedabilitytorepresentcomplex

functions,anditsgeneralizationabilityforcomplexclassificationproblemsisrestrictedto

acertainextent,andtheshallowneuralnetworktendstofallintoalocalminimumduring

training,whichispronetooverfittingduringtesting.Themulti-layerneuralnetworkcan

representcomplexfunctionswithfewerparametersbylearningadeepnonlinearnetwork

structureandhasstrongfeaturelearningability.Amulti-layerneuralnetworkhasgreat

potentialtosolvecomplexnonlinearstochasticproblemswithmanyinfluencingfactors

suchasclimateprediction.

3.2.ConvolutionalNeuralNetworks

ResearchonCNNsbeganinthe1980sand1990s,andtimedelaynetworksandLeNet-5

werethefirstCNNs.YannLeCunetal.[48]proposedaCNNalgorithmbasedongradient

learningin1998andappliedittohandwrittendigitrecognition.In2012,Hintonetal.[49]

wontheclassificationcompetition,whichopenedthepreludetothegradualdominationof

CNNsinthefieldofcomputervision.

Asatypeofneuralnetwork,CNNcaneffectivelyextractfeaturescontainedinimages,

soitiswidelyusedinfieldsinvolvingimageprocessing(suchasimagerecognition,object

detection,etc.)[49,50].Formeteorologicaldata,thedistributionfieldofacertainelementat

acertaintimecanberegardedasanimage,anditcanbeusedastheinputofCNN.Using

CNNtosolveitisactuallyanonlinearregressionoftheglobaloceanelementfieldandthe

Nino3.4regionalSSTinthenextfewmonths.

ThemainstructureofCNNincludesinputlayer,convolutionlayer,poolinglayer,

fullyconnectedlayer,andoutputlayer.Themainfunctionoftheconvolutionlayeristo

enhancetheoriginalsignalfeaturesandreducenoisethroughconvolutionoperations.The

expressionforconvolutionincalculusis:

(cid:26)

S(t)= x(t−a)w(a)da (8)

Thediscreteformis:

s(t)=∑ x(t−a)ω(a) (9)

a

Thisformulacanbeexpressedasamatrix:

(t)=(X∗W)(t) (10)

24

Mathematics2022,10,3793

Amongthem,∗representstheconvolutionoperation;ifitisatwo-dimensionalconvolution,

itisrepresentedas:

s(i,j)=(X∗W)(i,j)=∑∑ x(i−m,j−n)w(m,n) (11)

m n

TheconvolutionformulainCNNisslightlydifferentfromthedefinitioninmathemat-

ics.Forexample,fortwo-dimensionalconvolution,itisdefinedas:

s(i,j)=(X∗W)(i,j)=∑∑ x(i+m,j+n)w(m,n) (12)

m n

Amongthem,Wistheconvolutionkernel,andXistheinput.IfXisatwo-dimensional

inputmatrix,thenWisalsoatwo-dimensionalmatrix.However,ifXisamultidimensional

tensor,thenWisalsoamultidimensionaltensor.

Themainpurposeofthepoolinglayeristoreducetheamountofdataprocessingand

speedupnetworktrainingwhileretainingusefulinformation.Commonlyusedpooling

operationsincludeaveragepoolingandmaximumpooling. Theresultsofmaxpooling

andaveragepoolingareasfollows:

y il+1 ,j il+1 ,d= H 1 W 0≤i≤H ∑ ,0≤j≤W x i l l+1 ×H+i,jl+1×W+j,dl (13)

y il+1 ,j il+1 ,d= 0≤i≤ m H, a 0≤ x j≤W x i l l+1 ×H+i,jl+1×W+j,dl (14)

Theactivationfunctionlayerisalsocalledthenonlinearmappinglayer.Thepurpose

istoincreasetheexpressiveability(nonlinearity)oftheentirenetwork.Themainactivation

functionsincludethesigmoidfunction, thetanhfunction, andtherelufunction. The

formulaoftheactivationfunctionisshownin(15).Afterseverallayersofconvolutionand

poolingoperations,theobtainedfeaturemapsareexpandedrowbyrow,connectedinto

vectors,andinputintothefullyconnectednetwork.Thefullyconnectedlayerintegrates

thefeaturesinthefeaturemaptoobtainthehigh-levelmeaningoftheimagefeatures,

whichisthenusedforimageclassification.

sigmoid(x)=

1+

1

e −x

tanh(x)= 1 1 − + e e − − 2 2 x x (15)

(cid:15)

relu(x)= 0

x

(

(

x

x

≤

>

0

0

)

)

CNNsareappliedinmanyfieldsofweatherforecasting,andtheyarealsohelpful

forENSOforecasting. InSeptember2019,Hametal.[51]firstproposedusingaCNN

forENSOprediction. ThemodelstructureisshowninFigure3. CNNrequiresalarge

numberofimagesfortraininginordertoimprovetheaccuracyofprediction.Despitethe

largescaleofmeteorologicaldata,theuseofCNNsinENSOforecastinghasencountered

difficultieswithdatashortages. Hametal. proposedtocombineclimatemodelswith

artificial intelligence methods, using dozens of global climate models from CMIP5 to

generateaseriesofsimulateddatabasedonhistoricaloceandata.Asaresult,scientistsnot

onlyhaveasetofactualhistoricalobservationsbutalsothousandsofsimulationresultsfor

training.Theresearchresultsshowthatwhenthepredictiontimeismorethan6months,

thepredictionabilityoftheCNNmethodfortheNino3.4indexissignificantlyhigherthan

thatofthecurrentinternationalbestdynamicpredictionsystem.Whentestedonrealdata

from1984to2017,CNNwasabletopredictElNiñoevents18monthsinadvance.Atthe

time,theresearchresultswereregardedasthepioneeringworkofdeeplearninginthe

fieldofweatherforecasting.

25

Mathematics2022,10,3793

Figure3.StructureoftheCNNmodelforENSOprediction[51].

However,thedefectsofCNNitself,includingfixedinputvectorsizeandinconsistent

inputandoutputsize,limititsapplicationintime-seriesforecasting.In2020,Yanetal.[52]

proposedtheensembleempiricalmodedecomposition-temporalconvolutionalnetwork

(EEMD-TCN) hybrid method, which decomposes the variable Niño3.4 exponent and

SOI into relatively flat subcomponents; then, The TCN model is used to predict each

subcomponentinadvance,andfinally,thesub-predictionresultsarecombinedtoobtain

thefinalENSOpredictionresult.TheTCNresidualmodulediagramisshowninFigure4.

TCNisavariantofCNNthatusesrandomconvolutionanddilationforsequentialdata

withtemporalityandlargereceptivefields.Empiricalmodedecompositioncandecompose

high-frequencytimeseriesNiño3.4indexandSOIdataintomultipleadaptiveorthogonal

components,improvingthepredictionaccuracyofthemodel. Theexperimentalresults

showthattheTCNmethodhasagoodeffectintheadvancepredictionofENSO,which

hasimportantguidingsignificancefortheresearchintoENSO.Inresponsetotheproblem

ofdatashortage,inadditionto[51]usingclimatemodelstogeneratealargeamountof

simulateddata,in2021,Hu[53]etal.useddropoutandtransferlearningtoovercomethe

problemofinsufficientdataduringmodeltrainingandproposedamodelbasedonadeep

residualconvolutionalneuralnetwork.ThemodeleffectivelypredictstheNiño3.4index

with a lead time of 20 months during the 1984–2017 evaluation period, three months

morethantheexistingoptimalmodel.Inaddition,theyalsouseheterogeneoustransfer

learning.Thismodelachieved83.3%accuracyforforecastingthe12-month-leadEINiño

type.However,manyforecastsonlyconsidertemporalityandthelackofspatialfeatures

inENSO.In2022, Zhao[54]etal. proposedanend-to-endspatialtemporalsemantic

network,namedSTSNet,whichconsistsofthreemainmodules:(1)Geographicsemantic

enhancementmodule(GSEM)distinguishesvariouslatitudeandlongitudethrougha

learnableadaptiveweightmatrix;(2)Anovelspatiotemporalconvolutionalmodule(STCM)

isdesignedspeciallytoextractthemultidimensionalfeaturesbyalternatingtheexecution

oftemporalandspatialconvolutionandtemporalattention;(3)Combiningandexploiting

multi-scaletemporalinformationinathree-streamtemporalscalemodule(3sTSM)to

furtherimproveperformance.Figure5illustratesthepipelineoftheproposedSTSNet.The

resultsshowthatSTSNetcansimultaneouslyprovideeffectiveENSOpredictionsfor16

monthswithhighercorrelationandlowerbiascomparedtootherdeeplearningmodels.

26

Mathematics2022,10,3793

Figure4.TheTCNresidualmodule[52].

27

Mathematics2022,10,3793

Figure5.ThepipelineoftheproposedSTSNet[54].

3.3.RecurrentNeuralNetwork

Whentheinputdatahasdependenciesandisasequentialpattern,theresultsofCNNs

aregenerallynotverygood,becausethereisnocorrelationbetweenthepreviousinput

oftheCNNandthenextinput. In1982,Hopfield[55]proposedRNN.RNNisusedto

solvetheproblemthatthetrainingsampleinputisacontinuoussequence,andthelength

ofthesequenceisdifferent,suchastheproblembasedonthetimeseries. RNNsenable

deeplearningmodelstomakebreakthroughsinsolvingproblemsinNLPdomainssuchas

speechrecognition[56],languagemodels[57],machinetranslation[58],andtimeseries

analysis.In1997,JurgenSchmidhuberetal.[59]proposedlongshort-termmemory(LSTM),

anovelRNNvariantstructurethatusesgatingunitsandmemorymechanismstocapture

long-termtemporaldependencies,andsuccessfullysolvesgradientdisappearanceand

theexplosionproblem,whichcontrolstheflowofinformationthroughlearnablegates.

ThestructurecomparisonofRNNandLSTMisshowninFigure6.Amongthem,LSTM

introducestheconceptsoftheforgettinggate,inputgate,andoutputgate,thus,modifying

thecalculationmethodofthehiddenstateinRNN.Theformulaisasfollows:

It =σ(XtW

xi

+Ht−1W

hi

+b

i

) (16)

(cid:2) (cid:3)

Ft =σ XtW

xf

+Ht−1W

hf

+b

f

(17)

Ot =σ(XtWxo +Ht−1W

ho

+bo ) (18)

Amongthem,W

xi

,W

xf

,WxoandW

hi

, W

hf

, W

ho

arealllearnableweightparameters,

andb

i

, b

f

, boarelearnableoffsetparameters.Thecandidatecellinlongshort-termmemory

∼

Ctusesthehyperbolictangentfunctiontanhintherange[−1,1]astheactivationfunction:

∼

Ct =tanh(XtWxc +Ht−1W

hc

+bc ) (19)

Theflowofinformationinthehiddenstatecanbecontrolledbyinputgates,forget-

tinggates,andoutputgateswithelementvaluesintherange[0,1]: thiscanusuallybe

∼

performedwiththeelement-wisemultiplicationoperator(cid:13).ThecalculationofthecellCt

atthecurrentmomentcombinestheinformationofthecellatthepreviousmomentand

28

Mathematics2022,10,3793

thecandidatecellatthecurrentmoment,andcontrolstheflowofinformationthroughthe

forgettinggateandtheinputgate:

∼

Ct =Ft (cid:13)Ct−1 +It (cid:13)Ct (20)

Next,theinformationflowfromthecelltothehiddenlayervariableHtcanbecon-

trolledbytheoutputgate:

Ht =Ot (cid:13)tanh(Ct ) (21)

In2017,Zhang,Wang[60],andothersdefinedtheSSTpredictionproblemasatime-

seriesregressionproblemandusedLSTMasthemainlayerofthenetworkstructureto

predicttheBohaiSeatemperature. TheexperimentalresultscomparedwithSVRshow

thattheLSTMnetworkhasbetterpredictionperformance.In2018,Cliffordetal.[61]used

the“climatecomplexnetwork”toextractmeteorologicaldatafeatures,usedtheextracted

featuresaspredictors,andusedLSTMtopredicttheNino3.4index. Experimentsshow

thattrainingLSTMmodelsonnetworkmetrictimeseriesdatasetshasgreatpotentialfor

predictingENSOphenomenamanystepsahead.In2021,Zhouetal.[62]usedLSTMto

buildatropicalPacificNiño3.4indexforecastmodelandanalyzedtheseasonalforecast

errorofthemodel.Theresultsshowthatforthe1997/1998and2015/2016strongeastern-

typeElNiñoevents,themodelcanmoreaccuratelypredictthetrendsandpeaksofthe

events,andtheanomalouscorrelationcoefficient(ACC)reachesmorethan0.93.However,

forthe1991/1992and2002/2003weakcentralElNiñoevents,itdidnotperformwellin

peakforecasting.

Figure6.ComparisonoftheRNNandLSTMstructure.

Shi X et al. [63] proposed the concept of convolutional long short-term memory

(ConvLSTM)andestablishedanend-to-endtrainablefortheprecipitationnow-prediction

problembystackingmultipleConvLSTMlayerstoformanencoder–decoderstructureThe

modeldiagramisshowninFigure7.ConvLSTMisdesignedtosolvetheproblemof3D

dataprediction;theunitcanreceive2Dmatricesandevenhigherdimensionalinputsat

eachtimestep.ThekeyimprovementisthattheHadamardproductbetweentheweights

andtheinputisreplacedbyaconvolutionoperation,asshowninEquation(22). Itcan

notonlyestablishtemporalrelationshipssimilartoLSTMbutalsodescribelocalspatial

featuresbyextractingfeaturessimilartoCNN.

it =σ(W

xi

∗Xt +W

hi

∗Xt−1 +b

i

)

29

Mathematics2022,10,3793

(cid:2) (cid:3)

ft =σ W

xf

∗Xt +W

hf

∗Ht−1 +b

f

ot =σ(Wxo ∗Xt +W

ho

∗Ht−1 +bo ) (22)

∼

Ct =tanh(Wxc ∗Xt +W

hc

∗Ht−1 +bc )

∼

Ct = ft (cid:13)Ct−1 +it (cid:13)Ct

Ht =ot (cid:13)tanh(Ct )

Figure7.Encoding-forecastingConvLSTMnetwork[63].

Amongthem, “∗”representstheconvolutionoperation, “(cid:13)”representsHadamard

product.ThedifferencebetweenConvLSTMandLSTMisonlythattheinput-to-stateand

state-to-statepartsarereplacedbyfullyconnectedcalculationswithconvolutioncalculations.

In2019,DandanHeetal.[64]establishedadeeplearningENSOpredictionmodel

(DLENSO)usingConvLSTMtopredictENSObydirectlypredictingSSTinthetropical

Pacific.DLENSOisasequence-to-sequencemodel.ItsencoderanddecoderarebothCon-

vLSTM,andtheinputandpredictiontargetsarebothspatiotemporalsequences.DLENSO

issuperiortotheLSTMmodelandthedeterministicpredictionmodelandisalmostequiv-

alenttotheensembleaverageinthemediumandlong-termpredictionmodels.Tocapture

bothspatialandtemporalcorrelationsinSSTandimprovepredictionskillsoverlonger

timehorizons,Mu[65]etal. proposedtheConvLSTM-RMmodel,whichisahybridof

convolutionalLSTMandrollingmechanism,andusedittobuildanend-to-endtrainable

modelfortheENSOpredictionproblem.TheirexperimentsonhistoricalSSTdatasetsshow

thatConvLSTM-RMoutperformssevenwell-knownmethodsonmultipletimehorizons(6

months,9months,and12months).Thedeeplearningmethodsusedaboveareallsuper-

visedlearning,thetrainingdataarealllabeled,andthecostofdatalabelingisoftenhuge.In

recentyears,unsupervisedlearninghasbeenminedandgraduallydeveloped.Thebiggest

advantageofunsupervisedlearningisthatitdoesnotneedtolabelthedatasoitcansavea

lotofmanpowerandresources.Atthesametime,comparedwiththelimitedlabelsmarked

bysupervisedlearning,thefeaturesthatcanbelearnedbyunsupervisedlearningaremore

adaptiveandrich.In2021,Gengetal.[66]regardedENSOpredictionasanunsupervised

spatiotemporalpredictionproblemanddesignedadenseconvolution–longshort-term

memory(DC-LSTM).ThemodeldiagramisshowninFigure8.Toobtainamoreadequately

trainedmodel,theyaddedhistoricalsimulateddatatothetrainingset.Theexperimental

resultsshowthattheDC-LSTMmethodismoresuitableforlargeareaandsinglefactor

prediction.Duringthe1994–2010validationperiod,thefull-seasoncorrelationabilityof

theNino3.4indexofDC-LSTMwashigherthanthatoftheexistingdynamicmodelsand

regressionneuralnetworks,andthepredictioneffectforaleadtimeofupto20months

wasmuchhigherthan[51].In2022,Luetal.[67]developedanewhybridmodel,POP-Net,

topredictSSTinNiño3.4regionsbycombiningPOPanalysisprocedureswithCNNand

LSTM.POP-Netachievedahighcorrelationof17-monthlead-timepredictions(correlation

coefficientover0.5)duringthe1994–2020validationperiod. Inaddition,POP-Netalso

mitigatesSPB.

30

Mathematics2022,10,3793

Figure8.ModelstructurediagramofDC-LSTM[66].

RNNsalsohavetheirownflaws. TheRNNisoftenusedtoprocesssequencedata,

butthedisadvantageisthatitisnotsuitableforlongsequences,andthegradientiseasy

tovanish. LSTMisproposedtodealwiththeproblemofgradientdisappearance. It

is especially suitable for long sequences, but the disadvantage is the large amount of

calculation;GRUisproposedtosimplifythecalculationofLSTM;obviously,GRUlosta

gateinLSTM.Obviously,iftheparametersareless,thenaturalcalculationwillbefaster.

Whenthetrainingsetislarge,theperformanceisnaturallynotasgoodasLSTM.

3.4.GraphNeuralNetworks

TheconceptofGNNwasfirstproposedbyGori[68]andothersin2005. TheRNN

frameworkwasusedtodealwithundirectedgraphs,directedgraphs,labeledgraphs,and

cyclicgraphs. Thefeaturemapandnodeaggregationofthemethodgenerateavector

31

Mathematics2022,10,3793

representationforeachnode,whichcannotwelldealwiththecomplexandchangeable

graphdatainreality.Brunaetal.[69]proposedtoapplyCNNtographs,andthroughclever

transformationofconvolutionoperators,theyproposedthegraphconvolutionalnetwork

(GCN)andderivedmanyvariants.TheproposalofGCNisthe“pioneeringwork”ofthe

graphneuralnetwork.Forthefirsttime,theconvolutionoperationinimageprocessingis

simplyusedintheprocessingofgraphstructuredata,whichreducesthecomputational

complexityofthegraphneuralnetworkmodel.ThecalculationoftheLaplacianmatrixin

thecalculationprocesshassincebecomepasttense.Supposingwehaveabatchofgraph

data,whichhasNnodesandeachnodehasitsowncharacteristics,weletthecharacteristics

ofthesenodesformanN×D-dimensionalmatrixX,andthentherelationshipbetween

eachnodewillalsoformanN×D.AnN-dimensionalmatrixAiscalledanadjacency

matrix.XandAaretheinputstoourmodel,andtheformulaforGCNisasfollows:

(cid:24) (cid:31)

−1 −1

H

(l+1)=σ

D

˜ 2

A

˜

D

˜ 2

H

(l)

W

(l)

(23)

˜ ˜ ˜

Amongthem,A=A+I,Iistheidentitymatrix;DisthedegreematrixofA;Histhe

featureofeachlayer;fortheinputlayer,HisX;σisthenonlinearactivationfunction.The

modelofGCNisshowninFigure9.

Figure9.Graphconvolutionalneuralnetworks[68].

In2021,Cachayetal.[70]firstproposedtheapplicationofagraphneuralnetworkin

seasonalforecastingandpublisheditinNIPS.TheyadvocateddefiningtheONIprediction

problemasagraphregressionproblemandmodeleditusingGNNsthatgeneralized

convolutionstonon-Euclideandata,thus,allowingustomodellarge-scaleglobalcon-

nectionsasedgesofthegraph,exceptingraphconvolutionalneuralnetworks,andthey

alsodesignedanewgraph-connectedlearningmoduletoenableGNNmodelstolearn

large-scalespatialinteractionstogetherwithpracticalENSOpredictiontasks.Themodel

surpassesthestate-of-the-artdeeplearning-basedCNNmodelinENSOprediction,and

isalsomoreeffectivethantheLSTMmodelandthedynamicmodel,anditscorrelation

coefficientsinENSOpredictions1month,3months,and6monthsaheadoftimereach

0.97,0.92,and0.78. TheheatmapofitseffectisshowninFigure10. Simplyusingthe

graphicalmodelcanachievesuchexcellentresults.Ifthegraphicalmodeliscombinedwith

thepowercoupler,willtherebenewgains?Practicebringstrueknowledge.Bin[71]etal.

designedagraph-basedmultivariateair–seacoupler(ASC)usingthefeaturesofmultiple

physicalvariablestolearnmultivariatesynergythroughgraphconvolution.Basedonthis

coupler,anENSOdeeplearningpredictionmodel,ENSO-ASC,wasproposed,whichuses

stackedConvLSTMlayersastheskeletonoftheencodertoextractspatiotemporalfeatures,

andthedecoderconsistsofstackedtransformconvolutionallayersandupsamplinglayers.

ThemodelstructurediagramisshowninFigure11.Theexperimentalresultsshowthat

32

Mathematics2022,10,3793

ENSO-ASCoutperformsothermodels;seasurfacetemperatureandzonalwindaretwo

importantpredictors;andtheNiño3.4indexhascorrelationsofover0.78,0.65,and0.5

forleadtimesof6,12,and18months,respectively. Throughthiscase,wecanseethat

combiningdeeplearningmodelswithmultivariateair–seacouplersorotherdynamical

modelscanimprovetheeffectivenessandsuperiorityofpredictingENSOandanalyzing

underlyingdynamicalmechanismsinacomplexmanner.

Figure10.HeatmapoftheeffectofGNNpredictingENSO[70].(a–d)respectivelyrepresenttheheat

mapofGNN’spredictionofENSOonatimescaleof1,3,6and9monthsinadvance.

Figure11.ThestructureofENSO-ASC[71].

However,manyrecentcross-domainstudieshavefoundthatGNNmodelsdonot

providetheexpectedperformance.Whentheresearcherscomparedthemtosimplertree-

basedbaselinemodels,GNNscouldnotevenoutperformthebaselinemodels.GNNcan

onlyperformfeaturedenoisingandcannotlearnnonlinearmanifolds.GNNscan,therefore,

beviewedasamechanismforgraphlearningmodels(e.g.,forfeaturedenoising)rather

thanasacompleteend-to-endmodel.IthastobesaidthatGNN,asanemergingneural

network,hasgreatprospectsfordevelopment.

4.Discussion

WesummarizethetraditionalanddeeplearningmethodsforENSOpredictionlisted

inthispaperinTable1.MorethanhalfacenturyofENSOresearchhasachievedsignificant

results,especiallythepossibilityofreal-timepredictionofitsadvancemonth–seasonscale,

suchasthecurrentlinearstatisticalmodelsorthedynamicmodelsbasedonmathematical

equationscanpredictENSOatleast6monthsinadvance.Wehaveachievedbetterreal-time

forecasting,buttherearestilllargeerrorsanduncertaintiesinforecastingskills. Onthe

otherhand,deeplearningmethodswereputintouseinENSOforecastingandhavegreatly

33

Mathematics2022,10,3793

improvedourforecastingabilityforENSO.Theexperimentalindicatorsshowthatmost

spatiotemporalneuralnetworksaresuitableforENSOprediction.Althoughdeeplearning

methodscanimprovetheaccuracyofENSOforecasting,artificialintelligencemethods

arenotdevelopedforthefieldofscience,andresearchusingneuralnetworkstopredict

climatephenomenaisstillinitsinfancy,sotherearestillmanyproblems.

Table1.SummaryofdeeplearninganditsapplicationinENSOforecasting.

Method SpecificMethod Generalize Features

Usingdynamicequations,the Theaveragingskillsofdynamic

ocean,atmosphere,land,andother modelsaregenerallybetterthan

spheresandtheirinteractionsare statisticalmodels,butinpractice,

modeled,andthecomputeris itisdifficulttosimulatethe

DynamicMethods graduallyintegratedtosimulate interannualaveragevariationof

theevolutionoftheatmosphere. seasurfacetemperaturedueto

Rangingfromrelativelysimple uncertaintyininitialconditions.

physicalmodelstocomprehensive TheemergenceofSPB

Traditional fullycoupledmodels. phenomenon.

Method Realizetheanalysisandprediction

Linear

ofENSOphenomenonbysorting,

Statistical Statisticalmodelsrequirepast

summarizing,andanalyzing

Methods long-termforecastdatatodiscover

historicalENSOindicators.

potentialrelationships,but

Statistical

Nonlinearstatisticalmethod,by observationsofthetropicalPacific

Methods

learningandmininghistorical didnotbeginuntilthe1990s.

Machine

ENSOindexfeatures,using Comparedtocomplexdynamic

Learning

machinelearningmodelsto models,statisticalmodelsreduce

Methods

capturethenonlinearfeaturesof costandareeasiertodevelop.

ENSOforprediction.

TheforecastingskillsofCNNare

CNNisakindoffeed-forward muchhigherthanthecurrent

neuralnetworkwithconvolution state-of-the-artdynamicmodels

calculationanddeepstructure andcanalsobetterpredictthe

frominputtingoriginal detailedregionaldistributionof

ConvolutionalNeuralNetwork

information,self-learningfeatures, SST,overcomingtheweaknesses

asthenetworkgoesfromfrontto ofthedynamicpredictionmodels.

back,combiningfeaturesfrom CNNislessaffectedbySPB,butit

shallowtodeep. isnotsuitablefortime-series

forecasting.

RNNsareapatternfortext,

sequencedatarecognition.Its RNNissuitableforsolving

inputincludesmorethanjustthe sequenceproblemswith

Deep currentlyseeninputexample.It continuousanddifferentlengthof

Learning alsoincludesinformationthatthe trainingsampleinput,suchas

Methods RecurrentNeuralNetwork networkperceivesatthelast time-series-basedproblems.The

minute.Usingthisproperty, modelcanmoreaccuratelypredict

informationcancirculateinthe thetrendandpeakofstrongEl

networkforanylengthoftime. Niñoevents,butitisnotgoodfor

IncludingLSTM,ConvLSTM, weakElNiñopeaks.

ConvGRU,etc.

Thegriddedclimatedatacanbe

naturallymappedtothenodesof

GNNisadeeplearningmethod

GNN,andthepredictioneffectof

basedonagraphstructure,where

GNNinthefirst6monthsexceeds

dataisrepresentedintheformofa

GraphNeuralNetwork thecurrentstate-of-the-artCNN

graph,andinformationflowis

model.However,therearestill

explicitlymodeledthroughedge

problemssuchasdifficultyin

connections.

predictingextremeENSOevents

andlimitedtrainingsamples.

34

Mathematics2022,10,3793

First,deeplearninghasbettermodelingcapabilitiesonthebasisofbigdata,whilethe

numberofclimateobservationsamplesissmall,especiallyforextremeevents.Inthiscase,

theself-learningabilityofdeeplearningmethodsisgreatlylimited,sothedevelopmentof

deeplearningmethodsforsmallsampleeventsisacurrentdevelopmentdirection.Second,

inrecentyears,deeplearningmodelshavebecomemoreandmorecomplex. Generally

speaking,themorecomplexthemodel,thebetteritslearningability,buttheproblemis

thattheinterpretabilityofthemodelresultsisworse.

Inaddition,whenmakinglong-termpredictions,thepredictionofENSOeventpeaks

hastheproblemofunderestimationandpredictionlag.Wecouldtrytointroducesome

randomdisturbancemechanismssothatthemodelcanpredictgreaterintensity. ENSO

will also have the SPB problem in long-term forecasting, which is a difficult point in

dynamicforecasting. Morein-depthparameteradjustmentworkcanbeperformedon

thelearningratesofdifferentoptimizersinthedeeplearningmodel,perhapsbyfinding

hyperparametersthatmitigateSPBinthetrainingset.Inaddition,inordertoimprovethe

accuracyandlengthofENSOpredictions,wecouldtrythespatiotemporalpredictionmodel

andgraphneuralnetworkmodelrecentlyproposedbyAI,anduseobservationdataand

simulateddatafortrainingtoincreasetheamountoftrainingdata.Withsufficientdata,we

maybeabletotrainabettermodel.Atpresent,mostoftheresearchonartificialintelligence

toimproveENSOpredictionandotheraspectsmainlystaysonthedirectapplicationof

relatedartificialintelligencetechnology. ConsideringthatphenomenasuchasENSOin

earthscienceresearchhavecleartemporalandspatialstructuresandevolutionlawsof

physicalprocesses,theabilitytoorganicallycombinethetemporalandspatialevolution

characteristicsofENSObasedonphysicalanalysismethodswithartificialintelligence

methodsbasedonbigdatatofurtherimproveENSOForecastingskillsisahottopicin

thefieldofclimatechange. Itisalsoworthcontinuingtoexplorehowtocombinedeep

learningwithmeteorologyandclimateinthefuture.

5.Conclusions

TheseverecoldandheatcausedbytheclimatechangecausedbyENSOaffectpeople’s

dailylife,andimprovingtheaccuracyofENSOpredictionisstilladirectionthatresearchers

needtoworkon.Thispapersummarizesthemainknowledgeanddevelopmentstatusof

ENSOforecasting,includingtraditionalENSOforecastingmethodsandtheapplication

ofartificialintelligenceinENSOforecasting.Inthispaper,artificialintelligencemethods

aredividedintomachinelearningmethodsanddeeplearningmethods. Inthesection

onmachinelearning,themainmethodssuchasdecisiontree,Bayesian,supportvector

machineandARIMAarereviewedinENSOforecasting. Inthedeeplearningsection,

wesummarizedconvolutionalneuralnetworks,recurrentneuralnetworks,graphneural

networksandtheirvariants,focusingontheperformanceofthesemodelsinENSOpredic-

tion.Table1providesanoverviewofvariousENSOpredictionmethodsandcomparesthe

advantagesanddisadvantagesofeachmethod.FromtheintroductionsinSections2and3,

itcanbeseenthattheapplicationofdeeplearninginENSOpredictioniswidelyeffective

andhasgreatpotentialtofurtherimprovethepredictionaccuracyandlength.Bycombin-

ingdeeplearningandmeteorologicalscience,researchershavedrawnmoreconclusions,

contributingtobetterclimatepredictionsinthefuture.Finally,weanalyzedtheproblems

andresearchdirectionsofartificialintelligenceinENSOpredictionforfutureresearchers’

referenceandfurtherdevelopmentandbetteruseofdeeplearningtoexpandmorewaysto

helppredictENSOandevenotherclimateproblems.

AuthorContributions: Conceptualization,W.F.andY.S.; methodology,W.F.; investigation,Y.S.;

resources,W.F.;writing—originaldraftpreparation,W.F.andY.S.;writing—reviewandediting,W.F.

andV.S.S.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.

Funding:ThisworkwassupportedbytheNationalNaturalScienceFoundationofChina(GrantNo.

42075007),theOpenGrantsoftheStateKeyLaboratoryofSevereWeather(No.2021LASW-B19).

InstitutionalReviewBoardStatement:Notapplicable.

35

Mathematics2022,10,3793

InformedConsentStatement:Notapplicable.

DataAvailabilityStatement:Notapplicable.

Acknowledgments:TheauthorwouldliketothanktheresearchersinthefieldofENSOforecasting

andotherrelatedfields. Thispapercitestheresearchliteratureofseveralscholars. Itwouldbe

difficultformetocompletethisreviewwithoutbeinginspiredbytheirresearchresults.Thankyou

forallthehelpwehavereceivedinwritingthisarticle.

ConflictsofInterest:Theauthorsdeclarethattheyhavenoconflictofinteresttoreportregarding

thepresentstudy.

References

1. McPhaden,M.J.;Zebiak,S.E.;Glantz,M.H.ENSOasanintegratingconceptinearthscience. Science2006,314,1740–1745.

[CrossRef][PubMed]

2. Bjerknes,J.AtmosphericteleconnectionsfromtheequatorialPacific.Mon.WeatherRev.1969,97,163–172.[CrossRef]

3. Lin,J.;Qian,T.SwitchbetweenElNinoandLaNinaiscausedbysubsurfaceoceanwaveslikelydrivenbylunartidalforcing.Sci.

Rep.2019,9,13106.

4. Siegert,F.;Ruecker,G.;Hinrichs,A.IncreaseddamagefromfiresinloggedforestsduringdroughtscausedbyElNino.Nature

2001,414,437–440.[CrossRef][PubMed]

5. Pielke,R.A.;Landsea,C.N.LaNina,ElNino,andAtlanticHurricaneDamagesintheUnitedStates.Bull.Am.Meteorol.Soc.1999,

80,2027–2034.[CrossRef]

6. Ward,P.J.;Jongman,B.;Kummu,M.StronginfluenceofElNiñosouthernoscillationonfloodriskaroundtheworld.Proc.Natl.

Acad.Sci.USA2014,111,15659–15664.[CrossRef][PubMed]

7. Patz,J.A.;Campbell-Lendrum,D.;Holloway,T.Impactofregionalclimatechangeonhumanhealth.Nature2005,438,310–317.

[CrossRef]

8. Tang,Y.;Zhang,R.H.;Liu,T.ProgressinENSOpredictionandpredictabilitystudy.Natl.Sci.Rev.2018,5,826–839.[CrossRef]

9. Masson,S.;Terray,P.;Madec,G.Impactofintra-dailySSTvariabilityonENSOcharacteristicsinacoupledmodel.Clim.Dyn.

2012,39,681–707.[CrossRef]

10. Wang,Y.;Jiang,J.;Zhang,H.Ascalableparallelalgorithmforatmosphericgeneralcirculationmodelsonamulti-corecluster.

FutureGener.Comput.Syst.2017,72,1–10.[CrossRef]

11. Jin,E.K.;Kinter,J.L.;Wang,B.CurrentstatusofENSOpredictionskillincoupledocean-atmospheremodels.Clim.Dyn.2008,31,

647–664.[CrossRef]

12. Ren,F.M.;Yuan,Y.;Sun,C.H.ReviewofprogressofENSOstudiesinthepastthreedecades.Adv.Meteorol.Sci.Technol.2012,2,

17–24.

13. Clarke,A.J.ElNiñophysicsandElNiñopredictability.Annu.Rev.Mar.Sci.2014,6,79–99.[CrossRef][PubMed]

14. Hinton,G.E.;Osindero,S.;The,Y.W.Afastlearningalgorithmfordeepbeliefnets.NeuralComput.2006,18,1527–1554.[CrossRef]

15. Cane,M.A.;Zebiak,S.E.;Dolan,S.C.ExperimentalforecastsofELNino.Nature1986,321,827–832.[CrossRef]

16. Zebiak,S.E.;Cane,M.A.AmodelElNiñ-southernoscillation.Mon.WeatherRev.1987,115,2262–2278.[CrossRef]

17. Hirst,A.C.Unstableanddampedequatorialmodesinsimplecoupledocean-atmospheremodels.J.Atmos.Sci.1986,43,606–632.

[CrossRef]

18. Barnett,T.P.;Graham,N.;Pazan,S.ENSOandENSO-relatedpredictability.PartI:PredictionofequatorialPacificseasurface

temperaturewithahybridcoupledocean-atmospheremodel.J.Clim.1993,6,1545–1566.[CrossRef]

19. Luo,J.J.;Yuan,C.;Sasaki,W.;Behera,S.K.;Masumoto,Y.;Yamagata,T.;Masson,S.Currentstatusofintraseasonal-seasonal-to-

interannualpredictionoftheIndo-Pacificclimate.InIndo-PacificClimateVariabilityandPredictability;WorldScientificPublishing

Company:Singapore,2016;pp.63–107.

20. Ren,H.L.;Liu,Y.;Zuo,J.Q.ThenewgenerationofENSOpredictionsysteminBeijingclimatecentreanditspredictionsforthe

2014/2016superElNiñoevent.Meteorology2016,42,521–531.

21. Liu,Y.;Ren,H.L.ImprovingENSOpredictioninCFSv2withananalogue-basedcorrectionmethod.Int.J.Climatol.2017,37,

5035–5046.[CrossRef]

22. Johnson,S.J.;Stockdale,T.N.;Ferranti,L.SEAS5: ThenewECMWFseasonalforecastsystem. Geosci. ModelDev. 2019,12,

1087–1117.[CrossRef]

23. Webster,P.J.;Yang,S.MonsoonandENSO:Selectivelyinteractivesystems.Q.J.R.Meteorol.Soc.1992,118,877–926.[CrossRef]

24. Wang,B.;Fang,Z.Chaoticoscillationsoftropicalclimate:AdynamicsystemtheoryforENSO.J.Atmos.Sci.1996,53,2786–2802.

[CrossRef]

25. Chen,H.C.;Tseng,Y.H.;Hu,Z.Z.EnhancingtheENSOpredictabilitybeyondthespringbarrier.Sci.Rep.2020,10,984.[CrossRef]

26. Holt,C.C.Forecastingseasonalsandtrendsbyexponentiallyweightedmovingaverages.Int.J.Forecast.2004,20,5–10.[CrossRef]

27. Chang,V.;Wills,G.Amodeltocomparecloudandnon-cloudstorageofBigData.FutureGener.Comput.Syst.2016,57,56–76.

[CrossRef]

28. So,M.K.P.;Chung,R.S.W.Dynamicseasonalityintimeseries.Comput.Stat.DataAnal.2014,70,212–226.[CrossRef]

36

Mathematics2022,10,3793

29. Hanf,M.;Adenis,A.;Nacher,M.;Carme,B.TheroleofElNiñoSouthernOscillation(ENSO)onvariationsofmonthlyPlasmodium

falciparummalariacasesattheCayenneGeneralHospital,1996-2009,FrenchGuiana.MalarJ.2011,22,10–100.[CrossRef]

30. Li,X.;Shang,X.;Morales-Esteban,A.IdentifyingPphasearrivalofweakevents: Theakaikeinformationcriterionpicking

applicationbasedontheempiricalmodedecomposition.Comput.Geosci.2017,100,57–66.[CrossRef]

31. Dietrich,B.;Goswami,D.;Chakraborty,S.Timeseriescharacterizationofgamingworkloadforruntimepowermanagement.

IEEETrans.Comput.2013,64,260–273.[CrossRef]

32. Penland,C.AstochasticmodelofIndoPacificseasurfacetemperatureanomalies.Phys.DNonlinearPhenom.1996,98,534–558.

[CrossRef]

33. Tseng,Y.;Hu,Z.Z.;Ding,R.AnENSOpredictionapproachbasedonoceanconditionsandocean-atmospherecoupling.Clim.

Dyn.2017,48,2025–2044.[CrossRef]

34. Xue,Y.;Leetmaa,A.;Ji,M.ENSOpredictionwithMarkovmodels:Theimpactofsealevel.J.Clim.2000,13,849–871.[CrossRef]

35. Kondrashov,D.;Kravtsov,S.;Robertson,A.W.Ahierarchyofdata-basedENSOmodels.J.Clim.2005,18,4425–4444.[CrossRef]

36. Tangang,F.T.;Tang,B.;Monahan,A.H.ForecastingENSOevents:Aneuralnetwork-extendedEOFapproach.J.Clim.1998,11,

29–41.[CrossRef]

37. Jiang,G.R.;Zhang,R.;Sha,Y.W.ResearchonENSOpredictionusingEOFunfoldingandartificialneuralnetworkmethods.Mar.

Forecast.2001,18,1–11.

38. Aguilar-Martinez,S.;Hsieh,W.W.ForecastsoftropicalPacificseasurfacetemperaturesbyneuralnetworksandsupportvector

regression.Int.J.Oceanogr.2009,2009,167239.[CrossRef]

39. Liu,K.F.;Zhang,J.;Chen,Y.D.ENSOpredictionexperimentbasedonwaveletdecompositionandsupportvectormachine.J.PLA

Univ.Sci.Technol.Nat.Sci.Ed.2011,12,531–535.

40. Feng,Q.Y.;Vasile,R.;Segond,M.ClimateLearn:Amachine-learningapproachforclimatepredictionusingnetworkmeasures.

Geosci.ModelDev.Discuss.2016,10,1–18.

41. Zheng,F.;Zhu,J.Improvedensemble-meanforecastingofENSOeventsbyazero-meanstochasticerrormodelofanintermediate

coupledmodel.Clim.Dyn.2016,47,3901–3915.[CrossRef]

42. Nooteboom,P.D.;Feng,Q.Y.;López,C.UsingnetworktheoryandmachinelearningtopredictElNiño.EarthSyst.Dyn.2018,9,

969–983.[CrossRef]

43. Rumelhart,D.E.;Hinton,G.E.;Williams,R.J.Learningrepresentationsbyback-propagatingerrors.Nature1986,323,533–536.

[CrossRef]

44. Baawain,M.S.;Nour,M.H.;El-Din,M.G.G.ApplyingartificialneuralnetworkmodelsforENSOpredictionusingSOIandNino3

asonsetindicators.InProceedingsoftheCanadianSocietyforCivilEngineering-31stAnnualConference,2003Buildingour

Civilization,Moncton,NB,Canada,4–7June2003;pp.858–867.

45. Shukla,R.P.;Tripathi,K.C.;Pandey,A.C.PredictionofIndiansummermonsoonrainfallusingNiñoindices:Aneuralnetwork

approach.Atmos.Res.2011,102,99–109.[CrossRef]

46. Mekanik,F.;Imteaz,M.A.ForecastingVictorianspringrainfallusingENSOandIOD:Acomparisonoflinearmultipleregression

andnonlinearANN.InProceedingsoftheInternationalConferenceonUncertaintyReasoningandKnowledgeEngineering,

Jalarta,Indonesia,14–15August2012;pp.86–89.

47. Petersik, P.J.; Dijkstra, H.A.ProbabilisticforecastingofElNiñousingneuralnetworkmodels. Geophys. Res. Lett. 2020,

47,e2019GL086423.[CrossRef]

48. LeCun,Y.;Bottou,L.;Bengio,Y.Gradient-basedlearningappliedtodocumentrecognition. Proc. IEEE1998,86,2278–2324.

[CrossRef]

49. Krizhevsky,A.;Sutskever,I.;Hinton,G.E.ImageNetclassificationwithdeepconvolutionalneuralnetworks.Adv.NeuralInf.

ProcessingSyst.2012,1,1097–1105.[CrossRef]

50. Simonyan,K.;Zisserman,A.Verydeepconvolutionalnetworksforlarge-scaleimagerecognition.arXiv2014,arXiv:1409.1556.

51. Ham,Y.G.;Kim,J.H.;Luo,J.J.Deeplearningformulti-yearENSOforecasts.Nature2019,573,568–572.[CrossRef]

52. Yan,J.;Mu,L.;Wang,L.TemporalconvolutionalnetworksfortheadvancepredictionofENSO.Sci.Rep.2020,10,8055.[CrossRef]

53. Hu,J.;Weng,B.;Huang,T.;Gao,J.;Ye,F.;You,L.Deepresidualconvolutionalneuralnetworkcombiningdropoutandtransfer

learningforENSOforecasting.Geophys.Res.Lett.2021,48,e2021GL093531.[CrossRef]

54. Zhao,J.;Luo,H.;Sang,W.;Sun,K.SpatiotemporalsemanticnetworkforENSOforecastingoverlongtimehorizon.Appl.Intell.

2022,1–17.[CrossRef]

55. Hopfield,J.J.Neuralnetworksandphysicalsystemswithemergentcollectivecomputationalabilities.Proc.Natl.Acad.Sci.USA

1982,79,2554–2558.[CrossRef][PubMed]

56. Graves,A.;Jaitly,N.Towardsend-to-endspeechrecognitionwithrecurrentneuralnetworks.InProceedingsoftheInternational

ConferenceonMachineLearning,JMLR,Beijing,China,21–26June2014;pp.1764–1772.

57. Mikolov,T.;Karafiát,M.;Burget,L.Recurrentneuralnetworkbasedlanguagemodel.Interspeech2010,2,1045–1048.

58. Cho,K.;VanMerriënboer,B.;Gulcehre,C.LearningphraserepresentationsusingRNNencoder-decoderforstatisticalmachine

translation.arXiv2014,arXiv:1406.1078.

59. Hochreiter,S.;Schmidhuber,J.Longshort-termmemory.NeuralComput.1997,9,1735–1780.[CrossRef]

60. Zhang,Q.;Wang,H.;Dong,J.Predictionofseasurfacetemperatureusinglongshort-termmemory.IEEEGeosci.RemoteSens.Lett.

2017,14,1745–1749.[CrossRef]

37

Mathematics2022,10,3793

61. Broni-Bedaiko,C.;Katsriku,F.A.;Unemi,T.ElNiño-SouthernOscillationforecastingusingcomplexnetworksanalysisofLSTM

neuralnetworks.Artif.LifeRobot.2019,24,445–451.[CrossRef]

62. Pei,Z.;Yingjie,H.;Bingyi,H.SpringpredictabilitybarrierphenomenoninENSOpredictionmodelbasedonLSTMdeeplearning

algorithm.BeijingDaXueBao2021,57,1071–1078.

63. Shi,X.;Chen,Z.;Wang,H.ConvolutionalLSTMnetwork:Amachinelearningapproachforprecipitationnowcasting.Adv.Neural

Inf.Process.Syst.2015,28,802–810.

64. He,D.;Lin,P.;Liu,H.Dlenso:AdeeplearningENSOforecastingmodel.InProceedingsofthePacificRimInternationalConference

onArtificialIntelligence;Springer:Cham,Switzerland,2019;pp.12–23.

65. Mu,B.;Peng,C.;Yuan,S.;Chen,L.ENSOforecastingovermultipletimehorizonsusingConvLSTMnetworkandrolling

mechanism. InProceedingsoftheInternationalJointConferenceonNeuralNetworks,Budapest,Hungary,14–19July2019;

pp.1–8.

66. Geng,H.;Wang,T.SpatiotemporalmodelbasedondeeplearningforENSOforecasts.Atmosphere2021,12,810.[CrossRef]

67. Zhou,L.;Zhang,R.H.AhybridneuralnetworkmodelforENSOpredictionincombinationwithprincipaloscillationpattern

analyses.Adv.Atmos.Sci.2022,39,889–902.[CrossRef]

68. Scarselli,F.;Gori,M.;Tsoi,A.C.Thegraphneuralnetworkmodel.IEEETrans.NeuralNetw.2008,20,61–80.[CrossRef][PubMed]

69. Kipf,T.N.;Welling,M.Semi-supervisedclassificationwithgraphconvolutionalnetworks.arXiv2016,arXiv:1609.02907.

70. Cachay,S.R.;Erickson,E.;Bucker,A.F.C.TheWorldasaGraph:ImprovingElNi\~noForecastswithGraphNeuralNetworks.

arXiv2021,arXiv:2104.05089.

71. Mu,B.;Qin,B.;Yuan,S.ENSO-ASC1.0.0:ENSOdeeplearningforecastmodelwithamultivariateair-seacoupler.Geosci.Model

Dev.2021,14,6977–6999.[CrossRef]

38

mathematics

Article

Performance Analysis of Feature Subset Selection Techniques

for Intrusion Detection

YousefAlmaghthawi,IftikharAhmad*andFawazE.Alsaadi

FacultyofComputingandInformationTechnology,KingAbdulazizUniversity,Jeddah21589,SaudiArabia

* Correspondence:iakhan@kau.edu.sa

Abstract:Anintrusiondetectionsystemisoneofthemaindefenselinesusedtoprovidesecurityto

data,information,andcomputernetworks.Theproblemsofthissecuritysystemaretheincreased

processingtime,highfalsealarmrate,andlowdetectionratethatoccurduetothelargeamountof

datacontainingvariousirrelevantandredundantfeatures. Therefore,featureselectioncansolve

thisproblembyreducingthenumberoffeatures.Choosingappropriatefeatureselectionmethods

thatcanreducethenumberoffeatureswithoutanegativeeffectontheclassificationaccuracyisa

majorchallenge. Thischallengemotivatedustoinvestigatetheapplicationofdifferentwrapper

featureselectiontechniquesinintrusiondetection.Theperformanceoftheselectedtechniques,such

asthegeneticalgorithm(GA),sequentialforwardselection(SFS),andsequentialbackwardselection

(SBS),wereanalyzed,addressed,andcomparedtotheexistingtechniques.Theefficiencyofthethree

featureselectiontechniqueswithtwoclassificationmethods,includingsupportvectormachine(SVM)

andmultiperceptron(MLP),wascompared. TheCICIDS2017,CSE-CIC-IDS218,andNSL-KDD

datasetswereconsideredfortheexperiments.Theefficiencyoftheproposedmodelswasprovedin

theexperimentalresults,whichindicatedthatithadhighestaccuracyintheselecteddatasets.

Keywords:intrusiondetection;geneticalgorithm;greedysearch;backwardeliminationlearning;

NSL-KDD;CIC-IDS-2017;CIC-IDS2018

Citation:Almaghthawi,Y.;Ahmad,

MSC:68M25

I.;Alsaadi,F.E.PerformanceAnalysis

ofFeatureSubsetSelection

TechniquesforIntrusionDetection.

Mathematics2022,10,4745. https://

1.Introduction

doi.org/10.3390/math10244745

Currently,theinternetisnecessaryforstoringandtransferringthediverseinformation

AcademicEditor:WeiFang ofusers,companies,andgovernments.Protectingandsecuringsystemsandinformationis

necessary.Oneofthemostefficientexistingsystemsusedtosecuresystemsandcontrol

Received:30October2022

Accepted:6December2022 intrusionactivitiesistheintrusiondetectionsystem(IDS).Inrecentyears,severalIDSshave

Published:14December2022 beenproposed. Thesesecuritysystemshavemanyproblemssuchasanincreasingpro-

cessingtime,highfalsepositiverate(FPR),andlowdetectionrate(DR),whicharecaused

Publisher’sNote:MDPIstaysneutral

bythelargeamountofdatacontainingvariousirrelevantandredundantfeatures[1,2].

withregardtojurisdictionalclaimsin

Featureselection(FS)cansolvetheseproblemsbyreducingthenumberoffeaturesand

publishedmapsandinstitutionalaffil-

selectingonlyusefulfeatures.Severalfeatureselectionmethodsareavailable,butthetask

iations.

offindingwhichoneissuitableforIDSthatprovidestheminimumnumberoffeatures

withthemaximumaccuracyisamajorchallenge[2,3]. Thischallengemotivatedusto

investigatetheapplicationofdifferentFStechniquesinintrusiondetection. Theperfor-

Copyright: © 2022 by the authors. manceoftheselectedtechniques,suchastheGA[4],SFS[5],andSBS[3]wereanalyzed,

Licensee MDPI, Basel, Switzerland. addressed,andcomparedwithexistingtechniques.ThisstudyusedtherecentCICIDS2017

Thisarticleisanopenaccessarticle andCSE-CIC-IDS218[6]datasetsaswellastheNSL-KDD[7]dataset.

distributed under the terms and

conditionsoftheCreativeCommons 1.1.IntrusionDetectionSystem

Attribution(CCBY)license(https:// IDSisasoftwareorhardwarethatmonitorsactivitiesinsideandoutsidethenetwork

creativecommons.org/licenses/by/ todetectabnormalones[3]. Itisoneofthemostimportantmechanismsthatprotect

4.0/).

Mathematics2022,10,4745.https://doi.org/10.3390/math10244745 https://www.mdpi.com/journal/mathematics

39

Mathematics2022,10,4745

systemsandnetworksagainstmaliciousactivities[6,8].Thissystemgeneratesalarmsif

anyabnormalpatternisrecognized.IDSshavetwotypes:host-basedIDS,whichfocuses

onindividualcomputers,andnetwork-basedIDS,whichfocusesonthetrafficbetween

computers. Basedonthedetectionmethod, IDScanbeclassifiedintotwocategories,

namelysignature-basedandanomaly-baseddetection[1,9].

1.1.1.Signature-BasedDetection

Thisdetectionmethodisalsoknownasmisusedetection.Itusestheattacksignature

databasetoidentifyintrusionsorabnormalactivities.Whenapacketsignaturematches

withasignatureinthedatabase,IDSsdetectthatpacketasanintrusion. Thisdetection

typecandetectknownattacksonly[1].

1.1.2.Anomaly-BasedDetection

Inthisdetectiontype,IDSsbuildprofilesofthenormalnetworkpackets.Theythen

analyzeandmonitorthenetworkpackets.Whenthereisanydeviationfromthenormal

profile, IDSs detect the abnormal activity. This detection type can detect known and

unknownattacks[1].

1.2.FeatureSelectionMethods

Feature selection methods select the relevant and useful features from a dataset.

ThegoalofFStechniquesistoincreasetheaccuracyanddetectionrateanddecreasethe

executiontimeandfalsepositiverate.Toachievethisgoal,FSmeasurestheimportanceof

featuresandonlyallowsthemostimportantfeaturestoentertheclassification.Thenumber

offeaturesisthenreducedaswellastheclassificationtime. TherearetwotypesofFS

methodsbasedonevaluationcriteria[8,10].Thefirsttypeisthefiltermethod,whichitis

independentoftheclassifier.Itanalyzeseachsinglefeatureanddecideswhichfeaturesare

usefulandshouldbetrainedbasedonstatisticalmeasures[8,11,12].Thesecondtypeisthe

wrappermethod,whichisdependentontheclassifier.Incontrasttofiltermethods,wrapper

methodsusemachinelearningalgorithmstodeterminethebestfeaturesubsettoprovidea

highclassificationperformance[8,10–12].ThefilterandwrapperFSmethodsarebasedon

twocomponents:asearchstrategy(e.g.,GA,SFS,andSBS)andanobjectivefunctionor

fitnessfunction(e.g.,classifierperformanceinwrappermethodsandstatisticalmeasure

infiltermethods). Thesearchstrategydeterminestheoptimalsubsetoffeaturesthat

providehighaccuracyandlowfalsealarmsresultsbasedontheclassifier’sperformance(in

wrappermethods)orstatisticalmeasuressuchasinformationgain(infiltermethods)[13].

Thesearchstrategycanbemadeupofexhaustive,heuristic,andrandomsearches[14].

Exhaustivesearchesaretimeconsumingandimpracticalbecauseofthelargenumber

ofcombinationstoevaluate.

Forexample,asearchofan2n−1

possiblefeaturesubsets

innfeaturesdatasetbecomesanNP-hardproblemasthenumberoffeaturesgrow[13].

Heuristicsearchessuchastheforwardsequentialsearchandfuzzysystemsandrandom

searchessuchastheGAperformbetterinlargedatasets[15–17].

Filterselectionmethodsarefasterandhavealowerlevelofcomplexitythanwrapper

methods,butthelatteraremoreaccurate[18]. Therefore,weusedwrappermethodsin

ourstudytobuildanefficientIDSmodelthatprovidesalowFPRandhighACCwiththe

minimumnumberoffeatures.

SeveralfeaturesselectionmethodsareavailablesuchastheGA,SBS,andSFS,butthe

problemistofindwhichoneismoresuitableforanintrusiondetectionsystem(IDS)that

providesaminimumnumberoffeatureswithmaximumaccuracy[2,3].

1.2.1.SequentialForwardSelection(SFS)andSequentialBackwardSelection(SBS)

SFSandSBSaresimplesearchtechniquesthatruniniterationsandmakeagreedy

decisiontoselectthebestlocalsolutionineachiterationbasedontheobjectivefunction.

TheSFSalgorithmstartswithanemptysetandaddsonefeaturetothesubsetateach

iterationuntilastoppingcriterionismetsuchasthesearchiscompletedorthedesired

40

Mathematics2022,10,4745

numberofsubsetfeaturesisreached.Afterthat,itreturnsthelocaloptimalsolutionamong

iterationsorthesolutioninthedesirednumberofsubsetfeatures.Figure1ashowsanSFS

methodologyinwhichadatasethasthreefeatures: F1,F2,andF3. Inthefirstiteration,

SFSgeneratesandevaluatesseveralsubsetsthatcontainonlyonefeaturefromthecomplete

setoffeatures.Thefeaturethathasthemaximumobjectivefunctionisselectedasalocal

optimalsolutioninthisiteration.Intheseconditeration,italsogeneratesandevaluates

severalsubsets,inwhichonefeatureisaddedtotheselectedfeaturefromtheprevious

iteration.Subsequently,eachsubsetisevaluatedtoselectthebestlocaloptimalsolution.

Inthethirditeration,afeatureisaddedtotheselectedfeaturesfromthepreviousiteration;

inthiscase,thecompletesetoffeaturesisevaluated.Finally,itreturnsthebestlocaloptimal

solutionamongtheseiterationsastheoutput.Bycontrast,theSBSalgorithmstartsfroma

completesetoffeaturesanditerativelyremovesonefeatureuntilastoppingcriterionis

met. Afterthat,itreturnsthelocaloptimalsolutionamongiterationsorthesolutionin

thedesirednumberofsubsetfeatures.Figure1bshowsanSBSmethodologyinwhicha

datasethasthreefeatures:F1,F2andF3.

(a) (b)

Figure1.(a)AnexampleofSFS;(b)anexampleofSBS.

1.2.2.GeneticAlgorithm

TheGAisametaheuristicsearchandworkalgorithmbasedonadirectDarwinian

naturalselectionanalogyandgeneticsinbiologicalsystems[12,13].Itiscomposedoffour

components: apopulationofindividuals,afitnessfunction,aselectionfunction,anda

geneticoperator(e.g.,crossoverandmutations).TheGArandomlygeneratesapopulation

ofindividualsorchromosomesinwhicheachchromosomerepresentsasolutiontothe

problem[12,13].Thefitnessfunctiondeterminesthechromosome’schanceofbeingchosen

tocreatetheoffspringorthenextgenerationindividuals.Theselectionfunctionselectsthe

parentsoftheoffspringfromthecurrentgeneration,andthenthecrossoverandmutation

areappliedtotheselectedparentstogeneratetheoffspringorthenextgenerationof

individuals. Severalselectionfunctionsareavailable,suchasthetournamentselection

method,roulettewheel,andrankselection[13].Crossoverandmutationoperatorsarethen

appliedtotheselectedindividualsorchromosomestocreateoffspringorthegeneration

ofnewindividuals.Crossoveristheexchangeofindividualbitsbetweentworandomly

selectedparents.Mutationisthealterationofindividualbitstogeneratenewindividuals.

Newanddifferentindividualsaregeneratedfromthecurrentgenerationafterapplying

crossoverandmutationoperators. Theevaluationofindividuals, selection, crossover,

andmutationarerepeatedinapredefinednumberofgenerationsuntilastoppingcriterion

ismet.

2.RelatedWork

Sarvarietal.[19]usedthewrappercuckoosearchalgorithm(CSA)asanFStechnique

tobuildanefficientIDSmodel.TheyappliedtheFSmethodandtrainedanartificialneural

network(ANN)usingamultiverseoptimizer(MVO).Theproposedmodel,calledMCF&

41

Mathematics2022,10,4745

MVO-ANN,wasevaluatedusingtheNSL-KDDdataset.Asaresult,theirmodelachieved

ahighACC(98.16%),ahighDR(96.83%),andalowFPR(0.03%).

Salehetal.[8]presentedanIDSapproachbasedonthewrapperNBFStechniqueto

selectthebestfeaturesubsets.Theproposedmodelcombinesoptimizedsupportvector

machines(OSVMs)andprioritizedk-nearestneighbors(PKNN)techniques. Theyused

OSVMforrejectingoutliersandPKNNtodetectattacks.Theexperimentalresultsindicate

thatNBFSachievesahigherDR(approximately90.28%)thanothertechniquesusingan

NBclassifierwith18selectedfeatures.TheproposedmodelalsogivesahigherDR(95.77%

usingtheNSL-KDDdatasetand93.28%usingKDDCup99)thanothertechniques.

Atesetal.[5]usedthegreedysearch(GS)algorithmandSVMtodetectdistributed

denialofservice(DDoS)attacks.TheyusedGSforFSandSVMasaclassifier.Theproposed

modelcalculatesthedistancesbetweentheprobabilitydistributionsofheaderinforma-

tionusingtheGSalgorithmandKullback–Leiblerdivergence.Inthetestingphase,they

usedadatasetcollectedfromtheMITDarpa2000datasetandauniversitynetworkand

achievedahighACof99.99%andalowFPRof0.001%fortheMITDarpa200dataset.

However,theproposedmodelneedstobeevaluatedusingastandarddatasettocompare

itsperformanceresultswithrecentmodels.

Asdaghietal.[20]proposedanewbackwardelimination(BE)methodcalledSmart-BT

forwebspamdetection. Theyusedindexofbalanceaccuracyvaluesasaperformance

metric.Theproposedmodelusesthechi-squareasapre-processingprocess.Afterward,

Smart-BTselectstherelevantandusefulfeaturesbyeliminatingasetoffeaturesfrom

theinitialset.TheexperimentalresultsshowthattheSmart-BTgivesbetterclassification

resultsthanotherexistingFStechniquessuchastherankersearchalgorithmandparticle

swarmoptimization(PSO)techniques.

Taoetal.[4]introducedanFStechniquebasedontheGAandSVMtoimprovetheIDS.

TheypresentedanewfitnessfunctionforthechosenFSmethodtodeterminetheoptimal

featuresubset.Theexperimentalresultsindicatethattheirmodelsucceedsinminimizing

thenumberoffeaturesto19featuresandachievesahighDRandlowFPRusingtheKDD

Cup99dataset.However,thedeterminationoftheweightvaluesfortheTPRandselected

featurenumberiscarriedoutmanually.

ThakkarandLohiya[3]presentedaperformanceanalysisofFStechniquesinIDSs.

Chi-square,IG,andrecursivefeatureelimination(REF)wereimplementedseparatelyasFSs

withseveralMLclassifierssuchasSVMandANN.Fordeterminingthebestcombination

performanceintermsofFStechniqueandmachinelearningclassifierusingtheNSL-KDD

dataset,theyconductedseveralexperimentsandreportedthatthecombinationofSVMand

REFperformswellcomparedwithothertechniques.TheaverageACC,precision,recall,

andF-scorerateswere98.95%,99.2%,99.75%,and98.40%,respectively,fortheSVM-REF

model.

GSuseendranandT.Nathiya[10]presentedaGSFSmethodtoincreasetheaccuracy

anddecreasethefalsealarmrateinIDSs.Theyusedcorrelationfeatureselection(CFS)to

evaluatetheselectedfeaturesubsets.TheRFclassifierisusedintheirmodel.Theexperi-

mentsshowedthattheirmodelachieves98.32%intermsofACCand0.40%intermsofthe

falsealarmrateusingtheNSL-KDDdataset.

Aslahietal.[21]usedtheGAforFSandSVMasaclassifierforbuildinganewIDS

model. Theirmodelreducestheamountoffeaturesto10featuresfromtheoriginal41

features.TheKDDdatasetwasusedintheirexperiments.Theirmodelachieves97.30%in

termsofaccuracyand1.70%intermsoffalsealarmrate.

J. Lee et al. [22] proposed a sequential forward floating search (SFFS) method to

increasetheACCanddecreasethefalsealarmrateinIDSs. TheyusedaSFFStoselect

theoptimalfeaturesetandRFclassifierfortheevaluation. TheNSL-KDDdatasetwas

usedintheexperimentsfortheproposedmodel.Theexperimentsprovedthattheirmodel

achievesa0.40%falsealarmrateand99.89%ACCwith10selectedfeatures.

Lietal.[15]proposedamodifiedrandommutationhillclimbing(MRMHC)method

asawrapperFStechnique.TheyusedamodifiedlinearSVMasanevaluationcriterion.

42

Mathematics2022,10,4745

MRMHCgeneratesaninitialsubsetfromthecompletesetoffeatures.Then,theMLSVM

evaluatestheselectedsubsetandselectthebestsubset.TheirexperimentsontheKDDCup

datasetshowedthattheirapproachhasahighACCandlowdetectiontime.

LiYetal.[23]usedagradualfeatureremovalmethodtoselecttheimportantfeatures

inIDSs.Thismethoddeletesthelessimportantfeaturesgradually.TheyusedSVMclassifier

asanobjectivefunctionintheirproposedmodel.Theirmodelselected19featuresfromthe

KDDCupdataset,whichwasusedintheexperiments. TheresultsobtainedanACCof

98.62%.

Ramanetal.[24]proposedahypergraph-basedGA(HG-GA)tobuildanadaptive

IDSwithahighACCandlowfalsealarmrate. HG-GAisusedforFSintheirproposed

model,andSVMisusedforclassification.Intheirexperiments,theyusedtheNSL-KDD

dataset.TheproposedmodelachievesanACCof97.14%andafalsealarmrateof0.83%.

KhammassiandKrichen[13]usedtheGAforFSandlinearregressionasaclassifi-

cationalgorithm.Thiswrapperapproachselectstheimportantfeaturesfromtheoriginal

datasets(KDD99andUNSW-NB15).Then,theDTclassifierusestheselectedfeaturesto

measuretheefficiencyoftheselectedfeatures.Anaccuracyof99.90%andfalsealarmrate

of0.11%wereobtainedintheirexperimentsfortheKDD99datasetwith18features.

ZhouandCheng[25]developedanIDSmodelbasedoncorrelation-basedFS(CSF)

andthebatalgorithm(BA).TheycombinedRF,C4.5,andforestattributestobuildan

ensembleapproach.TheproposedmodelwasevaluatedusingseveralIDSdatasetssuch

astheCICIDS2017andNSL-KDDdatasets. Theirmodelobtains94.04%intermsofthe

detectionrate,2.38%intermsoftheFPRand96.76%intermsofACC.

Hua Y. [26] developed a hybrid filter and wrapper FS method based on IG and

LightGBM.Anunder-samplingtechniquewasusedtobalancetheusedCICIDS2017dataset.

TheproposedmodelachievesanACCof98.37%,aprecisionof98.17%,andarecallof

98.37%with10selectedfeatures.

SugandhSethetal.[27]usedrandomforest(RF)andprincipalcomponentanalysis

(PCA)asahybridfeatureselectionmethod.Alightgradientboostingmachine(LightGBM)

classifierwasusedtoclassifytheinstancesoftheCIC-IDS-2018dataset.Theauthorsused

anunder-samplingtechniquetobalancethedataset.Theirmodelachieves97.73%interms

ofaccuracyanda97.57%F1-Scorewith24selectedfeatures.

Alazzametal.[28]usedthepigeoninspiredoptimizer(PIO)technique.Theydesigned

twomodelsofthePOIsuchasthesigmoidPIOandbinarycosinePIOtodeterminethe

optimalnumberoffeatures.InthebinaryPIO,thecalculationofthevelocityofpigeons

isbasedonthecosinesimilarity. Theirmodelswereevaluatedusingthedecisiontree

(DT)technique.Throughexperiments,themodelswereevaluatedusingtheUNSW-NB15,

NSL-KDD,andKDDCUP99datasets.Theresultindicatethattheproposedmodel(cosine

PIO)outperformsseveralproposedFSalgorithmsintermsofAC,F-score,FPR,andTPR.

Mazinietal.[29]usedthewrapperartificialbeecolony(ABC)algorithmforFStobuild

anefficientanomalyIDS.TheAdaBoostclassifierisusedforevaluationandclassification.

Throughsimulation, themodelwasevaluatedusingtheISCXIDS2012andNSL-KDD

datasets.Asaresult,theproposedmodelachievesahighDR(99.61%),lowFPR(0.01%),

andhighACC(98.90%).However,theparametersettingsforFSaredeterminedmanually.

AweenSaeedandNoorJameel[30]usedtheparticleswarmoptimizationalgorithm

withadecisiontree(DT)tobuildawrapperfeatureselectionmodelforIDS.Theauthors

trainedandtestedtheirmodelusingaDTclassifier.Theirmodelselected19featuresfrom

theCIC-IDS-2018dataset,whichwasusedintheexperiments. Theresultsobtainedan

ACCof99.52%.

JahedShaikhandDeepakKshirsagar[31]usedinformationgain(IG)andacorrelation

attributeevaluationasafeatureselectionmethodtoselecttheoptimalnumberoffeatures

fromtheCIS-IDS-2017dataset.APARTrule-basedmachinelearningclassifierwasusedto

evaluatetheproposedmodel.Anaccuracyof99.98%andfalsealarmrateof1.35%were

obtainedintheirexperimentswith56features.

43

Mathematics2022,10,4745

PatilandKshirsagar[32]presentedanIDSmodelbasedoninformationgain(IG)and

rankermethodasafeatureselectionmethod.TheJ48classifierwasusedtoevaluatethe

selectedfeatures.Theirmodelselected75featuresfromtheCIC-IDS-2017dataset,which

wasusedintheexperiments.TheresultsobtainedanACCof87.44%.

ManyoftheaboveFStechniqueshavenotbeenevaluatedonhigh-dimensiondatasets

suchasCICI-IDS-2017andCSE-CIC-IDS-2018,whichcontainmorefeatures(80features)

comparedwithKDDCup99andNSL-KDD,whichcontain41features[17]. Inaddition,

certainresearchersdidnotmentiontheobtainednumberofselectedfeatures,whichaffects

theexecutiontimeintermsofclassification[2]. Moreover,BE,GA,andGStechniques

achievedhighresultsinpreviousworks[3–5,31].Hence,thepresentstudyinvestigated

theseFStechniquesusingseveralstandarddatasetstodeterminethemostappropriate

techniquethatprovidestheminimumnumberofrelevantfeatureswithmaximumaccuracy.

AsummaryoftheliteraturereviewisshowninTable1.

Table1.Summaryoftheliteraturereview.

FeatureSelection Classification Numberof

Ref. Dataset Result(%)

Algorithm Algorithm Features

ACC:98.95

[3] REF SVM NSL-KDD -

F-score:99.75

[4] GA SVM KDDCup99 19

ACC:99.99

[5] GreedySearch SVM MITDarpa2000 -

FPR:0.001

[8] NBFS PKNN+OSVMs NSL-KDD - DR:95.77

ACC:98.32

[10] GreedySearch+CFS RF NSL-KDD -

FPR:0.40

ACC:99.90

[13] GA DT KDD99 18

FPR:0.11

TPR:80.00

[15] MRMHC MLSVM KDDCup 4

FPR:3.65

ACC:98.81

[19] CSA MCF&MVO-ANN NSL-KDD 22 DR:97.25

FPR:0.03

ACC:97.30

[21] GA SVM KDDCup 10

FPR:1.70

ACC:99.89

[22] SFFS RF NSL-KDD 10

FPR:0.40

[23] Gradualfeatureremoval SVM KDDCup 19 ACC:98.62

ACC:97.14

[24] HG-GA SVM NSL-KDD -

FPR:0.83

ACC:96.76

RF+C4.5+FOREST NSL-KDD

[25] CSF+BA - DR:94.04

ATTRIBUTE CICIDS2017

FPR:2.38

[26] IG LightGBM CICIDS2017 10 ACC:98.37

HybridFeature

[27] Selection LightGBM CICIDS2018 24 ACC:97.73

(RF+PCA)

ACC:86.90

[28] SigmoidPOI DT NSL-KDD 18

FPR:6.40

ACC:86.90

[28] CosinePOI DT NSL-KDD 5

FPR:8.80

44

Mathematics2022,10,4745

Table1.Cont.

FeatureSelection Classification Numberof

Ref. Dataset Result(%)

Algorithm Algorithm Features

ACC:98.90

[29] ABC AdaBoost NSL-KDD 25

FPR:0.01

Binary-particleswarm

[30] Decisiontree CICIDS2018 19 ACC:99.52

optimization

IGandcorrelation

ACC:99.98

[31] attributeevaluation PART CICIDS2017 56

FPR:1.35

methods

Informationgainand

[32] J48 CICIDS2017 75 ACC:87.44

rankeralgorithm

3.Methodology

Figure2showsthemethodologywhichincludes:databaseselection,pre-processing,

featureselection,classification,evaluation,aswellastheanalysisandcomparisonofresults

steps.Wewillexplainthesestepsinthefollowingsubsections.

Figure2.Themethodology.

3.1.DatasetSelection

Newcybersecuritydatasetsareavailable,sothisworkusedthreedifferentdatasets,

namelyNSL-KDD,CIC-IDS-2017,andCIC-IDS-2018,fortheexperiments. Allofthese

datasetswereexploredtodeterminewhichwasthemostsuitabledatasetforbuildingan

efficientIDS.

3.1.1.NSL-KDD

TheNSL-KDDdatasetisoneofthemostwidelyusedbenchmarksforIDSs[8,19,28].

ItisanupgradedversionoftheoldKDDCup99dataset[7].Ithasfourattackcategories:

usertorootattack(U2R),denialofserviceattack(DoS),probingattack,andremotetolocal

attack(R2L).ThefullNSL-KDDtrainingdatasetcontains125,973records,whereasthefull

45

Mathematics2022,10,4745

NSL-KDDtestingdatasetcontains22,254records.Thereare41featuresintheNSL-KDD

dataset:threeofthemarenominalorsymbolicfeatures,andtherestarenumericfeatures.

3.1.2.CIC-IDS-2017

TheCIC-IDS-2017datasetisanetworktrafficdatasetthatconsistsofbothnormaland

avarietyofattackdatadevelopedbytheFacultyofComputerScience,UniversityofNew

BrunswickandtheCanadianInstituteofCybersecurity(CIC)in2017. Thisdatasetwas

capturedoveradurationoffivedays,anditusesalargevarietyofattacktypes[25,33,34].

IntheCIC2017dataset,theattacksimulationisdividedintosevencategoriesnamely,

botnet,bruteforceattack,DoSattack,DdoSattack,infiltrationattack,webattack,andheart

bleedattack[25,34].Thisdatasetcontainsover2.5millionrecordsand78features,including

thelabelcolumn,and19.70%ofCIC-IDS-2017isattacktraffic. Thedatasethasaclass

imbalance.Anunequaldistributionbetweenmajorityandminorityclassesindatabasesis

knownasclassimbalance,whichaffectstheperformanceofclassification[34].

3.1.3.CIC-IDS-2018

TheCIC-IDS-2018datasetisanetworktrafficdatasetconsistingofbothnormalanda

varietyofattackdatadevelopedbytheFacultyofComputerScience,UniversityofNew

Brunswick,theCIC,andtheCommunicationsSecurityEstablishment(CSE)in2018[6].

The structure of this dataset is similar to the previous dataset, and both have a class

imbalance. Roughly 17% of the total number of records, which is 16,233,002 records,

isattacktraffic.

3.2.Preprocessing

Thedatasetsmustbepreprocessedtoavoidinconsistent,irrelevant,andmissingdata

thataffecttheperformanceoftheIDS.Thisstepmayincludeseveraltaskssuchasremoving

nullormissingvalues,resampling,andscaling.

Certaindatasetshavemissing,null,orsymbolicvalues.Thesetypesofdatastructures

maketheclassificationalgorithmsdifficulttohandle. Therefore,missingvaluesornull

valuesareremoved, andsymbolicvaluesaremappedtonumericvalues. Duplicated

recordsandfeaturesshouldberemovedtopreventtheclassifiersfrombeingbiasedtothe

mostfrequentrecords[28]. CertainmachinelearningclassifierssuchasSVMandMLP

aresensitivetofeaturescalingandrequirethescalingofadatasetbecausetheseclassifiers

provideweightstotheinputfeaturesaccordingtotheirdatapointsandinferencesfor

output.Therefore,scalingalltheuseddatasetsbeforetheFS,training,andtestingphasesis

highlyrecommended.

ThehighlyunbalanceddatasetsintheCIC-IDS-2017andCIC-IDS-2018datasetsaffect

theperformanceoftheclassifier. Therandomunder-sampling(RUS)techniqueisused

tobalancetheclassdistribution.TheRUStechnique,inwhichspecificmajorityinstances

areremovedtobalanceadataset,providesagoodresultcomparedwithothersampling

methodsinthecontextoftheCIC-IDS-2017dataset[35].

3.3.FeatureSubsetSelection

ThisworkfocusedonFStechniquesandconsidereddifferentwrapperFStechniques

suchasSFS,SBS,andtheGA.DifferentmachinelearningtechniquessuchasMLPand

SVMwereappliedastheobjectivefunctionsforthechosenFStechniques.

NotallfeaturesoftheNSL-KDD,CIC-IDS-2017,andCIC-IDS-2018datasetsareimpor-

tanttobuildanefficientIDS.AsubsetofthesefeaturescanachievehighaACCandlow

FPR.Moreover,eliminatingcertainfeaturesusingFStechniquesisnecessarytobuildan

efficientIDSwithahighaccuracyandlowfalsealarms.Inthisstudy,theperformanceof

SFS,SBS,andGAFStechniqueswereexplored.WeusedthewrapperFSapproach.This

approachisbasedonthreecomponents:asearchstrategy,aclassifier,andanevaluation

function[13,14]. Weusedthreesearchstrategies(SFS,SBS,andtheGA).Ineachsearch

strategy,weusedSVMandMLPasclassifiers.Theevaluationofthefeaturesubsetswasa

46

Mathematics2022,10,4745

fitnessfunctionbasedonacustomscoreofthecross-validationofthepreviousclassifiers.

Cross-validationisaresamplingtechniquethatdividesthedatasetintoequaldifferent

portionstotrainandtestamodelondifferentiterations.Cross-validationgivesaninsight

onhowthemodelcanbegeneralizedtoanunknowndataset,anditisausefultechniqueto

identifytheoverfittingofamodel.IntheFSphase,two-fold,five-fold,andten-foldcross

validationareused.OurgoalinthisstudywastoproposeanFSmethodthatincreasesthe

ACCanddecreasesthefalsealarmratewiththeminimumnumberoffeatures.Therefore,

ourobjectivefunctionorfitnessfunctionwasbasedonthreecriteria: theclassification

accuracyofSVMorMLP,thefalsealarmrateorFPR,andthenumberofselectedfeatures.

Hence,thesubsethavingthesmallestnumberoffeatures,thehighestACC,andthelowest

FPRproducesthehighestobjectivefunction.

Severalobjectivefunctionsareavailable. Hence,weinvestigatedseveralobjective

functionsintheFSphase.Bamakanetal.[36]proposedanobjectivefunctionbasedonthe

detectionrate,thefalsealarmrateoftheclassifier,andthenumberofselectedfeatures,

asshowninEquation(1).HangandWang[37]proposedanobjectivefunctionbasedon

theaccuracyandthenumberofselectedfeatures,asshowninEquation(2).

ObjectiveFunction(X)=DR(X)∗WA+(1−FPR)∗WF+(1−N∗WN) (1)

ObjectiveFunction(X)=ACC(X)∗WA+(1−N∗WN) (2)

whereNisthenumberofselectedfeaturesinthesubset,WAisapredefinedweightforthe

accuracyscoreofthesubset,WFisapredefinedweightfortheFPRofthesubset,WDisa

predefinedweightfortheDRofthesubset,andWNisapredefinedweightforthenumber

ofselectedfeaturesinthesubset.Alltheweightsshouldbeinrange[0–1].

Inthefollowing,weexplaintheselectedFStechniquesinthisstudy,whichwerethe

SFS,SBS,andGAfeaturemethods.

3.3.1.SequentialForwardSelection(SFS)

SFSisawrapperFSthatselectskfeaturesfromaninitialdfeaturesdatasetwherek

<dthroughanumberofiterations. Itselectsthebestfeaturesubsetbystartingfroman

emptydatasetandaddingonefeatureatatimebasedontheclassifierperformanceinan

iterativeprocessuntilastoppingcriterionismet,suchasafeaturesubsetofthespecified

sizekbeingreached.Ifthedesirednumberoffeaturesisinarange(e.g.,1–40),SFSselects

thefeaturesubsetthatcontainsthehighestobjectivefunction(e.g.,accuracy)inthatrange.

SFSflowchartisshowninFigure3.

3.3.2.SequentialBackwardSelection(SBS)

Thismethodisessentiallythereverseoftheabovemethod.Itselectsthebestfeature

subsetbystartingfromtheoriginalfullfeaturedatasetandremovesonefeatureatatime

basedontheclassifierperformanceinaniterativeprocessuntilastoppingcriterionismet,

suchasafeaturesubsetofthespecifiedsizekbeingreached. Ifthedesirednumberof

featuresisinarange(e.g.,1–40),SBSselectsthefeaturesubsetthatcontainsthehighest

objectivefunction(e.g.,accuracy)inthatrange.SBSflowchartisshowninFigure4.

47

Mathematics2022,10,4745

Figure3.SFSflowchart.

Figure4.SBSflowchart.

3.3.3.GeneticAlgorithm(GA)

TheGAiscomposedoffivecomponents:theinitiationofthepopulation,afitnessfunc-

tion,aselectionfunction,geneticoperators(e.g.,crossoverandmutations),andstopping

criteria.Below,weexplaineachcomponentinaseparatesection.

PopulationInitiation

First,theGArandomlygeneratesapopulationofindividualsorchromosomesin

whicheachchromosomerepresentsasolutionfortheproblem[12,13].Eachchromosomeor

individualisencodedasbinary;afeatureiseitherincludedornotinthesubset.Thenum-

48

Mathematics2022,10,4745

berofindividualsorthepopulationsizeisdefinedbytheuser(n_population). Alarge

populationsizeprovidesalargesearchspacetotheGAbutitincreasestherequiredtimeto

evaluatealltheindividualsofthepopulation.Incontrast,asmallpopulationsizeprovides

asmallsearchspacetotheGAbuttherequiredtimetoevaluatealltheindividualsof

populationislessthaninthefirstsituation.

FitnessFunction

Thefitnessfunctiondeterminesthechromosome’schanceofbeingchosentocreate

theoffspringorthenextgeneration.Thefitnessfunctioncanbeanymetricoftheclassifier

performance,suchasaccuracy.Forexample,iftheclassifieraccuracyischosentobethe

fitnessfunction,thechromosomehavingthehighestaccuracyproducesthehighestfitness

value[13].

SelectionFunction

Theselectionfunctionselectstheparentsofoffspringorthenextgenerationofindivid-

ualsfromthecurrentgeneration.Inthisstudy,weusedthetournamentselectionmethod

thatselectsthebestindividualsfromapopulationofindividuals. Itrandomlyselectsa

predefinednumberofindividuals(tournament_size)andrunsatournamentamongthem.

Theindividualorchromosomewiththebestfitnessisthewinnerofthetournamentandit

isselectedforgeneratingthenextgeneration.Thetournamentselectionisrepeatedseveral

times,asspecifiedbytheuser.Thebestinduvialwiththehighestfitnessfunctionamong

otherindividualsineachgenerationisaddedtothepopulationofthenextgeneration.

Hence,eachgenerationintheGAhasanindividualthathasthehighestfitnessfunction

amongitspreviousgenerations.

CrossoverProcess

Thecrossoveroperatorisusedtogeneratenewoffspringorsolutionsfromthecurrent

solutions(theparents). Foreachtworandomlyselectedindividualsorchromosomes,

acrossoverisperformedwithapredefinedprobabilityinarange[0–1].Severalcrossover

operatorsareavailable, suchasone-point, two-point, anduniformcrossovers. Inthis

study,weusedauniformcrossoverinwhicheachbitinaparent’schromoneisswapped

basedonapredefinedprobabilityandarandomnumberinarange[0–1]. Forinstance,

ifthepredefinedprobabilityis0.5andtherandomnumberis0.7,inthiscasetherandom

numberisequaltoorgreaterthanthepredefinedprobability. Therefore,bitswapping

occurs.Thisprocessisrepeatedforallbitsintheparents’chromosome.Hence,wehave

twoprobabilities: aprobabilityforapplyingcrossoverbetweentwoindividualsanda

probabilityforexchangingthebitvaluebetweentwoindividuals.

MutationProcess

Mutation,whichisappliedafterthecrossoverprocess,isthealterationofindividual

bitstogeneratenewindividualsfromthecurrentindividuals.Severalmutationoperators

areavailable,suchasinversionmutation,insertionmutation,andflip-bitmutation[38].

Inthisstudy,weusedflip-bitmutation,whichswitchescertainbitsfrom1to0orvice

versa. Twoprobabilitiesareusedinmutation: theprobabilityofapplyingmutationon

theindividualandtheprobabilityofmutationorflippingthebitvalueoftheindivid-

ual.Newdifferentindividualsaregeneratedfromthecurrentgenerationafterapplying

crossoverandmutationoperators.

StoppingCriteria

Theevaluationofindividuals,selection,crossover,andmutationarerepeatedina

predefinednumberofgenerationsuntilastoppingcriterionismet(e.g.,themaximum

numberofgenerationoraspecifiednumberofgenerationsisreachedwhentheobjective

functioncannotimprove).

49

Mathematics2022,10,4745

3.4.Classification

TheselectedfeaturesubsetsarethenfedtoaclassifiersuchasMLPandSVMtoclassify

theinputsasnormalorattacktraffic.Differentclassifiersareinvestigatedtoidentifythe

mostsuitableonefortrainingandtestingtheIDSmodel.

3.4.1.SupportVectorMachine(SVM)

SVMisasupervisedlearningmodelthatprovidesagoodlevelofaccuracyinclassifi-

cationproblems[4,8,10,21,33].SVMbuildsoneormorehyperplanesbyusingthenearest

trainingdatapointsofeachdata(calledsupportvectors).Then,ittriestomaximizethe

marginbetweenthedatapoints.IntheimplementationofSVMs,therearecertainkernel

functionssuchaspolynomial,sigmoid,andradialkernelfunctions(RBF).Makingthe

trade-offbetweenconstantCandthetypeofkernelfunctioniscrucialtoachieveagood

resultfortheclassification[8].

3.4.2.ArtificialNeuralNetworkMultiPerceptron(ANN-MLP)

MLPisalsoasupervisedlearningmodel.ItisaclassoffeedforwardANN.Thereare

atleastthreelayersinMLP:aninput,hidden,andoutputlayer[19].Eachlayercontains

oneormoreneurons.Eachneuronconnectswithaspecificweighttoeveryneuroninthe

followinglayer[19].ThelearninginMLPoccursbychangingtheweightsaftereachinput

ofdata.

3.5.Evaluation

The performance of each FS technique is evaluated on the basis of performance

measuressuchasACC,FPRandF1scoreaswellasthenumberofselectedfeatures.Several

metricsareavailableforevaluatingfeatureselectionalgorithmssuchasaccuracy,false

positiverate, detectionrate, andprecision. Thesemetricscanbecalculatedusingthe

confusionmatrixthatisrepresentedbythefollowingfourmainparameters:

• Truepositive(TP):representsnumberofattacksamplesclassifiedcorrectly.

• Truenegative(TN):representsnumberofnormalsamplesclassifiedcorrectly.

• Falsepositive(FP):representsnumberofnormalsamplesclassifiedwrongly.

• Falsenegative(FN):representsnumberofattacksamplesclassifiedwrongly.

Inbinaryclassification,aconfusionmatrixisatableormatrixofsize2×2thatisused

todescribetheperformanceofmachinelearningclassifiers.Aconfusionmatrixisshown

inTable2,whereeachcolumnrepresentsthepredictiverecordsandeachrowrepresents

theactualrecords.

Table2.Confusionmatrix.

PredictiveRecords

TP FP

Actualrecords

FN TN

Thedefinitionandformulasoftheperformancemetricsareasfollows[28]:

- Accuracy:representstheproportionofcorrectclassifiedinstancestothetotalnumber

ofclassifications,asinEquation(3).

Accuracy=(TP+TN)/(TP+TN+FP+FN) (3)

- FPR(a.k.a.falsealarms):representstheproportionofthenormalinstancesthatare

identifiedasattackorabnormalinstances,asinEquation(4).

FPR=FP/(TN+FP) (4)

50

Mathematics2022,10,4745

- Precision: representstheratioofcorrectlypredictedpositiveinstancestothetotal

predictedpositiveinstances,asinEquation(5).

Percision=TP/TP+FP (5)

- Recall(a.k.a.detectionrate(DR)):representstheratioofcorrectlypredictedpositive

instancestotheoverallnumberofactualpositiveinstances,asinEquation(6).

Recall=TP/TP+FN (6)

- F1score:representstheweightedaverageofprecisionandrecallvalues,asinEquation

(7).

F1score=2∗ p p e e r r c c i i s s i i o o n n + ∗r r e e c c a a l l l l (7)

3.6.AnalysisandComparisonofResults

Theresultsobtainedfromthepreviousstepwereanalyzedandcomparedwithone

anothertoselectanefficientIDSmodelwithahighaccuracy,lowfalsealarm,andasmall

numberoffeatures.

4.Implementation

Inthissection,theexperimentalsettingsarepresented,andtheeffectivenessofthe

SFS,SBS,andGAmethodsareillustrated.Theexperimentalenvironmentwassetupas

follows:adesktopcomputerrunningWindows10onanIntelCorei9-12thGenwith48

GBRAM,Anaconda3withPython3distribution,theScikit-learnlibrary,andtheJupyter

notebook[39].Figure5illustratesandsummarizesthestepsofimplementation,whichare

presentedindetail.

Figure5.Implementationflowchart.

4.1.Preprocessing

Theprocessingphaseweusedconsistofeightstepswhichare:

1. IntheNSL-KDDdataset,threecategoricalfeatures,whichareflag,service,andproto-

col_typefeatures,aremappedtonumericvaluesrangingfrom0toN−1,whereNis

thenumberofsymbolsinthefeature.

2. MissingvaluesornullvaluesareremovedfromtheCIC-IDS-2017andCIC-IDS-2018

datasets.AscriptwritteninPythonisusedforremovingtheserecords.

51

Mathematics2022,10,4745

3. AduplicatefeatureinCIC-IDS-2017,namelyFwdHeaderLength,isremovedman-

ually. ThetimestampfeatureisremovedmanuallyinCIC-IDS-2018. Inaddition,

tenfeaturesareremovedmanuallyinCIC-IDS-2017andCIC-IDS-2018,astheyhave

zerovalues.

4. Duplicatedrecordsareremovedinalldatasets.AscriptwritteninPythonisusedfor

removingtheserecords.

5. Theclasslabelismappedto0fornormalclassand1forattack.Asweusebinaryclas-

sificationinthisstudy,allthesub-categoryattacklabelsaremappedto1.Theresulted

labelfeaturecontains0fornormalrecordsand1forattackrecords.

6. TheStandardScalermethodfromthesklearnlibraryinPythonisappliedtostandard-

izethefeaturevarianceinalltheuseddatasets.

7. Alldatasetsaresplitinto70%trainingand30%testingdatasets.

8. Therandomunder-sampling(RUS)techniqueisappliedinalltrainingdatasets.

4.2.FeatureSelection

Thescikit-learnlibraryandJupyternotebookareusedtoimplementSFS,SBS,andGA

FSmethods. Theperformanceevaluationoftheselectedfeaturesofthesubsetsineach

iterationinSFS,SBS,andtheGAiscarriedoutusingthecross-validationtechniquein

whichthedatasetisrandomlydividedintoseveralKsubsets.Onesubsetisusedfortesting

themodel,andtheremainingsubsetsareusedfortraining.ThisprocessisiteratedKtimes,

andthetestingsubsetisdifferentineachiteration[13].Table3showstheselectedweights

intheselectedfitnessfunctions.

Table3.Parametersoffitnessfunctions.

ObjectiveFunction Parameter Value

WD 0.45

Equation(1) WF 0.45

WN 0.1

WA 0.94

Equation(2)

WN 0.06

ImplementationofSFS,SBSandtheGA

TheMLxtendlibraryinPythonisusedtoimplementSFSandSBS,whiletheSklearn-

genetic,whichisageneticFSmoduleforscikit-learn,isusedtoimplementtheGA[40,41].

SVMandMLPareusedseparatelyasestimatorsinSFS,SBSandtheGA.Toevaluatethe

subsetsofselectedfeaturesineachiteration,two-fold,five-fold,andten-foldcrossvalida-

tionareusedseparatelyintheimplementationofSFS,SBSandtheGA.Theparameters

ofSFSandSBSareconfiguredasshowninTable4,whiletheparametersoftheGAare

configuredasshowninTable5.

Table4.ParametersofSFSandSBS.

Parameter Value Parameter Value

SVM n_jobs −1

Estimator

MLP floating False

Equation(1) 2

Scoring

Equation(2) cv 5

NSL-KDD(1,40) 10

k_features CIC-IDS-2017(1,66) forward True(SFS)

CIC-IDS-2018(1,67) False(SBS)

52

Mathematics2022,10,4745

Table5.ParametersofGA.

Parameter Value Parameter Value

SVM crossover_proba 0.6

Estimator

MLP crossover_independent_proba 0.6

Equation(1) mutation_proba 0.1

Scoring

Equation(2) mutation_indenpdent_proba 0.1

NSL-KDD(40) caching True

Max_features CIC-IDS-2017(66) NSL-KDD(50)

CIC-IDS-2018(67) n_gen_no_change CIC-IDS-2017(65)

NSL-KDD(60) CIC-IDS-2018(65)

n_population CIC-IDS-2017(80) n_jobs −1

CIC-IDS-2018(80) verbose 1

n_generations NSL-KDD(50) 2

CIC-IDS-2017(65) cv 5

CIC-IDS-2018(65) 10

4.3.TrainingandTesting

Foreachselectedsubset,wetransformtheoriginaltrainingdatasettohavethesame

numberofselectedfeaturesfromtheFSphase. Theselectedfeaturesubsetsfromthe

previousFSmethodsarefittedintothesameusedclassifierintheFSphasetodetermine

andevaluatetheperformanceoftheselectedfeaturesubset.Hence,SVMisusedtoevaluate

theselectedfeaturesubsetsselectedfromtheFSphasewhenSVMisusedasanobjective

function.MLPisusedtoevaluatetheselectedfeaturesubsetsselectedfromtheFSphase

whenMLPisusedanobjectivefunction.

4.4.ResultsandDiscussion

Theexperimentalresultsofthechosenfeatureselectionmethodsarepresentedinthis

section.

Table6showstheresultofSFS,SBSandtheGAbasedonSVMandMLPintheNSL-

KDDdatasetusinganobjectivefunctionbasedonaccuracyandthenumberofselected

features.Asshowninthetable,theresultsarepresentedandcomparedusingdifferentcross

validationssuchastwo-fold,five-fold,andten-foldcrossvalidationforeachcombination

ofFSmethodandclassifier.Thehighestaccuracyamongallthesecombinationsis99.23%

withtheGA+SVM,witha0.77%falsealarmrateand29selectedfeaturesusingtwo-fold

crossvalidationinthefeatureselectionphase. ThismodelalsohasthehighestF1score,

of99.20%,amongthemodels. Thelowestfalsealarmrateamongthesecombinationsis

0.73%withtheGA+SVM,withanaccuracyof99.06%. SBS+SVMperformswellwitha

differentnumberoffolds.Itobtained98.92%,98.95%,and98.99%intermsofaccuracyand

1.20%,1.36%,and1.16%intermsofFPR,respectively,withthesameselectednumberof

features(10features).AgraphicalillustrationofTable6isshowninFigure6.

Table7showstheresultofSFS,SBS,andtheGAbasedonSVMandMLPintheCIC-

IDS-2017datasetusinganobjectivefunctionbasedonaccuracyandthenumberofselected

features.Asshowninthetable,thehighestaccuracyamongallthesecombinationsis99.96%

withtheGA+MLP,witha0.03%falsealarmrateand40selectedfeaturesusingfive-fold

crossvalidationinthefeatureselectionphase.Thelowestfalsealarmrateamongallthese

combinationsis0.01%withSFS+MLPandtheGA+SVM,withaccuraciesof88.74%and

99.9%,respectively.SBS+SVMperformswellwithadifferentnumberoffolds.Itobtained

99.65%,99.81%,and99.75%intermsofaccuracyand0.50%,0.13%,and0.27%intermsof

FPR,withthesix,five,andfiveselectedfeatures,respectively.AnillustrationofTable7is

showninFigure7.

53

Mathematics2022,10,4745

Table6.PerformanceofSFS,SBSandtheGAusingobjectivefunctionbasedonaccuracyandnumber

ofselectedfeaturesinNSL-KDD.

Metric Fold SFS+SVM SFS+MLP SBS+SVM SBS+MLP GA+SVM GA+MLP

)%(ycaruccA 2 98.94 97.83 98.95 98.25 99.23 99.01

5 98.80 97.66 98.82 98.81 99.16 99.02

10 98.89 98.78 98.88 98.16 99.06 99.06

forebmuN

detceles serutaef

2 10 9 10 16 29 38

5 9 9 10 14 27 35

10 10 13 10 13 29 36

)%(RPF 2 1.14 2.51 0.99 1.50 0.77 0.95

5 1.44 2.84 1.18 1.26 0.84 1.20

10 1.39 1.59 1.26 1.84 0.73 1.16

)%(1F

2 98.90 97.75 98.81 98.17 99.20 98.98

5 98.76 97.59 98.77 98.77 99.13 98.98

10 98.85 98.83 98.84 98.09 99.03 99.02

(cid:4)(cid:272)(cid:272)(cid:437)(cid:396)(cid:258)(cid:272)(cid:455)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:69)(cid:437)(cid:373)(cid:271)(cid:286)(cid:396)(cid:3)(cid:381)(cid:296)(cid:3)(cid:94)(cid:286)(cid:367)(cid:286)(cid:272)(cid:410)(cid:286)(cid:282)(cid:3)(cid:3)(cid:38)(cid:286)(cid:258)(cid:410)(cid:437)(cid:396)(cid:286)(cid:400)

(cid:1013)(cid:1013)(cid:856)(cid:1009)

(cid:1013)(cid:1013) (cid:1008)(cid:1004)

(cid:1013)(cid:1012)(cid:856)(cid:1009)

(cid:1007)(cid:1004)

(cid:1013)(cid:1012)

(cid:1006)(cid:1004)

(cid:1013)(cid:1011)(cid:856)(cid:1009)

(cid:1013)(cid:1011) (cid:1005)(cid:1004)

(cid:1013)(cid:1010)(cid:856)(cid:1009) (cid:1004)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

(cid:38)(cid:87)(cid:90)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:38)(cid:1005)(cid:882)(cid:94)(cid:272)(cid:381)(cid:396)(cid:286)(cid:3)(cid:894)(cid:1081)(cid:895)

(cid:1007) (cid:1013)(cid:1013)(cid:856)(cid:1009)

(cid:1013)(cid:1013)

(cid:1006)

(cid:1013)(cid:1012)(cid:856)(cid:1009)

(cid:1005)

(cid:1013)(cid:1012)

(cid:1004) (cid:1013)(cid:1011)(cid:856)(cid:1009)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

Figure6.PerformanceofSFS,SBSandGAusingobjectivefunctionbasedonaccuracyandnumber

ofselectedfeaturesinNSL-KDD.

54

Mathematics2022,10,4745

Table7.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonaccuracyandnumberof

selectedfeaturesinCIC-IDS-2017.

Metric Fold SFS+SVM SFS+MLP SBS+SVM SBS+MLP GA+SVM GA+MLP

)%(ycaruccA 2 99.75 99.83 99.65 94.79 99.94 99.93

5 99.78 89.61 99.81 99.84 99.94 99.96

10 99.28 88.74 99.75 99.83 99.9 99.91

forebmuN

detceles serutaef

2 5 7 5 6 42 44

5 5 5 6 5 39 40

10 5 5 5 6 45 38

)%(RPF 2 0.27 0.04 0.5 1.12 0.02 0.02

5 0.22 0.03 0.13 0.17 0.02 0.03

10 1.44 0.01 0.27 0.12 0.01 0.03

)%(1F

2 99.78 99.86 99.69 95.24 99.95 99.96

5 99.81 89.93 99.83 99.86 99.93 99.94

10 99.36 89.00 99.78 99.85 99.93 99.39

(cid:4)(cid:272)(cid:272)(cid:437)(cid:396)(cid:258)(cid:272)(cid:455)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:69)(cid:437)(cid:373)(cid:271)(cid:286)(cid:396)(cid:3)(cid:381)(cid:296)(cid:3)(cid:94)(cid:286)(cid:367)(cid:286)(cid:272)(cid:410)(cid:286)(cid:282)(cid:3)

(cid:38)(cid:286)(cid:258)(cid:410)(cid:437)(cid:396)(cid:286)(cid:400)

(cid:1005)(cid:1004)(cid:1004)

(cid:1013)(cid:1012) (cid:1008)(cid:1009)

(cid:1008)(cid:1004)

(cid:1013)(cid:1010) (cid:1007)(cid:1009)

(cid:1013)(cid:1008) (cid:1006) (cid:1007) (cid:1009) (cid:1004)

(cid:1013)(cid:1006) (cid:1006)(cid:1004)

(cid:1005)(cid:1009)

(cid:1013)(cid:1004) (cid:1005)(cid:1004)

(cid:1009)

(cid:1012)(cid:1012) (cid:1004)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

(cid:38)(cid:87)(cid:90)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:38)(cid:1005)(cid:882)(cid:94)(cid:272)(cid:381)(cid:396)(cid:286)(cid:3)(cid:894)(cid:1081)(cid:895)

(cid:1005)(cid:1004)(cid:1004)

(cid:1005)(cid:856)(cid:1008)

(cid:1005)(cid:856)(cid:1006) (cid:1013)(cid:1012)

(cid:1005) (cid:1013)(cid:1010)

(cid:1004)(cid:856)(cid:1012) (cid:1013)(cid:1008)

(cid:1004)(cid:856)(cid:1010)

(cid:1013)(cid:1006)

(cid:1004)(cid:856)(cid:1008)

(cid:1004)(cid:856)(cid:1006) (cid:1013)(cid:1004)

(cid:1004) (cid:1012)(cid:1012)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

Figure7.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonaccuracyandnumber

ofselectedfeaturesinCIC-IDS-2017.

Table8showstheresultofSFS,SBS,andtheGAbasedonSVMandMLPinthe

CIC-IDS-2018datasetusinganobjectivefunctionbasedonaccuracyandthenumberof

selectedfeatures.Asshowninthetable,thehighestaccuracyamongallthesecombinations

is99.87%withtheSFS+MLPandSBS+MLPmodels.SFS+MLPobtainsalowerFPR,of0.1%,

55

Mathematics2022,10,4745

thanSBS+MLPwitheightselectedfeaturesusingfive-foldcrossvalidationinthefeature

selectionphase.Threemodels,whichareSFS+MLP,SBS+SVM,andtheGA+MLPobtain

thelowestfalsealarmrate,of0.1%,amongthemodels. AdemonstrationofTable8is

showninFigure8.

Table8.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonaccuracyandnumberof

selectedfeaturesinCIC-IDS-2018.

Metric Fold SFS+SVM SFS+MLP SBS+SVM SBS+MLP GA+SVM GA+MLP

)%(ycaruccA 2 99.46 99.87 99.78 99.87 99.71 99.69

5 97.67 99.87 99.64 99.51 99.82 99.83

10 97.72 99.80 99.69 99.67 99.8 99.78

forebmuN

detceles serutaef

2 21 11 7 8 18 23

5 6 8 7 10 21 26

10 6 8 8 11 24 25

)%(RPF 2 0.32 0.90 0.10 0.90 0.16 0.21

5 0.18 0.10 0.10 0.84 0.16 0.10

10 0.30 0.30 0.20 0.90 0.19 0.17

)%(1F

2 99.46 99.88 99.77 99.88 99.71 99.69

5 97.61 99.85 99.64 99.51 99.82 99.80

10 97.63 99.80 99.71 99.74 99.80 99.75

(cid:4)(cid:272)(cid:272)(cid:437)(cid:396)(cid:258)(cid:272)(cid:455)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:69)(cid:437)(cid:373)(cid:271)(cid:286)(cid:396)(cid:3)(cid:381)(cid:296)(cid:3)(cid:94)(cid:286)(cid:367)(cid:286)(cid:272)(cid:410)(cid:286)(cid:282)(cid:3)

(cid:38)(cid:286)(cid:258)(cid:410)(cid:437)(cid:396)(cid:286)(cid:400)

(cid:1005)(cid:1004)(cid:1004)

(cid:1013)(cid:1013)(cid:856)(cid:1009) (cid:1007)(cid:1004)

(cid:1013)(cid:1013) (cid:1006)(cid:1009)

(cid:1013)(cid:1012)(cid:856)(cid:1009) (cid:1006)(cid:1004)

(cid:1005)(cid:1009)

(cid:1013)(cid:1012)

(cid:1005)(cid:1004)

(cid:1013)(cid:1011)(cid:856)(cid:1009) (cid:1009)

(cid:1013)(cid:1011) (cid:1004)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

(cid:38)(cid:87)(cid:90)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:38)(cid:1005)(cid:882)(cid:94)(cid:272)(cid:381)(cid:396)(cid:286)(cid:3)(cid:894)(cid:1081)(cid:895)

(cid:1005) (cid:1005)(cid:1004)(cid:1004)

(cid:1004)(cid:856)(cid:1012) (cid:1013)(cid:1013)

(cid:1004)(cid:856)(cid:1010)

(cid:1013)(cid:1012)

(cid:1004)(cid:856)(cid:1008)

(cid:1013)(cid:1011)

(cid:1004)(cid:856)(cid:1006)

(cid:1004) (cid:1013)(cid:1010)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

Figure8.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonaccuracyandnumber

ofselectedfeaturesinCIC-IDS-2018.

56

Mathematics2022,10,4745

Table9showstheresultofSFS,SBS,andtheGAbasedonSVMandMLPinthe

NSL-KDDdatasetusinganobjectivefunctionbasedondetectionrate,falsepositiverate,

andnumberofselectedfeatures.Asshowninthetable,theGA+SVMobtainsthehighest

accuracyandlowestfalsealarmrateamongallthesecombinations.Itobtainsanaccuracy

of99.21%andanFPRof0.83%with30selectedfeaturesusing10-foldcrossvalidation

inthefeatureselectionphase.Inaddition,thismodelobtainsanaccuracyof99.19%and

anFPRof0.81%with33selectedfeaturesusingfive-foldcrossvalidationinthefeature

selectionphase.Table9isdepictedinFigure9.

Table9.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonDR,FPR,andnumberof

selectedfeaturesinNSL-KDD.

Metric Fold SFS+SVM SFS+MLP SBS+SVM SBS+MLP GA+SVM GA+MLP

)%(ycaruccA 2 98.77 97.83 97.76 97.7 99.18 99.11

5 98.19 97.66 98.82 97.99 99.19 98.98

10 98.19 98.82 98.65 97.93 99.21 98.93

forebmuN

detceles serutaef

2 9 9 6 9 27 37

5 7 9 10 10 33 28

10 7 12 8 10 30 39

)%(RPF 2 1.46 2.51 1.94 2.76 0.89 0.85

5 1.85 2.84 1.81 1.76 0.81 1.17

10 1.85 1.65 1.82 2.64 0.83 1.28

)%(1F

2 98.72 97.96 97.66 97.63 99.15 99.08

5 98.12 97.59 98.78 97.91 99.16 98.92

10 98.12 98.09 98.61 98.01 99.18 98.88

(cid:4)(cid:272)(cid:272)(cid:437)(cid:396)(cid:258)(cid:272)(cid:455)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:69)(cid:437)(cid:373)(cid:271)(cid:286)(cid:396)(cid:3)(cid:381)(cid:296)(cid:3)(cid:94)(cid:286)(cid:367)(cid:286)(cid:272)(cid:410)(cid:286)(cid:282)(cid:3)

(cid:38)(cid:286)(cid:258)(cid:410)(cid:437)(cid:396)(cid:286)(cid:400)

(cid:1005)(cid:1004)(cid:1004)

(cid:1008)(cid:1009)

(cid:1013)(cid:1013) (cid:1008)(cid:1004)

(cid:1007)(cid:1009)

(cid:1007)(cid:1004)

(cid:1013)(cid:1012) (cid:1006)(cid:1009)

(cid:1006)(cid:1004)

(cid:1013)(cid:1011) (cid:1005)(cid:1009)

(cid:1005)(cid:1004)

(cid:1009)

(cid:1013)(cid:1010) (cid:1004)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

Figure9.Cont.

57

Mathematics2022,10,4745

(cid:38)(cid:87)(cid:90)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:38)(cid:1005)(cid:882)(cid:94)(cid:272)(cid:381)(cid:396)(cid:286)(cid:3)(cid:894)(cid:1081)(cid:895)

(cid:1006) (cid:1005)(cid:1004)(cid:1004)

(cid:1005)(cid:856)(cid:1012)

(cid:1005)(cid:856)(cid:1010)

(cid:1013)(cid:1013)

(cid:1005)(cid:856)(cid:1008)

(cid:1005)(cid:856)(cid:1006)

(cid:1005) (cid:1013)(cid:1012)

(cid:1004)(cid:856)(cid:1012)

(cid:1004)(cid:856)(cid:1010)

(cid:1013)(cid:1011)

(cid:1004)(cid:856)(cid:1008)

(cid:1004)(cid:856)(cid:1006)

(cid:1004) (cid:1013)(cid:1010)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

Figure9.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonDR,FPR,andnumber

ofselectedfeaturesinNSL-KDD.

Table10showstheresultsofSFS,SBS,andtheGAbasedonSVMandMLPinthe

CIC-IDS-2017datasetusinganobjectivefunctionbasedonthedetectionrate,falsepositive

rate,andnumberofselectedfeatures.Asshowninthetable,GA+MLPobtainsthehighest

accuracy,of99.95%,amongallthesecombinationsandalowfalsealarmrateof0.007%with

35selectedfeaturesusingtwo-foldcrossvalidationinthefeatureselectionphase.TheGA

modelsobtainahigheraccuracythantheSFSandSBSmodelsandgivealowfalsealarm

rate(lessthan0.035%)inalltheircombinations.Figure10displaysTable10initsentirety.

Table10.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonDR,FPR,andnumber

ofselectedfeaturesinCIC-IDS-2017.

Metric Fold SFS+SVM SFS+MLP SBS+SVM SBS+MLP GA+SVM GA+MLP

)%(ycaruccA 2 97.86 98.07 99.86 96.41 99.94 99.95

5 99.87 97.9 99.9 98.17 99.93 99.91

10 99.87 97.62 99.89 94.72 99.94 99.93

forebmuN

detceles serutaef

2 27 17 16 10 38 35

5 31 24 14 14 42 40

10 29 24 19 9 41 33

)%(RPF 2 0.06 0.05 0.03 0.03 0.003 0.007

5 0.09 0.003 0.05 0.05 0.03 0.01

10 0.06 0.05 0.04 0.04 0.02 0.005

)%(1F

2 98.08 98.28 99.88 96.74 99.93 99.92

5 99.89 98.12 99.92 98.36 99.93 99.93

10 99.89 97.86 99.91 95.12 99.92 99.89

58

Mathematics2022,10,4745

(cid:4)(cid:272)(cid:272)(cid:437)(cid:396)(cid:258)(cid:272)(cid:455)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:69)(cid:437)(cid:373)(cid:271)(cid:286)(cid:396)(cid:3)(cid:381)(cid:296)(cid:3)(cid:94)(cid:286)(cid:367)(cid:286)(cid:272)(cid:410)(cid:286)(cid:282)(cid:3)

(cid:38)(cid:286)(cid:258)(cid:410)(cid:437)(cid:396)(cid:286)(cid:400)

(cid:1005)(cid:1004)(cid:1004)

(cid:1008)(cid:1009)

(cid:1013)(cid:1013) (cid:1008)(cid:1004)

(cid:1007)(cid:1009)

(cid:1007)(cid:1004)

(cid:1013)(cid:1012) (cid:1006)(cid:1009)

(cid:1006)(cid:1004)

(cid:1013)(cid:1011) (cid:1005)(cid:1009)

(cid:1005)(cid:1004)

(cid:1009)

(cid:1013)(cid:1010) (cid:1004)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

(cid:38)(cid:87)(cid:90)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:38)(cid:1005)(cid:882)(cid:94)(cid:272)(cid:381)(cid:396)(cid:286)(cid:3)(cid:894)(cid:1081)(cid:895)

(cid:1004)(cid:856)(cid:1005) (cid:1005)(cid:1004)(cid:1004)

(cid:1004)(cid:856)(cid:1004)(cid:1012)

(cid:1013)(cid:1013)

(cid:1004)(cid:856)(cid:1004)(cid:1010)

(cid:1013)(cid:1012)

(cid:1004)(cid:856)(cid:1004)(cid:1008)

(cid:1013)(cid:1011)

(cid:1004)(cid:856)(cid:1004)(cid:1006)

(cid:1004) (cid:1013)(cid:1010)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

Figure10.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonDR,FPR,andnumber

ofselectedfeaturesinCIC-IDS-2017.

Table11showstheresultofSFS,SBS,andtheGAbasedonSVMandMLPinthe

CIC-IDS-2018datasetusinganobjectivefunctionbasedonthedetectionrate,falsepositive

rate,andnumberofselectedfeatures. Asshowninthetable,theGA+MLPobtainsthe

highestaccuracy,of99.92%,andlowestfalsealarmrate,of0.07%,with47selectedfeatures

usingtwo-foldcrossvalidationinthefeatureselectionphase. TheGAmodelsobtaina

higheraccuracythantheSFSandSBSmodelsandgivealowfalsealarmrate(lessthan

0.20%)inalltheircombinations.Figure11depictsTable11indetail.

Table11.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonDR,FPR,andnumber

ofselectedfeaturesinCIC-IDS-2018.

Metric Fold SFS+SVM SFS+MLP SBS+SVM SBS+MLP GA+SVM GA+MLP

)%(ycaruccA 2 97.41 97.57 98.2 99.56 99.56 99.92

5 97.41 99.78 99.6 99.09 99.8 99.89

10 97.38 98.21 99.01 99.16 99.74 99.82

59

Mathematics2022,10,4745

Table11.Cont.

Metric Fold SFS+SVM SFS+MLP SBS+SVM SBS+MLP GA+SVM GA+MLP

forebmuN

detceles serutaef

2 6 8 6 8 14 47

5 4 7 5 7 15 41

10 6 7 6 9 17 38

)%(RPF 2 0.35 0.19 0.36 0.15 0.13 0.07

5 0.30 0.16 0.19 1.31 0.19 0.11

10 0.33 0.19 0.20 1.22 0.15 0.19

)%(1F

2 97.35 97.51 98.91 99.55 99.56 99.93

5 97.34 99.78 99.60 99.07 99.80 99.89

10 98.85 98.83 98.84 98.09 99.03 99.02

(cid:4)(cid:272)(cid:272)(cid:437)(cid:396)(cid:258)(cid:272)(cid:455)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:69)(cid:437)(cid:373)(cid:271)(cid:286)(cid:396)(cid:3)(cid:381)(cid:296)(cid:3)(cid:94)(cid:286)(cid:367)(cid:286)(cid:272)(cid:410)(cid:286)(cid:282)(cid:3)

(cid:38)(cid:286)(cid:258)(cid:410)(cid:437)(cid:396)(cid:286)(cid:400)

(cid:1005)(cid:1004)(cid:1004)

(cid:1013)(cid:1013) (cid:1008)(cid:1009)

(cid:1008)(cid:1004)

(cid:1007)(cid:1009)

(cid:1013)(cid:1012) (cid:1007)(cid:1004)

(cid:1006)(cid:1009)

(cid:1006)(cid:1004)

(cid:1013)(cid:1011) (cid:1005)(cid:1009)

(cid:1005)(cid:1004)

(cid:1009)

(cid:1013)(cid:1010) (cid:1004)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

(cid:38)(cid:87)(cid:90)(cid:3)(cid:894)(cid:1081)(cid:895) (cid:38)(cid:1005)(cid:882)(cid:94)(cid:272)(cid:381)(cid:396)(cid:286)(cid:894)(cid:1081)(cid:895)

(cid:1005)(cid:1004)(cid:1004)

(cid:1005)(cid:856)(cid:1008)

(cid:1005)(cid:856)(cid:1006)

(cid:1013)(cid:1013)

(cid:1005)

(cid:1004)(cid:856)(cid:1012)

(cid:1013)(cid:1012)

(cid:1004)(cid:856)(cid:1010)

(cid:1004)(cid:856)(cid:1008) (cid:1013)(cid:1011)

(cid:1004)(cid:856)(cid:1006)

(cid:1004) (cid:1013)(cid:1010)

(cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1006)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1009)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282) (cid:1005)(cid:1004)(cid:882)(cid:38)(cid:381)(cid:367)(cid:282)

(cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:94)(cid:38)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:94)(cid:115)(cid:68)

(cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:94)(cid:17)(cid:94)(cid:1085)(cid:68)(cid:62)(cid:87) (cid:39)(cid:4)(cid:1085)(cid:94)(cid:115)(cid:68) (cid:39)(cid:4)(cid:1085)(cid:68)(cid:62)(cid:87)

Figure11.PerformanceofSFS,SBS,andGAusingobjectivefunctionbasedonDR,FPR,andnumber

ofselectedfeaturesinCIC-IDS-2018.

4.5.PerformanceComparisonwiththeRecentMethods

Tables12–14showthecomparisonbetweenourbestobtainedresultsandthoseof

otherrecentmethodsintheNSL-KDD,CIC-IDS-2017,andCIC-IDS-2018datasets.

60

Mathematics2022,10,4745

Table12.PerformancecomparisonwithrecentmethodsinNSL-KDD.

Numberof ACC FPR

Ref. FSTech. Classifier

SelectedFeatures (%) (%)

[19] CSA MCF+MVO-ANN 22 98.81 0.02

[28] SigmoidPOI DT 18 86.90 6.40

[28] CosinePOI DT 5 88.30 8.80

[29] ABC AdaBoost 25 98.90 0.01

Proposedmodel GA SVM 29 99.23 0.77

Table13.PerformancecomparisonwithrecentmethodsCIC-IDS-2017.

Numberof ACC FPR

Ref. FSTech. Classifier

SelectedFeatures (%) (%)

IGandcorrelationattribute

[31] PART 56 99.98 1.35

evaluationmethods

Informationgainandranker

[32] J48 75 87.44 -

algorithm

[26] IG LightGBM 10 98.37 -

Proposedmodel GA MLP 35 99.95 0.007

Proposedmodel GA SVM 38 99.94 0.003

Table14.PerformancecomparisonwithrecentmethodsinCIC-IDS-2018.

Numberof ACC FPR

Ref. FSTech. Classifier

SelectedFeatures (%) (%)

[27] Hybridfeatureselection(RF+PCA) LightGBM 24 97.73 -

[30] Binary-particleswarmoptimization Decisiontree 19 99.52 -

Proposedmodel SFS MLP 11 99.87 0.90

Proposedmodel SBS MLP 8 99.87 0.90

Proposedmodel GA MLP 47 99.92 0.07

5.Conclusions

Thispaperhaspresentedacomparativestudyofsequentialforwardselection,se-

quentialbackwardselection,andgeneticalgorithmfeatureselectionmethodsinintrusion

detectionsystemstoselectanefficientIDSmodelthatprovidesahighaccuracyandlow

falsealarmwithaminimumnumberoffeatures.Theefficienciesofthethreefeatureselec-

tiontechniqueswithtwoclassificationmethods,namelySVMandMLP,werecompared.

Thesemethodswereappliedtothreepubliclyavailableintrusiondetectionsystemdatasets,

namelyNSL-KDD,CICIDS2017,andCICIDS2018.Thispaperhaspresentedanassessment

ofthesedatasets,identifyingtheirlimitationsandprovidingsolutionstoovercomethese

limitations.

Theperformanceoftheproposedmodelswasanalyzed,addressed,andcompared

toexistingtechniques.Theefficienciesoftheproposedmodelswereprovenintheexper-

imentalresults,whichindicatedthatthehighestaccuracyintheNSL-KDDdatasetwas

99.23%,achievedusingtheGA+SVM,witha0.77%falsealarmrateand29selectedfeatures

usingtwo-foldcrossvalidationinthefeatureselectionphase. Thismodelalsohasthe

highestF1score,of99.20%,amongthemodels. IntheCICIDS2017dataset,thehighest

accuracyamongtheproposedmodelsis99.96%,achievedwiththeGA+MLP,witha0.03%

falsealarmrateand40selectedfeaturesusingfive-foldcrossvalidationinthefeature

61

Mathematics2022,10,4745

selectionphase.Thelowestfalsealarmrateamongtheproposedmodelsis0.01%inthe

caseofSFS+MLPandtheGA+SVM,withaccuraciesof88.74%and99.9%,respectively.

IntheCSE-CIC-IDS218dataset,SFS+MLPandSBS+MLPachievedanaccuracyof99.87%.

SFS+MLPobtainsalowerFPR,of0.10%,thanSBS+MLPwitheightselectedfeaturesusing

five-foldcrossvalidationinthefeatureselectionphase.

AuthorContributions:Conceptualization,I.A.andY.A.;methodology,I.A.;software,Y.A.;valida-

tion,I.A.,Y.A.andF.E.A.;formalanalysis,I.A.andY.A.;investigation,Y.A.;resourcesI.A.andF.E.A.;

datacuration,I.A.;writing—originaldraftpreparation,Y.A.;writing—reviewandediting,I.A.,Y.A.

andF.E.A.;visualization,I.A.;supervision,I.A.andF.E.A.;projectadministration,I.A.;funding

acquisition,I.A.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.

Funding:ThisresearchworkwasfundedbyInstitutionalFundProjectsundergrantno.(IFPRC-076-

611-2020).TheauthorsacknowledgetechnicalandfinancialsupportfromtheMinistryofEducation

andKingAbdulazizUniversity,DSR,Jeddah,SaudiArabia.

InstitutionalReviewBoardStatement:Notapplicable.

InformedConsentStatement:Notapplicable.

DataAvailabilityStatement:Notapplicable.

Acknowledgments:ThisresearchworkwasfundedbyInstitutionalFundProjectsundergrantno.

(IFPRC-076-611-2020).Therefore,theauthorsgratefullyacknowledgetechnicalandfinancialsupport

fromtheMinistryofEducationandKingAbdulazizUniversity,DSR,Jeddah,SaudiArabia.

ConflictsofInterest:Thereisnoconflictofauthors.

References

1. Thakkar,A.;Lohiya,R.Asurveyonintrusiondetectionsystem:Featureselection,model,performancemeasures,application

perspective,challenges,andfutureresearchdirections.Artif.Intell.Rev.2022,55,453–563.[CrossRef]

2. Alhakami,W.;Alharbi,A.;Bourouis,S.;Alroobaea,R.;Bouguila,N.NetworkAnomalyIntrusionDetectionUsingaNonparametric

BayesianApproachandFeatureSelection.IEEEAccess2019,7,52181–52190.[CrossRef]

3. Thakkar,A.;Lohiya,R.Attackclassificationusingfeatureselectiontechniques:Acomparativestudy.J.Ambient.Intell.Humaniz.

Comput.2020,12,1249–1266.[CrossRef]

4. Tao,P.;Sun,Z.;Sun,Z.AnImprovedIntrusionDetectionAlgorithmBasedonGAandSVM.IEEEAccess2018,6,13624–13631.

[CrossRef]

5. Ates,C.;Ozdel,S.;Anarim,E.ANewNetworkAnomalyDetectionMethodBasedonHeaderInformationUsingGreedy

Algorithm.InProceedingsofthe6thInternationalConferenceonControl,DecisionandInformationTechnologies(Codit2019),

Paris,France,23–26April2019;IEEE:NewYork,NY,USA,2019;pp.657–662.[CrossRef]

6. Sharafaldin,I.; Lashkari,A.H.; Ghorbani,A.A.Towardgeneratinganewintrusiondetectiondatasetandintrusiontraffic

characterization.InProceedingsoftheInternationalConferenceonInformationSystemsSecurityandPrivacy,Funchal,Portugal,

22–24January2018;pp.108–116.

7. Tavallaee,M.;Bagheri,E.;Lu,W.;Ghorbani,A.AdetailedanalysisoftheKDDCUP99dataset.InProceedingsoftheSecond

IEEESymposiumonComputationalIntelligenceforSecurityandDefenceApplications,Ottawa,ON,Canada,8–10July2009;pp.

1–6.[CrossRef]

8. Saleh,A.I.;Talaat,F.M.;Labib,L.M.Ahybridintrusiondetectionsystem(HIDS)basedonprioritizedk-nearestneighborsand

optimizedSVMclassifiers.Artif.Intell.Rev.2019,51,403–443.[CrossRef]

9. Leevy,J.L.;Khoshgoftaar,T.M.AsurveyandanalysisofintrusiondetectionmodelsbasedonCSE-CIC-IDS2018BigData. J.

BigData2020,7,104.[CrossRef]

10. Wang,W.;Du,X.;Wang,N.BuildingaCloudIDSUsinganEfficientFeatureSelectionMethodandSVM.IEEEAccess2019,7,

1345–1354.[CrossRef]

11. Guyon,I.;Elisseeff,A.AnIntroductiontoVariableandFeatureSelection.J.Mach.Learn.Res.2003,3,1157–1182.

12. Thangavel,N.S.G.BuildinganEfficientofFeatureSelectionUsingGreedySearchMethodforHNIDSinCloudComputing.J.

Adv.Res.Dyn.ControlSyst.2019,11,307–316.

13. Khammassi,C.;Krichen,S.AGA-LRwrapperapproachforfeatureselectioninnetworkintrusiondetection.Comput.Secur.2017,

70,255–277.[CrossRef]

14. Kohavi,R.;John,G.H.Wrappersforfeaturesubsetselection.Artif.Intell.1997,97,273–324.[CrossRef]

15. Li,Y.;Wang,J.-L.;Tian,Z.-H.;Lu,T.-B.;Young,C.Buildinglightweightintrusiondetectionsystemusingwrapper-basedfeature

selectionmechanisms.Comput.Secur.2009,28,466–475.[CrossRef]

62

Mathematics2022,10,4745

16. Mohammadzadeh,A.;Taghavifar,H.Arobustfuzzycontrolapproachforpath-followingcontrolofautonomousvehicles.Soft

Comput.2020,24,3223–3235.[CrossRef]

17. Varma,P.R.K.;Kumari,V.V.;Kumar,S.S.FeatureSelectionUsingRelativeFuzzyEntropyandAntColonyOptimizationApplied

toReal-timeIntrusionDetectionSystem.ProcediaComput.Sci.2016,85,503–510.[CrossRef]

18. Mohammadi,S.;Mirvaziri,H.;Ghazizadeh-Ahsaee,M.;Karimipour,H.Cyberintrusiondetectionbycombinedfeatureselection

algorithm.J.Inf.Secur.Appl.2019,44,80–88.[CrossRef]

19. Sarvari,S.;Sani,N.F.M.;Hanapi,Z.M.;Abdullah,M.T.AnEfficientAnomalyIntrusionDetectionMethodwithFeatureSelection

andEvolutionaryNeuralNetwork.IEEEAccess2020,8,70651–70663.[CrossRef]

20. Asdaghi,F.;Soleimani,A.Aneffectivefeatureselectionmethodforwebspamdetection.Knowl.-BasedSyst.2019,166,198–206.

[CrossRef]

21. Aslahi-Shahri,B.M.;Rahmani,R.;Chizari,M.;Maralani,A.;Eslami,M.;Golkar,M.J.;Ebrahimi,A.Ahybridmethodconsistingof

GAandSVMforintrusiondetectionsystem.NeuralComput.Appl.2016,27,1669–1676.[CrossRef]

22. Lee,J.;Park,O.FeatureSelectionAlgorithmforIntrusionsDetectionSystemusingSequentialforwardSearchandRandomForest

Classifier.KSIITrans.InternetInf.Syst.2017,11,5132–5148.[CrossRef]

23. Li,Y.;Xia,J.;Zhang,S.;Yan,J.;Ai,X.;Dai,K.Anefficientintrusiondetectionsystembasedonsupportvectormachinesand

graduallyfeatureremovalmethod.ExpertSyst.Appl.2012,39,424–430.[CrossRef]

24. Raman,M.G.;Somu,N.;Kirthivasan,K.;Liscano,R.;Sriram,V.S.Anefficientintrusiondetectionsystembasedonhypergraph

—Geneticalgorithmforparameteroptimizationandfeatureselectioninsupportvectormachine.Knowl.-BasedSyst.2017,134,

1–12.[CrossRef]

25. Zhou,Y.;Cheng,G.;Jiang,S.;Dai,M.Buildinganefficientintrusiondetectionsystembasedonfeatureselectionandensemble

classifier.Comput.Netw.2020,174,107247.[CrossRef]

26. Hua,Y.AnEfficientTrafficClassificationSchemeUsingEmbeddedFeatureSelectionandLightGBM.InProceedingsofthe

InformationCommunicationTechnologiesConference(ICTC),Nanjing,China,29–31May2020;pp.125–130.[CrossRef]

27. Seth,S.;Singh,G.;Chahal,K.K.Anoveltimeefficientlearning-basedapproachforsmartintrusiondetectionsystem.J.BigData

2021,8,1–28.[CrossRef]

28. Alazzam,H.;Sharieh,A.;Sabri,K.E.AfeatureselectionalgorithmforintrusiondetectionsystembasedonPigeonInspired

Optimizer.ExpertSyst.Appl.2020,148,113249.[CrossRef]

29. Mazini,M.;Shirazi,B.;Mahdavi,I.Anomalynetwork-basedintrusiondetectionsystemusingareliablehybridartificialbee

colonyandAdaBoostalgorithms.J.KingSaudUniv.-Comput.Inf.Sci.2019,31,541–553.[CrossRef]

30. Saeed,A.A.;Jameel,N.G.M.Intelligentfeatureselectionusingparticleswarmoptimizationalgorithmwithadecisiontreefor

DDoSattackdetection.Int.J.Adv.Intell.Inform.2021,7,37.[CrossRef]

31. Shaikh,J.M.;Kshirsagar,D.FeatureReduction-BasedDoSAttackDetectionSystem.InNextGenerationInformationProcessing

System;Springer:Berlin/Heidelberg,Germany,2021;pp.170–177.[CrossRef]

32. Patil,A.;Kshirsagar,D.TowardsFeatureSelectionforDetectionofDDoSAttack.Comput.Eng.Technol.2019,215–223.[CrossRef]

33. Ahmad,I.;Hussain,M.;Alghamdi,A.;Alelaiwi,A.EnhancingSVMperformanceinintrusiondetectionusingoptimalfeature

subsetselectionbasedongeneticprincipalcomponents.NeuralComput.Appl.2014,24,1671–1682.[CrossRef]

34. He,H.;Garcia,E.A.LearningfromImbalancedData.IEEETrans.Knowl.DataEng.2009,21,1263–1284.[CrossRef]

35. Ho,Y.B.;Yap,W.S.;Khor,K.C.Theeffectofsamplingmethodsonthecicids2017networkintrusiondataset.InITConvergence

andSecurity.InITConvergenceandSecurity;Springer:Singapore,2021;pp.33–41.

36. Bamakan,S.M.H.;Wang,H.;Yingjie,T.;Shi,Y.AneffectiveintrusiondetectionframeworkbasedonMCLP/SVMoptimizedby

time-varyingchaosparticleswarmoptimization.Neurocomputing2016,199,90–102.[CrossRef]

37. Huang,C.-L.;Wang,C.-J.AGA-basedfeatureselectionandparametersoptimizationforsupportvectormachines.ExpertSyst.

Appl.2006,31,231–240.[CrossRef]

38. Gen,M.;Cheng,R.GeneticAlgorithmsandEngineeringOptimization;JohnWiley&Sons:Hoboken,NJ,USA,1999;Volume7.

39. Pedregosa,F.;Varoquaux,G.;Gramfort,A.;Michel,V.;Thirion,B.;Grisel,O.;Blondel,M.;Prettenhofer,P.;Weiss,R.;Dubourg,V.;

etal.Scikit-learn:Machinelearninginpython.J.Mach.Learn.Res.2011,12,2825–2830.

40. Raschka,S.Mlxtend:Providingmachinelearninganddatascienceutilitiesandextensionstopython’sscientificcomputingstack.

J.OpenSourceSoftw.2018,3,638.[CrossRef]

41. Calzolari,M.Manuel-Calzolari/Sklearn-Genetic:Sklearn-Genetic0.5.1(0.5.1).Zenodo.2022.Availableonline:https://zenodo.

org/record/5854662#.Y5knyH1ByUk(accessedon18January2022).

63

mathematics

Article

Health Status-Based Predictive Maintenance Decision-Making

via LSTM and Markov Decision Process

PanZheng,WenqinZhao,YaqiongLv*,LuQian*andYifanLi

SchoolofTransportationandLogisticsEngineering,WuhanUniversityofTechnology,Wuhan430063,China

* Correspondence:y.q.lv@whut.edu.cn(Y.L.);qianlu@whut.edu.cn(L.Q.)

Abstract:Maintenancedecision-makingisessentialtoachievesafeandreliableoperationwithhigh

performanceforequipment.Toavoidunexpectedshutdownandincreasemachinelifeaswellas

systemefficiency,itisfundamentaltodesignaneffectivemaintenancedecision-makingschemefor

equipment.Inthispaper,weproposeanovelmaintenancedecision-makingmethodforequipment

basedonLongShort-TermMemory(LSTM)andMarkovdecisionprocess,whichcanprovidespecific

maintenancestrategiesindifferentdegradationstagesofthesystem.Specifically,theLSTMmodel

isfirstlyappliedtopredicttheremainingservicelifeofequipmenttodistinguishitshealthstate

quantitatively.Then,basedonthebearingresiduallifepredictioncurve,thedegradationprocess

modelisconstructed,andthecorrespondingparametersofthemodelareidentified. Finally,the

bearingdegradationcurveisobtainedbythedegradationprocessmodel,basedonwhichtheMarkov

decisionprocessmodelisconstructedtoprovideaccuratemaintenancestrategiesfordifferenthealth

conditionsofsystem. Todemonstratetheeffectivenessoftheproposedmethod,anexperimental

studywiththefulllifecycledatasetofrollingbearingsiscarriedout.Theexperimentalresultsshow

thattheproposedmethodcanachieveefficientmaintenancedecisionsforbearingsunderdifferent

healthstates,whichprovidesafeasiblesolutionforthemaintenanceofbearingsystems.

Keywords:Markovdecisionprocess;maintenancedecision-making;rollingbearing;LSTM

MSC:90C40

Citation:Zheng,P.;Zhao,W.;Lv,Y.;

Qian,L.;Li,Y.HealthStatus-Based

1.Introduction

PredictiveMaintenance

Decision-MakingviaLSTMand Withthecontinuousimprovementinmodernindustrialization,aswellastheprogress

MarkovDecisionProcess. ofsocietyandtherapiddevelopmentofscienceandtechnology,mechanicalequipmentis

Mathematics2023,11,109. https:// becomingmoreintelligent,systematicandmodular.Thefunctionsofmechanicalequip-

doi.org/10.3390/math11010109 menthavebecomeincreasinglydiversifiedtomeetthegrowingrequirementsofindustrial

production.Intheprocessoflong-termoperation,mechanicalequipmentwillbegradu-

AcademicEditor:WeiFang

allyaging,alongwithgraduallydecliningoperatingperformanceandremaininglife,the

Received:25November2022 possibilityoffailurewillincrease.Oncethefailureoccurs,itmaycausecostlyindustrial

Revised:12December2022 downtime,casualtiesorevenserioussocialimpact. Therefore,howtodesigneffective

Accepted:21December2022

maintenancedecision-makingscheme,inordertoensurethelong-termsafeandstable

Published:26December2022

operationofthemechanicalequipmentisanurgentproblemtobesolved.

Toensurethereliableandsafeoperationofequipment,theexistingresearchpaidalot

ofattentiontofaultdetectionanddiagnosisfordifferentequipmentviavariousmeans[1–4].

Copyright: © 2022 by the authors. Actually,furtherstudyoneffectivemaintenancedecision-makingmethodisalsoofgreat

Licensee MDPI, Basel, Switzerland. importance. Due to the crucial role in mechanical equipment, maintenance decisions

Thisarticleisanopenaccessarticle forbearingshavedrawnincreasingattentionofmanyscholars[5,6]. Themaintenance

distributed under the terms and decision-makingschemeforthebearingsystemisalsoourfocusinthispaper.

conditionsoftheCreativeCommons Toattainsafeandreliableoperationwithhighperformanceofequipmentandachieve

Attribution(CCBY)license(https:// thelowestpossiblemaintenancecostsatthesametime,anovelmaintenancedecision-

creativecommons.org/licenses/by/ makingmethodforequipmentbasedonLSTMandMarkovdecisionprocessisproposedin

4.0/).

Mathematics2023,11,109.https://doi.org/10.3390/math11010109 https://www.mdpi.com/journal/mathematics

65

Mathematics2023,11,109

thispaper.Tothisend,thepredictioncurveofthebearingremaininglifeisfirstlyobtained

byapplyingtheLSTMmodel.Then,thedegradationprocessmodelisconstructed,andthe

correspondingparametersareestimatedbasedonthebearingremaininglifeprediction

curve.Finally,basedonthebearingdegradationcurveacquiredbythedegradationprocess

model,theMarkovdecisionprocessmodelisappliedtoprovideoptimalmaintenance

strategiesfordifferenthealthconditionsofthesystem.Themaincontributionsofthispaper

aregivenasfollows.

(1) Anovelmaintenancedecision-makingmethodisdevelopedforrotatingmechani-

calsystem.

(2) AnLSTMmodelisadoptedtopredicttheremaininglifeofsystem,andtheremaining

lifepredictiondataareusedastheinputofthefollowingdegradationprocessmodel

toidentifythemodelparameters.

(3) Amaintenancedecision-makingmodelisconstructedbasedonMarkovdecision

processtoprovideaneffectivemaintenancesolutionforequipment.Furthermore,the

revenueofmaintenancedecisionsunderdifferenthealthconditionsisdesignedforthe

instructionofmaintenancestrategies.Moreover,themaintenancedecision-making

modelistestedontheexperimentalplatformofrollingbearings,andtheeffectiveness

oftheproposedmethodhasbeenvalidated.

Theremainderofthispaperisorganizedasfollows. InSection2,therelatedwork

isreviewed,whichsummarizesthemainresearchprogressinthefieldofmaintenance

decision-making. Section3presentstheframeworkoftheproposedmethodindetail,

including the prediction of remaining life based on LSTM and maintenance decision-

makingmodelforbearings.Theeffectivenessoftheproposedmethodisverifiedbythe

experimentalstudyinSection4. Finally,theconclusionsofthispaperaresummarized

inSection5.

2.LiteratureReview

Withthedevelopmentofscienceandtechnology,aswellasincreasingdemandfor

economicandhealthyoperationofequipment,autonomousdecision-makingandequip-

mentmaintenancedecision-makinghasdrawnincreasingattentionfromtheacademy[7–9].

Inthepastdecades,theresearchtopicofmaintenancedecision-makinghasbeenwidely

studied[10].Theexistingmethodscanbemainlydividedintotwocategories:time-based

maintenance(TBM)andcondition-basedmaintenance(CBM).

Manyscholarshavemadein-depthresearchonTBMstrategyoptimization.Buchholz,

Peteretal.[11]proposedageneralmodelofpartiallyobservablestatesandnon-exponential

fault,maintenanceandrepairtimebasedonphasedistribution.D.E.Ighravweetal.[12]

proposedafuzzyobjectiveprogrammingmodelandusedittoestablishasingleobjective

functionofmaintenanceoptimizationconsideringrandomconstraints,soastogenerate

reliableinformationforfaultmaintenanceplan.Consideringthetime-basedpreventive

maintenanceschedulingproblemundertheuncertaintyofunitlifedistribution,DeJonge

etal.[13]evaluatedthelong-termbenefitsofinitiallydelayingpreventivemaintenanceand

madethebenefitsmaximizationthroughthenumericalresearch.YimingChenetal.[14]

proposedtwooptimizationproblemsbytakingthestaticavailabilityorexpectedperfor-

mancecapacityofthesystemasthegoal.

Thecondition-basedmaintenance(CBM)isbasedonthemethodsofintegratingcur-

rentstateprediction,plandiagnosisandfuturestateprediction. Thesemethodscanbe

classifiedintophysicalmodel-basedmethods,data-drivenmethodsandhybridmethods.

GuangZou[15]developedaprobabilisticmaintenanceoptimizationmethodusingin-

formationvalue(VOI)calculationandBayesiandecisionoptimization. TheVOIbased

approachexplicitlyquantifiestheaddedvalueoffutureinspectionsandgivesthebest

decisionbydirectlymodelingdecisionalternativesandevaluatingtheirexpectedresults.

InthefieldofCBM,moreandmorescholarsusetheMarkovdecisionprocesstostudy

thedegradationprocessofequipment.Paté-Cornelletal.[16]appliedMarkovchainswith

fourstatestosimulatethedegradationprocessofproductionsystem,wheretime-based

66

Mathematics2023,11,109

maintenanceandthreecondition-basedmaintenancestrategiesareconsidered.Thelatteris

basedonproductinspection,machinesignalsandsignalsprovidedbyproductinservice.

MinouC.A.OldeKeizeretal.[17]constructedaparallelsystem,whichissubjecttoboth

faultdependenceandeconomicdependencebymaintenancecostthroughloadsharing.The

systemisformulatedasaMarkovdecisionprocess,wheretheoptimalreplacementdecision

isobtainedtominimizethelong-termaveragecostperunittime.YaqiongLvandQianwen

Zhou et al. [9] proposed an intelligent predictive maintenance system for production

equipmentmultigranularityfaultbasedonBPneuralnetworkandfuzzydecision-making,

whichsuccessfullyrealizedtheautomaticpredictivemaintenancedecision-making.Renny

Arismendietal.[18]exploredtheapplicationofpiecewisedeterministicMarkovprocess

(PDMP)tocoverdifferentmodelingassumptions,suchasnon-ignorablemaintenancedelay

andinspection-basedstatusmonitoring.

Inaddition,someresearchersconsiderthecombinationofthetwotypesofmethods

inapplications.MckoneandWeiss[19]combinedCBMwithTBMmethods.Theavailable

statusinformationislimitedtopotentialfaultsignalsthatmaybereceivedbeforetheactual

fault. Therefore,theperformanceofCBMdependsonthepredictionaccuracy. Insome

cases,TBMorthecombinationofCBMandTBMispreferred.

From the state of art and development of the study on equipment maintenance

decision-making, existingresearchhasbeendemonstratedbyrelativelyidealresearch

resultsinsomerespects.However,inthefieldofequipmentmaintenancedecision-making,

lesseffortshavebeenreportedtosystematicallymapoutthespecificmaintenancestrategies

indifferentdegradationstagesofthesystem,whichisworthytobefurtherexplored.Dueto

thesuperiorabilitytofindastrategicsolutionwithmaximumreturnandbroadapplication

prospectsinautomaticcontrolandrecommendationsystems,theMarkovdecisionprocess

hasgreatpotentialinthefieldofequipmentmaintenancedecision-making.Motivatedby

theaforementionedstudies,thispaperdevelopsanovelmaintenancedecision-making

schemebasedonLSTMandMarkovdecisionprocess,whichcanprovideeffectivemainte-

nancestrategiesindifferentdegradationstagesoftheequipment.

3.Methodology

Theframeworkofthemaintenancedecision-makingmethodproposedinthispaperis

showninFigure1.Specifically,theLSTMmodelisappliedtopredicttheremaininglife

curveoftheequipment.Then,basedonthebearingremaininglifepredictioncurve,the

degradationprocessmodelisconstructed,andtheparametersofthemodelareidentified.

Finally, the bearing degradation curve is obtained by the degradation process model,

basedonwhichtheMarkovdecisionprocessmodelisconstructedtoprovideaccurate

maintenancestrategiesfordifferenthealthconditionsofsystem.

3.1.PredictionofRemainingLifeBasedonLSTM

LSTM is a special type of Recurrent Neural Network (RNN) that can learn long-

termdependentinformation,whichhasbeendemonstratedbymanysuccessfulapplica-

tions[20,21].

ThespecificstructureofLSTMisshowninFigure2,whereXtistheinputofcellstate

attimetandHtistheoutputofcellstateattimet.LSTMrealizesinformationprotection

andcontrolthroughthreegateunitstructures,includinginputgate,forgettinggateand

outputgate.

(1) Forgettinggate

ThefirststepinLSTMistodecidewhatinformationwillbediscardedfromthecellular

state.Thedecisionismadethroughtheforgettinggate.Thegatewillreadtheoutputofthe

hiddenlayeratthelastmomentandtheinputofthecurrentcell,andthenoutputavalue

between0and1,where1means“completelypreserved”,0means“completelydiscarded”.

(2) Inputgate

67

Mathematics2023,11,109

Thenextstepistodecidehowmuchnewinformationwillbeaddedtothecellular

state. Tothisend,therearetwostepstobeperformed: first,theinputgatedetermines

whichinformationneedstobeupdated. Atanhlayergeneratesavector,whichisthe

alternativecontentforupdating.Inthesecondstep,thetwopartsarecombinedtoupdate

thecellstate.

(3) Outputgate

Finally,weneedtodeterminetheoutputvalue.Thisoutputwillbebasedonthecell

state.Firstly,werunasigmoidlayertodeterminewhichpartofthecellstatewillbeoutput.

Then,wedealwiththecellstatethroughtanh(getavaluebetween−1and1)andmultiply

itwiththeoutputofthesigmoidgate. Finally,wejustoutputthepartoftheoutputwe

determined.

(cid:1)

Figure1.Frameworkoftheproposedapproach.

(cid:1)

Figure2.LSTMStructure.

68

Mathematics2023,11,109

Throughtheabovethreegatingunits,LSTMrealizestheselectiveretentionandoutput

ofinformation,andmeanwhilesolvestheproblemofgradientdisappearanceofRNN.

The remaining life prediction based on LSTM can integrate the original learning

sampleswiththenewlearningmodetorealizethere-trainingofsamples.Itcannotonly

improvetheaccuracyofremaininglifeprediction,butalsohasthecharacteristicsoffast

convergenceandhighstability.Duetothegreatadvantagesintheprocessingofserialdata,

LSTMisappliedforremaininglifepredictionofbearingsbymakinguseofthevibration

signalsinoperation,whichalsohaveserialcharacteristics.

Inwhatfollows,theremaininglifepredictiondataobtainedbyLSTMmodelwillbe

usedtoquantifythehealthstatusofthebearing.

3.2.DegradationProcessModel

ThebearingdegradationcurveinidealconditionsisshowninFigure3.Accordingto

thecurve,thetrendofthebearingdegradationhasthefollowingcharacteristics[22]:

(1) Thenormaloperationtimeofbearingislong,accountingfor80–90%ofthewholelife

cycleofthebearing.

(2) Whenasmallcrackappearsonthesurfaceofthebearingrollingelementsorraceways,

thebearingbeginstoenterthedegradationstage.

(3) Whenthedegreeofbearingdegradationaccumulatestoacertainextent,theprobabil-

ityofbearingdamageandequipmentfailurewillincreasesignificantly

Figure3.Bearingdegradationcurve.

ThedegradationquantityofrollingbearinginacertainperiodΔtisexpressedas

Z(Δt),includingbothcontinuousdegradationquantityandsuddendegradationquantity

intheprocessofbearingdegradation. Thedegradationprocessofbearingfollowsthe

Gauss–Poissonprocess:

Z(Δt)=X(Δt)+βY(Δt) (1)

(cid:11) (cid:12)

whereX(Δt)denotesthecontinuousdegradationofbearings,andX(Δt)~N μ,σ2 .Y(Δt)

representsthequantityofdegradationduetosuddenfactors,andY(Δt)~Poisson(λ).βis

theaveragedegradationamountgeneratedbyeachsuddendegradation.

Inordertoevaluatethehealthstateofthesystem,thehealthscoreisintroducedin

theconstructionofdegradationprocessmodel. Theinitialhealthscoreofthebearingis

settobe1. Afteroperationtimet,thenormalcontinuousdegradationofthebearingis

denotedbyX(t),andthequantityofsuddendegradationis Y(t),thenthehealthscoreof

thebearingisgivenby:

t

Ht=1−∑(X(t)+βY(t))

(2)

t=0

Theparametersofthehealthstatedegradationprocesscanbeidentifiedbythehistori-

calhealthscoredegradationdata,whichisdiscussedinthefollowing.

69

Mathematics2023,11,109

Afterobtainingtheremaininglifepredictiondata,thebearinghealthscoredegradation

datacanbeobtainedfromthefollowingformula:

Ht (n)=H(t)−H(t+1) (3)

AssumethatHN (n)(n=1,2,3,...,N)isagroupofhistoricaldegradationdataofhealth

score,wherenrepresentsthestatenumber.Accordingtothehealthscoredegradationdata

HN (n),theparametersinEquation(2)areestimatedbycalculatingthecentralmomentsof

eachorderofHN (n).Theestimationofparametersisgivenasfollows:

E(HN )=μ+λβ (4)

D(HN )=σ2+λβ2 (5)

E(HN −E(HN ))3=β3λ (6)

E(HN −E(HN ))4

(7)

=3σ2+3β4λ2+β4λ+6σ2β2λ

whereμ,σ,λ,βaretheparametersofrollingbearingdegradationprocess. Thecentral

momentsofeachorderofthegroupofdataarecalculatedbythehealthscoredegradation

data,whichcanberecordedasH1,H2,H3,...,Hn. Theobtainedcentralmomentsare

expressedasa1,a2,a3,a4respectively,whichcanbecalculatedasfollows:

a1 =E(HN )=

n

1

N

∑ n

−1

HN (8)

a2 =D(HN )=

n

1

N

∑ n

−1

(HN −a1 )2 (9)

a3 =E(HN −E(HN ))3=

n

1

N

∑ n

−1

(HN −a1 )3 (10)

a4 =E(HN −E(HN ))4=

n

1

N

∑ n

−1

(HN −a1 )4 (11)

Basedontheaboveequations,eachparameteroftheGauss–Poissonprocessmodelis

givenby:

a4

λ= (cid:11) 3 (cid:12) (12)

a4 −3a2

2

3

a2

σ= a2 −

a4 −

3

3a2

2

(13)

a3

μ=a1 −(cid:11)

a4 −

3

3a2

2

(cid:12)

2

(14)

β=

a4 −3a2

2 (15)

a3

Accordingtotheabovediscussions,theparametersofthebearingdegradationprocess

arecompletelyidentified.

3.3.MaintenanceDecision-MakingModel

3.3.1.MarkovDecisionProcessModel

Thehealthscore(0–1)ofthesystemcanbeobtainedinSection3.2.Higherhealthscore

indicatesbettersystemhealthstate. Healthscore1meansthatthesystemiscompletely

healthy,andhealthscore0indicatesthatthesystemisfailed.

70

Mathematics2023,11,109

Thehealthscorecaneffectivelyrepresentthedeteriorationofthesystem,motivating

ustousetoevaluatethehealthstatusofthesystem.Thehealthscoreisdividedintofour

intervals: [1,0.8),[0.8,0.6),[0.6,0.4)and[0.4,0],correspondingtofourdifferenthealth

statesofthebearing:

Healthy(thatis,thebearingisunderacompletelyhealthystatewithonlyslightdegra-

dation),

Good(thebearingbeginstodeterioratebutisnotobvious),

Sub-health(thebearinghasbeenseriouslydegradedanditsperformancehasbeen

obviouslyreduced),

Damaged(thebearingiscompletelydamagedandcannotbeused).

Theirhealthstatesarerecordedas1,2,3,4respectively.Therefore,thehealthstateset

ofrollingbearingcanbedefinedasS={1,2,3,4},whichisacontinuousMarkovprocess.

Sincethebearingdegradationprocessiscontinuous,therollingbearingmustbeinacertain

state(health,good,sub-health,damage)atanytimeinitsfulllifecycle[23]. Thehealth

statetransitionprocessofrollingbearingisshowninFigure4,whereeachcirclerepresents

differenthealthstates,andthevalueinthecirclerepresentsthebenefitofremainingin

eachstate.

Figure4.Statetransitionprocessmodel.

3.3.2.TransitionProbability

Inthispaper,theMonteCarlomethodisusedtocalculatethetransitionprobabilityof

theMarkovprocess[24].Thetransitionprobabilitycanbecalculatedasfollows:

M

P = ij (16)

ij M

i

whereP isthetransitionprobabilityofstatefromitoj; M isthenumberofsamples

ij ij

transferringfromstateiatthelastmomenttostatejatthenextmoment,andM isthetotal

i

numberofsamplesinstatei.

3.3.3.MaintenanceEffect

Accordingtotheimpactofdifferentmaintenancemodesonbearingservicelife,the

maintenanceeffectofdifferentmaintenancemodescanberepresented,aswellastheimpact

ofdifferentmaintenancemodesonthehealthstatusofthebearing.

In this paper, the effect of different maintenance modes in this paper is given as

follows.Simplemaintenanceappliedtorollingbearingscanprolongthebearingservice

lifeby10%onaverage.Ifthebearingsarerepairedbycompletemaintenance,thehealth

scorecandirectlychangeto1. Ifweapplystatemaintenancetorepairrollingbearings,

thebearingservicelifecanbeextendedby40%onaverage. Thehealthstatestransition

probabilitymatrixunderdifferentmaintenancestatescanbeobtainedthroughthehealth

scorerepresentedbythelifeextension.

3.3.4.CostAnalysis

Differentmaintenancemodesofbearingsunderdifferenthealthconditionsbrings

differentcost, whichhassignificantimpactonthedecision-makingprocess. Thecost

includesthreeparts:

71

Mathematics2023,11,109

(1) Maintenancecosts(themaintenancecostsincurredbyvariousmaintenanceactivities);

(2) Continuousmaintenancecosts(thecostsincurredfromcontinuouscareandmainte-

nanceofrollingbearingstokeepthemhealthyandeffective);

(3) Signaldetectioncosts(thecostscausedbythevibrationsignaldetectionofthebearing

toidentifythecurrenthealthstatus).

Atpresent,thereisnouniformstandardforthemaintenancemodeandcostofme-

chanicalequipment,andthemaintenancemodesettinginthispaperisonlytoverifythe

effectivenessofthismethod.Therefore,thispaperformulatesthemaintenancecostbased

onsomemaintenanceexperience.Tosumup,thecostsofeachsimplemaintenance,state

maintenanceandcompletemaintenanceare15,40and300,respectively,wheretherelative

valueisselectedtofacilitatethecalculationofthetotalreward.

ForaMarkovdecisionprocess,Gtisdefinedasthecumulativerewardofthesystem,

whichcanbeexpressedas:

∞

Gt =Rt+1 +Rt+2 +Rt+3 +···= ∑γkR t+k+1 (17)

k=0

whereγrepresentsthediscountfactor,whichissetas1.Rtdenotestheincomeattimet.

4.ExperimentAnalysis

4.1.BearingDataAcquisition

Thedatausedinthispaperarethelifecycleexperimentaldataofbearingsfrom

Xi’anJiaotongUniversity[25].TheexperimentalplatformisshowninFigure5[26].The

acceleratedlifetestsforvarioustypesofbearings(includingrollingbearingsandsliding

bearings) under different working conditions can be carried out on the experimental

platform,wherethelifecycledataofthetestbearingscanbecollected.Themainbearing

operatingparameters,includingtheradialforceandtherotatingspeed,whichcanbe

adjustedbythetest-bed. ThetestbearingtypeisLDKUER204rollingbearing,whose

parametersareshowninTable1.

Figure5.Bearingaccelerationexperimentalplatform[26].

72

Mathematics2023,11,109

Table1.LDKUER204Bearingparameters.

Parameters NumericalValue

Diameterofinnerrace/mm 29.30

Outerringracewaydiameter/mm 39.80

Bearingpitchdiameter/mm 34.55

Basicdynamicloadrating/N 12,820

Balldiameter/mm 7.92

Numberofballs 8

◦

Contactangle/( ) 0

Basicstaticloadrating/kN 6.65

4.2.PredictionoftheRemainingUsefulLifeofBearings

Theaforementioneddataareusedfortheverificationoftheproposedmethod.Several

groupsofdatasamplesareselectedasthetrainingsetfromthebearinglifecycledata

ofXi’anJiaotongUniversity, includingBearing1_1, earing1_2andBearing1_4. While

Bearing1_5isselectedasthetestset.(Operatingcondition:speed2100r/min,radialforce

12kN,samplingfrequency25.6kHz,samplinginterval1min,samplingduration1.28s).

Theactualremaininglifeofthebearingisusedasthetrainingandtestinglabelvaluey.

Theprocessoflabelconstructionisdiscussedasfollows.label1representsthebearingstate

thatitisingoodcondition,andlabel0meansthatthebearingisincompletefailure.For

example,Bearing1–2datasethasatotalof2496groupsofdata,whichmeansthetotallife

ofthebearingis2496min.Ifthecurrentsampleisthe1000thdatum,thentheremaining

lifeofthebearingis1496min,andthevalueofthecorrespondinglabelyunderthesample

is1496/2496=0.599358. Accordingtotheremaininglifeoftherollingbearing,thedata

samples,arelabeledinthesamemanner.

TheLSTMmodelisdesignedbasedonthePythonopen-sourcedeeplearningframe-

work. Intheexperiment,theAdamoptimizerisselectedtooptimizethetrainingloss

ofLSTMmodel. Adamisapopularoptimizerinthecurrentarchitecture. Compared

withotheroptimizers,itcanlearnparametersadaptively,whichhastheadvantagesof

fastconvergence,smallmemoryrequirements,andbetterprocessingofnoisesamples.

TheobtainedlifepredictioncurveofBearing1_5isshowninFigure6,andtheprediction

accuracyrateis96.7%.

(cid:6)(cid:7)(cid:2)

(cid:2)(cid:7)(cid:5)

(cid:2)(cid:7)(cid:4)

(cid:2)(cid:7)(cid:3)

(cid:2)(cid:7)(cid:1)

(cid:2)(cid:7)(cid:2)

(cid:2) (cid:1)(cid:2)(cid:2) (cid:3)(cid:2)(cid:2) (cid:4)(cid:2)(cid:2) (cid:5)(cid:2)(cid:2) (cid:6)(cid:2)(cid:2)(cid:2) (cid:6)(cid:1)(cid:2)(cid:2) (cid:6)(cid:3)(cid:2)(cid:2) (cid:6)(cid:4)(cid:2)(cid:2)

(cid:9)(cid:8)

(cid:10)(cid:11)(cid:12)(cid:13)

Figure6.Bearinglifepredictioncurve.

Toillustrate,thestatusofbearingisprovided. AsshowninFigure7,attimepoint

400,thebearingstatusisshownastheleftbearing,whileattimepoint1400,thebearing

statusisshownastherightbearing.Itcanbeseenthattheleftbearingisingoodcondition,

73

Mathematics2023,11,109

whiletherightbearinghasbeenseverelyworn,whichisconsistentwiththelifeprediction

resultsbytheLSTMmodel.Therefore,themethodinthispapercanfitwellwiththewhole

lifedegradingtrendofthebearingsoastopredicttheremaininglifeofit.

Figure7.Bearingsintwodifferentstates.

4.3.ParametersEstimation

Atpresent,wehaveobtainedthepredictedvalueoftheremaininglifeofthebearing.

Basedonthis,wesubtractthepredictedvalueoftheremaininglifeofthebearingatadjacent

timepointstoobtainthedeteriorationofthebearinghealthscore(HN (n)),thenwecan

calculatetherelevantparametersofthemodel.

BasedonthehealthscoreofbearinglifepredictioncurveobtainedinFigure6,which

representsthedegradationquantityofbearings,theparametersofthebearingdegradation

processmodelareidentifiedasfollows:

μ=0.000243, o=0.0208β=0.000596, λ=0.400

Accordingtotheobtainedbearingdegradationprocessmodel,wecanestimatethe

bearingdegradationcurveasshowninFigure8.

(cid:6)(cid:7)(cid:2)

(cid:2)(cid:7)(cid:5)

(cid:2)(cid:7)(cid:4)

(cid:2)(cid:7)(cid:3)

(cid:2)(cid:7)(cid:1)

(cid:2)(cid:7)(cid:2)

(cid:2) (cid:1)(cid:2)(cid:2) (cid:3)(cid:2)(cid:2) (cid:4)(cid:2)(cid:2) (cid:5)(cid:2)(cid:2) (cid:6)(cid:2)(cid:2)(cid:2) (cid:6)(cid:1)(cid:2)(cid:2) (cid:6)(cid:3)(cid:2)(cid:2) (cid:6)(cid:14)(cid:15)(cid:2)

(cid:1)

(cid:9)(cid:8)

(cid:10)(cid:11)(cid:12)(cid:13)

Figure8.CurveofBearingDegradationProcess.

Basedonthebearingdegradationcurve,thetransitionprobabilityofMarkovdecision

processcanbecalculated.AccordingtothemaintenanceeffectinSection3.3,theimpactof

eachmaintenancemodeonthebearinghealthstatetransitionisdiscussedasfollows:

74

Mathematics2023,11,109

Thestatetransitionprobabilitymatrixaftersimplemaintenanceis:

⎡ ⎤

1 0 0 0

⎢ ⎥

A1=⎢

⎣

0.64 0.36 0 0 ⎥

⎦

0 0.27 0.63 0

0 0 0.09 0.91

Thestatetransitionprobabilitymatrixaftercondition-basedmaintenanceis:

⎡ ⎤

1 0 0 0

⎢ ⎥

A2=⎢

⎣

1 0 0 0 ⎥

⎦

0.14 0.71 0.15 0

0 0 0.29 0.71

Thestatetransitionprobabilitymatrixaftercompletemaintenanceis:

⎡ ⎤

1 0 0 0

⎢ ⎥

A3=⎢

⎣

1 0 0 0⎥

⎦

1 0 0 0

1 0 0 0

AccordingtoEquation(16),thehealthstatetransitionprobabilitymatrixoftherolling

bearingcanbeobtainedas:

⎡ ⎤

0.977 0.023 0 0

⎢ ⎥

A4=⎢

⎣

0.067 0.916 0.017 0 ⎥

⎦

0 0.034 0.933 0.033

0 0 0.013 0.987

Therowoftheabovematrixrepresentstheoriginalstate,andthecolumnisthestate

aftertransition.Thevaluemeanstheprobabilityoftransitionfromtheoriginalstatetothe

newstate.Finally,theMarkovdecisionprocessmodeloftheentirebearingdegradation

processisobtainedasshowninFigure9.Eachcircleofthefigurerepresentsthedifferent

healthstatesofthebearing,inwhichthevaluerepresentsthebenefitofremainingineach

state,andthevalueonthelineofcirclesrepresentsthetransitionprobabilityofeachstate.

Figure9.MarkovDecisionModel.

Tocalculatethevalueofeachmaintenancedecisiononeachstate,theBellmanequation

isusedtoiterativelycalculatethevaluefunctionofeachstate,andthefollowingresults

areobtained:RevenueinhealthystateR1=4631.84,revenueingoodstateR2=4195.92,

revenueinsub-healthstateR3=2141.21,andrevenueindamagedstateR4=0.

Thebenefitsofdifferentmaintenancemodesunderdifferentconditionsareobtained

bycombiningtheeffectsoftheabovemaintenancedecisionsondifferenthealthstatus,as

showninTable2.

75

Mathematics2023,11,109

Table2.Revenuefromdifferentmaintenancedecisions.

MaintenanceModes Health Good Sub-Health Damage

Simplemaintenance 4616.84 4429.91 2466.86 177.71

Condition-based

4591.84 4591.84 3908.72 580.95

maintenance

Completemaintenance 4331.84 4331.84 4331.84 4331.84

4.4.Summary

ItcanbeseenfromTable2thatwhentherollingbearingisinhealthystate, and

simplemaintenanceisapplied,i.e.,routinemaintenance,themaximumbenefitcanbe

obtained.Whilethebenefitofcondition-basedmaintenanceisonlyslightlylowerthanthat

ofsimplemaintenance.Whentherollingbearingisundergoodcondition,themaximum

benefitcanbeobtainedbycarryingoutappropriateconditionmaintenanceaccordingto

itscondition,andconsiderablebenefitcanbegainedbycarryingoutsimplemaintenance

orcompletemaintenanceunderthiscondition.Iftherollingbearingisundersub-health

state,thebenefitofcompletemaintenance,i.e.,directlyreplacingthebearing,isthelargest,

whichisfargreaterthanthatoftheothertwomaintenancemodes.However,iftherolling

bearinghasbeendamaged,onlywhenthebearingiscompletelyrepaired,thatistosay,the

replacementofthebearingcanobtaingreaterbenefits.

Ourconclusionsobtainedaboveareconsistentwiththehistoricalexperienceofbear-

ingmaintenance,verifyingthattheproposedmaintenancedecision-makingmethodcan

provideeffectiveguidanceforthemaintenancestrategyofrollingbearingsunderdiffer-

entstates.

5.Conclusions

Inthispaper, amaintenancedecision-makingschemeforequipmentisproposed

basedonLSTMandMarkovdecisionprocess,whichcanprovideeffectivemaintenance

decisionsforsystemunderdifferentdegradationstages.First,theLSTMmodelisadopted

topredicttheremainingservicelifetodistinguishthehealthstatequantitatively.Then,the

degradationprocessmodelisconstructed,andtheparametersofthemodelareidentified.

Withtheaidofthedegradationcurveobtainedfromthedegradationprocessmodel,the

maintenancedecision-makingmodelisestablishedbasedontheMarkovdecisionprocess.

Moreover,tofacilitatemoreappropriatemaintenancestrategyidentification,therevenueof

maintenancedecisionsunderdifferenthealthconditionsisanalyzed.Experimentalstudy

withthefulllifecycledatasetofbearingsiscarriedouttodemonstratetheeffectiveness

oftheproposedmethod.Besidestherotatingmechanicalsystems,theapplicationofthe

proposedmethodcanbefurtherextendedtootherindustrialfields.

AuthorContributions:Conceptualization,Y.L.(YaqiongLv)andL.Q.;methodology,P.Z.andY.L.

(YaqiongLv);software,P.Z.andW.Z.;validation,Y.L.(YaqiongLv),L.Q.andY.L.(YifanLi);data

curation,P.Z.andW.Z.;writing—originaldraftpreparation,P.Z.;writing—reviewandediting,L.Q.

andY.L.(YaqiongLv);projectadministration,Y.L.(YifanLi);fundingacquisition,Y.L.(YaqiongLv).

Allauthorshavereadandagreedtothepublishedversionofthemanuscript.

Funding:ThisresearchwassponsoredbytheHumanitiesandSocialScienceFoundationofMinistry

ofEducationofChina(ProjectNo.20YJC630096)andpartiallysponsoredbytheNationalNatural

ScienceFoundationofChina(ProjectNo.72101194).

DataAvailabilityStatement:Notapplicable.

Acknowledgments:Theauthorswouldliketothankalltheeditorsandreviewersfortheirinvaluable

commentsonthismanuscript.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

76

Mathematics2023,11,109

References

1. Ainapure,A.;Siahpour,S.;Li,X.;Majid,F.;Lee,J.Intelligentrobustcross-domainfaultdiagnosticmethodforrotatingmachines

usingnoisyconditionlabels.Mathematics2022,10,455.[CrossRef]

2. Chen,H.;Jiang,B.Areviewoffaultdetectionanddiagnosisforthetractionsysteminhigh-speedtrains.IEEETrans.Intell.Transp.

Syst.2019,21,450–465.[CrossRef]

3. Wu,J.;Lin,M.;Lv,Y.;Cheng,Y.Intelligentfaultdiagnosisofrollingbearingsbasedonclusteringalgorithmoffastsearchand

findofdensitypeaks.Qual.Eng.2022,11,1–14.

4. Khan,A.;Hwang,H.;Kim,H.S.SyntheticDataAugmentationandDeepLearningfortheFaultDiagnosisofRotatingMachines.

Mathematics2021,9,2336.[CrossRef]

5. Lv,Y.;Zhao,W.;Zhao,Z.;Li,W.;Kam,K.H.N.Vibrationsignal-basedearlyfaultprognosis:Statusquoandapplications.Adv.

Eng.Inform.2022,52,101609.[CrossRef]

6. Qian,L.;Pan,Q.;Lv,Y.;Zhao,X.FaultDetectionofBearingbyResnetClassifierwithModel-BasedDataAugmentation.Machines

2022,10,521.[CrossRef]

7. Wang,T.;Wu,Q.;Zhang,J.;Wu,B.;Wang,Y.Autonomousdecision-makingschemeformulti-shipcollisionavoidancewith

iterativeobservationandinference.Ocean.Eng.2020,197,106873.[CrossRef]

8. Arzaghi,E.;Abaei,M.M.;Abbassi,R.;Garaniya,V.;Chin,C.;Khan,F.Risk-basedmaintenanceplanningofsubseapipelines

throughfatiguecrackgrowthmonitoring.Eng.Fail.Anal.2017,79,928–939.[CrossRef]

9. Lv,Y.;Zhou,Q.;Li,Y.;Li,W.Apredictivemaintenancesystemformulti-granularityfaultsbasedonAdaBelief-BPneuralnetwork

andfuzzydecisionmaking.Adv.Eng.Inform.2021,49,101318.[CrossRef]

10. LaFata,C.M.;Giallanza,A.;Micale,R.;LaScalia,G.ImprovedFMECAforeffectiveriskmanagementdecisionmakingbyfailure

modesclassificationunderuncertainty.Eng.Fail.Anal.2022,135,106163.[CrossRef]

11. Buchholz,P.;Dohndorf,I.;Scheftelowitsch,D.Time-BasedMaintenanceModelsunderUncertainty.Lect.NotesComput.Sci.2018,

10740,3–18.

12. Ighravwe,D.E.;Oke,S.A.Amachinesurvivaltime-basedmaintenanceworkforceallocationmodelforproductionsystems.Afr.J.

Sci.Technol.Innov.Dev.2016,8,457–466.[CrossRef]

13. DeJonge,B.;Dijkstra,A.S.;Romeijnders,W.Costbenefitsofpostponingtime-basedmaintenanceunderlifetimedistribution

uncertainty.Reliab.Eng.Syst.Saf.2015,140,15–21.[CrossRef]

14. Chen,Y.;Liu,Y.;Jiang,T.OptimalMaintenanceStrategyforMulti-StateSystemswithSingleMaintenanceCapacityandArbitrarily

DistributedMaintenanceTime.Reliab.Eng.Syst.Saf.2021,211,107576.[CrossRef]

15. Guang,Z.;Havbro,F.M.;Arturo,G.;Kian,B.Fatigueinspectionandmaintenanceoptimization:Acomparisonofinformation

value,lifecyclecostandreliabilitybasedapproaches.Ocean.Eng.2020,220,108286.

16. Paté-Cornell,M.E.;Lee,H.L.;Tagaras,G.WarningsofMalfunction:TheDecisiontoInspectandMaintainProductionProcesses

onScheduleoronDemand.Manag.Sci.1987,33,1277–1290.[CrossRef]

17. Keizer,M.C.O.;Teunter,R.H.;Veldman,J.;Babai,M.Z.Condition-basedmaintenanceforsystemswitheconomicdependenceand

loadsharing.Int.J.Prod.Econ.2018,195,319–327.[CrossRef]

18. Renny,A.;Anne,B.;Antoine,G.PiecewisedeterministicMarkovprocessforcondition-basedmaintenancemodels-Applicationto

criticalinfrastructureswithdiscrete-statedeterioration.Reliab.Eng.Syst.Saf.2021,212,107540.

19. McKone,K.E.Guidelinesforimplementingpredictivemaintenance.Prod.Oper.Manag.2002,11,109–124.[CrossRef]

20. Greff,K.;Srivastava,R.K.;Koutník,J.;Steunebrink,B.R.;Schmidhuber,J.LSTM:ASearchSpaceOdyssey.IEEETrans.Neural

Netw.Learn.Syst.2016,28,2222–2232.[CrossRef]

21. Zhao,X.;Lu,H.;Yu,W.;Tao,B.;Ding,H.RoboticGrindingProcessMonitoringbyVibrationSignalBasedonLSTMMethod.

IEEETrans.Instrum.Meas.2022,71,1–10.[CrossRef]

22. Lei,Y.;He,Z.;Zi,Y.;Hu,Q.FaultdiagnosisofrotatingmachinerybasedonmultipleANFIScombinationwithGas.Mech.Syst.

SignalProcess.2007,21,2280–2294.[CrossRef]

23. Sun,Q.;Zhou,J.;Zhong,Z.;Zhao,J.;Duan,X.Gauss-PoissonJointDistributionModelforDegradationFailure. IEEETrans.

Plasma2004,32,1864–1868.[CrossRef]

24. Zhou,D.;Yu,Z.;Zhang,H.;Weng,S.AnovelgreyprognosticmodelbasedonMarkovprocessandgreyincidenceanalysisfor

energyconversionequipmentdegradation.Energy2016,109,420–429.[CrossRef]

25. Lei,Y.;Han,T.;Wang,B.;Li,N.;Yan,T.;Yang,J.XJTU-SYRollingElementBearingAcceleratedLifeTestDatasets: ATuto-

rial(Article).J.Mech.Eng.2019,55,1–6.

26. Wang,B.;Lei,Y.;Li,N.;Li,N.AHybridPrognosticsApproachforEstimatingRemainingUsefulLifeofRollingElementBearings.

IEEETrans.Reliab.2018,69,401–412.[CrossRef]

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

77

mathematics

Article

A Provable Secure Cybersecurity Mechanism Based on

Combination of Lightweight Cryptography and Authentication

for Internet of Things

AdelA.Ahmed1,*,SharafJ.Malebary1,WaleedAli1andAhmedA.Alzahrani2

1 InformationTechnologyDepartment,FacultyofComputingandInformationTechnology-Rabigh,

KingAbdulazizUniversity,Jeddah25729,SaudiArabia

2 InformationTechnologyDepartment,FacultyofComputingandInformationTechnology,

KingAbdulazizUniversity,Jeddah21589,SaudiArabia

* Correspondence:aaaabdullah1@kau.edu.sa;Tel.:+966-563-884-738

Abstract:InternetofThingsdevices,platformprograms,andnetworkapplicationsareallvulnerable

tocyberattacks(digitalattacks),whichcanbepreventedatdifferentlevelsbyusingcybersecu-

rityprotocol. IntheInternetofThings(IoT),cyberattacksarespecificallyintendedtoretrieveor

change/destroysensitiveinformationthatmayexceedtheIoT’sadvantages.Furthermore,thede-

signofalightweightcybersecuritymechanismexperiencesacriticalchallengethatwouldperfectly

fitresource-constrainedIoTdevices. Forinstance,identifyingthecompromiseddevicesandthe

users’dataandservicesprotectionarethegeneralchallengesofcybersecurityonanIoTsystemthat

shouldbeconsidered.Thispaperproposesasecurecybersecuritysystembasedontheintegration

ofcryptographywithauthentication(ELCA)thatutilizesellipticcurveDiffie–Hellman(ECDH)to

undertakekeydistributionwhiletheweakbitsprobleminthesharedsecretkeyisresolved. In

thispaper,threesystemsofintegrationareinvestigated,whileELCAproposessecureintegration

betweenauthenticationandencryptiontofacilitateconfidentialityandauthenticitytransfermessages

betweenIoTdevicesoveraninsecurecommunicationchannel.Furthermore,thesecurityofELCAis

provenmathematicallyusingtherandomoraclemodelandIoTadversarymodel.Thefindingsofthe

emulationresultsshowtheeffectivenessofELCAperformanceintermsofareducedCPUexecution

Citation:Ahmed,A.A.;Malebary,S.J.; timeby50%,reducedstoragecostby32–19.6%,andreducedenergyconsumptionby41%compared

Ali,W.;Alzahrani,A.A.AProvable tothebaselinecryptographicalgorithms.

SecureCybersecurityMechanism

BasedonCombinationofLightweight

Keywords:IoT;ECDH;symmetriccryptographic;authentication

CryptographyandAuthenticationfor

InternetofThings.Mathematics2023,

MSC:68M25

11,220. https://

doi.org/10.3390/math11010220

AcademicEditor:WeiFang

1.Introduction

Received:30November2022

TheInternetofThings(IoT)enablescommunicationbetweenvariousitemsandthings

Revised:23December2022

Accepted:28December2022 thathaveinternetworkingdevicesaswellastechnologicaldevices.AnIoTdeviceiscon-

Published:1January2023 figuredwithauniqueIPaddresstoperformvarioussmartapplicationswithouthuman

intervention.Moreover,IoTdevicesareextremelyheterogeneous,differintheircapabilities,

andhaveverylimitedresourcesintermsofstoragecapacityandprocessingcomplexity,

input/outputhardwarefeatures,andsourcesofenergy[1].Thecybersecuritymechanism

Copyright: ©2023bytheauthors. remainsasignificantchallengeforIoTimplementationanddeploymentduetothesoftware

Licensee MDPI, Basel, Switzerland. andhardwarevulnerabilityagainstcyberattacks.Moreover,cybersecurityhasbecomea

Thisarticleisanopenaccessarticle transversaldisciplinetoguaranteetheconfidentiality,authenticity,andintegrityofthe

distributed under the terms and generateddata,transmittedand/orstoredonIoTdevices.Privacyandsecuritymustbe

conditionsoftheCreativeCommons ensuredbythecybersecuritymechanismtogeneratetrustindata,whichisadecisivefactor

Attribution(CCBY)license(https://

inmakingcriticaldecisionsforthedevelopmentofallareasinvolvedinthisinterconnected

creativecommons.org/licenses/by/

world.Generally,cyberattacksutilizetheinternettogainunauthorizedaccesstodisable

4.0/).

Mathematics2023,11,220.https://doi.org/10.3390/math11010220 https://www.mdpi.com/journal/mathematics

79

Mathematics2023,11,220

IoTdevices,anddestroyanddisruptthecriticalinformationoftheIoT[2–6].Regardless

ofthenetworkstructurelayers,theIoTissusceptibletonumerouskindsofattacksatthe

application,network,andsensinglayers. Theaccesscontrolmechanismcaneffectively

monitortheaccessactivitiesofresourcesbylegitimateusers[3].Forinstance,cyberattacks

causedangerouscompromisesontheIoTthestrengthsofwhichincludesensorimpris-

onment,knownkeysecurity,stolen-verifierandcontrolledinformation,denialofservice

(DoS),linksniffing,man-in-the-middle,forceddelay,sessionhijacking,bruteforce,and

dictionaryattacks[7–10].Furthermore,keydistributionisthepredicamentofthesymmet-

riccryptography,anditrepresentstheessentialchallengetaskinaresource-constrained

systemsuchastheIoT.OneofthepracticalsolutionsisusingECDH,whichisconsidered

anappropriatesolutionforsecretkeydistributionamongIoTdevices.Thisisprimarily

duetoECDHhavingasmallerkeysizewithhighersecuritystrengthcomparedtoanRSA

cryptosystem[11].Furthermore,ECDHrequiresfewerCPUresources,whichcausesless

powerconsumptionandprocessingdelaycomparedtoRSA.

Figure1illustratesthescenarioofacyberattackthatcancompromisethechannel

communicationbetweenthesensordevicesandtheIoTgatewayorcompromisetheIoT

cloud networks. The standard cryptosystem solutions (e.g., RSA, AES, DES) require

theimperativecomputationoverhead,longkeysize,highmemorycapacity,andlong

processingdelay. Asaresult,theycannotbeappliedimmediatelytothetechnologyor

sensorswiththelowestresourcerequirements,suchastheIoT.Therefore,itisadifficulttask

tobuildeffective,quick,small,andsafecryptographictechniquesfortheIoT.Additionally,

theIoTnetworksshouldputinplaceaminimalcybersecuritysystemtoguardagainst

unauthorized attackers disclosing sensitive information and to confirm that users are

permittedtouseIoTservices(e.g.,authenticationandaccesscontrol)[12–19].

Figure1.ScenarioofcyberattacksontheIoTnetwork.

Cryptography,digitalsignature,andauthenticationaretheessentialsolutionstode-

fendagainstcyberattacksontheIoT.Oneofthetwowidelyusedencryptiontechniques

symmetric(privatekey)orasymmetric(publickey)encryptioncanbeusedwithIoTcryp-

tography.Thesamekeyisusedforthecryptographicoperationinsymmetricencryptions

atboththesourceandthedestination. ThedistributionoftheprivatekeyamongIoT

devicesdetermineshowstrongthesymmetricencryptionis. Asopposedtosymmetric

encryptions,asymmetricencryptionsusetwodistinctkeys:thepublickeyandtheprivate

key.Thepublickeycanbecommunicatedacrossasecurechanneltotheauthorizeddevices,

whiletheprivatekeyiskepthiddenandnevershared.

Whileencryptioncanguaranteeprivacy,messageauthenticationcanguaranteeauthen-

ticity/integrityofthereceiveddata.Nevertheless,IoTsystemsneedbothauthentication

andconfidentiality.Itmaybeattractivetointegrateencryptionandauthentication;how-

ever,notallcombinationswillprovidebothprivacyandauthentication.Certainly,itisa

80

Mathematics2023,11,220

verydifficulttasktocombinecryptographictoolssecurely,whichmeansthat,sometimes,

outstandingcryptographictoolscanbeintegratedinawaythatproducesaninsecure

combination.Consequently,withoutprovensecurityofaspecificcombination,itisrisky

touseit. Thepopularmethodstomergemessageauthenticationandencryptioncanbe

describedasfollows[11]:

• Method1: Encrypt-and-authenticate(EAT),whichmeanstheoriginaldatashould

beencryptedusingK1asC=E

k1

(M)andthemessageauthenticationcodeshouldbe

calculatedusingK2asT=MAC

k2

(M).Thesendingmessageisthepair(C,T),which

shouldbesentseparatelyasshowninFigure2a.

• Method2:Authenticate-then-encrypt(ATE),whichmeansthetagTisfirstcalculated,

andthentheoriginaldataandTareencryptedtogether. Thesendingmessageis

C=E (M+T)whereT=MAC (M)asillustratedinFigure2b.

k1 k2

• Method3:Encrypt-then-authenticate(ETA),whichmeanstheoriginaldataMisfirst

encryptedusingK1asC=E

k1

(M),andthenthetagTiscalculatedoverC.Thesending

messageisthepair(C,T)whereT=MAC (C)asillustratedinFigure2c.

k2

Figure2.Integrationmethodsbetweenencryptionandauthentication:(a)Encrypt-and-authenticate;

(b)authenticate-then-encrypt;(c)encrypt-then-authenticate.

81

Mathematics2023,11,220

1.1.AdversaryModelonIoT

ThemaingoalofanadversarycyberattackagainsttheIoTistodisruptitscontrol

function by taking advantage of one or more weaknesses that a malicious adversary

couldusetopenetratetheIoTenvironment’ssecuritysystem[20–22]. Theadversaryis

presumptivelycapableofreading,transmitting,andfakingIoTnetworktraffic,whichcould

raiseconcernsaboutsenseddata,IoTdeviceprivacy,andIoTgatewaycontrolmanagement.

ThemostcrucialadversaryattacksonELCAaredescribedasfollows:

• Spoofingattack.ToobtaintheIoTdevicecredentialneededtoaccessthesenseddata,

theattackerinterceptsoreavesdropsontheIoTnetworktraffic.

• Aman-in-the-middle.Inthisattack,themaliciousadversaryhastheabilitytoconnect

toanyIoTdeviceandlistentoanynetworkdata.Additionally,theadversarycanalter

thecapturedmessagesbeforetheyaretransmittedtothereceiverifitengagesinactive

man-in-the-middlebehavior[8].

• Areplayattacks. Areplayattackcreatesareplicaofthemessagetobeusedlater,

asopposedtotransmittingitdirectlytotherecipient. Anopponentdoesthisby

interceptingthedataanddelaying,replaying,orretransmittingit.

• Abruteforce.EventhoughthedomainparametersthatbothpartiesuseforECDH

are adequately robust, the malicious adversary in this attack tries every possible

combinationofletters,digits,andcharacterstocrackthesharedsecretkey.

• Asensorcaptureattack.Inthisattack,theimpostoradversaryseizesasensornode

andtakesthesharedsecretkeyandshareddomainparametersinordertocarryout

unethicalactivitiesontheInternetofThingsnetwork.

• Astolen-verifierattack.Iftheimposterattackerhasobtainedthesharedsecretkey

fromanIoTdevice,theycanpretendtobeanauthorizeddevicetolaunchattacks

againstotherIoTdevices,stealdata,orgetaroundaccesscontrols.

1.2.ResearchMotivation

Themotivationoftheproposedmethodistodevelopacybersecuritymechanismthat

securelycombinesalightweightcryptographywithauthenticationtopreventacyberattack

andfittheresource-constrainedIoTsystem.Inaddition,theproposedsolutionprotectsIoT

messagesfrommodification,andspoofingattacks.

1.3.ResearchContribution

Thefollowingcontributionsarereportedinthisresearch:

• Itproposesalightweightsymmetricencryptionbasedonthescalarmultiplicationof

thehashfunctionandthebasepointoftheellipticcurve.Themodularmultiplicative

basedonorderofbasepointhasbeenusedtocreatethefinalciphertext.Additionally,

theproposedELCAconfidentiallydistributesasharedsecretkeybetweenIoTparties

overaninsecurecommunicationchannelusingtheECDHmethod.Indeed,thesecure

sharedkeyisanephemeralthatresolvestheweakbitsproblemandisrecommended

byRFC8442toprovideperfectforwardsecrecy.

• Itproposesanefficacioussecurecombinationbetweenauthenticationandencryption

tofacilitateconfidentialityandauthenticitytransfermessagesbetweenIoTdevices

overaninsecurecommunicationchannel.

• Acomprehensivecryptanalysisbasedontherandomoraclemodelmathematically

provesthesecurityoftheproposedcombinationbetweenauthenticationandencryp-

tionontheIoT.

• Thewell-knownIoTadversarymodelisalsoexploitedtoverifythesecuritystrength

andtoprovethesecurityoftheproposedscheme.

• Finally,theperformanceofthesuggestedELCAisalsoevaluatedintermsofCPU

executiontime,powerconsumption,andstoragecostthroughanumberofemula-

tionexperiments.

82

Mathematics2023,11,220

Therestofthispaperisorganizedasfollows:therelatedworksonauthenticationand

encryptionoveranIoTplatformispresentedinSection2.Thealgorithmoftheproposed

ELCAisexplainedinSection3.Additionally,Section4describesthecybersecurityanalysis

fortheELCAmechanisms. TheimplementationandevaluationofELCAontheIoTis

presentedinSection5. Finally,Section6presentstheconclusionandfuturework. All

notationsusedinELCAaresummarizedinTable1.

Table1.Frequentlyusednotation.

Notation Meaning Notation Meaning

ConvertingMtothe

C Ciphertext m

integernumber

Messageauthentication

CCA Chosen-ciphertextattack MAC

code

CPA Chosen-plaintextattack n OrderofG

Anextrapointatinfinityof

CMA Chosen-messageattack O

thecurve

d Privatekey P Modularprime

D Destinationnode Pb Randompointinthecurve

Ellipticcurve

ECC Pb.X1 XcoordinateofPb

cryptography

Ellipticcurve Probabilisticpolynomial

ECDH PPT

Diffie–Hellman time

Effective,lightweight

ELCA cryptographicand PRF pseudorandomfunction

authentication

Existentiallyunforgeable

EU-CMA underchosen-message Q Publickey

attack

G Basepointgenerator ROM Randomoraclemodel

h Subgroupcofactor S Sourcenode

Indistinguishability

IND-CPA

chosen-plaintextattack

SSK/XK Sharedsecretkey

M Plaintextmessage T Authenticationtag

2.RelatedWorksonCryptographicandAuthenticationAlgorithms

Asmallnumberofstudieshavepreviouslybeenestablishedtofitresource-constrained

devices,particularlyforsensorsandactuatorsonIoTnetworks,despitethefactthatmany

academicshaveinvestigatedthesecurityalgorithmsontheIoT.Inourearlierwork[23],

thedigitalcertificateauthoritywasusedtolinkapublickeytoitsownerusingadigital

certificate,therebyauthenticatingthesender’sgenuineidentity. Therefore,therelated

effortsinthisresearchfocusoncreatingsimplecryptographicalgorithmsandlightweight

authenticationacrossIoTnetworks.

Ellipticcurveintegratedencryption(ECIES),whichiscombinedwithadvancedstan-

dardencryptionandisknownasECIESAES,wasproposedbyV.Shoup. Additionally,

ECIESincludesrabbitencryption,knownasECIESRa,inaccordancewiththespecifications

inRFC4503.NISTproposedalightweightauthenticatedencryptionwithassociateddata

(AEAD)thatcanoperatewithadevicethathaslimitedresources,suchasanInternetof

Thingssystem[24].TheencryptionandtagprovidedbyAEADcanbeusedasamessage

authenticationcode(MAC).AEADprovidesdataauthentication,confidentiality,andin-

tegrityasaresult.TomatchanIoTresource-constrainedsystem,ByoungjinSeoketal.[25]

createdsecuredevice-to-devicecommunicationusingtheconceptsofAEADandECC.

83

Mathematics2023,11,220

Asecuredatasharingmechanismfordevice-to-devicecommunicationonthe5Gmobile

systemwaspresentedbyAtefehetal.[26].Thevirtualcheckconceptwasusedinthisstudy

asasystemofencouragementtoencouragemanipulators’involvementinthedevelopment

ofdatasharing.InthestudysuggestedbyAdeeletal.[27],apublickeyinfrastructure(PKI)-

basedlightweightauthenticationmethodwascombinedwithellipticElGamalencryption.

Additionally,Yasiretal.[28]createdasmallcryptographicsystemthatreliesonECCand

ElGamaloverpublickeyinfrastructure(EEoP).Additionally,Adeletal.[29]proposed

apowerfulmultifactorauthentication(CMA)systemthatmakesuseoftheconceptof

combiningvarioushashfunctionswithgeolocationauthenticationovertheIoT.Inorderto

verifythekeygeneration,Sciancaleporeetal.[30]integratedECDHexchangewithadigital

certificate.Inordertoenhanceuserauthentication,MohammadAyoubetal.[31]createda

secureECC-basedauthenticationandencryptionsystemthatmakesuseofusercredentials

andbiometricparameters. SecureIoT(SIT),whichmakesuseofa64-bitkeyofFeistel

andaconsistentsubstitution–permutation,wasproposedbyMuhammadU.etal.[32].

Shahetal.[33]presentedtheintegrationofDiffie–Hellman-basedcryptographyandau-

thentication.ToshareasecretkeythroughtheInternetofThings,multifactorauthentication

isused.One-timepasswords(OTPs)thatrelyonECCandisogenytoensureIoTsecurity

wereproposedbyBadisHammietal.[34].TheOTPbasedonECC’sunpredictabilityisnot

guaranteedthough.Asafesystemwithprivacyandauthenticationbasedonthreefactors

wasproposedbyRangwani,D.etal.[35].

Thelimitationsofthepreviousliteraturestudies[23–35]aresummarizedinTable2.In

thistable,themainlimitationscanbespecifiedinfourfacts:First,theintegrationbetween

authenticationandencryptionhasnotbeenproventobesecure.Second,theoutstanding

constructionoftheIoTandtheresourceconstraintshavenotbeenconsidered. Third,

thevulnerabilitiesofECDH(i.e.,weakbitsandchosen-ciphertextattack)havenotbeen

resolvedandrecovered.Finally,thecryptanalysisunderarandomoraclemodelhasnot

beeninvestigated.

Table2.SummaryofRelatedWorks.

Approaches DatePublished MethodologyandFeatures Limitations

Itprovidedthecipherandthetagthat

Itdoesnotprovidesecure

AEAD[24] 2020 offersdataconfidentiality,integrity,and

integration.

authentication.

InordertoaccommodateanIoTsystem

withlimitedresources,itdevelopeda Thecryptanalysiswasnot

B.Seoketal.[25] 2020

securedevice-to-devicecommunication studied.

usingtheconceptsofAEADandECC.

Inordertomanagethepublickey

Itlackstheadversarymode

Adeeletal.[27] 2019 infrastructure(PKI),itcombinedthe

analysis.

twoalgorithmsElGamalandECC.

Itcreatedasmall-scalecryptography Thecryptanalysiswasnot

Yasiretal.[28] 2017

systemthatutilizesECCandElGamal. studied.

Itproposedasecuremultifactor

authentication(CMA)thatusesrobust Thetimeprocessing

Adeletal.[29] 2019

combinersofthehashfunctionsand complexityishigh.

geolocationauthenticationoverIoT.

Duetotheimplicitcertificate’s

Toverifythekeygeneration,ECDH

powerconsumption,itdoes

KMP[30] 2017 exchangeandadigitalcertificatewere

notfitIoTresource

included.

constraints.

84

Mathematics2023,11,220

Table2.Cont.

Approaches DatePublished MethodologyandFeatures Limitations

ItcreatedasecureECC-based

Duetothevulnerabilityof

authenticationandencryptionsystem

biometricparametermistake,

M.Ayoubetal.[31] 2020 thatstrengthensuserauthenticationby

itdoesnotfitIoTresource

usingpersonalinformationand

constraints.

biometrics.

Itusedtheideaofcombination64-bit Duetopowerconsumption,it

SIT[32] 2017 keyofFeistelandauniform doesnotfittheIoTresource

substitution–permutation. limitations.

ToshareasecretkeyviaanIoT

network,itintegratedauthentication Itdoesnotprovethesecurity

Shahetal.[33] 2017

andcryptographybasedon forintegration.

Diffie–Hellman.

ItproposedOTPthatreliesonECCand TherandomnessoftheOTP

B.Hammietal.[34] 2020

isogenytoguaranteeIoTsecurity. basedonECCisnotensured.

Itsuggestedasafe,private,and Itdoesnotstudytheeffectof

Rangwani,D[35] 2021 three-factorauthenticationmechanism three-factorauthenticationon

fortheInternetofThings. theoperatingsystem.

3.SystemDesignofELCAAlgorithm

ThesystemdesignoftheproposedELCAalgorithmmainlyconsistsofkeymanage-

mentbasedonECDH,symmetricencryptionalgorithmwitharandompaddingsystem,

andmessageauthenticationbasedonmultifactorhashfunction.Thisresearchproposes

secureintegrationbetweensymmetriccryptographyandauthenticationbasedonmethod3

(e.g.,encrypt-then-authenticate).Thethreealgorithmsareorganizedtoguaranteecyberat-

tackprotectionsontheIoT.Thethreeproposedfunctionsinthisstudywerecreatedunder

thefollowingpresumptions:

• TheIoTgatewayhasarobustsecuritymechanismandhencecannotbecompromised.

• Thesharedsecretkey(SSK)iscalculatedbasedonECDHanditisconsideredasthe

privatekeyoftheELCAcryptography.

• SSKinallIoTdevicesusesthepreinstalledtwosecurekeys:thepublickey,whichis

calculatedatallinvolvedIoTdevices,andtheprivatekey,whichisnotknownpublicly.

• Allkeysintheproposedsystemareephemeral(dynamic),whichmeanstheymustbe

changedineachnewsession.

• ThedomainparametersoftheECDHareinsertedandprogrammedintoallIoTdevices

duringtheinitializationsession.

• ThedetailofELCAisexplainedinthefollowingsections.

3.1.KeyManagementAlgorithmBasedonECDH

The exchange of the common secret key between the IoT devices is the essential

concern in traditional symmetric cryptography. This is primarily due to the insecure

communicationchannelthatmakesIoTdevicessusceptibletomanycyberattacks.Conse-

quently,theproposedencryptionmechanismutilizestheECDHtosecurelycalculaterather

thandistributeanewSSKforeachtransmissionsessionbetweenIoTdevices(i.e.,forward

secrecy).Theellipticcurveisasetofpointsidentifiedbysolvingthefollowingequation:

(cid:13) (cid:30) (cid:14)

E= (x,y)(cid:30) y2=x3+ax+b ∪{O},

wherea,b∈K(Z/PZ)satisfy(4a3+27b2)(cid:9)=0 (1)

whereKpresentsanintegerfinitefieldoveramodularprimeP.Anextrapointatinfinity

(e.g.,O)hasbeenaddedtotheequationtoaddanypointtoitself. LetusassumethatS

andDaretheIoTsourceandtheIoTdestination,respectively.Thedomainparametersof

85

Mathematics2023,11,220

ellipticcurveconsistofp,G,n,hwhicharetheprimenumber,thebasepointgenerator,the

orderofG,andthesubgroupcofactorthatisusually1.Theseparametersdemonstratethe

agreedinformationbetweenSandDtoutilizetheECDHkeyexchangeprotocol.Ineach

newsession,theprivatekeyatSandDisgeneratedusingtherandomfunction,which

isselectedbetween1andn-1.Thepublickeyisapointinthecurve,namelyQ,whichis

producedusingscalarmultiplicationofdandG(e.g.,Q=d×G)asshowninFigure3.In

thisfigure,Shasakeypair(dS,QS)andD(dD,QD),whichrepresenttheprivateandpublic

keysateachnode.EachSandDshouldreceivethepublickeyfromtheotherpartypriorto

implementingtheECDHprotocol.Later,ScomputesitsSSKpointasK(XK,YK)=dS ×QD

andDcomputesitsSSKpointasK(XK,YK)=dD ×QS.Asaresult,theagreedSSKisthex

coordinateofthepointK,whichisk1=XK.Moreover,k2=YKrepresentstheagreedSSK

forauthentication.ItisinterestingtonotethattheSSKthatiscalculatedbybothparties

isequalbecausedS ×QD=dS ×dD ×G=dD ×dS ×G=dD ×QS,where“×”denotes

ellipticcurvescalarmultiplication.

Figure3.ECDHkeymanagement.

3.2.SecureIntegrationbetweenEncryptionandAuthentication

Thecombinationbetweenencryptionandauthenticationshouldbecarefullydesigned

becauseitisveryhardtocombinecryptographictoolscorrectlytoprovidebothprivacy

andauthenticity.Thismeansthatexcellentcryptographictoolscansometimesbeapplied

inawaysothattheresultisnotsecure. Thisresearchproposessecureintegrationbe-

tweensymmetriccryptographyandauthenticationbasedontheencrypt-then-authenticate

methodcalledELCA.InordertofitthemaximumtransmissionunitintheIoTnetwork,

themessageMisparsedintoseveralchunksbasedonSecp192r1ellipticcurvedomain

parameters[36].Hence,themaximumsizeofeachchunkis127bytes,andtheminimum

sizeis24bytes. ThecryptographicstepsofELCAatthesourcenodeareimplemented

asfollows:

• CalculateE=StrToInt(Hash(XK));theHashisasecurecryptographichashfunction

suchasCMA[29]orSHA-256[37].

• CalculatethecurvepointPb(X1,Y1)=E×G;theECCscalarmultiplicationhasa

one-wayfunctionproperty,whichmeansitishardtoreverse.

• CalculatetheciphertextC

i

=(m

i

×X1)modn;whereirepresentsthechunknumber.

Thepaddingschemeisusedtoconvertthechunk(M)totheintegernumberm,which

i i

shouldbeagreeduponinreversibleprotocol.

86

Mathematics2023,11,220

• CalculateahashfunctionforC asZ=StrToInt(Hash(C))modn.

i

• CalculatetheauthenticationcodeasTs=(YK ×Z)modn;

• Thetransmittedmessageisthepair(Ci,Ts).

ThecryptographicstepsofELCAatthedestinationnodeuponreceivingthepair

(Ci,Ts)areperformedasfollows:

• CalculateahashfunctionoftheintegernumbermasZ=StrToInt(Hash(C))modn

i

whereHash()representsthesimilarcryptographichashfunctionthatisusedinthe

encryptionprocess.

• CalculateT

d

=(YK ×Z)modn.

• IfT

d

=Ts,themessageisaccepted(e.g.,messageisauthentic,andintegritychecked).

Otherwise,themessageisrejected.

• Ifthemessageisaccepted,calculateE=StrToInt(Hash(XK)).

• CalculatethecurvepointPb(X1,Y1)=E×G.

• Calculatem

i

=(C

i

×X1 −1)modnwhereX1 −1modncanberesolvedusingamodular

multiplicativeinverse.

• Convertthem tostringM andrecovertheplaintextM=whereListhenumber

i i

ofchunks.

Figure4showstheflowphasesandAlgorithm1presentsthepseudocodeofthe

ELCAalgorithm.Inthesefigures,thesourcenodeandthedestinationmustusethesame

domainparametersoftheECDHequation. Uponthepublickeybeingcalculatedatthe

twoparties,itissenttotheotherparty,whichcancalculatethesharedsecretkey.Finally,

thecombinationofencrypt-then-authenticateinELCAisutilizedasexplainedabove.

Figure4.FlowdiagramofELCAalgorithm.

87

Mathematics2023,11,220

Algorithm1PseudocodeofELCAalgorithm

ELCAatIoTSender(S)

Input:Secp192r1domainparametersp,a,b,G,n,h;

Output:QS,T,C;//QS:PublickeyofS,T:authenticationtagC:Ciphertext

StartAlgorithm(ELCA)

1 |While(newsessionstart)do

2 | Determinetheprivatekey(dS);//1≤dS ≤n

3 | QS=(dS ×G);//QS:thepublickeyofS

4 | Send_Public_key(QS);//Sendthepublickeytodestination

5 | Receive_Public_key(QD);//ReceivethepublickeyofD

6 | K(XK,YK)=dS ×QD;//calculatethesharedkey

7 | For(i=0;i<L;i++)//L:numberofchunks

8 | mi=StrToInt(Mi);//converttheplaintexttoaninteger.

9 | E=StrToInt(Hash(XK))modn;//E:thehashfun.ofkeyXK

10 | Pb(X1,Y1)=E×G;

11 | Ci=(mi ×X1)modn;//Ci:theciphertextofmessagemi

12 | Z=StrToInt(Hash(Ci))modn;//hashfun.forintegerm.

13 | TS=YK ×Zmodn;//TS:Authenticationcodeatthesender

14 | Send(“Ci”+”TS”);//Thesourcesends“Ci”+”TS”toD

15 | End;//ForLoopStatement

16 | End;//Whileloop

17 End;//Algorithm

ELCAatIoTReceiver(D)

Input:thedomainparametersp,a,b,G,n,h;

Output:QD,TS,C;//QD:PublickeyofD

18 StartAlgorithm(ELCA)

19 |While(newsessionstart)do

20 | Determinetheprivatekey(dD);//1≤dD ≤n

21 | QD=(dD ×G);//QD:thepublickeyofD

22 | Send_Public_key(QD);//Sendthepublickeytosourcenode

23 | Receive_Public_key(QS);//Receivethepublickeyfromsource

24 | K(XK,YK)=dD ×QS;//ifQSisavalidcurvepoint,thesharedkeywillbe

calculated

25 | Foreach(msgreceived;i++)do

26 | Get(TS,Ci);//Receivethemessagepair(TS,Ci)

27 | Z=StrToInt(Hash(Ci))modn;//hashfun.forC

28 | TD=YK ×Zmodn;//TD:Authenticationcodeatthedestination

29 | IfTd=Ts,themessageisaccepted.Otherwise,themessageisrejected.

30 | E=StrToInt(Hash(XK))modn;

31 | Pb(X1,Y1)=E×G;

32 | mi=(Ci ×X1 −1)modn;//Recoverthepaddedmessage

33 | For(i=0;i<L;i++)//L:numberofchunks

34 | Mi=Convert_IntToStr(mi);//convertintegertoplaintext.

35 | M=M+Mi//concertanteallchunks.

36 | End;//forloop

37 | End;//Whileloop

38 End;//Algorithm

4.CybersecurityAnalysis

InordertomeasurethesecuritylevelofELCA,thecryptanalysisforELCAontheIoT

wasdevelopedandanalyzed.

4.1.CryptanalysisofELCA

Letusimaginethat,evenifthesharedsecretkeyisunknown,theadversarymay

decryptencryptedmessagesandbypasstheauthenticationandencryptionoftheELCA

mechanism.Thefollowingaresomeexamplesofthemosttypicalcryptanalysisattacksthat

havebeenstudiedusingtherandomoraclemodel:

88

Mathematics2023,11,220

• Chosen-plaintextattack(CPA).Itisexpectedthattheadversarywillobtainthecipher-

textsforanyplaintextsofitschoosing.Additionally,theadaptiveCPA(CPA2)allows

theadversarytoselectafreshinputforELCA(ELCAE)encryptionbasedonananalysis

oftheplaintextquerieshepreviouslyselectedandtheaccompanyingciphertexts[38].

ByassumingthatanadvertiserAhasaccesstoanencryptionoraclewithanypair

ofequal-lengthmessages(m1,m2)asinput,wecandescribethedefinitionofCPA

mathematically[20–22].

Definition1.LetELCAE=(K,E,D)beanencryptionmechanisminELCA,Eisencryption,Dis

decryption,andKisthespaceofallkeys.Theadvantageofindistinguishabilityofchosen-plaintext

attack(IND-CPA)ofAisdefinedas:

Advi E n L − CA cP E a(A) = −P P r r [ [ k k ← ← K K ; ; C C ← ← E E k k ( ( m m 2 1 ) ) : : A A ( ( C C ) ) = = 1 1 ] ] (2)

• IftheadvantageofIND-CPAisnegligible,whichindicatesthatAisstruggling,the

aforementioned equation demonstrates that ELCA is secure. Contrarily, ELCAE

is not stable if the IND-advantage of CPA is non-negligible, indicating that A is

performingwell.

• Chosen-ciphertextattack(CCA).Itisexpectedthattheadversarywillobtainthe

decryptionofanyciphertext(s)ofitschoosing.AfurtherbenefitoftheadaptiveCCA

(CCA2)isthattheadversarycanselectafreshinputforthedecryptionofELCA

(ELCAD)basedontheanalysisofhispreviouslychosenqueries[39].

Definition2.LetELCAE=(K,E,D)beanencryptionmechanisminELCA,andAisanadversary

whocanaccesstheencryption(E)anddecryption(D)oracle.TheadvantageofIND-CCAofAis

definedas:

Advi

E

n

L

−

CA

cc

E

a(A)=Pr [k←

b (cid:16)

K

←

;C

A

←

(E

E

( k .

(

)

m

,D b

);

(

b

.)

←

):

{

b (cid:16)

0,

=

1}

b

;

] (3)

k k

Accordingtotheaforementioneddefinition,theadversaryisfreetoaccessthedecryp-

tionoracleatanytimeandwithanyciphertextC,withtheexceptionofthepreviously

answeredqueriesfromitsencryptionoracle.Therefore,iftheadversarywhowasprovided

accesstotheoraclesmayfindlittlebenefitindifferentiatingthetwooccurrencesofb(0/1),

thenELCAEcanberegardedsecureagainstIND-CCA.

4.1.1.CryptanalysisofCombinationbetweenCryptographicTools

Thecombinationcryptanalysiswilluseanallornothingapproachtovalidateboth

messageconfidentialityandauthenticationforeverypossiblecombinationbetweenthem.

Thisdoesnotmeanthatthecombinationisnotalwayssecureforeveryencryptionand

authentication;however,itmeansthereexistsevenonecasewherethecombinationis

notsecure. ThesecuritylevelthatshouldbeconsideredintheanalysisisIND-CPAfor

encryption and existentially unforgeable under chosen-message attack (EU-CMA) for

authentication.Thetwoattacks(e.g.,IND-CPAandEU-CMA)meettherequirementfor

gainingchosen-ciphertextsecuritytogetherwithexistentialunforgeability.Generally,the

proposedcryptanalysisapproachtoprovethesecurityforthecombinationistoprovethata

givencombinationmeetsthedefinitionofthesecurecommunicationchannel[11].Lettuple

ofalgorithms(K,ET,D,V)beacombinationof(K,E,D)and(K,T,V),whereKrepresents

theECDHkey-generationalgorithmandproducessharedsecretkeys(k1=XK,k2=YK).

ThecombinationalgorithminELCAisrepresentedbyET,whichreceivesapairofkeys

(k1,k2)andamessagemasinputandoutputsCandauthenticationtagT.Furthermore,V

representstheverificationprocedureinELCA,whichappliesacombinationofE(XK)and

89

Mathematics2023,11,220

T(YK)uponreceivingapairofkeys(k1,k2)andavalueCand/orT.Latterly,Voutputs1or

0. TheDrepresentsthedecryptionalgorithminELCA,whichappliesacombinationof

E(XK)andT(YK)uponreceivingapairofkeys(k1,k2)andavalueC.Finally,Drecoversthe

originalmessagem.

Thesatisfactoryrequirementisthatforeveryk1=XK,k2=YK,andforeveryvalue

m,D (ET (m))=mandV (ET (m))=1. Thecombination(K,ET,D,V)is

k1,k2 k1,k2 k1,k2 k1,k2

requiredtosatisfybothaCCA-securityandauthenticationsecurityforET asdefined

k1,k2

inthefollowing:

Definition3. ELCA=(K,ET,D,V)isconsideredasasecurecombinationofencryptionand

authenticationif(K,E,D)hasIND-CPAandthescheme(K,T,V)isEU-CMA.

NextweanalyzethethreecombinationapproachesthatareillustratedinFigure2.

• Encrypt-and-authenticate(EAT).Thiscombinationcanrevealtheoriginalmessagem

foranyencryptionmechanism.Forinstance,if(K,T,V)providesasecuremessage

authenticationcodeand T (m)=(m, T(m)),itdoesnotnecessarilyimplyprivacy.

k k

Hence,thecombination(E (m),T (m))completelyrevealsmandisthereforenot

k1 k2

IND-CPA.Asaresult,theEATdoesnotyieldasecurecombinationofencryptionand

messageauthentication.

• Authenticate-then-encrypt(ATE).Letusdiscussthecontrivedencryptionexample

thatsufficestoshowthattheATEmethodisnotalwayssecure.

(cid:2) Letusassumethatthereexistsanencryption(E (m))mechanismthatworksas

k

follows:any0inmischangedto00,andany1inmischangedrandomlyto01

or10.ThedecryptionofC(D (C))inthisschemeworksasfollows:change00

k

backto0,and01and10backto1.Nevertheless,apairofbits11willresultin⊥.

(cid:2) DefineE (m)=PRF⊕E (m)andPRFisapseudorandomfunctionthatcreates

k k

anewnumberforeachmessagetoencrypt.

(cid:2) LetusstudythecryptanalysisoftheATEcombinationbasedonE (m)with

k

any message authentication in the presence of a CCA attack. Let A be an

adversary who implements the CCA attack as follows. Given a challenge

C = E ((m, T (m)), A basically complements the first two bits of C and

k1 k2

verifiesiftheresultingciphertextisvalid.IfthenewCisvalid,thenAdecides

thatthefirstbitofmwas1.Thisisprimarilyduetothefactthatifthefirstbit

ofmequals1,thenthefirsttwobitsofE (m)canbe01or10.Therefore,the

k1

complementofthesetwobitsstillyieldsthesamebit1.However,ifthenewC

isnotvalid,thenAdecidesthatthefirstbitofmequals0.Thisismainlydue

tothefactthat0ismappedto00andsoflippingthesebitsyields11,which

meansanincorrectC.Accordingly,misnull(⊥),whichcontradictswiththe

assumptionthatT isstillcomputedoverm.

k2

4.1.2.ProvenSecurityofETACombinationinELCAUsingROM

TheETAcombinationintheproposedELCAisprovensecurebasedonthefollowing

securityanalysis.

Theorem1.LetELCAE=(K,E,D)betheencryptionofELCAthatissecureunderIND-CPA,

andletELCAM=(K,T,V)betheauthenticationofELCAthatisEU-CMA.Then,ELCA=(K,

ET,D,V)createdbytheencrypt-then-authenticateisasecurecombinationofELCAEandELCAM.

Methodology of Proof. The contradiction methodology is used to prove Theorem 1.

SinceELCAMisEU-CMA,allqueries(exceptthatobtainedfromencryptionoracle)tothe

decryptionoraclecanbeassumedtobeinvalid.Thus,thecryptanalysisofELCAcanbe

reducedtoIND-CPAofELCAEbecausethedecryptionoracleiseffectuallyuseless.Atthe

beginning,thispaperprovesthat,exceptwithnegligibleprobability,theonlyvalidqueries

madebyAwereCthatwerepreviouslyobtainedfromtheencryptionoracle.Therefore,if

90

Mathematics2023,11,220

ELCAisprovenasnotsecureunderCCA,thenitshouldbethatELCAEisnotsecureunder

IND-CPA,whichcontradictstheassumptioninTheorem1.

Proof.LetAbeanyPPTadversarythatimplementsCCAattackonELCA,whichcanbe

denotedasPrivKC

A

C

,E

A

LCA

(n).Additionally,letusdefineVQueryA,ELCA(n)tobetheevent

thatAinputsavalidquery(C,T)toitsdecryptionoracle,whichdoesnotreply⊥.Generally,

ifweprovethatthePr[VQueryA,ELCA(n)]isatmostnegligible,thenthatwillbesufficient

toproveTheorem1.Thisisbecauseifthedecryptionoracledoesnotreply⊥,thenTisa

validtagforC.Consequently,if(C,T)isavalidinputforthedecryptionoracle,thismeans

thatAessentialforgedamessageauthentication.IftheprobabilitythatVQueryoccursis

non-negligible,AmaccanbeconstructedtobreakthemessageELCAMasfollows:Letus

defineq(·)tobeapolynomialthatrepresentstheupperboundsofqueriesthatareissued

f

r

r

a

o

n

m

do

A

m

.T

k

h

i

e

fo

M

re

a

n

c

c

−

ry

f

p

o

t

r

i

g

o

e

n

A

w

mac

h

,E

e

L

r

C

e

A

i

M← (n

{1

)

,

is

..

in

.

t

.

e

.

r

.

ac

q

t

(

e

n

d

)}

b

.

y

M

A

or

m

e

a

o

c,

v

w

er

h

,

i

A

ch

ma

c

c

a

u

lls

se

t

s

he

k1

A

a

w

nd

ith

its

ch

M

o

A

se

C

n

oracletosimulatetheencryptionanddecryptionoracleforA.Letusassumethatallqueries

tothedecryptionoracleareinvalidexcepttheithquery,whichishopedtobevalid.This

meansifAqueriestheencryptionoraclewithM,AmaccomputesC=E

k1

(M)andcallsits

MACoracletoobtainahopeforgedTforC.Finally,Amacreturnsthepair(C,T)toAasits

oraclereply. Ontheotherhand,ifAsendsanydecryptionoraclequery(C,T)exceptith,

Amacwillreviewif(C,T)hasbeencreatedbefore,thenAmacreturnsM.Otherwise,Amac

returns⊥. However,Amacreturns(C,T)asitsmessageauthenticationforgeryandhalts

uponreceivingithdecryptionoraclequeryfromA.WeremarkthatsinceELCAMprovidesa

uniquetag,thismeansthatthequeryCwasneverrequestedbyAmactoitsMAC-tagoracle.

Thisisprimarilydueto(C,T)notbeinggainedfromanencryptionquery,whichmeans

thereisonlyasinglelikelihoodthatTisavalidtagforC.Theprobabilitythattheithquery

isthefirstvalidquerybyAisatleast1/q(n)sinceAmakesatmostq(n). Consequently,

theprobabilitythatAmacdoeswellinMac−forge

Amac,ELCAM

(n)isatleast1/q(n)timesthe

probabilitythattheVQueryeventoccurs.Subsequently,theprobabilityofAmactodowell

inMac−forge (n)isatmostnegligibleprobability;thismeansVQueryoccurs

Amac,ELCAM

withatmostnegligibleprobability,whichprovesthefirstpartofTheorem1.Asaresult,

forsomenegligiblefunctionnegl(n),theprobabilityofVQuerycanbewrittenas:

Pr [VQueryA,ELCA (n)]<negl(n)

Given that the probability of VQuery happens at most negligible probability, the

combinationofencrypt-then-authenticateinELCAwillbeproventobeCCA-secure.For

simplicity,ifweprovethesecurityofELCAEagainstIND-CPAattack,thenELCAisproven

secure. Letanadversary Aenc becreatedusingAfortheCPAexperimentwithELCAE.

Aencselectsakeyk2andcallsA.EachtimeArequestsanencryptionqueryforM,Aenc

callsitsencryptionoraclewithMandreceivesbackC.Afterthat,AenccalculatesT=T

k2

(C)

andreturnsthepair(C,T)toA.Incontrast,whenArequestsadecryptionqueryforthe

pair(C,T),Aencwillsearchaboutthepair(C,T)initshistorytable,whichwaspreviously

generatedfromitsencryptionquery,andreturnsMtoAifitisavailable.Otherwise,Aenc

returns⊥.ItiscleartoconcludethatifAencsucceedsinPrivKCPAwhenVQuerydoesnot

happen,thenthisequalsthesuccessofAinPrivKCCA whenVQuerydoesnothappen,

whichcanbedefinedasfollows[11]:

P r [Priv = KC A P P en r A c[ , P EL r C iv A K E C A (n C ,E ) A LC = A 1 (n ∩ ) ¬ = V 1 Q ∩ u ¬ er V yC A Q P ,E u A L e C r A yC A (n P ,E A ) L ] CA (n)] (4)

Implyingthat:

P r [PrivKC A P e = ≥n A c,E P P L r r C [ [P P A r r E i i ( v v n K K ) C C A A = C P , e E n A A c L 1 ,E C ] L A C ( A n E) ( = n) 1 = ∩ 1 ¬ ∩ V ¬ Q V u Q er u y e A r ,E y L A C ,E A L ( C n A ) ( ] n)] (5)

91

Mathematics2023,11,220

Letususethecontradictionbyassuminganon-negligiblefunctionεexistssuchthat:

P r [PrivKC A C ,E A LCA (n)=1]= 1 2 +ε(n) (6)

UsingthefactthatPr[VQueryA,ELCA(n)]isnegligible,thismeansitissmallerthan

ε(n)/2.Asaresult,wecanconcludethefollowing:

P r [PrivKC A C ,E A LCA (n)=1∩VQueryA,ELCA (n)]<

ε(

2

n)

(7)

Thismeans:

P

(cid:24)r

[PrivKC

A

C

,E

A

LCA

(n)=1]=

(cid:31)

P

r

[PrivKC

A

C

,E

A

LCA

(n)=1∩VQueryA,ELCA (n)]

(cid:2)

+P

r

[PrivKC

A

C

,E

A

LCA

(n)=1∩¬VQueryA,ELCA ( (cid:3)n)]

(8)

< P

r

[PrivKC

A

C

,E

A

LCA

(n)=1∩¬VQueryA,ELCA (n)]+ε(

2

n)

BymeansthatAsucceedsinPrivKCCAwithprobability1/2+ε(n),thenEquation(8)

canbeexpressedas:

P

r

[PrivKC

A

C

,E

A

LCA

(n)=1∩¬VQueryA,ELCA (n)]>

P r [PrivKC A C ,E A LCA (n)=1]−ε( 2 n) (9)

= 1+ε(n)−ε(n) = 1+ε(n)

2 2 2 2

Equations(5)and(9)canbecombinedas:

P r [PrivKC A P en A c,ELCAE (n)=1]> 1 2 + ε( 2 n) (10)

Equation(10)showsthattheadvantageofAenctosucceedinPrivKCPAisnon-negligible

over1/2.Asaresult,thiscontradictsIND-CPAofELCAEandweconcludethatthecombi-

nationofencrypt-then-authenticateinELCAisCCA-secure.(cid:2)

4.2.ELCACybersecurityAnalysis

ELCAcontainsimportantsecurityfeaturessuchasimpersonationresilienceagainst

keycompromiseandperfectforwardsecrecy(PFS).ELCAemploysahashfunctionto

produceapseudorandomfunction(PRF)sinceitmaybethoughtofasarandomoracle

function. AsstatedinSection3,theELCA’s(i.e.,CMA’s)hashfunctionusestheshared

secretkey(XK)asaninputtocreatethesecurerandomparameter(H(XK)),whichisthen

multipliedbythebasepoint(G)inascalarmannertoobtaintherandompointPb(). To

protectagainstIND-CPAandreplayattacks,Pb.X1(i.e.,thexcoordinateofPb)isarandom

valuethatisperiodicallymodified.

ProvenSecurityofELCAinROM

ThelengthofthesharedsecretkeyXK ∈ {0,1}LcanberepresentedasL=|XK | =

|n| = |p|,whichisequalsthelengthoftheusedellipticcurveSecp192r1(e.g.,192bits).

The hash function is instantiated in ROM using the established security in ELCA as

H(.): {0,1}∗→{0,1}L.

Theorem2.IfPbisa(t,(cid:3))-pseudorandomfunction(PRF),thentheELCAcryptographicissecure

againstIND-CPA.

92

Mathematics2023,11,220

MethodologyofProof.Thesecondtheoremisprovenusingthecontradictionmethodology.

LetusassumethatArunsinPPTexistandthattheycompromiseELCAE’ssecurity.With

non-negligiblecost,algorithmAcreatesaPPTdistinguisherBthatseparatestheoutput

ofPbfromarandomnumber.SincePbisaPRF,thepriorconclusionthatPbisarandom

functionisincorrect.Asaresult,theinitialhypothesisisincorrect,andtheELCAEneedsto

besecure.

Proof.LetusassumeAattacksELCAEinthesenseofIND-CPAandtwomessagesM0,M1

areusedasfollows:

(cid:30) (cid:30)

(cid:30) (cid:30) (cid:30) − P P r [ r H [H (X (X K K ) ) ← ← Z Zn ∗ ; n ∗ P ;P b b ← ← H H (X (X K K ) ) × × G G ;C ;C ← ← M M 0 1 × × P P b. b X .X 1 1 :A :A (C (C ) ) = = 0] 0] (cid:30) (cid:30) (cid:30) =γ(L) (11)

whereγ(L)isnon-negligible. ThealgorithmBwasconstructedtodistinguishPbfrom

therandomfunction.ThiscanbeaccomplishedbydeterminingifPbisaPRForatotally

randomfunctionutilizingB’sabilitytocallPb.Bfunctionsasfollows:(1)Pickarandomb

between0and1,(2)BcomputesC=Pb.X1×M modn,(3)RuntheexperimentA(C)to

b

obtainA’sguessastotheencryptedmessage.Acorrectlypredictedifb=,bthenBestimates

thePRFandtheresultis“1”asindicatedbyB.However,Aguessedincorrectlyifb(cid:9)=bifB

guessesrandomfunctionandthiscanberepresentedbyBresultingas“0”.Thealgorithm

BdistinguishestheoutputofPb.X1as:

(cid:30) (cid:30)

(cid:30) (cid:30) (cid:30) P r [H(XK )←Z n ∗ ;Pb←(H(XK − )× P r G [y ); ← y← Z n ∗ P : b B .X (y 1 ) : = B( 1 y ] )=1] (cid:30) (cid:30) (cid:30) (12)

We will study each of these terms separately as: P1 Pr [H(XK ) ← Z∗

n

;

Pb←(H(XK )×G);y←Pb.X1:B(y)=1],andP2 Pr [y←Z∗

n

:B(y)=1].Instep3,the

algorithmBobtainedthefollowing:

P 1 =P r [H(XK ) b ← ∈ Z {n ∗ 0 ; , P 1 b }; ← b (cid:16) ( ← H( A X ( K P ) b. × X1 G × );y M ← ) P :b b (cid:16) .X = 1 b : ] (13)

b

Byusingtheconditiononbgives:

P 1 + = Pr P [H r [H (X ( K X ) K ← )← Z n ∗ Z ; n ∗ y ; ← y← Pb P .X b. 1 X : 1 A : ( A P ( b P .X b. 1 X × 1× M M 1 ) 0 = )= 0] 0 × ]× Pr P [b r [ = b= 1] 0] (14)

Withapplyingthefact:

Pr [b=0]=Pr [b=1]= 1

2

and

1 P − r [H Pr ( [ X H K ( ) X ← K ) Z ←n ∗ ; Z y n ∗ ← ;y P ← b.X Pb 1 .X :A 1 ( : P A b ( .X Pb 1 .X × 1 M × 1 ) M = 1 ) 1 = ]= 0] (15)

gives:

! (cid:22) (cid:23)(cid:27) (cid:22) (cid:23)

P 1 = 1 2 + 1 2 × − P P r [ r H [H ( ( X X K K ) ) ← ← Z Zn ∗ n ∗ ; ; y y ← ← P P b b .X .X 1 1 : : A A ( ( P P b b .X .X 1 1 × × M M 0 1 ) ) = = 0 0 ] ] = 1 2 + 1 2 ×γ(L) (16)

P2iscalculatedas:

P 2 =Pr [y←Z n ∗ :b∈{0,1};b (cid:16)←A(Pb.X1×M b ):b (cid:16)=b] (17)

93

Mathematics2023,11,220

Asbefore,weeventuallyobtain:

! (cid:22) (cid:23)(cid:27)

P 2 = 1 2 + 1 2 × − P P r [ r y [y ← ← Z Zn ∗ n ∗ : : A A ( ( P P b b .X .X 1 1 × × M M 0 1 ) ) = = 0 0 ] ] (18)

SinceyiscompletelyrandomandPb=H(XK )×G,theprobabilityofAwinswhen

breaking the one-time pad is 0. Therefore, P 2 is 1/2. The final result after using all

parameterstogethergives:

(cid:30) (cid:30)

(cid:30) (cid:30) (cid:30) P y r ← [H P (X b. K X ) = 1 ← :(cid:30) (cid:30) (cid:30)1 B Z ( + n ∗ y ; ) γ P ( = b L) ← 1 − ]− ( 1 H (cid:30) (cid:30) (cid:30) P = ( r X [y K γ ← ( ) L × ) Z G n ∗ ) : ; B(y)=1] (cid:30) (cid:30) (cid:30) =|P 1 −P 2 | (19)

2 2 2 2

Sincethetermγ(L)wasnon-negligible,theterm γ(L) isalsonon-negligible. Asa

2

result,Ahasanon-zeroadvantageinbreakingELCAEandhenceBhasanon-negligible

advantageinbreakingthePRF(i.e.,distinguishingresultofPbfromrandom).However,

thiscontradictsthefactthatPbisa(t,(cid:3))-PRF.SincenosuchAmayexist,theassumption

mustbeincorrect,thusELCAEissecureagainstIND-CPA.(cid:2)

4.3.CountermeasuresSpoofingAttacks

ELCAcanpreventspoofingattacks(e.g.,replayattacksandtheman-in-the-middle

attacks)usingthesecurecombinationintegrationbetweenencryptionandauthentication.

Moreover,ELCAdropsthereplypacketfromtheintrudersbecauseofthefollowingreasons:

• TheMACshouldbecheckedbeforeperformingthedecryptionprocess.

• Theephemeralsharedsecretkeyiscomputedatthesourceanddestination.

• Thethreestagesmustbecarriedoutbyreplayattacksbeforeresendingtheinter-

ceptedcommunication. Thesesteps—calculatingthesharedsecretkey,encrypting

messages,andcalculatingtheauthenticationtag—makeitincrediblydifficulttoaccess

informationwithoutcompromisingthesharedsecretkeyandhashfunction.

4.4.CountermeasuresagainstBruteForceAttacks

ELCAaddressestheweakbitsissueandoffersperfectforwardsecrecybecausethe

sharedsecretkeymustchangewitheachcommunicationsession.√Additionally,theelliptic

curvediscretelogarithmproblem(ECDLP),whichrequires0.886∗ ksteps,mustbesolved

by the brute force attacker. This indicates that the security strength is 96, which will

probablyrequirealotofcomputerpower[37,40].

4.5.CountermeasuresagainstSessionHijackingAttack

SecurehashfunctionssuchasSHA-2andCMAareappliedusingthesharedsecret

keyinELCA[29].Thismethodproducesarandomintegerthatcanbeusedtocreatethe

sessionidentification,suchasthedigestofasharedsecretkeyafterithasbeenhashed.In

ordertoobtainaccesstothecommunicationchannelbetweentheIoTparties,theattacker

mustdeterminetheauthenticationcodeifheissuccessfulincrackingthesessionID.Thisis

mostlybecausetheverificationprocessbetweentheIoTsenderandreceiverofthesession

requirestheauthenticationcode.

4.6.CountermeasuresagainstIoTDeviceCaptureandStolen-VerifierAttacks

TheELCAcryptographicsystemusesthebuilt-inmultifactorhashfunctions(e.g.,

CMA[29])thatareburnedduringprogrammingsessionsinsideallIoTdevicestoprotect

againstIoTdevicecaptureandstolen-verifierattacks. Asstatedintheassumption,the

multifactorhashfunctionsusedinELCAareflashedandtransformedintolowlevelsource

codelanguage. Therefore,thestolenkeywillnotfunctionwithoutdisablingthehash

algorithms,preventingthehackerfromaccessinganysafedataintheIoTdevice.

94

Mathematics2023,11,220

5.ImplementationandPerformanceEvaluationofELCAonIoT

Basedontheresourceconstraintsintermsofcomputingcost,storageutilization,and

powerconsumption,thesecuritysoftwareinIoTplatformsshouldbeassessed.Therefore,

ELCAadoptedtheconceptofECDHforexchangingthesecretkeyadvisedbySECG/NIST

(suchasSecp192r1)[37].FollowingaresomereasonswhyutilizingtheSecp192r1standard

ellipticcurveinELCAisadvantageous:

• Thesizeoftheencryptionandauthenticationkeysis24bytes(192bits), andthe

processinglatencyfortheECDHtogenerateandexchangethesecretkeyhasbeen

assessedtobe√0.576sthroughexperimentaltesting[31].

• Ittakes0.886∗ kstepstodeterminethek-sizeoftheacknowledgedidealalgorithm

fortheECDLP.Ingeneral,ifthesecuritysystememploysatleast2*k-bitkeysize,a

k-bitsecuritystrengthcanbeattained. Becauseofthis,ELCAchosetoemploythe

Secp192r1curve,whichcanoffer96-bitsecuritystrength[37,40].

• The6LowPANprotocol,whichusesa40-byteheadertoestablishconnectionsbetween

IoTdevicesandsensornodes,canbeusedtoconstructIoTdeviceswithmessagesup

to127bytesinsize[41].

SinceMininet-IoTcanreplicatetheIoThardwareandcommunicationdescription,itis

usedintheassessmentscenariostoimplementandverifytheperformanceofELCA[42].

AscanbeshowninFigure5,oneIoTgateway(BaseST1),eightstaticIoTdevices(sensors1

through8),twointruders(Intrudr6andIntrudr7),andonemobileIoTdevice(IoTDev5)

makeuptheexperiment’sIoTnetworktopology.Theadversarymodelthatwascoveredin

thepreviouspartismostlyimplementedbyintruders.EachIoThardwareboardincludes

twonetworkinterfacecards,oneforIPv4andoneforIPv6communicationswiththeIoT

basestation(i.e.,6LowPAN).Additionally,allsensors,IoTDev5,andBaseST1havethe

suggestedELCAsoftwareuploaded. Additionally,alllegitimateIoTdevicesexchange

publickeysandsecurepacketsutilizingclient–serversocketprogrammingincombination

withELCAcode.BaseST1implementstheservercode,andIoTDev5andallsensorsrunthe

clientcode.ThesettingsandsetupoftheexperimentareshowninTable3.InMininet-IoT,

the6LowPANprotocolisimplementedontheTCP/IPmodelusingthe802.15.4hwsimand

802.11hwsimwirelessmodels.Additionally,thewirelesssignal’spropagationmodelisset

upusingashadowingmodel,whichdepictstheactualsignaldegradationbroughtonby

signalimpairmentsincludingattenuation,noise,andinterference.Intheexperiment,the

gridnetworkareameasures1000mby900m,andrandommovementisusedtoconstruct

themobilitymodelofmobiledevices. ToinvestigatetheeffectivenessofELCAagainst

intrudersusingdictionaryandbruteforceattacks,theoperatingtimeofeveryexperimental

programissetto1000s.

Table3.ExperimentConfiguration.

Parameter Values

MACandPHY 802.15.14_hmsimand802.11_hmsim

PropagationModel Shadowing

Pathlossexponent 3.0

Shadowingdeviation(dB) 3.0

Eventarea (1000m×900m)

NumberofIoTdevices 12

CoverageofIoTdevice 150m

CoverrangeofBaseST1 250m

TrafficEmulator TCPSocketclient/server;1000messages.

CPUexecutiontime,storagecost,andenergy

Performancemetrics

consumption

ECDHcurve Secp192r1

MessageSize 127bytes

Keysize 192Bits

Emulationduration 1000s

95

Mathematics2023,11,220

Figure5.IoTmeshtopology.

5.1.PerformanceEvaluationandResultsDiscussion

IntermsofCPUexecutiontime,memoryutilization,andpowerconsumptionex-

penses,thesuggestedintegrationofencryptionandauthentication(forexample,ELCA)

wasevaluatedintermsofperformance.Forthethreecombinationsofauthenticationand

encryptionshowninFigure2,acomparisonofperformanceanalysiswasinvestigated.

Additionally,ECIESAESandECIESRa(RFC4503),twobenchmarksecurityalgorithms,

wereusedtocompareELCA’sperformance.Pythonisusedthroughoutthesourcecodeand

isimplementedintheMininet-IoTemulator.Additionally,allbaselinealgorithms’primary

sourcecodescanbedownloadedfromthesecuritywebsite[43]. Numerousscenarios

wererun,andeachtestbedwasrepeatedtentimeswhileexchanging1000packets.Finally,

usingthemeanandstandarddeviationasinputsandaccepting5%variationerrorsinthe

sample,theaveragefindingsweredeterminedwithaconfidenceintervalthatexceeds95%.

Furthermore,thememoryprofilerandcProfileprogramsofferdeterministiccostprofiling

ofthebaselinemethodsandELCA.Memoryprofilercanbeusedtocalculateanalgorithm’s

executiontime,storageexpense,andenergyusage.TheproductofCPUexecutiontime

andthequantityofstepsperexecution(s/e)canbeusedtoevaluatetheentirecostofCPU

executiontime. Additionally,thetotalcostofcommunication(send/receivedmessage)

data,senseddata,andthecostofthesourcecodeinatimeunitcanbeusedtocalculatethe

storagecostineachIoTdevice.Additionally,thetotalenergyrequiredbyIoTdevices(mJ)

canbecalculatedasthetotalenergyusedtocarryoutthesecurityalgorithm’ssourcecode

plusanypacketoverhead[44].

5.1.1.ComparisonbetweenIntegrationMethodsofAuthenticationandEncryption

Inthisexperiment,theperformanceofusingELCAinthreemethodsofintegration

betweenauthenticationandencryptionwasevaluated.ELCAwasimplementedusingthe

threecombinationapproaches(e.g.,ATE,EATandETA)illustratedinFigure2.Generally,

theresultsinFigure6showthattheperformancecostofBaseST1inthreecombinationis

higherthanIoTDev5. ThisismainlyduetothetypeofconnectionintheIoTsystemis

many-to-onethatmeansallsensordevicessendtheenvironmentdatatothesink(BaseST1).

ThesinkinFigure6manipulatedthesecurityforalldataintheIoTsystem.Asshownin

Figure6a,theELCAwithETAexperiencesonaverage30.74%lessCPUexecutiontime

comparedtoELCAwithATE,anditexperiencesonaverage15%lessCPUexecution

timecomparedtoELCAwithEAT.Moreover,Figure6billustratesthatELCAwithETA

experiencesonaverage22.5%lessmemoryusagecomparedtoELCAwithATE,andit

96

Mathematics2023,11,220

experiencesonaverage32.63%lessmemoryusagecomparedtoELCAwithEAT.Moreover,

Figure6cshowsthatELCAwithETAconsumesonaverage68.7%lessenergyconsumption

comparedtoELCAwithATE,anditconsumesonaverage52.5%lessenergyconsumption

comparedtoELCAwithEAT.TheresultspresentedinFigure6showthattheimpressive

performanceoftheELCAwithETAalgorithmismainlyachievedduetothefollowing

reasons:Firstly,ELCAwithETAusesfewerstepsofcallfunctionsduetotheverification

ofauthenticationbeingimplementedbeforethedecryption,whichcausesareducedCPU

executiontime,lessmemorytobeused,andreducedpowerconsumption.However,ATE

andEATmustimplementdecryptionandverificationofauthenticationwithallreceived

ciphertextsandtags,whichconsumesmoreresourcesintermofenergyconsumption,

storagecost,andCPUexecutiontime. Finally,ATEandEATconsumehighercallfunc-

tions,executiontime,andcommunicationoverheadsduetothefrequentusesofscalar

multiplicationandtheinversemodularmultiplicativeinthedecryptionprocess.

Figure6.Cont.

97

Mathematics2023,11,220

Figure6.Comparisonbetweenintegrationmethodsofauthenticationandencryption.(a)Execution

cost;(b)storagecost;(c)energyconsumption.

5.1.2.PerformanceofCryptographicAlgorithms

IthasbeendeterminedhowwellELCAencryption(ELCA_E)performsincomparison

toECIES_RaandECIES_AES.AscanbeseeninFigure7a, ELCA_Eexecuteswithan

averageexecutiontimethatis50%lowerthanthatofEDIDS_AESandaverages39.4%

lowerthanthatofECIES_Ra.Additionally,Figure7bshowsthatELCA_Eusesmemory

onaverage19.6%and32%lessefficientlythanECIES_AESandECIES_Ra.Additionally,

Figure7cdemonstratesthatELCA_Eusesanaverageof32.6%lessenergythanECIES_Ra

andthereisadifferenceof41.2%betweenECIES_AESandELCA_E.Theaforementioned

resultsshowthatELCAEoutperformsECIES_AESandECIES_RaintermsofCPUtime

execution,storagecost,andenergyusage.Thisismostlybecauseofthefollowingfactors:

Firstly,ELCA_Euseslesscomputingpowerandenergyduringencryptionanddecryption

becauseitisbasedonaneffectivemathematicalrandomfunction.Foreachsessionbetween

IoTdevices,ELCA_Egeneratesanoverallsharedsecretkeythatensuresperfectforward

secrecyoftheencryptedmessage. Second,becausefewerfunctionsarecalledandthere

are fewer execution steps for each function, ELCA_E uses less storage space. Finally,

ECIES_AESandECIES_Raemploymoredifficultandinefficientencryptionanddecryption

techniquesthanELCA_E.Inconclusion,theexperimentalfindingsdemonstratethatthe

suggestedintegrationofauthenticationandencryptioninELCAisefficient,lightweight,

andoffersexceptionalperformanceintermsofCPUexecutiontime,storagecost,and

energyconsumption.Morecrucially,itfixestheissueswithsymmetriccryptography’skey

distributionandtheverificationofthesender’sidentityindigitalsignatures.

98

Mathematics2023,11,220

Figure7.ComparisonbetweenELCAencryption(ELCA_E)andbaselinecryptographicalgorithms

onIoT.(a)Executioncost;(b)storagecost;(c)energyconsumption.

99

Mathematics2023,11,220

6.ConclusionsandFutureWork

Theproposedsecureintegrationbetweenencryptionandauthentication(e.g.,ELCA)

algorithmwaspresentedandcomparedwithstandardlightweightcryptographicschemes.

ELCAutilizedECDHtoimplementkeydistribution,whiletheweakbitsprobleminthe

sharedsecretkeyisresolved.ThesecurityofELCAwasprovenmathematicallyusingthe

IoTadversarymodelandtherandomoraclemodel.Thefindingintheexperimentalresults

showstheefficiencyandeffectivenessofELCAperformanceintermsofareducedCPU

executiontimeby50%,reducedstoragecostby32–19.6%,andreducedenergyconsumption

by41%comparedtothebaselinecryptographicalgorithms.Thefutureworkofthisresearch

willfocusondevelopinganunforgeabledigitalsignaturebasedonthethreestepsofhash

functioninspectionsforIoTnetworks.Moreover,theweakbitproblemwillberesolved

usingadvancedkeygenerationwithoutconcernsabouttheIoTkeyselection.

AuthorContributions:Conceptualization,A.A.A.(AdelA.Ahmed)andW.A.;methodology,A.A.A.

(AdelA.Ahmed);software,A.A.A.(AdelA.Ahmed);validation,S.J.M.,A.A.A.(AhmedA.Alzahrani)

andW.A.;formalanalysis,S.J.M.;investigation,W.A.;resources,A.A.A.(AdelA.Ahmed);data

curation,A.A.A.(AhmedA.Alzahrani);writing—originaldraftpreparation,A.A.A.(AdelA.Ahmed);

writing—reviewandediting,W.A.;visualization,A.A.A.(AhmedA.Alzahrani);supervision,A.A.A.

(AdelA.Ahmed);projectadministration,A.A.A.(AdelA.Ahmed);fundingacquisition,A.A.A.(Adel

A.Ahmed).Allauthorshavereadandagreedtothepublishedversionofthemanuscript.

Funding:ThisresearchworkwasfundedbyinstitutionalFundProjectsundergrantno.(IFPIP:324-

830-1443). Theauthorsgratefullyacknowledgetechnicalandfinancialsupportprovidedbythe

MinistryofEducationandKingAbdulazizUniversity,DSR,Jeddah,SaudiArabia.

DataAvailabilityStatement:Notapplicable.

Acknowledgments:ThisresearchworkwasfundedbyinstitutionalFundProjectsundergrantno.

(IFPIP:324-830-1443).Theauthorsgratefullyacknowledgetechnicalandfinancialsupportprovided

bytheMinistryofEducationandKingAbdulazizUniversity,DSR,Jeddah,SaudiArabia.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

References

1. Malina,L.;Hajny,J.;Fujdiak,R.;Hosek,J.J.Onperspectiveofsecurityandprivacy-preservingsolutionsintheinternetofthings.

Comput.Netw.2016,102,83–95.[CrossRef]

2. Hussain,S.; Ullah,S.S.; Ali,I.; Xie,J.; Inukollu,V.N.CertificatelesssignatureschemesinIndustrialInternetofThings: A

comparativesurvey.Comput.Commun.2022,181,116–131.[CrossRef]

3. Qiu,J.;Tian,Z.;Du,C.;Zuo,Q.;Su,S.;Fang,B.Asurveyonaccesscontrolintheageofinternetofthings.IEEEInternetThingsJ.

2020,7,4682–4696.[CrossRef]

4. Li,S.;Zhang,T.;Yu,B.;He,K.AProvablySecureandPracticalPUF-BasedEnd-to-EndMutualAuthenticationandKeyExchange

ProtocolforIoT.IEEESens.J.2021,21,5487–5501.[CrossRef]

5. Arne,B.;Le,N.;Dominik,S.;Stephan,S.;Lars,C.W.SecurityPropertiesofGaitforMobileDevicePairing.IEEETrans.Mob.

Comput.2019,19,697–710.

6. Attarian,R.;Hashemi,S.AnanonymitycommunicationprotocolforsecurityandprivacyofclientsinIoT-basedmobilehealth

transactions.Comput.Netw.2021,190,107976.[CrossRef]

7. Almajed,H.N.;Almogren,A.S.SE-Enc:ASecureandEfficientEncodingSchemeUsingEllipticCurveCryptography.IEEEAccess

2019,7,175865–175878.[CrossRef]

8. Bu,L.;Isakov,M.;Kinsy,M.A.AsecureandrobustschemeforsharingconfidentialinformationinIoTsystems.AdHocNetw.

2019,92,101762.[CrossRef]

9. Hendaoui,F.;Eltaief,H.;Youssef,H.UAP:AunifiedauthenticationplatformforIoTenvironment.Comput.Netw.2021,188,107811.

[CrossRef]

10. Vidya,R.;Prema,K.V.LightweighthashingmethodforuserauthenticationinInternet-of-Things.AdHocNetw.2019,89,97–106.

11. Katz,J.;Yehuda,L.IntroductiontoModernCryptography;CRCPress:BocaRaton,FL,USA,2007.

12. Barker,E.RecommendationforKeyManagement.InComputerSecurity;NISTSpecialPublication800-57Part1,Revision5;USA,

DepartmentofCommerce:Washington,DC,USA,20May2020.[CrossRef]

13. Chuang,Y.-H.;Lo,N.-W.;Yang,C.-Y.;Tang,S.-W.ALightweightContinuousAuthenticationProtocolfortheInternetofThings.

Sensors2018,18,1104.[CrossRef][PubMed]

100

Mathematics2023,11,220

14. Alaba,F.A.;Othman,M.;Hashem,I.A.T.;Alotaibi,F.InternetofThingssecurity:Asurvey.J.Netw.Comput.Appl.2017,88,10–28.

[CrossRef]

15. Riad,K.;Huang,T.;Ke,L.AdynamicandhierarchicalaccesscontrolforIoTinmulti-authoritycloudstorage.J.Netw.Comput.

Appl.2020,160,102633.[CrossRef]

16. Alexander,J.M.;Kueffer,C.;Daehler,C.;Edwards,P.J.;Pauchard,A.;Seipel,T.;Arévalo,R.J.;Cavieres,L.A.;Dietz,H.;Jakobs,

G.;etal.NETRA:EnhancingIoTSecurityUsingNFV-BasedEdgeTrafficAnalysis.IEEESens.J.2019,19,4660–4671.[CrossRef]

17. Hellaoui,H.;Koudil,M.;Bouabdallah,A.Energy-efficientmechanismsinsecurityoftheinternetofthings:Asurvey.Comput.

Netw.2017,127,173–189.[CrossRef]

18. Magdich,R.;Jemal,H.;Ayed,M.AresilientTrustManagementframeworktowardstrustrelatedattacksintheSocialInternetof

Things.Comput.Commun.2022,191,92–107.[CrossRef]

19. Liu,X.;Yu,W.;Liang,F.;Griffith,D.;Golmie,N.OndeepreinforcementlearningsecurityforIndustrialInternetofThings.

Comput.Commun.2021,168,20–32.[CrossRef]

20. Li,X.;Niu,J.W.;Ma,J.;Wang,W.D.;Liu,C.L.Cryptanalysisandimprovementofabiometrics-basedremoteuserauthentication

schemeusingsmartcards.J.Netw.Comput.Appl.2011,34,73–79.[CrossRef]

21. Al-Karaki,J.N.;Gawanmeh,A.;Almalkawi,I.T.;Alfandi,O.Probabilisticanalysisofsecurityattacksincloudenvironmentusing

hiddenMarkovmodels.Trans.Emerg.Telecommun.Technol.2022,33,e3915.[CrossRef]

22. Wang,Y.;Yang,G.;Li,T.;Li,F.;Tian,Y.;Yu,X.Beliefandfairness:Asecuretwo-partyprotocoltowardtheviewofentropyforIoT

devices.J.Netw.Comput.Appl.2020,161,102641.[CrossRef]

23. Ahmed,A.A.LightweightDigitalCertificateManagementandEfficaciousSymmetricCryptographicMechanismoverIndustrial

InternetofThings.Sensors2021,21,2810.[CrossRef][PubMed]

24. NISTComputerSecurityResourceCenter.LightweightCryptographyProject.Availableonline:https://csrc.nist.gov/projects/

lightweight-cryptography(accessedon13March2022).

25. Seok,B.;Sicato,J.C.S.;Erzhena,T.;Xuan,C.;Pan,Y.;Park,J.H.SecureD2DCommunicationfor5GIoTNetworkBasedon

LightweightCryptography.Appl.Sci.2020,10,217.[CrossRef]

26. Mohseni-Ejiyeh,A.;Ashouri-Talouki,M.;Mahdavi,M.AnIncentive-AwareLightweightSecureDataSharingSchemeforD2D

Communicationin5GCellularNetworks.ISeCure2018,10,15–27.

27. Abro,A.;Deng,Z.;Memon,K.A.ALightweightElliptic-Elgamal-BasedAuthenticationSchemeforSecureDevice-to-Device

Communication.FutureInternet2019,11,108.[CrossRef]

28. Javed,Y.;Khan,A.S.;Qahar,A.;Abdullah,J.EEoP:AlightweightsecurityschemeoverPKIinD2Dcellularnetworks.J.Telecom-

mun.Electron.Comput.Eng.2017,9,99–105.

29. Ahmed,A.A.;Ahmed,W.A.AnEffectiveMultifactorAuthenticationMechanismBasedonCombinersofHashFunctionover

InternetofThings.Sensors2019,19,3663.[CrossRef]

30. Sciancalepore,S.;Piro,G.;Boggia,G.;Bianchi,G.PublicKeyAuthenticationandKeyAgreementinIoTDeviceswithMinimal

AirtimeConsumption.IEEEEmbed.Syst.Lett.2017,9,1–4.[CrossRef]

31. Khan,M.A.;Quasim,M.T.;Alghamdi,N.S.;Khan,M.Y.ASecureFrameworkforAuthenticationandEncryptionUsingImproved

ECCforIoT-BasedMedicalSensorData.IEEEAccess2020,8,52018–52027.[CrossRef]

32. Muhammad,U.;Ahmed,I.;Imran,M.A.;Shujaat,K.;Usman,A.S.SIT:Alightweightencryptionalgorithmforsecureinternetof

things.Int.J.Adv.Comput.Sci.Appl.2017,8,402–411.

33. Shah,R.H.;Salapurkar,D.P.AmultifactorauthenticationsystemusingsecretsplittingintheperspectiveofCloudofThings.In

ProceedingsoftheInternationalConferenceonEmergingTrends&InnovationinICT(ICEI),Pune,India,3–5February2017;pp.1–4.

34. Hammi,B.;Fayad,A.;Khatoun,R.;Zeadally,S.;Begriche,Y.ALightweightECC-BasedAuthenticationSchemeforInternetof

Things(IoT).IEEESyst.J.2020,14,3440–3450.[CrossRef]

35. Rangwani,D.;Sadhukhan,D.;Ray,S.;Khan,M.K.;Dasgupta,M.Arobustprovable-secureprivacy-preservingauthentication

protocolforIndustrialInternetofThings.Peer-to-PeerNetw.Appl.2021,14,1548–1571.[CrossRef]

36. Lochter,M.;Merkle,J.RFC5639:EllipticCurveCryptography(ECC)BrainpoolStandardCurvesandCurveGeneration;IETF:Felemon,

CA,USA,2010;ISSN2070-1721.

37. NIST.FipsPublication180-2: SecureHashStandard;TechnicalReport;NationalInstituteofStandardsandTechnology(NIST):

Gaithersburg,MD,USA,2003.

38. Biryukov,A.AdaptiveChosenPlaintextAttack.InEncyclopediaofCryptographyandSecurity;VanTilborg,H.C.A.,Jajodia,S.,Eds.;

Springer:Boston,MA,USA,2011.

39. Biryukov,A.RelatedKeyAttack.InEncyclopediaofCryptographyandSecurity;VanTilborg,H.C.A.,Jajodia,S.,Eds.;Springer:

Boston,MA,USA,2011.

40. Silverma,J.H.AnIntroductiontotheTheoryofEllipticCurves,SummerSchoolonComputationalNumberTheoryandApplicationsto

Cryptography;BrownUniversity:Providence,RI,USA,2006.

41. IPv6overLow-PowerWirelessPersonalAreaNetworks(6LoWPANs):Overview,Assumptions,ProblemStatement,andGoals.

Availableonline:http://www.ietf.org/rfc/rfc4919.txt(accessedon27November2022).

42. Mininet-IoTEmulatorofInternetofThings. Availableonline: https://github.com/ramonfontes/mininet-iot(accessedon

27November2022).

101

Mathematics2023,11,220

43. ASecuritySite.Availableonline:https://asecuritysite.com/encryption(accessedon27November2022).

44. Ahmed,A.A.AnoptimalcomplexityH.264/AVCencodingforvideostreamingovernextgenerationofwirelessmultimedia

sensornetworks.SignalImageVideoProcess.2016,10,1143–1150.[CrossRef]

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

102

mathematics

Article

Assisting Glaucoma Screening Process Using Feature Excitation

and Information Aggregation Techniques in Retinal Fundus Images

AliRaza1,†,SharjeelAdnan1,MuhammadIshaq1,HyungSeokKim2,RizwanAliNaqvi3,*,†

andSeung-WonLee4,*

1 DepartmentofPrimaryandSecondaryHealthcare,Lahore54000,Pakistan

2 DepartmentofIntelligentMechatronicsEngineering,SejongUniversity,Seoul05006,RepublicofKorea

3 DepartmentofUnmannedVehicleEngineering,SejongUniversity,Seoul05006,RepublicofKorea

4 SchoolofMedicine,SungkyunkwanUniversity,Suwon16419,RepublicofKorea

* Correspondence:rizwanali@sejong.ac.kr(R.A.N.);swlsejong@sejong.ac.kr(S.-W.L.)

† Theseauthorscontributedequallyandareco-firstauthors.

Abstract:Therapidlyincreasingtrendofretinaldiseasesneedsseriousattention,worldwide.Glau-

comaisacriticalophthalmicdiseasethatcancausepermanentvisionimpairment.Typically,oph-

thalmologistsdiagnoseglaucomausingmanualassessmentswhichisanerror-prone,subjective,

andtime-consumingapproach. Therefore,thedevelopmentofautomatedmethodsiscrucialto

strengthenandassisttheexistingdiagnosticmethods.Infundusimaging,opticcup(OC)andoptic

disc(OD)segmentationarewidelyacceptedbyresearchersforglaucomascreeningassistance.Many

researchstudiesproposedartificialintelligence(AI)baseddecisionsupportsystemsforglaucoma

diagnosis.However,existingAI-basedmethodsshowseriouslimitationsintermsofaccuracyand

efficiency.Variationsinbackgrounds,pixelintensityvalues,andobjectsizemakethesegmentation

challenging.Particularly,OCsizeisusuallyverysmallwithunclearboundarieswhichmakesitsseg-

mentationevenmoredifficult.Toeffectivelyaddresstheseproblems,anovelfeatureexcitation-based

densesegmentationnetwork(FEDS-Net)isdevelopedtoprovideaccurateODandOCsegmentation.

FEDS-Netemploysfeatureexcitationandinformationaggregation(IA)mechanismsforenhancing

theOCandODsegmentationperformance.FEDS-Netalsousesrapidfeaturedownsamplingand

efficientconvolutionaldepthfordiverseandefficientlearningofthenetwork,respectively. The

Citation:Raza,A.;Adnan,S.;Ishaq,

proposedframeworkiscomprehensivelyevaluatedonthreeopendatabases:REFUGE,Drishti-GS,

M.;Kim,H.S.;Naqvi,R.A.;Lee,S.-W.

andRim-One-r3.FEDS-Netachievedoutperformingsegmentationperformancecomparedwithstate-

AssistingGlaucomaScreening

ProcessUsingFeatureExcitationand of-the-artmethods.Asmallnumberofrequiredtrainableparameters(2.73million)alsoconfirmsthe

InformationAggregationTechniques superiorcomputationalefficiencyofourproposedmethod.

inRetinalFundusImages.

Mathematics2023,11,257. https:// Keywords: assistingglaucomascreening;convolutionalneuralnetwork;deeplearning;fundus

doi.org/10.3390/math11020257 imageanalysis;informationaggregation

AcademicEditor:WeiFang

MSC:68T07

Received:5December2022

Revised:23December2022

Accepted:26December2022

Published:4January2023 1.Introduction

Ophthalmic diseases have a significant impact on the well-being of human lives.

Retinaldiseasesareincreasingatarapidpace,worldwide[1].Therefore,moderndiagnostic

solutionsneedtobeintroducedforfastandaccurateophthalmicdiagnosis.Glaucomaisa

Copyright: © 2023 by the authors.

publiclyverycommonneurodegenerativediseasethatcancausepermanentvisionloss[2].

Licensee MDPI, Basel, Switzerland.

Earlyandaccurateglaucomascreeningishighlydesirableforitseffectivetreatment[2].

Thisarticleisanopenaccessarticle

Typically,manualproceduresandassessmentsarecarriedoutbyophthalmologistsfor

distributed under the terms and

glaucomadiagnosis. Thesemanualproceduresareusuallytime-consuming,subjective,

conditionsoftheCreativeCommons

Attribution(CCBY)license(https:// tedious,anderror-prone. Hence,automaticmethodsarecruciallyrequiredtoassistthe

creativecommons.org/licenses/by/ existingapproaches.

4.0/).

Mathematics2023,11,257.https://doi.org/10.3390/math11020257 https://www.mdpi.com/journal/mathematics

103

Mathematics2023,11,257

Artificialintelligence(AI)isprovidingrobustautomationsolutionstoautomateman-

ual procedures [3]. AI-based models significantly contributed to the biomedical and

diagnosticindustrybyintroducingintelligentmethodsfordeliveringcomputer-assisteddi-

agnosis[4].Deeplearningsolvedmanycomplexdiagnosticproblemsusingconvolutional

neuralnetworks(CNNs). Specifically,CNN-basedsemanticsegmentationhasaproven

recordinophthalmicdiagnosticsupport[5].Fundusimagingiswidelyacceptedbyexperts

forglaucomascreening[6].Opticcup(OC)andopticdisc(OD)segmentationareperformed

forglaucomadetection.Glaucomaproducessomemorphologicalandstructuralchanges

inOCandOD.SegmentationofbothOCandODprovidesexactareaandboundaries

whichconsequentlyhelpsinglaucomascreening.Verticalcup-to-disc-ratio(V-CDR)isalso

awidelyacceptedbiomarkerbyresearcherstohelpinglaucomadiagnosis[7].Theratio

betweentheverticaldiameterofOCandODiscalculatedforcomputingV-CDR.Higher

valuesofV-CDRrefertoahighchanceofglaucomaoccurrence. Ahigh-performance

OCandODsegmentationisthepreliminarysteptoobtainaccurateV-CDRmeasures.

Similarly,enlargementintheOCsizewhichistermedcuppingisalsoabiomarkerfor

glaucomadiagnosis.AreasofOCandODarecomputedtoprovidearea-cup-to-disc-ratio

(A-CDR)[8].A-CDRcomputationsalsoassistophthalmologistsintheglaucomascreening

process. Pixel-wisesegmentationofOCandODenablestheframeworkstoobtainall

theabove-mentionedcomputationsforassistingtheglaucomadiagnosisprocess.Hence,

accuratesegmentationofOCandODprovidesasolidfoundationforsupportingmedical

expertsinglaucomascreening.

ManyresearchstudiesproposedOCandODsegmentationforglaucomascreening.

However,OCandODsegmentationischallengingbecauseoftheextensivevariationsin

theimages. Thisvariationincludesdifferentbackgroundeffects,pixelintensityvalues,

sizes,andshapes.Specifically,thesizeofOCisusuallyquitesmallwithunclearboundaries

thatmakeitssegmentationmuchmorechallenging.Therefore,existingmethodsexhibited

seriouslimitationsinOCboundarypredictions.Lastly,theOCandODregionsarevery

smallcomparedwiththoseofthebackgroundclassanditcreatesaclassimbalanceproblem

thatnegativelyimpactsthelearningofthenetwork.Tomitigatethesechallenges,anovel

featureexcitation-baseddensesegmentationnetwork(FEDS-Net)isdevelopedforthe

semanticsegmentationofOCandOD.FEDS-Netisanoveldevelopmentanditisnot

basedonanyothernetwork.FEDS-Netusesfeatureexcitationandaggregationtoobtain

accuratepredictionsforOCandODclasses. FEDS-Netalsointroducedabruptfeature

downsamplingandaggregationmechanismforexpandedlearning.

ManyresearchworksproposedCNNsforglaucomadiagnosisusingOCandOD

segmentation.Nevertheless,mostofthemethodsemployexpensiveframeworkswhichuse

alargenumberofparametersfortraining.Alargenumberofparameters’requirementsnot

onlyincreasesthetrainingtimebutalsoenhancesthememoryrequirements.Toaddress

thisproblem,FEDS-Netdesignedanefficientdepthmechanismtominimizethenumberof

parameters.FEDS-Netisevaluatedusingthreeopendatabasesnamely;REFUGE,Drishti-

GS, and Rim-One-r3. The proposed network showed excellent segmentation without

leveragingcomputationalefficiency. FEDS-Netneedsonly2.73millionparametersfor

itstraining.

Thecontributionofthisworkissummarizedasfollows:

• Anovelarchitecture,FEDS-Net,isdevelopedforaccurateOCandODsegmentation

toassisttheexistingglaucomascreeningprocedures.FEDS-Netusesfeatureexcitation

andinformationaggregation(IA)tosignificantlyimprovepredictionaccuracy.

• InFEDS-Net,rapidfeaturedownsampling(RFD)andefficientconvolutionaldepth

(ECD)arealsointroducedfordiverseandefficientlearning,respectively.

• Theproposedarchitectureisevaluatedusingthreeopendatabases:REFUGE1,Drishti-

GS2,andRim-One-r33.FEDS-Netshowedexcellentperformancecomparedwithstate-

of-the-artmethods.Inaddition,outperformingresultsareobtainedwithasuperior

computationalefficiencyhavingarequirementofonly2.73millionparametersfor

fulltraining.

104

Mathematics2023,11,257

Theremainingpaperisorganizedasfollows.InSections2and3proposedmethods

andresultsarepresented, respectively. DiscussionisprovidedinSection4whereasa

conclusionofthestudyisgiveninSection5.

2.RelatedWork

Automatic glaucoma screening is a topic of vast interest. Many research studies

conductedtoautomateandassisttheglaucomadiagnosisprocedure.Existingstudiescan

bebroadlydividedintohandcraftedanddeepfeature-basedmethods.

2.1.MethodsBasedonHandcraftedFeatures

Manyresearchstudiesusedhandcraftedfeature-basedmethodsforautomaticglau-

comascreeningpurposes. Inthisstudy[9],ODpixel-wisesegmentationisperformed

usingthebloodvesselsinpaintingmechanism.Initially,aregiongrowingapproachisused

andthenabloodinpaintingschemeisemployedtodetectODregion.Evaluationofthe

proposedmodelisperformedusingmultipledatabasestoanalyzetheeffectivenessofthe

method.Preprocessingemployedinthismethodcanbeattributedasthelimitationofthis

study[9].

Similarly, anothermethod[10]usestexturefeaturesfortheglaucomaassessment.

Featureswereselectedbasedusingaproperfeatureselectionstructure. Theproposed

methodofthisstudyincludespreprocessingtoobtaintheregionofinterest(ROI)[10].

Inawork[11],pixelsbelongingtoODaredetectedbycombiningedgedetectionwith

adeformablemodelandHoughtransform[11]. Preprocessingrequirementstoremove

retinalvesselscanbeconsideredthelimitationofthiswork[11].

Inastudy[12],pixelsofODboundarywerepredictedbyreconstructingthemorphol-

ogyinfundusimages.Aconvexhullestimationwascarriedoutasthefinalsteptoextract

theboundaryofOD[12]. Adatasetthatneedstobeusedforthepreprocessingofthis

methodcanbeattributedasthelimitationofthiswork[12]. Anothermethod[13]uses

principalcomponentanalysis(PCA)fortheconversionoforiginalimagestoagrayscale

images. Inthismethod,ODisautomaticallydetectedusingmathematicalmorphology

incombinationwithPCA[13]. Theproposedmethodin[14]eliminatedperipapillary

atrophyforsegmentingtheODarea.Athree-stageprocesspipelinebasedonROIdetection,

edgefiltering,andHoughtransformisusedforeliminatingperipapillaryatrophy[14].

Approachingtheobtainedresultsusingthismethodrequirespostprocessing[14].

In[15],ODregioncandidatesarefirstselectedusingk-meansclustering.Secondly,OD

areaselectionisfinalizedbasedonthemaximumsaliency.Preprocessingrequirementscan

beattributedasthelimitationofthismethod[15].Similarlyin[16],anexpertsystemusing

anactivecontourapproachisproposedfortheOCandODsegmentation.Althoughthis

methodachievesahighsensitivityinperformance,however,itneedspreprocessing[16].

Anotherstudy[17]proposesacombinationoflevelsetandclusteringforpixel-wiseOC

andODsegmentation.Atfirst,ODboundariesareroughlypredictedusingclustering,and

segmentationresultswererefinedwiththehelpofalevelsetapproach[17].

2.2.MethodsBasedonDeepFeatures

Deeplearninghasavitalcontributiontoprovidingrobustandintelligentsolutions.In

manyresearchworks,deepfeature-basedsolutionsarepresentedalmostineveryfieldof

life[18].Deeplearning-basedmethodsareusuallyacceptedasaneffectiveandefficient

choicefordealingwithcomplexpatternsinimagesandvideos.Severalmethodsarealso

introducedforperformingsegmentationtaskstodetectdesiredfeaturesorpatternsfrom

medicalimages[19].Segmentationnetworksprovidepixel-wisepredictionsthathelpin

pixel-levelimageanalysis.Deepfeature-basedsegmentationalgorithmsareextensively

applied to retinal images for different disease quantification [20]. A recent study [5]

presentedapromptdeeplight-weightvesselsegmentationnetwork(PLVS-Net)todiagnose

diabeticretinopathy.PLVS-Netisbasedonpromptblocksthatcontainseparable,standard,

andasymmetricconvolutionallayers.Thesepromptblocksensureimprovedretinalvessels

105

Mathematics2023,11,257

segmentationwithenhancedcomputationalefficiency[5].However,theevaluationoftheir

methodwithdatasetshavinglessnumberofimagescanbeattributedasthelimitationof

thiswork.Subsequently,manyimageprocessing-basedautomatedmethodsusedOCand

ODsegmentationtoassisttheglaucomascreeningprocess[6].Inthiswork[6],adouble

thresholdmethodisemployed;initially,backgroundandretinalvesselsareremovedand

thensuperintensitypixelsinOCandODaresegmented.Preprocessingrequirementsof

thismethodcanbeconsideredastheweaknessoftheirproposedmethod[6]. Inref[7],

severaldeepfeature-basedmethodsassociatedwithglaucomaarediscussed.Alongwith

glaucomascreening,thisstudyalsoemphasizesdetectingglaucomaprogression[7].

AlthoughOCandODsegmentationisconsideredagoldstandardforcomputer-aided

glaucomadiagnosis. Nevertheless,fewmethodsuseotherfeaturesoffundusimaging

tostrengthentheautomateddiagnosis[8]. Inthiswork[8],ODandOCsegmentation

processisfollowedbyfocalnotchanalysisoftheneuralrimtoaidglaucomascreening.

Evaluationoftheproposedmethodwithasingledatasetcanbeattributedasthelimitation

of this work [8]. In a study [21], an encoder-decoder fashion architecture is used for

segmentingOCandOD,simultaneously.Theframeworkusedinthisstudyprovidesboth

imageclassificationandsegmentationoutputs[21]. Comparativelypoorsegmentation

performanceforOCcanbeattributedasthelimitationofthisstudy[21].Similarlyin[22],

opticdiscsegmentationisperformedusingaparticleswarmoptimizationnetwork.The

segmentationperformanceofmaskR-CNNisimprovedusingtransferlearningcombined

withoptimizationframeworks[22].ThismethodislimitedtoOD(notOC)segmentation

only[22].

Themethodproposedin[23]referstoanattention-basedmechanismfortheefficient

trainingprocessofthenetwork. Inthismethod, ODandOCrefinedsegmentationis

also achieved using a cascading approach [23]. Cascading itself can be the limitation

ofthismethodconsideringthecaseoftransferringfalsepredictiontothenextstage[23].

Similarlyin[24],acombinationofDenseNetandafullyconvolutionalnetworkisemployed

forsegmentingfundusimagesforglaucomascreening.Thecomputationalefficiencyof

thisframeworkisalsoenhancedusingthefeaturereuseapproach[24]. Limitationof

thismethodincludespreprocessingrequirementandinefficienttraining[24]. Another

method[25]employeddifferentCNNswithDeepLabv3+attheencoderendforsegmenting

ODpixels. Moreover, image-levelpredictions(classification)arealsogeneratedusing

transferlearningandpre-trainedmodels[25].Thisworkshowsseverallimitationsinterms

ofpriorrequirementssuchastransferlearning,preprocessing,andpretrainedmodels[25].

Afewmethodsalsousedadversariallearningforassistingtheglaucomascreening

process[26].Inthismethod,thedomain-shiftingproblemisaddressedusingapatch-based

adversarialframework[26].Thelimitationofthisstudycanbeattributedtoitspreprocess-

ingandpostprocessingrequirements[26]. Subsequently,anothermethod[27]basedon

adversariallearningisusedtosegmentretinalvesselsandOD.Inthisstudy,thefamous

U-Net[28]isusedasthegeneratorwhereasmultiplemodelsservefordiscrimination

purposesinadversariallearning[27].Inanotherstudy[29],arecurrentfullyconvolutional

mechanismisdevelopedtoovercometheproblemoffeaturelossinCNNs. High-level

informationalongwithedgeinformationisprocessedtoimprovethepixel-wiseOCand

ODsegmentationperformance[29].Evaluationwithasingledatabasecanbeconsidered

thelimitationofthisstudy[29].

U-Net[28]isconsideredabenchmarkarchitecture,especiallyformedicalimageseg-

mentation.FewstudiesreproducedandimplementedU-Netonacomputerforperforming

OCandODsegmentation[30]. TheeffectivenessofU-Netwithlimitedtimewasana-

lyzedinOCandODsegmentationtasks.Subsequently,anothermethod[31]madesome

modificationstothestandardU-Net[28]andevaluatedforOCandODsegmentation.

Channelsusedintheconvolutionallayersofthisnetworkwereoptimizedforanefficient

trainingprocess[31].Preprocessingrequirementscanbeattributedasthelimitationofthis

work[31].

106

Mathematics2023,11,257

3.MaterialandMethods

3.1.Datasets

Inourwork,theproposedmethodisevaluatedusingthreedatasetscontainingfundus

imagesforOCandODsegmentation.Allthreedatasets,namely;REFUGE1,Drishti-GS2,

andRim-One-r33[26]haveoriginalimageswithcorrespondingexpertannotations.Sample

imagesfortheREFUGEdatasetareshowninFigure1.Rows1and2inFigure1represent

originalandgroundtruthimages,respectively.Pixelsshowninblackandgraycolorsof

groundtruthimagesrepresentODandOCwhereaswhitecolorshowsthebackgroundclass.

REFUGEhasequallydivided(400imagesforeachcategory)imagesfortraining,validation,

andtestingpurposes.REFUGEisamongthelatestandmostchallengingdatasetsbecause

oftheextensiveintra-datasetvariations.

Figure1.SampleimagesfromtheREFUGEdatasetalongwithexpertannotationimages.

InFigure2,sampleimagesfromRim-One-r3andDrishti-GSdatasetsareshownin

rows1and2,respectively. Rim-One-r3iscollectedbyMIAGgroup(Spain)andithasa

totalof159fundusimageswithexpertannotations.TheDrishti-GSdatasetisalsooneof

thebenchmarkdatasetsforOCandODsegmentation. Ithasatotalof101imageswith

50trainingand51testingimages.TheODandOCannotationsforbothRim-One-r3and

Drishti-GSareprovidedinFigure2b,c.Blackpixelsinthegroundtruthimagesrepresent

thebackgroundclasswhereaswhitepixelsrefertodesiredclasses(OCandOD).Itis

worthnotingthatallthreedatasetshaveextensivevariationsinbackgroundeffects,pixel

intensityvalues, objects (OCandOD) sizes, andilluminationeffects whichmakesits

segmentationchallenging. Inaddition,mostoftheimageshaveasmall-sizedOCwith

unclearboundaries;therefore,accuratesegmentationbecomesevenmorechallenging.

(a) (b) (c)

Figure2.Sampleimagesfromrow1:Rim-One-r3;row2:Drishti-GSdatabases.(a)Originalimage

(b)groundtruthimagewithODannotation(c)groundtruthimagewiththeOCannotation.

107

Mathematics2023,11,257

3.2.ProposedMethod

3.2.1.OverviewoftheProposedMethod

OCandODpixel-wisesegmentationprovidesvaluableanalysisforglaucomadiag-

nosisandprognosis. AccuratesegmentationofOCandODischallengingbecauseof

thehighinterandintra-datasetsvariationsalongwithanindistinctareaofOC.Anovel

architecture,FEDS-Net,isdevelopedtoovercomethesechallenges.Anoverviewofthe

proposedframeworkisshowninFigure3.Inputimagesarefedtothenetworkandafter

featureprocessing, thenetworkprovidesapredictionmaskforOCand/orODatthe

output.Networksusuallyrequirealargeamountoftrainingdataforoptimallearningof

thenetwork.Tofulfillthisneed,trainingimagesareresizedandaugmentedtoproducea

sufficientamountoftrainingdata.FEDS-NetusesfeatureexcitationandIAmechanism

toboostthesegmentationaccuracy. Moreover,RFDandECDensureadiversifiedand

efficientlearningofthenetwork(detailsareprovidedinthesubsequentsubsection).The

trainedmodelofFEDS-Netgeneratesapredictionmaskandpredictionsarecompared

withgroundtruthimagesforresultsgeneration.Resizingthepredictionmaskbacktothe

originalsizeiscarriedoutforavalidevaluation. Trainingimagesareusedfortraining

purposeswhereastestingisperformedonlyforunseentestsplit.Inthepredictionmask,

whiteandblackpixelsrepresentdesired(OCand/orOD)andundesired(background)

classes,respectively,whereasFEDS-NetprovidessegmentedOCand/orODattheoutput.

Figure3.Theoverviewdiagramoftheproposedmethod.

3.2.2.ExplanationoftheProposedMethod

Existingmethodsareusuallybasedonsomefamousnetworksorusepre-trained

modelsasabackbone. InthecaseofODandOCsegmentation,famoussegmentation

architecturessuchasU-Net[28]andSegNet[32]cannotdeliverconvincingresultsbecause

ofthesmallobjectsizewithunclearboundaries. BothU-NetandSegNetarchitectures

exhibitvanishinggradientproblemsbecauseoftheexcessivelysmallfinalfeaturemapsize.

FEDS-Netisdevelopedfromscratch,anditisnotbasedonotherarchitecture.Thedetailed

networkarchitectureofFEDS-NetisshowninFigure4.Trainingimagesfromthetraining

splitareresizedforanefficienttrainingprocess.Inputimagesareprovidedtothenetwork

usingtheimageinputlayer. Imagefeaturesareextractedandactivationsareproduced

usingconvolutionallayers.InFEDS-Net,spatialinformationfromdifferentstagesofthe

networkisaggregatedwithspatialfeaturesatdifferentIApoints.FEDS-Nethasatotalof

fiveIApointsalmostateverystageofthenetwork.

108

Mathematics2023,11,257

Figure4.ThearchitectureoftheproposedFEDS-Net(Con:Convolutionallayer;BN:Batchnormal-

izationlayer;St-Con:Stridedconvolutionallayer;BotlNeck:Bottlenecklayer;RFD:Rapidfeature

downsampling;Trans-Con:Transposedconvolutionallayer;GC:Groupedconvolutionallayer;ECD:

Efficientconvolutionaldepth;PCL:Pixelclassificationlayer;IA:Informationaggregation).

InCNNs,theinitialspatialfeaturehasthepotentialtoimprovethepredictionaccuracy

ofthenetwork[33].Therefore,initialspatialfeatureexcitationisobtainedbyaggregating

featureswithdifferentprocesslevelsandchannelsatIA-1.InIA-1,initialspatialfeatures

fromthreedifferentconvolutionaleffectsalongwithidentitymappingfromthefirstconvo-

lutionallayerareaggregatedforinitialfeatureexcitation.TheoutputofIA-1isprovidedto

thestridedconvolutional(St-Con)layerviaabottleneck(BotlNeck)layer. Furthermore,

St-Conreducesthefeaturemapsizeandprocessesthespatialinformationfromaseriesof

fourconvolutionlayersforfurtheractivations.Activatedinformationfromtheseriesof

convolutionallayersisfurtheraggregatedwiththedownsampledspatialfeatureusing

St-ConatIA-2.ItisnotablethatFEDS-Netarchitecturedoesnotincludemaximumpooling

orunpoolinglayerstochangethefeaturemapdimensionstoavoidspatiallosscausedby

theselayers. Instead,FEDS-NetusesSt-Conandtransposedconvolutional(Trans-Con)

layerstoreduceandincreasethefeaturemapsize,respectively.

InCNNs,arelativelyhighstridevalueofSt-Conresultsinmoreefficientlearningofthe

network[34].Therefore,FEDS-NetusesRFDusingahighstrideof4intwoSt-Conlayers.

ThespatialinformationfromIA-2isfurtheractivatedthroughacoupleofconvolutional

layersviaaBotlNecklayerfollowedbyaStr-Con.InIA-3,rapiddownsampledfeaturesare

aggregatedwithspatialinformationfromacoupleofconvolutionallayers.Thisaggregated

informationisprovidedtoECD.TheECDhasvaluablesemanticinformationwiththe

maximumnumberofchannelsandminimumfeaturemapdimension.ECDisbasedonone

St-Con,fourgroupedconvolutionallayers,oneIApoint,andaBotlNecklayer.InCNNs,the

maximumdepthofthenetworkisthemostexpensivepartofthenetworkwhichstrongly

hitthecomputationalefficiencyofthenetwork.Nevertheless,FEDS-Netusedfourgrouped

convolutionallayerstocontaintherequirednumberofparametersinmaximumdepth.In

ECD(IA-4),aggregatedspatialinformationisfurtheraggregatedwithdownsampledand

activatedspatialfeaturesthroughthreeconvolutionallayers.FeatureaggregationinECD

helpsinlearningsemanticsandconsequentlyenhancepredictionaccuracy.

109

Mathematics2023,11,257

Subsequently,thespatialinformationdimensionisincreasedusingaTrans-Conlayer

andfedtoIA-5viaasingleconvolutionallayer. Asearliermentioned,initialfeatures

havethepotentialtoimprovetheoveralllearningofthenetwork. Theseinitialfeatures

underwentRFDandwereprovidedtoIA-5foraggregationwithupsampledfeaturesfrom

ECD.Thespatialdimensionoffinalaggregatedfeatures,fromIA-5,isincreasedusingtwo

Trans-Conlayersoneaftertheother.ThefinalspatialfeaturefromthelastTrans-Conlayer

isrefinedusingacoupleofconvolutionallayersbeforeprovidingtothesoftmaxandpixel

classificationlayers(PCL)forpixel-wisepredictions.PCLproducesapredictionmaskwith

themarkingofeachpixelbelongingtotherespectiveclass.

Keypartsoftheaggregationprocessarefurtherexplainedusingaschematicdiagram

inFigure5.Spatialinformation(Is )isfedtoIA(x)viaconvolutionallayersanditbecomes

(cid:16)

I. Similarly,initialfeaturesarerepresentedwithF andafterundergoingRFDbecome

s i

therapiddownsampledinitialfeatures(F (cid:16) ). InIA(x),I (cid:16) isaggregatedwithF (cid:16) andit

rdi s rdi

providesaggregatedspatialfeatures(Fax ),asfollows.

Fax =I

s

(cid:16) F

r

(cid:16)

di

(1)

Figure5.SchematicdiagramshowinginformationaggregationinFEDS-Net.

Becauseinformationaggregationisbasedonconcatenation;therefore,aggregation

isrepresentedwithsymbol©.afteractivationsthroughconvolutionallayersFaxbecome

(cid:16) (cid:16)

F .Subsequently,F isfurtherrefinedthroughaseriesofconvolutionallayersanditis

ax (cid:16)(cid:16)rdi (cid:16) (cid:16)(cid:16)

representedwithF . Inconvolutionaldepth,F isaggregatedwithF andfinally,it

rdi ax rdi

providesaggregatedfeaturesfromconvolutionaldepth(F )asgivenbelow

acd

F =F (cid:16) F (cid:16)(cid:16) (2)

acd ax rdi

F arefurtheractivatedusingconvolutionlayersandfinalfeaturesoutofconvolu-

acd

tiondepth(F (cid:16) )areprovidedforupsamplingbeforethepredictionstage. Thisfeature

acd

aggregationingeneralandinthemaximumdepth,inparticular,improvestheoverall

segmentationperformance.

3.2.3.Training,Testing,andtheExperimentalEnvironmentoftheProposedMethod

Inthisstudy,experimentationisperformedonthreepubliclyavailabledatabases.The

datasplitofREFUGEandDrishti-GSdatabasesarepre-definedbythedatasetproviders

andwefollowedthesameofficialsplitsinourexperiments.Fortheexperimentalworkof

Rim-One-r3,thesamedatasplitusedby[26]isfollowedforafaircomparison.Imagesfrom

thetrainingsplitareresizedusingnearestneighborinterpolationforfasttrainingofthe

network.Thelimitedavailabilityofannotatedmedicaldataisacommonlimitation,world-

wide.Therefore,trainingimagesareaugmentedtocreateartificialimages.Inthiswork,

arithmeticandgeometricoperationssuchascropping,flipping,androtationarerandomly

usedforaugmentation.NopreprocessingisinvolvedforthetrainingofFEDS-Net.

Asshowninsampleimages(Figures1and2),pixelsofdesiredclasses(OCandOD)are

significantlydominatedbyundesiredclass(background)pixelsandthisscenariotriggersa

110

Mathematics2023,11,257

class-imbalanceproblem.Intheexperimentalworkofthisstudy,diceloss(DL)isemployed

asthelossfunctionforthetrainingofthenetwork. DLmitigatestheclass-imbalance

problemandminimizesthemetricwhilebackpropagationandensuresconvergenceofthe

networkforeffectivetraining.Mathematically,DLisexpressedasfollows

(cid:24) (cid:31)

DL=1− 2×∑A k P Pro−k G Truth−k (3)

∑A

k

P2

Pro−k

+∑A

k

G2

True−k

Intheabovemathematicalexpression,Asymbolizesallpixelswhichareavailable

whereaskrepresentsthecurrentpixel.Theprobabilityofpredictionforkpixelisreferred

byP Pro−k andthetruegroundtruthlabelisrepresentedbyG Truth−k .Prepresentsgenerated

labelafterpredictionwhereasGdenotesthegroundtruth.

The proposed method is comprehensively evaluated on three publicly available

databases.Testingwasconductedonlyontheunseentestingsplitoftherespectivedatabase

forafairevaluation.AtrainedmodelbyFEDS-Netisappliedtothetestingimagesand

apixels-levelpredictionmaskisgeneratedforeachimage. Thepixelsoftheprediction

maskarecomparedwiththoseofthegroundtruthpixelstocomputeresultsonthebasesof

evaluationmeasures.Insemanticsegmentation,accuracy(AC),sensitivity(S),specificity

(SPE),dicesimilaritycoefficient(DSC),andJaccardindex(JCI)arethecommonlyaccepted

measuresforevaluation[35]. Inevaluationmeasures,truepositive(tp),truenegative

(tn),falsepositive(fp),andfalsenegative(fn)pixelsarecomputedfortheevaluation

purposes.Mathematicallyevaluationmeasurescanbegiven,asfollows

AC= tp+f t n p+ + t f n p+tn (4)

S= tp+ tp fn (5)

SPE= tn+ tn fp (6)

DSC= 2tp+ 2 f t p p +fn (7)

JCI= tp+f t p p +fn (8)

FEDS-Netisdevelopedfromscratchandalltheexperimentalworkisperformed

usingMATLAB2021a[36]framework. Inaddition,Intel®Core™i7CPU950@3.7GHz

processor(IntelCorporation,Seoul,RepublicofKorea)withanNVIDIAGeForceGTX

1080graphicsprocessingunit(GPU)[37](NVIDIACorporation,Seoul,RepublicofKorea)

having8GBgraphicsmemoryisusedforexperiments.Computationaldetailsrelatedto

trainableparametersandinferencetimearepresentedinTables4and5,respectivelyin

Section5.

4.Results

Theproposedmethodisevaluatedusingthreeopendatabasescontainingretinal

fundusimages.FEDS-Netdeliveredexcellentsegmentationresults.Bothqualitativeand

quantitativeresultsforallthreedatabasesaregiveninsubsequentsubsections.

4.1.FEDS-NetEvaluationUsingREFUGEDatabase

REFUGEisoneofthelatestandmostchallengingdatasetsforODandOCsegmen-

tation. ImagesinREFUGEdatasetsareentirelydifferentfromtheothertwodatabases.

Nonetheless,FEDS-NetprovidedsuperiorsegmentationperformanceforbothOCand

ODclasses. ManyimagesinthetestingsplithaveaverysmallOCareawithindistinct

boundaries.However,FEDS-Netdeliveredabettersegmentationaccuracyevenforsuch

challengingcases.QualitativegoodandpoorsegmentationresultsusingFEDS-Netonthe

111

Mathematics2023,11,257

REFUGEdatabaseareshowninFigures6and7,respectively. Poorresultsareperhaps

becauseoftheunclearobjects’boundariesalongwiththesmallsizeofOC.

(a) (b) (c)

Figure6. GoodOCandODsegmentationqualitativeresultsontheREFUGEdatabase,attained

byapplyingFEDS-Net.(a)Inputimage,(b)correspondinggroundtruthimage,and(c)segmented

outputimages(tppixelsforODandOCareindicatedinyellowandblue,respectively.Likewise,red

andgreenshowfnandfppixels,respectively).

(a) (b) (c)

Figure7.PoorOCandODsegmentationqualitativesampleresultsontheREFUGEdatabase,attained

byapplyingFEDS-Net.(a)Inputimage,(b)correspondinggroundtruthimage,and(c)segmented

outputimages(tppixelsforODandOCareindicatedinyellowandblue,respectively.Likewise,red

andgreenshowfnandfppixels,respectively).

112

Mathematics2023,11,257

QuantitativeOCandODsegmentationresultsarefurthercomparedwiththoseof

thestate-of-the-artmethodstoconfirmtheeffectivenessoftheproposedmethod. The

listedresultsinTable1showabettersegmentationperformanceofFEDS-Netcompared

withexistingmethods. Itisworthnotablethatmostofthemethodsrequireextensive

preprocessingtoachievethedesiredperformance.Instead,theproposedmethoddidnot

employanypreprocessingtokeepthemethodstraightforward.

Table1.SegmentationquantitativeresultscomparisonofFEDS-Netwithstate-of-the-artmethods

usingtheREFUGEdatabase. “-“indicatesthatnoresultisavailable(unit: %). (OC:opticcup;

OD:opticdisc;AC:accuracy;S:sensitivity;SPE:specificity;DSC:dicesimilaritycoefficient;JCI:

jaccardindex).

OC OD

Methods

AC S SPE DSC JCI AC S SPE DSC JCI

Variationalauto-encoder[38] - - - 88.91 - - - - 95.81 -

Patch-basedpOSALseg-T[26] - - - 88.2 - - - - 96.0 -

M-Ada[21] - - - 88.25 - - - 95.85 -

SLSR-Net[39] 99.90 94.70 99.90 89.50 81.50 99.80 96.90 99.90 96.50 93.30

U-Net+VGG16encoder[40] - - - - - 99.8 95.7 - 94.0 89.0

Mask-RCNN[41] - - - 85.4 - - - - 94.7 -

ET-Net[42] - - - 89.1 - - - - 95.2 -

U-Net[28] - - - 85.4 - - - - 93.0 -

Self-attention[23] 85.36 95.09

Teammasker[43] - - - 88.3 - - - - 94.6 -

Cascadednetwork[25] - - - 88.04 - - - - 93.31 -

TeamBUCT[43] - - - 87.2 - - - - 95.2 -

Segtran(eff-B4)[44] - - - 87.2 - - - - 96.1 -

Multi-modalapproach[45] - - - - 79.02 - - - - 92.25

ConditionalGAN[46] - - - - 80.0 - - - - 88.4

FEDS-Net(Proposedmethod) 99.91 90.40 99.96 89.80 82.13 99.89 96.62 99.94 96.53 93.39

4.2.FEDS-NetEvaluationUsingDrishti-GSDatabase

EvaluationofFEDS-NetisextendedtobenchmarkDrishti-GSdatabase. Imagesin

theDrishti-GSdatabaseareentirelydifferentfromthoseoftheothertwodatabasesofthis

study. Nevertheless,theproposedmethodprovidedsuperiorsegmentationaccuracies

fortheDrishti-GSdatabasetoo. QualitativeresultsofODandOCsegmentationonthe

Drishti-GSdatabasearepresentedinFigures8and9,respectively. Figure8(rows1–3),

showsgoodODsegmentationvisualresultswhereasFigure8(row4)showssamplevisual

resultofrelativelypoorsegmentation.Similarly,goodsegmentationqualitativeresultsfor

OCsegmentationoftheDrishti-GSdatabaseareshowninFigure9(rows1–3)whereasthe

relativelypoorvisualresultisshowninFigure9(row4).Poorsegmentationcasescanbe

attributedtoindistinctobjectboundaries.

InTable2,quantitativeresultsproducedbyFEDS-Netarecomparedwithstate-of-

the-artmethodsontheDrishti-GSdatabase. Resultsconfirmaconvincingperformance

byFEDS-NetusingitsfeatureexcitationandIAmechanism. FEDS-Netensuresahigh

segmentationperformancewithoutdisregardingthetrainingparameters’overheads.FEDS-

Netusedasmallnumberoftrainingparameterstoachieveoutperformingresults.

4.3.FEDS-NetEvaluationUsingRim-One-r3Database

TheproposedmethodisfurtherevaluatedusingtheRim-One-r3databasewithchal-

lengingpixelintensityvariations.FEDS-Neteffectivelydealswiththesevariationsusing

itsarchitecturalstrengths.QualitativeresultsproducedbyFEDS-NetfortheODandOC

segmentationareprovidedinFigures10and11,respectively.Qualitativeresultsconfirm

thatFEDS-Netprovidesexcellentsegmentationaccuracyfordifferentpixelintensityvaria-

tionsandilluminationeffects. Goodsegmentationperformance’squalitativeresultsare

presentedinFigures10and11(rows1–3)whereasrelativelypoorsegmentationisshown

113

Mathematics2023,11,257

inFigures10and11(row4).Poorsegmentationcasescanbeattributedtoindistinctobjects’

boundariesalongwithvariationsinpixelintensityvaluesandilluminationeffects.

(a) (b) (c)

Figure8.GoodODsegmentationqualitativeresultsontheDrishti-GSdatabase,attainedbyapplying

FEDS-Net.(a)Inputimage,(b)correspondinggroundtruthimage,and(c)segmentedoutputimages

(tpandfnpixelsforODareindicatedinblueandred,respectively.Whereas,fppixelsarepresented

withgreencolor)(Rows1–3:goodsegmentationresults;Row4:poorsegmentationresult).

(a) (b) (c)

Figure9.GoodOCsegmentationqualitativeresultsontheDrishti-GSdatabase,attainedbyapplying

FEDS-Net.(a)Inputimage,(b)correspondinggroundtruthimage,and(c)segmentedoutputimages

(tpandfnpixelsforODareindicatedinyellowandred,respectively,whereasfppixelsarepresented

ingreencolor)(Rows1–3:goodsegmentationresults;Row4:poorsegmentationresult).

114

Mathematics2023,11,257

Table2.SegmentationquantitativeresultscomparisonofFEDS-Netwithstate-of-the-artmethods

usingtheDrishti-GSdatabase. “-”indicatesthatnoresultisavailable(unit: %). (OC:opticcup;

OD:opticdisc;AC:accuracy;S:sensitivity;SPE:specificity;DSC:dicesimilaritycoefficient;JCI:

jaccardindex).

OC OD

Methods

AC S SPE DSC JCI AC S SPE DSC JCI

U-NetwithVGG16encoder[40] - - - - - 99.79 97.54 - 96.5 93.1

ModU-Net[47] - - - 88.7 80.4 - - - 97.3 94.9

RACE-Net[48] - - - 87.0 - - - - 97.0 -

RetinaGAN[27] - - - - - - - - 96.7 -

Entropysampling[49] - - - 87.1 - - - - 97.3 -

FC-DenseNet[24] 99.4 - - 82.8 71.1 99.6 - - 94.9 90.4

Depthestimation[50] - - - 83.0 - - - - 97.0 -

FCNandadversarial[51] - - - 85.0 75.0 - - - - -

Edgesmoothingapproach[52] - - - 81.0 - - - - 95.0 -

ModifiedU-Net[31] - - - 85.0 - - - - - -

Shaperegression[53] - - - 85.0 - - - - 95.0 -

Multi-Stageframework[54] - - - 84.0 - - - - 97.0 -

Drishti-GSChallenge[55] - - - 79.0 - - - - 96.0 -

EdgeTPU[30] - - - 88.0 - - - - 90.0 -

U-Net[28] 98.1 86.5 98.3 70.2 57.8 99.2 92.8 99.4 91.3 85.8

NAS-U2-Net[56] - - - 87.69 - - - - 96.95 -

FEDS-Net(Proposedmethod) 99.66 93.28 99.81 90.40 83.38 99.86 97.64 99.94 98.01 95.99

(a) (b) (c)

Figure10. GoodODsegmentationqualitativeresultsontheRim-One-r3database,attainedby

applyingFEDS-Net.(a)Inputimage,(b)correspondinggroundtruthimage,and(c)segmentedoutput

images(tpandfnpixelsforODareindicatedinblueandred,respectively.Whereasfppixelsare

presentedwithgreencolor)(Rows1–3:goodsegmentationresults;Row4:poorsegmentationresult).

115

Mathematics2023,11,257

(a) (b) (c)

Figure11. GoodOCsegmentationqualitativeresultsontheRim-One-r3database,attainedby

applyingFEDS-Net.(a)Inputimage,(b)correspondinggroundtruthimage,and(c)segmentedoutput

images(tpandfnpixelsforODareindicatedinyellowandred,respectively.Whereasfppixelsare

presentedingreencolor)(Rows1–3:goodsegmentationresults;Row4:poorsegmentationresult).

FEDS-NetquantitativeresultsarelistedinTable3forcomparisonwithexistingmeth-

ods.Resultsexhibitacompetitiveandconvincingperformancebytheproposedmethod.

Aggregationoffeaturesresultsineffectivetraining;therefore,FEDS-netmaintainsitsbetter

performanceevendealingwithchallengingvariations.

Table3.SegmentationquantitativeresultscomparisonofFEDS-Netwithstate-of-the-artmethods

usingRim-One-r3database. “-”indicatesthatnoresultisavailable(unit: %). (OC:opticcup;

OD:opticdisc;AC:accuracy;S:sensitivity;SPE:specificity;DSC:dicesimilaritycoefficient;JCI:

jaccardindex).

OC OD

Methods

AC S SPE DSC JCI AC S SPE DSC JCI

Patch-basedpOSALseg-T[26] - - - 85.6 - - - - 96.8 -

DRIU[57] - - - - - - - - 95.5 -

U-Netwithmodification[31] - - - - - - - - 95.0 -

RetinaGAN[27] - - - - - - - - 95.5 -

Entropysampling[49] - - - 82.4 - - - - 94.2 -

Auto-encoder[58] - - - - - 99.45 87.30 99.81 90.2 88.24

EdgeTPU[30] - - - 84.0 - - - - 85.0 -

FEDS-Net(Proposedmethod) 99.60 87.67 99.80 86.20 76.20 99.73 96.97 99.86 97.01 94.13

5.Discussion

Thetrendofophthalmicdiseasesisontherise,worldwide.Ophthalmologistshave

toexaminemanyglaucoma-suspectedpatientsdaily.Typically,glaucoma-relatedexami-

nationsareconductedmanuallywhichissubjective,time-consuming,andpronetoerror

procedure. Therefore,theneedofthetimeistoassistophthalmologistswithAI-based

automatedsolutions.HundredsofresearchstudiesacceptedthatOCandODsegmentation

116

Mathematics2023,11,257

canassisttheglaucomadiagnosisprocess.However,OCandODsegmentationtaskhas

manyassociatedchallenges.Fundusimageshaveahighvariationinpixelintensityvalues,

backgrounds,OC/ODsizes,andilluminationsthatmakesthesegmentationtricky. In

addition,OCsizeisusuallyverysmallanditsboundaryistooindistincttoaccurately

segment.Nevertheless,FEDS-Netovercomesthesechallengesusingfeatureexcitation,IA,

RFD,andECDinitsarchitecture.Computationalefficiencyisanotherseriouscriterionfor

modernAI-basedframeworks.Inmostcases,existingmethodsshowseriouslimitations

incomputationalefficiencyandrequirealargenumberofparametersforthecomplete

trainingoftheirmodel.FEDS-Netnotonlyprovidesexcellentsegmentationaccuraciesbut

alsomaintainscomputationalefficiency.FEDS-Netrequiresonly2.73millionparameters

whichturnsouttoconfirmitscomputationalstrength.ThecomparisonofFEDS-Netwith

existingmethodsintermsofrequiredtrainableparametersislistedinTable4.Parameters’

comparisonexhibitsthattheproposedmethodrequiresasmallernumberofparameters

comparedwiththoseofthestate-of-the-artmethods. Inaddition, inferencetime(per

image)forallthreedatasetsusingFEDS-NetisalsocomputedandpresentedinTable5.A

considerablylessinferencetimeisalsobecauseofthecomputationaleffectivenessofthe

proposedmethod.

Table4.Comparisonoftrainableparameterswiththoseoftheexistingmethods.(OC:opticcup;OD:

opticdisc;DSC:dicesimilaritycoefficient).

DSC(%)

Methods NumberofParameters(Million)

OC OD

Teammasker[43] 1224 88.3 94.6

Mask-RCNN[41] 127 85.4 94.7

Segtran(eff-B4)[44] 93.1 87.2 96.1

pOSAL(Xception)[26] 41.3 88.5 95.3

U-Net[28] 31.03 85.4 93.0

U-NetwithVGG16encoder[40] 16.8 - 94.0

pOSAL(MobileNetV2)[26] 5.8 88.5 95.6

FEDS-Net(Proposed) 2.73 89.80 96.53

Table5.Inferencetime(perimage)computationusingFEDS-Net.

Sr. Dataset InferenceTime(Seconds)

1 REFUGE 0.11

2 Rim-One-r3 0.091

3 Drishti-GS 0.097

5.1.AssistingtheGlaucomaScreeningProcess

Automatedglaucomadiagnosismethodsarerequiredtostrengthenexistingtradi-

tionalglaucomascreeningmethods.TheOCandODsegmentationcanprovidevaluable

computationalandmorphologicaldetailsthatcanworkasparallelsupportforophthalmol-

ogists[26].AccurateOCandODsegmentationcanleadtoprovidingpreciseV-CDRvalue

andV-CDRisanimportantbiomarkerforophthalmologistsinglaucomadiagnosisand

prognosis.Glaucomausuallycausescupping,whichreferstoanincreaseinthesizeofOC.

TheincreasedsizeofOCincreasestheV-CDRvaluewhichconsequentlyreflectsahighrisk

ofglaucoma[53].V-CDRismathematicallyexpressedas

V−CDR= vDc (9)

vDD

Intheabovemathematicalexpression,vDcrepresentstheverticaldiameterofthecup

areawhereasvDDsymbolizesdiscarea.Theratiobetweenbothverticaldiametersofthe

cupanddiscprovidesaV-CDRvalue.AsampleV-CDRcomputationfromtheREFUGE

databaseispresentedinFigure12.TheCDRvalueofgroundtruthimageisrepresentedby

117

Mathematics2023,11,257

CDRgtwhereaspredictedCDRbyFEDS-NetisshownwithCDRpr.ThecomputedCDR

byFEDS-NetisquiteclosertothatoftheCDRgtvaluethatconfirmstheeffectivenessof

FEDS-NetinaccuratelysegmentingtheOCandOD.

Figure12.SampleCDRcomputationusingtheREFUGEdataset.

AlthoughV-CDRcomputationprovidespotentialinsightforassistingtheglaucoma

screeningprocess,nevertheless;segmentation-basedglaucomascreeningisnotlimited

toonlyV-CDRcomputations.Thearea-cup-to-disc-ratio(Ar-CDR)isanothermeasureto

assesstheglaucomaoccurrence[8].Ar-CDRistheratiobetweentheareaofthecupregion

andthediscregion. Glaucomaoccurrenceandprogressionbringchangesintheareaof

OCandOD(mainlyOC);therefore;Ar-CDRcanalsoprovideconsiderableassistancein

glaucomadiagnosisandprognosis[8]. V-CDRhasalimitationinselectingareference

centerpointforcalculatingverticaldiameterswhereasAr-CDRisanarea-basedapproach

anddoesnotrequireanyreferencepoint. Moreover,glaucomaprogressioncanalsobe

assessedbyanalyzingthechangeintheareaofonlyOCduringpatients’multiplevisits[17].

TherimareabetweenODandOCistermedaneuralrim.Thenotchingphenomenonis

theshrinkageoftheneuralrim,itcanbealsoanalyzedforglaucomascreening.Similarly,

thediscdamagelikelihoodscale(DDLS)iscalculatedfortheestimationandquantification

ofthisdisease[59].TheDDLScanbecomputedbytakingtheratiobetweenthethinnest

partoftheneuralrimanddiscdiameter[59].Subsequently,theinferiorsuperiornasaland

temporal(ISNT)rulealsoprovidesasolidbasistodiscriminatebetweenglaucomatous

andnon-glaucomatouscases[60]. AccordingtotheISNTrule,thewidthoftheneural

rimshouldbebiggesttosmallestfortheinferior,superior,nasal,andtemporalregions,

respectively[60].CasessatisfyingtheISNTruleareclassifiedasnon-glaucomatouscases

otherwisevice-versa.

5.2.OCandODSegmentationfortheDiagnosisofOtherDiseases

AccuratesegmentationofOCandODnotonlyassistsinglaucomascreeningbutalso

helpsinthediagnosisofsomeotherdiseases.Alzheimer’sdisease(AD)isaneurodegenera-

tiveproblemthatcanbeassessedusingOCandODsegmentation[61].Similartoglaucoma

suspects,ahighV-CDRvaluereferstoahighriskofAD.Subsequently,poorcognitive

functioniscommonamongpostmenopausalwomen[62].MedicalexpertsconsiderV-CDR

forcognitiveassessmentofthepatient.Hence,accurateOCandODsegmentationisalso

crucialforassistinginthediagnosisofnumerousdiseases.

5.3.DemonstratingLearningoftheNetworkusingHeatActivationMaps

UnderstandingthelearningprocessorfeatureselectionofaCNNisveryhardto

visuallyexplain.Gradient-weightedclassactivationmapping(Grad-CAM)[63]isusedfor

thevisualdemonstrationofnetworklearning.InFigure13,heatactivationmapsofODand

OCusingtheRim-One-r3databasearepresentedinrows1and2,respectively.Asshown

inFigure13c–f,heatactivationmapsareextractedfromdifferentlayersofthenetworkto

assessthelearningprocess.Grad-CAMreferstothemainfeaturesselectedbytheCNN

duringtrainingandmarksthemwithdistinguishedcolors.Figure13(lastcolumn)istaken

118

Mathematics2023,11,257

fromthelastlayersofthenetwork,anditconfirmsthatFEDS-netrightfullyfocuseson

desiredclasseswithoutanybiases.

(a) (b) (c) (d) (e) (f)

Figure13.VisualexplanationofFEDS-NetlearningprocessusingheatactivationmapswithRim-

One-r3database. ActivationmapsfortheODandOCareprovidedinrows1and2,respectively.

(a)Inputimage.(b)groundtruthimage.Heatactivationmapsextractedfrom(c)Initiallayer,(d)first

convolutionallayerafterIA-2,(e)convolutionallayerafterECD,and(f)finalconvolutionallayerof

thenetwork.

6.Conclusions

Glaucomaisoneofthemostcriticalophthalmicdiseasesthatcanleadtoirreversible

visionloss. Glaucomaistypicallydiagnosedwithmanualassessmentswhichisatime-

consuming,error-prone,andinefficientprocedure.Therefore,AI-basedautomaticmethods

aredesirabletoassistophthalmologistsinglaucomadiagnosis. MostoftheexistingAI-

basedmethodsrequirecomplexpreprocessing,lacksegmentationperformance,andshow

seriouslimitationsintermsofcomputationalefficiency. Toaddressalltheseproblems,

anovelarchitectureFEDS-NetisdevelopedforaccuratesegmentationofOCandOD.

FEDS-NetusesfeatureexcitationandIAmechanismtoenhancethepredictionaccuracies.

Moreover,FEDS-NetemploysECDandRFDblocksfordiverseandefficientlearningof

thenetwork.Theproposedmethodisevaluatedonthreechallengingdatabases;REFUGE,

Drishti-GS,andRim-One-r3.FEDS-Netshowedoutperformingsegmentationperformance

withoutdisregardingthecomputationalrequirementsofthenetwork.FEDS-Netrequires

only2.73milliontrainingparametersforitscompletetraining.FEDS-Netproducedbetter

resultscomparedwiththoseofstate-of-the-artmethods.Hence,theproposedmethodcan

beusedassecond-levelsupportforophthalmologistsinglaucomadiagnosisandprognosis.

RelativelylowsegmentationaccuraciesforOCbecauseofitsindistinctboundaries

canbeattributedasthecommonlimitationforallmethods. AlthoughFEDS-Netdeliv-

ered a better performance for OC, still more techniques can be researched for further

improvement. Inthefuture, weintendtoexploremoretechniquesforenhancingOC

segmentationperformance.

AuthorContributions:A.R.,S.A.andM.I.Conceptualization,Methodology,Software,Visualization,

WritingOriginalDraft.;H.S.K.andR.A.N.DataCuration,Resources,Software,Editing;R.A.N.Re-

sources,Validation,Methodology;S.-W.L.Projectadministration.Investigation,Fundingacquisition,

Supervision.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.

Funding:Thisworkwassupportedbyanationalresearchfoundation(NRF)grantfundedbythe

MinistryofScienceandICT(MSIT),RepublicofKoreathroughtheDevelopmentResearchProgram

(NRF2022R1G1A1010226)and(NRF2021R1I1A2059735).

119

Mathematics2023,11,257

InstitutionalReviewBoardStatement:Thisstudyisbasedonpubliclyavailabledatasetsmentioned

inSection3.1.Thedatasetsarepublicforresearchpurposes,thereforeitisnotapplicable.Weblinks

foruseddatasetsofthisstudyareasfollows.REFUGE:https://ai.baidu.com/broad/download?

dataset=gon.(accessedon10August2022)Drishti-GS:http://cvit.iiit.ac.in/projects/mip/drishti-

gs/mip-dataset2/Home.php.(accessedon10August2022)Rim-One-r3:http://medimrg.webs.ull.

es/rim-one-release-3-is-finally-here/(accessedon10August2022).

InformedConsentStatement:Notapplicable.

DataAvailabilityStatement:Notapplicable.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

References

1. Troy,J.B.Visualprostheses:Technologicalandsocioeconomicchallenges.Engineering2015,1,288–291.[CrossRef]

2. Shanmugam,P.;Raja,J.;Pitchai,R.Anautomaticrecognitionofglaucomainfundusimagesusingdeeplearningandrandom

forestclassifier.Appl.SoftComput.2021,109,107512.[CrossRef]

3. Haider,A.;Arsalan,M.;Choi,J.;Sultan,H.;Park,K.R.Robustsegmentationofunderwaterfishbasedonmulti-levelfeature

accumulation.Front.Mar.Sci.2022,9,1010565.[CrossRef]

4. Arsalan,M.;Haider,A.;Cho,S.W.;Kim,Y.H.;Park,K.R.Humanblastocystcomponentsdetectionusingmultiscaleaggregation

semanticsegmentationnetworkforembryonicanalysis.Biomedicines2022,10,1717.[CrossRef]

5. Arsalan,M.;Khan,T.M.;Naqvi,S.S.;Nawaz,M.;Razzak,I.Promptdeeplight-weightvesselsegmentationnetwork(PLVS-Net).

IEEE/ACMTrans.Comput.Biol.Bioinform.2022,1–9.[CrossRef]

6. Dutta,M.K.;Mourya,A.K.;Singh,A.;Parthasarathi,M.;Burget,R.;Riha,K.Glaucomadetectionbysegmentingthesuperpixels

fromfunduscolourretinalimages.InProceedingsoftheInternationalConferenceonMedicalImaging,m-Health,andEmerging

CommunicationSystems,GreaterNoida,India,7–8November2014;pp.86–90.

7. Thompson,A.C.;Jammal,A.A.;Medeiros,F.A.Areviewofdeeplearningforscreening,diagnosis,anddetectionofglaucoma

progression.Transl.Vis.Sci.Technol.2020,9,42.[CrossRef]

8. Dasgupta,S.;Mukherjee,R.;Dutta,K.;Sen,A.Deeplearningbasedframeworkforautomaticdiagnosisofglaucomabasedon

analysisoffocalnotchingintheopticnervehead.arXiv2021,arXiv:2112.05748.

9. Sarathi,M.P.;Dutta,M.K.;Singh,A.;Travieso,C.M.BloodVesselinpaintingbasedtechniqueforefficientlocalizationand

segmentationofopticdiscindigitalfundusimages.Biomed.SignalProcess.Control2016,25,108–117.[CrossRef]

10. Septiarini,A.;Harjoko,A.;Pulungan,R.;Ekantini,R.Automateddetectionofretinalnervefiberlayerbytexture-basedanalysis

forglaucomaevaluation.Healthc.Inf.Res2018,24,335–345.[CrossRef]

11. Yin,F.;Liu,J.;Ong,S.H.;Sun,Y.;Wong,D.W.K.;Tan,N.M.;Cheung,C.;Baskaran,M.;Aung,T.;Wong,T.Y.Model-basedoptic

nerveheadsegmentationonretinalfundusimages.InProceedingsoftheIEEEonInternationalConferenceonIEEEEngineering

inMedicineandBiologySociety,Boston,MA,USA,30August–3September2011;pp.2626–2629.

12. Roychowdhury,S.;Koozekanani,D.D.;Kuchinka,S.N.;Parhi,K.K.Opticdiscboundaryandvesseloriginsegmentationoffundus

images.IEEEJ.Biomed.HealthInform.2016,20,1562–1574.[CrossRef]

13. Morales,S.;Naranjo,V.;Angulo,J.;Alcañiz,M.AutomaticdetectionofopticdiscbasedonPCAandmathematicalmorphology.

IEEETrans.Med.Imaging2013,32,786–796.[CrossRef][PubMed]

14. Cheng,J.;Liu,J.;Wong,D.W.K.;Yin,F.;Cheung,C.;Baskaran,M.;Aung,T.;Wong,T.Y.Automaticopticdiscsegmentationwith

peripapillaryatrophyelimination.InProceedingsoftheIEEEInternationalConferenceonIEEEEngineeringinMedicineand

BiologySociety,Boston,MA,USA,30August–3September2011;pp.6224–6227.

15. Xue,L.-Y.;Lin,J.-W.;Cao,X.-R.;Zheng,S.-H.;Yu,L.Opticdiskdetectionandsegmentationforretinalimagesusingsaliency

modelbasedonclustering.J.Comput.2018,29,66–79.[CrossRef]

16. Mittapalli,P.S.;Kande,G.B.Segmentationofopticdiskandopticcupfromdigitalfundusimagesfortheassessmentofglaucoma.

Biomed.SignalProcess.Control2016,24,34–46.[CrossRef]

17. Thakur,N.;Juneja,M.Opticdiscandopticcupsegmentationfromretinalimagesusinghybridapproach.ExpertSyst.Appl.2019,

127,308–322.[CrossRef]

18. Arsalan,M.;Haider,A.;Choi,J.;Park,K.R.detectingblastocystcomponentsbyartificialintelligenceforhumanembryological

analysistoimprovesuccessrateofinvitrofertilization.J.Pers.Med.2022,12,124.[CrossRef]

19. Haider,A.;Arsalan,M.;Lee,Y.W.;Park,K.R.Deepfeaturesaggregation-basedjointsegmentationofcytoplasmandnucleiin

whitebloodcells.IEEEJ.Biomed.HealthInform.2022,26,3685–3696.[CrossRef]

20. Arsalan,M.;Haider,A.;Koo,J.H.;Park,K.R.Segmentingretinalvesselsusingashallowsegmentationnetworktoaidophthalmic

analysis.Mathematics2022,10,1536.[CrossRef]

21. Hervella,Á.S.;Rouco,J.;Novo,J.;Ortega,M.End-to-endmulti-tasklearningforsimultaneousopticdiscandcupsegmentation

andglaucomaclassificationineyefundusimages.Appl.SoftComput.2022,116,108347.[CrossRef]

22. Zhang,L.;Lim,C.P.Intelligentopticdiscsegmentationusingimprovedparticleswarmoptimizationandevolvingensemble

models.Appl.SoftComput.2020,92,106328.[CrossRef]

120

Mathematics2023,11,257

23. Bian,X.;Luo,X.;Wang,C.;Liu,W.;Lin,X.Opticdiscandopticcupsegmentationbasedonanatomyguidedcascadenetwork.

Comput.MethodsProgramsBiomed.2020,197,105717.[CrossRef]

24. Al-Bander,B.;Williams,B.M.;Al-Nuaimy,W.;Al-Taee,M.A.;Pratt,H.;Zheng,Y.Densefullyconvolutionalsegmentationofthe

opticdiscandcupincolourfundusforglaucomadiagnosis.Symmetry2018,10,87.[CrossRef]

25. Sreng,S.;Maneerat,N.;Hamamoto,K.;Win,K.Y.Deeplearningforopticdiscsegmentationandglaucomadiagnosisonretinal

images.Appl.Sci.2020,10,4916.[CrossRef]

26. Wang,S.;Yu,L.;Yang,X.;Fu,C.-W.;Heng,P.-A.Patch-basedoutputspaceadversariallearningforjointopticdiscandcup

segmentation.IEEETrans.Med.Imaging2019,38,2485–2495.[CrossRef][PubMed]

27. Son,J.;Park,S.J.;Jung,K.-H.Towardsaccuratesegmentationofretinalvesselsandtheopticdiscinfundoscopicimageswith

generativeadversarialnetworks.J.Digit.Imaging2019,32,499–512.[CrossRef]

28. Ronneberger,O.;Fischer,P.;Brox,T.U-Net:Convolutionalnetworksforbiomedicalimagesegmentation.InProceedingsoftheIn-

ternationalConferenceonMedicalImageComputingandComputer-AssistedIntervention,Munich,Germany,5–9October2015;

pp.234–241.

29. Gao,J.;Jiang,Y.;Zhang,H.;Wang,F.Jointdiscandcupsegmentationbasedonrecurrentfullyconvolutionalnetwork.PLoSONE

2020,15,e0238983.[CrossRef]

30. Civit-Masot,J.;Luna-Perejón,F.;Corral,J.M.R.;Domínguez-Morales,M.;Morgado-Estévez,A.;Civit,A.Astudyontheuseof

edgeTPUsforeyefundusimagesegmentation.Eng.Appl.Artif.Intell.2021,104,104384.[CrossRef]

31. Sevastopolsky,A.OpticdiscandcupsegmentationmethodsforglaucomadetectionwithmodificationofU-netconvolutional

neuralnetwork.PatternRecognit.ImageAnal.2017,27,618–624.[CrossRef]

32. Badrinarayanan,V.;Kendall,A.;Cipolla,R.SegNet:Adeepconvolutionalencoder-decoderarchitectureforimagesegmentation.

IEEETrans.PatternAnal.Mach.Intell.2017,39,2481–2495.[CrossRef][PubMed]

33. HosseinzadehKassani,S.;HosseinzadehKassani,P.;Wesolowski,M.J.;Schneider,K.A.;Deters,R.Deeptransferlearningbased

modelforcolorectalcancerhistopathologysegmentation:Acomparativestudyofdeeppre-trainedmodels.Int.J.Med.Inform.

2022,159,104669.[CrossRef][PubMed]

34. Kong,C.;Lucey,S.Takeitinyourstride:DoweneedstridinginCNNs?arXiv2017,arXiv:1712.02502.[CrossRef]

35. Bengani,S.;Jothi,J.A.A.J.;Vadivel,S.Automaticsegmentationofopticdiscinretinalfundusimagesusingsemi-superviseddeep

learning.Multimed.ToolsAppl.2021,80,3443–3468.[CrossRef]

36. MATLABR2021a.Availableonline:https://www.mathworks.com/products/matlab.html(accessedon5March2022).

37. GeForceGTX.Availableonline:https://www.nvidia.com/en-gb/geforce/products/10series/geforce-gtx-1070/(accessedon

5March2022).

38. Cheng,P.;Lyu,J.;Huang,Y.;Tang,X.Probabilitydistributionguidedopticdiscandcupsegmentationfromfundusimages.

InProceedingsoftheIEEEInternationalConferenceinMedicine&BiologySociety,Montreal,QC,Canada,20–24July2020;

pp.1976–1979.

39. Haider,A.;Arsalan,M.;Lee,M.B.;Owais,M.;Mahmood,T.;Sultan,H.;Park,K.R.ArtificialIntelligence-basedcomputer-aided

diagnosisofglaucomausingretinalfundusimages.ExpertSyst.Appl.2022,207,117968.[CrossRef]

40. Sarhan,A.;Al-KhazÁly,A.;Gorner,A.;Swift,A.;Rokne,J.;Alhajj,R.;Crichton,A.Utilizingtransferlearningandacustomized

lossfunctionforopticdiscsegmentationfromretinalimages.arXiv2020,arXiv:2010.00583.

41. Almubarak,H.;Bazi,Y.;Alajlan,N.Two-stagemask-RCNNapproachfordetectingandsegmentingtheopticnervehead,optic

disc,andopticcupinfundusimages.Appl.Sci.2020,10,3833.[CrossRef]

42. Zhang,Z.;Fu,H.;Dai,H.;Shen,J.;Pang,Y.;Shao,L.ET-Net: Agenericedge-attentionguidancenetworkformedicalim-

agesegmentation. InProceedingsoftheMedicalImageComputingandComputerAssistedIntervention,Shenzhen,China,

13–17October2019;pp.442–450.

43. Orlando,J.I.;Fu,H.;BarbosaBreda,J.;vanKeer,K.;Bathula,D.R.;Diaz-Pinto,A.;Fang,R.;Heng,P.-A.;Kim,J.;Lee,J.;etal.

REFUGEchallenge:Aunifiedframeworkforevaluatingautomatedmethodsforglaucomaassessmentfromfundusphotographs.

Med.ImageAnal.2020,59,101570.[CrossRef][PubMed]

44. Li,S.;Sui,X.;Luo,X.;Xu,X.;Liu,Y.;Goh,R.Medicalimagesegmentationusingsqueeze-and-expansiontransformers.arXiv2021,

arXiv:2105.09511.

45. Hervella,Á.S.;Ramos,L.;Rouco,J.;Novo,J.;Ortega,M.Multi-modalself-supervisedpre-trainingforjointopticdiscandcup

segmentationineyefundusimages. InProceedingsoftheIEEEInternationalConferenceonAcoustics,SpeechandSignal

Processing,Barcelona,Spain,4–9May2020;pp.961–965.

46. Liu,S.;Hong,J.;Lu,X.;Jia,X.;Lin,Z.;Zhou,Y.;Liu,Y.;Zhang,H.Jointopticdiscandcupsegmentationusingsemi-supervised

conditionalGANs.Comput.Biol.Med.2019,115,103485.[CrossRef]

47. Yu,S.;Xiao,D.;Frost,S.;Kanagasingam,Y.Robustopticdiscandcupsegmentationwithdeeplearningforglaucomadetection.

Comput.Med.ImagingGraph.2019,74,61–71.[CrossRef]

48. Chakravarty,A.;Sivaswamy,J.RACE-Net:Arecurrentneuralnetworkforbiomedicalimagesegmentation.IEEEJ.Biomed.Health

Inform.2019,23,1151–1162.[CrossRef]

49. Zilly,J.;Buhmann,J.M.;Mahapatra,D.Glaucomadetectionusingentropysamplingandensemblelearningforautomaticoptic

cupanddiscsegmentation.Comput.Med.ImagingGraph.2017,55,28–41.[CrossRef]

121

Mathematics2023,11,257

50. Chakravarty,A.;Sivaswamy,J.Jointopticdiscandcupboundaryextractionfrommonocularfundusimages.Comput.Methods

ProgramsBiomed.2017,147,51–61.[CrossRef][PubMed]

51. Shankaranarayana,S.M.;Ram,K.;Mitra,K.;Sivaprakasam,M.Jointopticdiscandcupsegmentationusingfullyconvolutional

andadversarialnetworks.InProceedingsoftheInternationalWorkshoponFetalandInfantImageAnalysis,QuébecCity,QC,

Canada,10September2017;pp.168–176.

52. Haleem,M.S.;Han,L.;vanHemert,J.;Li,B.;Fleming,A.;Pasquale,L.R.;Song,B.J.Anoveladaptivedeformablemodelfor

automatedopticdiscandcupsegmentationtoaidglaucomadiagnosis.J.Med.Syst.2017,42,20.[CrossRef][PubMed]

53. Sedai,S.;Roy,P.K.;Mahapatra,D.;Garnavi,R.Segmentationofopticdiscandopticcupinretinalfundusimagesusingshape

regression.InProceedingsoftheInternationalConferenceoftheIEEEEngineeringonMedicineandBiologySociety,Orlando,FL,

USA,16–20August2016;pp.3260–3264.

54. Joshi,G.D.;Sivaswamy,J.;Krishnadas,S.R.Opticdiskandcupsegmentationfrommonocularcolorretinalimagesforglaucoma

assessment.IEEETrans.Med.Imaging2011,30,1192–1205.[CrossRef][PubMed]

55. Sivaswamy,J.;Krishnadas,S.R.;DattJoshi,G.;Jain,M.;SyedTabish,A.U.Drishti-GS:Retinalimagedatasetforopticnerve

head(ONH)segmentation. InProceedingsoftheIEEEInternationalSymposiumonBiomedicalImaging,Beijing,China,

29April–2May2014;pp.53–56.

56. Sun,J.-D.;Yao,C.;Liu,J.;Liu,W.;Yu,Z.-K.GNAS-U2Net:Anewopticcupandopticdiscsegmentationarchitecturewithgenetic

neuralarchitecturesearch.IEEESignalProcess.Lett.2022,29,697–701.[CrossRef]

57. Maninis,K.-K.;Pont-Tuset,J.;Arbeláez,P.;VanGool,L.Deepretinalimageunderstanding.InProceedingsoftheMedicalImage

ComputingandComputer-AssistedIntervention,Athens,Greece,17–21October2016;pp.140–148.

58. Salehi,S.S.M.;Erdogmus,D.;Gholipour,A.Tverskylossfunctionforimagesegmentationusing3dfullyconvolutionaldeep

networks.InProceedingsoftheInternationalWorkshoponMachineLearninginMedicalImaging,QuébecCity,QC,Canada,

10September2017;pp.379–387.

59. Thakur,N.;Juneja,M.Surveyonsegmentationandclassificationapproachesofopticcupandopticdiscfordiagnosisofglaucoma.

Biomed.SignalProcess.Control2018,42,162–189.[CrossRef]

60. Pathan,S.;Kumar,P.;Pai,R.M.;Bhandary,S.V.Automatedsegmentationandclassifcationofretinalfeaturesforglaucoma

diagnosis.Biomed.SignalProcess.Control2021,63,102244.[CrossRef]

61. Malik,F.H.;Batool,F.;Rubab,A.;Chaudhary,N.A.;Khan,K.B.;Qureshi,M.A.Retinaldisorderasabiomarkerfordetectionof

humandiseases.InProceedingsoftheIEEEInternationalConferenceonMultitopic,Bahawalpur,Pakistan,5–7November2020;

pp.1–6.

62. Vajaranant,T.S.;Hallak,J.;Espeland,M.A.;Pasquale,L.R.;Klein,B.E.;Meuer,S.M.;Rapp,S.R.;Haan,M.N.;Maki,P.M.An

associationbetweenlargeopticnervecuppingandcognitivefunction.Am.J.Ophthalmol.2019,206,40–47.[CrossRef]

63. Selvaraju,R.R.;Cogswell,M.;Das,A.;Vedantam,R.;Parikh,D.;Batra,D.Grad-CAM:Visualexplanationsfromdeepnet-

worksviagradient-basedlocalization.InProceedingsoftheIEEEInternationalConferenceonComputerVision,Venice,Italy,

22–29October2017;pp.618–626.

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

122

mathematics

Article

Log-Linear-Based Logic Mining with Multi-Discrete Hopfield

Neural Network

GaeithryManoharam1,MohdShareduwanMohdKasihmuddin1,*,SitiNoorFarwinaMohamadAnwarAntony1,

NurulAtiqahRomli1,Nur‘AfifahRusdi1,2,SuadAbdeen1andMohd.AsyrafMansor3

1 SchoolofMathematicalSciences,UniversitiSainsMalaysia,Gelugor11800,Penang,Malaysia;

gaeithry@student.usm.my(G.M.);farwina@usm.my(S.N.F.M.A.A.);nurulatiqah_@student.usm.my(N.A.R.);

afifahrusdi@student.usm.my(N.‘A.R.);suadabdeen@student.usm.my(S.A.)

2 InstituteofEngineeringMathematics,UniversitiMalaysiaPerlis,KampusPauhPutra,Arau02600,Perlis,Malaysia

3 SchoolofDistanceEducation,UniversitiSainsMalaysia,Gelugor11800,Penang,Malaysia;

asyrafman@usm.my

* Correspondence:shareduwan@usm.my;Tel.:+60-4-6534769

Abstract:Choosingthebestattributefromadatasetisacrucialstepineffectivelogicminingsinceit

hasthegreatestimpactonimprovingtheperformanceoftheinducedlogic.Thiscanbeachieved

byremovinganyirrelevantattributesthatcouldbecomealogicalrule. Numerousstrategiesare

availableintheliteraturetoaddressthisissue.However,theseapproachesonlyconsiderlow-order

logicalrules,whichlimitthelogicalconnectionintheclause.Eventhoughsomemethodsproduce

excellentperformancemetrics,incorporatingoptimalhigher-orderlogicalrulesintologicmining

ischallengingduetothelargenumberofattributesinvolved. Furthermore,suboptimallogical

rulesaretrainedonanineffectivediscreteHopfieldneuralnetwork,whichleadstosuboptimal

inducedlogic.Inthispaper,weproposehigher-orderlogicminingincorporatingalog-linearanalysis

duringthepre-processingphase,themulti-unit3-satisfiability-basedreverseanalysiswithalog-linear

approach.Theproposedlogicminingalsointegratesamulti-unitdiscreteHopfieldneuralnetwork

toensurethateach3-satisfiabilitylogicislearnedseparately. Inthiscontext,ourproposedlogic

miningemploysthreeuniqueoptimizationlayerstoimprovethefinalinducedlogic. Extensive

Citation:Manoharam,G.; experimentsareconductedon15real-lifedatasetsfromvariousfieldsofstudy.Theexperimental

Kasihmuddin,M.S.M.; resultsdemonstratedthatourproposedlogicminingmethodoutperformsstate-of-the-artmethods

Antony,S.N.F.M.A.;Romli,N.A.;

intermsofwidelyusedperformancemetrics.

Rusdi,N.‘A.;Abdeen,S.;

Mansor,M.A.Log-Linear-Based

Keywords:logicmining;datamining;log-linearanalysis;reverseanalysis;statisticalclassification;

LogicMiningwithMulti-Discrete

evolutionarycomputation;discreteHopfieldneuralnetwork

HopfieldNeuralNetwork.

Mathematics2023,11,2121. https://

MSC:68T07

doi.org/10.3390/math11092121

AcademicEditor:WeihuaXu

Received:7March2023

1.Introduction

Revised:7April2023

Accepted:21April2023 Dataminingistheprocessofdiscoveringpatterns,relationships,andinsightsfrom

Published:30April2023 large datasets using various mathematical and computational techniques. It involves

extractingvaluableinformationfromdataandtransformingitintoanunderstandable

structureforfurtheruse.Dataminingiscommonlyusedinvariousfields,suchasbusiness,

healthcare, and science, to make informed decisions and predictions [1–4]. In theory,

Copyright: © 2023 by the authors. data mining enables us to make an informed decision or to explore the outcome of a

Licensee MDPI, Basel, Switzerland. decisionwithoutmakingthedecisionitself. Thus,thismethodofhandlingdatacanbe

Thisarticleisanopenaccessarticle usedinamultitudeofreal-lifeapplications, includingthoseinthemedical[5], water

distributed under the terms and research[6],stockmarket[7],datamining[8],landslideprediction[9],education[10],and

conditionsoftheCreativeCommons

diagnostics[11]fields,amongothers[12,13].Withtherapidadvancementofscienceand

Attribution(CCBY)license(https://

technology,itisvitaltoreturntothefundamentalsofdatamining. Typically,dataare

creativecommons.org/licenses/by/

convertedintoacertainruleandprocessedbyanAIplatform[14].TheAIplatformisthen

4.0/).

Mathematics2023,11,2121.https://doi.org/10.3390/math11092121 https://www.mdpi.com/journal/mathematics

123

Mathematics2023,11,2121

usedtoexplorethebehaviorofthedatasetandtoprovidetheenduserwithinterpretable

rules.Inthiscontext,thedatamustbeeasilyinterpretedbybothAIandhumans,sothat

theAIsystemgoverningtheoutcomecanbewellunderstood[15]. Thisleadsustothe

mainissuewithdatamining:mostoftherulesextractedfromdatasetsarenotoptimally

interpretedbyearlyandendusers.Toovercomethisproblem,insteadofextractingrules

fromthedatausingtheblackboxmodel,thedatacanberepresentedintermsoflogicthat

issupportedbymathematics.Therefore,onemustunderstandhowlogiccanbeappliedto

representdatainartificialneuralnetworks.

Oneofthemostchallengingtasksincreatinganoptimallogicminingmethodis

choosingtherightlogictorepresentthedataset.Thelogicisthenlearnedusingintelligent

systems,suchasadiscreteHopfieldneuralnetwork(DHNN)[16].Thefirstimplementation

oflogicinanANNwaspioneeredbyAbdullah[17],wherelogicwasimplementedina

DHNN.Inthatpaper,thesynapticweightofaneuronwasobtainedbycomparingthe

costfunctionofalogicwiththeLyapunovenergyfunction. Bycomputingthesynaptic

weightofthenetwork,theoptimalfinalneuronstatecorrespondingtothelearnedlogic

couldbeobtained.FollowingtheintroductionoflogicintotheDHNN,severalvariantsof

logicfromtheliteraturewereimplementedintoDHNNs.Kasihmuddinetal.[18]proposed

incorporating2-satisfiabilitylogic(2SAT)intoaDHNNwithexactlytwoneuronsperclause.

Withtheaidofamutationoperatorduringtheretrievalphase,theproposedlogicinthe

DHNNwasreportedtooutperformallexistingstate-of-the-artDHNNsingoverning2SAT

logic.In[19],thefirstnon-systematiclogic,random2-satisfiabilitylogic(RAN2SAT),was

implementedintoaDHNN.ThefirstandsecondclausesoftheRAN2SATformulation

wereconnectedbyadisjunction. Despitefacinglearningproblemsduringthelearning

phase,RAN2SATwasstillcompatiblewithalowernumberofneurons.Interestingly,this

studyattractedalargenumberofstudiesinthefieldofnon-systematiclogic. Recently,

Zamrietal.[20]proposedweightedrandom2-satisfiability(r2SAT)logicinaDHNNasan

extensionofRAN2SAT.Theproposedlogicrequiredanadditionalphase,thelogicphase,

toensurethateachlogicembeddedintotheDHNNhadacertainratioofnegatedliterals.

Thus,theDHNNhadmoresearchspacetorepresenttheneuronintermsofthelogical

rule. Gaoetal.[21]proposedY-typerandom2-satisfiabilitylogic(YRAN2SAT),which

randomlygeneratesafirst-andsecond-orderclause. Thislogicexhibitsaninteresting

behaviorbecauseYRAN2SATcanberepresentedintermsofsystematicandnon-systematic

logicalrules.DespitetherapiddevelopmentoflogicinDHNNs,theuseofhigher-order

systematiclogicinDHNNsislimitedtoasingle-unitDHNN.Forexample,theworkby

Mansoretal.[22]demonstratedtheuseofasingle-unitDHNNthathaslimitedstorage

information,whichleadstoapotentialoverfittingissuewhenthedataarerepresentedin

theformoflogic.

DHNN,whichisgovernedbylogic,playsapivotalroleincreatinganoptimallogic

miningmethod. Logicminingisasubsetofdataminingwheretheinformationfrom

thedatasetisextractedintheformoflogicalrules. Logicminingwasfirstproposedby

SathasivamandAbdullah[23],namelyareverseanalysisthatextractedlogicalrulesfrom

real-lifedatasets.Inthatpaper,WanAbdullah’smethodwasutilizedtofindthesynaptic

weightoftheneuronresponsibleforthefinalinducedlogic.Theinducedlogicwasverified

usingsupportandconfidencemetrics.Themainissuewiththatstudywastheabsenceof

generalinducedlogicthatrepresentsthebehaviorofthedataset.Totacklethisproblem,

Khoetal.[24]proposedanovellogicminingmethodcalled2-satisfiabilityreverseanalysis

(2SATRA)toextractinformationfromthedatasetintheformof2SAT.Comparedwiththe

previousmethod,2SATRAhasthecapabilitytoproduceinducedlogicthatcanclassify

theoutcomeofthedataset.Theproposed2SATRAwasreportedtobeusefulinextracting

logicalrulesinE-gamesintermsoferrorandaccuracy.Zamrietal.[25]proposedahigher-

orderlogicminingmethodbyrepresentingdataintheformof3SAT.Withtheaidofthe

clonalselectionalgorithm(CSA),theproposedlogicminingmethod(3SATRA)managed

toextractoptimalinducedlogicfromdataonAmazonemployees’resourceaccess.Despite

reportinghugesuccessinobtainingthebestinducedlogicforthedataset,thequalityofthe

124

Mathematics2023,11,2121

logiclearnedbyDHNNwasfarfromoptimal.Jamaludinetal.[26]arguedthatthelogic

usedduringlogicminingcanbefurtheroptimizedbyapplyingapermutationtochange

theconfigurationoftheattributeinthe2SAT.Thisargumentledtothedevelopmentof

permutations2SATRAandP2SATRA,whereallpossible2SATcontainingtheattributes

ofthedatasetswereembeddedintoaDHNN.TheproposedP2SATRAwasreportedto

outperformthestate-oftheartlogicminingmethodsinextractingthebestinducedlogic

fromthebenchmarkdataset. Inanotherstudy,Jamaludinetal.[27]ensuredthateach

inducedlogicproducedbylogicminingmustbederivedfromthefinalneuronstatethat

achievedtheglobalminimumenergy. Thisledtotheintroductionofanenergy-based

2-satisfiability reverse analysis method (E2SATRA), where the proposed logic mining

methodwasutilizedtoextractalogicalrulefromE-recruitmentdata.Byusingtheinduced

logic,thebehaviorofthepotentialrecruitscouldbeoptimallyclassified. Althoughthe

proposedE2SATRAwasreportedtoobtainglobalinducedlogic,thereisahighchance

thattheselectedattributeisaninsignificantvariableforthelogicalrule.Inthiscontext,the

insignificantattributemakesthefinalinducedlogicuninterpretable.

Duetothepotentialpitfallofunsupervisedlogicmining,Kasihmuddinetal.[28]

proposedthefirstsupervisedlogicmining,thesupervised2-satisfiability-basedreverse

analysismethod(S2SATRA).Inthismodel,thecalculationforeachattributeiscomputed

withrespecttotheoutcomeofthedatasets.TheproposedS2SATRAhasoutperformedall

thestate-of-the-artlogicminingmodelsinvariousperformancemetrics.Aftersupervised

learningwasintroduced,Jamaludinetal.[29]proposedanotherinterestinglogicmining

modelbycapitalizingonthelog-linearmodel(A2SATRA)toextractsignificantattributes

with respect to the outcome of the dataset. The proposed A2SATRA uses the k-Way

interactiontoensureonlysignificantattributesrepresentthe2-satisfiabilitylogic. After

obtainingthebestlogic,theDHNNlearnsthelogicandproducestheinducedlogicfor

datasetclassification.Despitetheusefulnessofsupervisedlearninginthecontextoflogic

mining,previousstudiesonlyutilizedonlyasingleobjectivefunction,whichleadsto

potentialoverfittingduringthelearningphaseofaDHNN.Anotherpossibleissuewith

currentlogicminingisthelackofhigher-orderlogictorepresenttheinducedlogic.Higher-

orderlogic,suchas3SATlogic,iscrucialtoensurethatmoreattributesfitintoeachlogical

clause.Inotherwords,eachattributeallowsformorethanoneattributetobeconnected,

whichwebelievewillimprovethegeneralizabilityoftheinducedlogic.Althoughthework

ofZamrietal.[25]showssomedevelopmentintermsofhigher-orderlogic,theselectionof

attributesfromthedatasetswasstillpoorlyexecutedandpronetopotentialoverfitting.

Accordingtotheexistingliterature[29],thelog-linearmodelhasbeenfoundtobe

effectiveinrepresentingdataclassification. Byutilizingamulti-unitdiscreteHopfield

neuralnetworkgovernedbyhigher-orderlogicandapermutationoperator,ourproposed

logicminingmethodisabletoobtainoptimalinducedlogicforareal-lifedataset.Therefore,

thesearethecontributionsofthispaper:

(a) Alog-linearapproachisformulatedbyselectingsignificantattributeswithrespectto

thefinallogicaloutcome. Thelog-linearapproachremovesinsignificantattributes

fromdatasetsbeforebeingtranslatedintoahigher-orderlogicalrule(3-satisfiability),

whichreducesthecomplexityofthelogicminingtoselectthebestattributetorepre-

sentthedataset.

(b) Anovelobjectivefunctionthatutilizesbothtruepositivesandtruenegativeswhen

derivingoptimal3-satisfiabilitylogicisformulated.Inthiscontext,thelogicmining

methodselectsthetopandbestlogicbeforeenteringthelearningphaseofthediscrete

Hopfieldneuralnetwork.Usingmultioptimallogicalrulesthatmaximizetheobjective

function,thatthesearchspaceofthenetworkcanbeexpandedinonedirection.

(c) Amulti-unitdiscreteHopfieldneuralnetworkthatisgovernedbythebestlogic

obtainedfromthedatasetsisproposed. Themulti-unitdiscreteHopfieldneural

networkindependentlylearnsthelogicfromthedatasetsandderivesrespective

synapticweightsusingWanAbdullah’smethod.Usingthemulti-unitnetwork,the

numberofinducedlogicsthatrepresentthebehaviorofthedatasetscanbeincreased.

125

Mathematics2023,11,2121

(d) Apermutationoperatorof3-satisfiabilitylogicisproposedinadiscreteHopfieldneu-

ralnetwork.Inthiscase,thechosenattributefromthelog-linearanalysisundergoes

permutationtoensurethattheoptimalattributeconfigurationineachlogicalclause

canbeobtained.Byallowinglogicalpermutation,logicmininghasthecapabilityto

identifythehighestperforminginducedlogicintermsofaconfusionmatrix.

(e) Anextensiveanalysisoftheproposedhybridlogicminingisperformedinreal-life

datasets. Theperformanceoftheproposedhybridlogicminingiscomparedwith

state-of-the-artlogicminingmethods.Inthiscontext,variousperformancemetricsare

analyzedtovalidatetheperformanceoftheproposedlogicminingmethod. Anon-

parametrictestisperformedtovalidatethesuperiorityoftheproposedlogicmining.

Thispaperisorganizedasfollows:Section2presentsthemotivationbehindthepaper.

Then,inSection3,weintroducethehigher-order3-satisfiabilityrepresentation.Next,in

Section4,weexplainhow3-satisfiabiltyisimplementedintoaDHNN.Section5described

theintegrationofalog-linearmodelinto3SATRA.Section6outlinestheexperimental

setup.ThemostimportantpartsofthepaperarepresentedinSection7wherewediscuss

thesimulationoflog-linearmodelina3-satisfiability-basedreversemulti-unit.Section8,

werevealthelimitationofourresearchandinSection9discussedfuturework.Finally,we

concludewiththeresultsofourfindingsinSection10.

2.Motivation

Inthissection,wediscussthemotivationbehindourwork.Eachmotivationaddresses

theproblemwithexistinglogicminingandhowourproposedlogicminingcanfillthese

gapsinthefield.

2.1.LackofHigher-OrderLogictoRepresentSelectedAttributes

Logicalrulesplayapivotalroleinrepresentingtheinformationinadataset.Inthe

conventionalparadigm,attributeswithmoreconnectiontothelogicalrulehavethecapacity

tostoremoreinformation.Incurrentmethodsoflogicmining,suchas2SATRA[26]and

E2SATRA[27],logicislimitedtothesecondorder,whereonlytwoattributesareembedded

intotheclause. Inthiscontext,eachattributeconnectswithonlyoneattributetosatisfy

theclause. Thiscausesproblemsinsatisfyingtheinterpretationofthelogicduringthe

learningphasebecausetheprobabilityofthe2SATbeingsatisfiedislessthanthatofa

higher-orderclause[29]. Therearetwopotentialissueswithlower-orderlogicinlogic

mining. Firstly,obtainingthewrongsynapticweightcanleadtoawrongfinalneuron

stateduringtheretrievalphaseofaDHNN,whichcanimpacttheperformanceofthe

inducedlogic.Secondly,lower-orderlogichasasmallersearchspace,whichmaynotbe

sufficienttoaccuratelyrepresentthebehaviorofthedataset.Ontheotherhand,higher-

orderlogiccanrepresentmoreattributes,whichcanimprovethegeneralizabilityofthe

inducedlogic.Furthermore,thepermutationoperatorcanbeimplementedtoexploremore

possiblecombinationsofattributes,whichcanleadtothediscoveryofbettersolutions.The

workbyJamaludinetal.[30]demonstratedthatapermutationoperatorcanrevealpossible

inducedlogicalrules.However,ifthenumberofattributesislow,theperformanceoflogic

miningwillnotimprove.Thiswillresultinahugelossinpotentialoptimalinducedlogic.

Althoughtherearesomeattemptstorealizehigher-orderlogicmining,suchasthework

proposedbyZamrietal.[25],where3SATwasutilizedtorepresentlogicinlogicmining,

therehasnotbeenanyattemptstorepresentthe“right”3SATlogicbecauseallattributesin

thedatasethaveequalprobabilityofbeingchosen.Inthispaper,weproposeahigher-order

logicminingbycapitalizingontheuseof3-satisfiabilitylogictorepresentattributesina

dataset.Inthiscontext,ourproposedlogicmining.willutilizelog-linearmodelstoextract

themostoptimalattributewithrespecttothelogicaloutcome.

2.2.LimitedSingle-UnitDHNN

Duetoitssimplicityandeffectivesynapticweightmanagement,aDHNNgoverned

bylogichasgoodpotentialinlearningthebehaviorofadataset. Giventhesimplicity

126

Mathematics2023,11,2121

ofDHNNssuchascontentaddressablememory(CAM)andeffectivesynapticweight

management,aDHNNhasthecapabilitytoretaininformationaboutthedatasetandto

retrieveanynecessaryrulesduringtheretrievalphase. Despitedemonstratingstellar

performanceinsimulatedlearning[20,21],DHNNshavebeenshowntobeineffectiveat

extractinginformationfromreal-lifedatasets.Thisisduetoonlyonelogicbeingtranslated

intoCAM,whichleadstoasingleoutcome, becauseonlyonesetofsynapticweights

waslearnedduringthelearningphaseoftheDHNN.Inthiscontext,thepossibilityof

logicminingobtainingthemostoptimalinducedlogicisreduceddrastically.Forinstance,

thelogicminingmethodproposedbyKhoetal.[24]embeddedthesinglebestlogicinto

DHNN.SinceeachDHNNcanonlylearnonetypeoflogic,thefinalinducedlogicobtained

fromlogicminingwaslimitedtothedirectionofthelocalfield. Whenthenumberof

inducedlogicalruleswassmall, theperformanceofthelogicminingdeteriorated. A

similarobservationwasfoundintheworkbyAlwayetal.[31],whereasingle-unitDHNN

reducedtheprobabilityofthenetworkarrivingattheoptimalinducedlogic.Toremedy

thismatter,thispaperproposesamulti-unitDHNNtoincreasethesolutionspaceforlogic

mining.Afterobtainingafewlogicalruleswithhighfitnessvalues,eachlogicislearnedby

theDHNN.Inthiscontext,eachDHNNlearnsthelogicindependentlyandrecommends

theirowninducedlogicwithoutanyinteractionbetweenotherCAMs.Thisperspective

helpsthelogicminingmethodachieveoptimalinducedlogic[32].

2.3.IssuewithSingleObjectiveFunction

Inadditiontothemulti-unitDHNNdiscussedinSection2.2,thequalityofthebest

logicmustbeimprovedtoreducepotentialoverfittingoftheDHNN.Generally,theobjec-

tivefunctionoflogicminingduringthepre-processingphaseistomaximizethenumberof

truepositives.Forexample,thelogicminingproposedbyZamrietal.[25]dependssolely

onthenumberofpositiveoutcomesfromthelearningphaseanddoesnotconsiderthe

numberoftruenegativesalthoughbothoutcomesareconsistentwiththelearnedlogic.In

theeventofalloutcomesachievingalltruenegatives,theproposedlogicminingisreduced

toarandomclassifierbecausetheDHNNisunabletoobtainthemostoptimalsynaptic

weight.AsimilarobservationwasreportedintheworkbyKasihmuddinetal.[26].Despite

achievingoptimalinducedlogicusingS2SATRA,theinducedlogiccouldlearndatathat

ledtotruepositives.ThisisthemajorlimitationoftheproposedS2SATRAbecausemostof

thelogicfromthedatasetthatyieldstruenegativesareignored.Inthiscontext,thelearning

dataembeddedintotheDHNNisreduceddrastically,whichreducesthesensitivityof

thelogicminingtowardsmorespecializeddatasets.Toaddresstherootofthisproblem,

thebestlogicobtainedfromthepre-processingphasemustbeflexibleenoughwithout

sacrificingvaluableinformationaboutthelearningdata.Inthisway,theobjectivefunction

ofthebestlogicmustaccommodatethefrequencyofthetruenegativeoutcome. Inthis

paper,weproposealogicminingthatmaximizesanylogicaloutcomesthatarebothtrue

positivesandtruenegativesbeforebeinglearnedbytheDHNN.Therefore,theproposed

logicminingcontributestoenhancingthesearchabilityofinducedlogicinextractingmore

accuratelogicalrulesfromadataset.

3.Higher-Order3-SatisfiabilityRepresentation

Thesystematic3SATisalogicalrulethatstrictlycomprisesthreevariablesineach

clausewithdisjunctionbetweentheclauses.Thislogicwaspopularizedinseveralpromi-

nentstudies,suchas[22],whereeachvariablerepresentedinformationabouttheapplica-

tionorproblem.Since3SATwasproveninNPby[33],therewasnoefficientmethodto

guaranteethataconsistentassignmentthatsatisfies3SATcanbefoundbythealgorithm.

Basedon[25],3SATconsistsofthefollowingfeatures:

(a) Asetofnvariables,L1,L2,L3,......Ln;

(b) Asetofliterals,wherealiteralisavariableLoranegationofvariableL;

(c) Asetofmdistinctclauses,whichareconnectedwiththelogicalAND(∧)andin

whicheachM consistsofexactlythreeliteralsvariablesformingthek-SATclause

i

127

Mathematics2023,11,2121

andeverylogicalclausenormallyhasexactlykvariablesthatarelinkedwiththeOR

(∧)operator.

Thegeneralformulafor3SATcanbedefinedasfollows:

Byconsideringfeatures(a)–(c),theformulationfor3SATcanbegeneralizedasfollows:

(cid:11) (cid:12)

L3SAT =∧ i m =j C i where C i =∨3 i=j x ij, y ij, z ij (1)

whereeachclausecontainsexactlythreeliterals.Notethateachvariableintheclausecan

be1,whichrepresentstrue,or−1,whichrepresentsfalse.ThegoalofEquation(1)isto

alignallthestatesofthevariablesothatL3SAT =1.

ThesuggestedlogicalformulaofL3SATisshowninEquation(2):

L3SAT =(A∨B∨C)∧(D∨E∨F)∧(G∨H∨I) (2)

AspresentedinEquation(2),L3SATissatisfiablewhen(A, B, C, D, E, F, G, H&I)

intheinitialneuronstateare{−1,−1,−1,−1,−1,−1,1,1,1},whichrepresentstrue.Onthe

other hand, if (A, B, C, D, E, F, G, H&I) in the initial neuron state is

{−1,−1,−1,−1,−1,−1,1,1,1}, it is not satisfied. This logical structure does not con-

siderredundantliterals.Thedimensionalityfeature,whichpermitsonlythreedecisions

toaffecttheoutcomeofthedatasets,isanotherbenefitofsuggestingthreevariablesper

clause. Whenalogicalruleisembeddedintoanartificialneuralnetwork,thechoiceof

three-dimensionalmodelremainsinterpretablebasedonthelogicalrule.Furthermore,we

needtosavetheinteractionbetweenthevariablesinthesentence.Optimizingthevalueof

kisnecessaryasreachingk=3istheprimarygoal.Thisstudyalsoutilizedapermutation

operatorinthelogicalstructure.ThebasicdefinitionoftheL3SATisasfollows:

(cid:2) (cid:3)

Li 3SAT =∧n u=1 CuwhereCu =∨k v=1 X u a vw ,Y u b vw ,Z u c vw ,k=3 (3)

wherea,b,andcarethearraysofattributesanda(cid:9)=b(cid:9)=c.Then,Xa ,Yb istheselected

uvw uvw

attributesaandb,respectively.The3SATlogicalstructureisahigher-orderlogicalstructure

thatisprobablysatisfiedandcompatibleintotheDHNN.Thelogicalstructureobtainsthe

correctsynapticweightinordertoachievetheglobalminimumvalue.Thepossiblelogical

structureafterthepermutationisshowninEquations(4)and(5).

L1 3SAT = (C∨E∨H)∧ (G∨F∨I)∧ (D∨B∨A) (4)

L2 3SAT = (G∨D∨C)∧ (F∨V∨H)∧ (E∨A∨B) (5)

Equation(4)hasadifferenceinthearrangementoftheliteralsineachclauseinthe

logicalstructure.Thelogicalpermutationinbothequationsgivesahigheraccuracyforthe

logicalstructure.

4.3-Satisfiability(L3SAT )inDiscreteHopfieldNeuralNetwork

ThediscreteHopfieldneuralnetwork(DHNN)consistsofinterconnectedneurons

thathaveinputandoutputpatternsintheformofdiscretevectors.Thenetwork’sweights

aresymmetrical,andtherearenoself-connections[17].Thesymmetricalsynapticweights

areconnectedbyinterconnectedneuronsinaconventionalrecurrentnetwork.Lowcompu-

tation,highconvergence,andgoodcontentaddressablememory(CAM)areallelements

ofthisnetwork[24]. Furthermore,inthisstudy,theHNNiscompatiblewiththebipo-

larneuronrepresentation,andthefundamentalneuronupdatecanbeexpressedusing

128

Mathematics2023,11,2121

Equation(6),andthefundamentalneuronupdatecanbeexpressedusingEquation(6).

HNN’sgeneralasynchronousupdatingruleisasfollows:

⎧

⎪⎨ N

1, ∑W S ≥ε

S i = ⎪⎩ j ij j (6)

−1, otherwise

whereS istheweightforunitsatob,andεreferstothethresholdoftheHNN.

i

ToincorporateL3SATintoaDHNN,aneuronisassignedtoeachvariableinEquation(3).

Eachneuronisdefinedin[–1,1],whichstandsforfalseandtrue,respectively. Tomodel

neuronscollectively,thecostfunctionassociatedwiththeL3SATmustbeminimized. In

general,thecostfunction,δL3SAT,isformulatedasfollows:

NC NV

δL3SAT = ∑ ∏ wuv (7)

u=1v=1

whereNVdenotesthenumberofvariables,whereasNCdenotesthenumberofclauses,

andEquation(8)presentsthedefinitionoftheL3SATinconsistency:

(cid:15)

wuv = 1 2

1 2

(

(

1

1

−

+

S

S

x

x

)

)

,

, O

if

the

x

rwise

(8)

BeforeidentifyinganyinconsistenciesintheL3SAT,thefirststepistoidentifythe

costfunctionoftheL3SAT.Inthelearningphase,theαL3SATmustbeabletoproduceat

leasttheminimumcostfunctionsothatthesynapticweightresultscanguaranteethatthe

proposedL3SATcanbemodelledintotheDHNN.ThefinalneuronstateoftheDHNN

willbesequentiallyupdatedintheretrievalphaseusingthelocalfieldHαL3SAT ,showsin

Equation(9):

hL (t)=

c=1

∑ n

,c(cid:9)=bb=1

∑ n

,b(cid:9)=c

W

a

(

b

3

c

) S

b

Sc +

b=1

∑ n

,b(cid:9)=a

W

a

(

b

2) S

b

+Wc (1) (9)

(3) (2)

wherethesynapticweightsareconnectedatthethirdorderW ,secondorderW ,and

abc ab

(1)

firstorderWc .ThemostrecentfinalneuronstateS

i

,isasfollowedbyEquation(10):

"

S i = 1 − , 1, O ta t n h h e h rw L ( i t s ) e ≥ 0 (10)

The hyperbolic tangent activation function (HTAF), abbreviated as hL (t), is shown in

Equation(11):

tanh(h)=

ehL (t)−eh(t)L

(11)

i ehL (t)+eh(t)L

Itisimportantthat,accordingto[23],HTAFcapacityisnon-linearlyclassifiedandthat

theoptimalsolutionisdifferentiatedbyminimizingneuronoscillationduringtheretrieval

phaseintheDHNN.ThefinalneuronstategeneratedbyDHNN-L3SATdenotestheL3SAT

performance. ThepropertiesofDHNN,asdescribedbyTheorem1in[17],includeits

tendencytoconverge,whichisalsocorroboratedby[18].

Theorem1. AssumethatN=(W,θ),whereθisthemodel’sthresholdfortheDHNN.Assume

thatWisasymmetricmatrixwithnonnegativediagonalcomponentsandthatNoperatesinan

asynchronousmode.DHNNwillthenalwaysreachastablestate.

Sincethesuggested3SATintoDHNNdoesnotcontainahiddenlayer,thenetwork

mustbeexaminedbeforetransferringintotheidealneuronstate. Itwillbesimpleto

evaluatetheoptimalityasLyapunovenergyinthisscenariothatbeinstantlyidentifyifthe

129

Mathematics2023,11,2121

finalneuronstatewascapturedinasuboptimalcondition.Thefollowingistheformulation

oftheHδL3SAT Lyapunovenergyfunction,whichrelatestotheDHNN-L3SAT.

HL3SAT (t)=−1

3

∑ n ∑ n ∑ n W

a

(

b

3

c

) SaS

b

Sc

a=1,a1b1cb=1,a1b1cc=1,a1b1c

(12)

−1

2 a=

∑ n

1,a1b=

∑

1

n

,a1b

W

a

(

b

2) SaS

b

−

a

∑

=

n

1

Wa (1) Sa

ThevalueofHδL3SAT istheabsolutefinalenergy,andHδL3SAT ismonotonicallyre-

ducedtoproducetheminimumenergyHδ m

L

i

3

n

SAT

.Accordingto[17]and[22],thenumberof

clausescanbeusedtopredicttheabsoluteminimumenergyofanylogicalrule.Thelowest

energyoftheL3SATispresentedinEquation(13)asthispaperaddresseslogicalrulesthat

includethreevariablesperphase.Hδ m

L

i

3

n

SAT

iscalculatedusingEquation(13).

(cid:2) (cid:3)

Hδ m

L3

i

S

n

AT

=−1

8

n χ3

i

(13)

Meanwhile,χ3

i

andarepresentthethirdorderandthreeliteralclausesinHδL3SAT .

Finally,toidentifytheglobalandlocalminimumsolutions,Equation(14)canbeused.

Significantly,thefinalneuronstateswillreachtheglobalminimumsolutionifitissatisfied;

ifnotsatisfied,theybecomethelocalminimumsolution.υisthetolerancevalue,whichis

anindicatorofasatisfiedsolution.

(cid:30) (cid:30)

(cid:30) (cid:30)

(cid:30)HδL3SAT −Hδ m

L

i

3

n

SAT

(cid:30)≤ υ (14)

Figure1presentsaschematic3SAToutline,andFigure2presentsaflowchartofthe

DHNN-3SATstepsusingthefollowingpseudocode.G3SATRAμthenupdatestheneuron

attimet+1.InFigure1,themainblockrepresentedbytheblackdottedlinesshowsthe

higher-orderlogicbasedonthenumberofclauses.Insidethehigher-orderlogicblock,the

blue,red,andgreenlinesindicatetheconnectionsbetweentheneuronslabelledw2 ij=w2

ji

,

w3 ijk=w3

kji

=w3

jki

,andw1 i=w1

j

,respectively.

Figure1.SchematicdiagramforDHNN-L3SAT.

130

Mathematics2023,11,2121

Figure2.FlowchartoftheworkflowofG3SATRAμ.

ThemethodologyusedinthisstudyisillustratedinFigure2andcomprisesalogic

phaseandatrainingphase.Theflowchartshowsthatthepre-processingmethodisinvolved

inthelearningphase,makingitacriticalstep.Therefore,thequalityandappropriatenessof

thepre-processingmethodcansignificantlyinfluencetheperformanceofthelogicmining

model.Toevaluatetheperformanceoftheinducedlogicaftercompletingthetrainingphase,

performancemetricswereutilized. Thesemetricswereusedtodeterminewhetherthe

G3SATRAμmodelaccuratelypredictedtheoutcomeorifitrequiredimprovement.

5.ProposedHigher-OrderLog-LinearModelinLogicMining

Thispaperdiscussesthemethodofahigher-orderlog-linearanalysisandtheobjective

functionofamulti-unitDHNN.Thefollowingsectionexplorestheformulationofalog-

linearmodel,includingtheselectionofsignificantattributes,andthecreationofamulti-unit

DHNN.Furthermore,ineachsection,thelog-linearformulaiswellexplainedaccordingto

theobjectivefunction.

131

Mathematics2023,11,2121

5.1.Log-LinearAnalysistoRepresent3-SatisfiabilityLogic

OneofthesignificantapplicationsoflogicinDHNNislogicmining.Logicmining

isusedtoextractlogicalrulesfromreal-lifedatasets.Logicminingisdifferentfromdata

miningmethodsintheliterature[23–31]becausetheendproductforlogicminingisa

classificationmodelbasedonSATrules.Themaingoaloflogicminingistoextractalogical

rulethatexplainsthebehaviorofthedataset.Notethatlogicminingthatutilizes3SATin

aDHNNwasfirstproposedbyZamrietal.[25]andcanbeabbreviatedas3SATRA.In

thiscontext,itisimperativeforlogicminingtohaveamoreeffectiveDHNNmodelthatis

governedbyhigher-orderlogic.However,areal-lifedatasetmightconsistofhundredsof

attributesandoftencontributestothe“curseofdimensionality”[32]inlogicmining.One

ofthepossiblesolutionstothisproblemischoosingtherightattributetobeprocessedby

logicmining.

Oneofthepossiblemethodsofextractingtherightattributesisthroughalog-linear

analysis.Inthispaper,weproposealog-linearanalysisusing3SATRAorG3SATRAμ.Let

NbethequantityofvariablesthatrepresentstheattributeP

i

= (P1,P2,P3,......PN )in

bipolarformP = {−1,1}. BeforeproceedingtotheDHNN,wearerequiredtoextract

i

thebestrattributesfromthetotalofNfromthedatasets.Thelog-linearmodelisusedto

examinewhetherthereisasignificantdifferencebetweentheproportionofcategorieswith

twoormoregroupvariables[33].Thismodelexpressesthelogofanexpectedfrequency

inacontingencytableasasummationofthefunctionforallparametersinvolvedinthe

datasets. Notethatthetwo-waytablewithrespecttotheexpectedfrequency,L ,fora

ij

columnisgivenasfollowsifeachoftheneuronsisindependentfromeachother[34].

L

ij

=nr

ij

=nr i+r+j (15)

wherenisthesumofentries,whileρ andρ standforpartialdistributionsforthevariables

i j

inthei-throw(rowprobabilities)andj-thcolumn(columnprobabilities),respectively.The

outcomeofperformingalinearregressiononEquation(15)isshowninEquation(16):

ln L ij =lnn+lnρ i+ +lnρ +j (16)

Thefrequencyforthecross-tabulationcellispredictedusingalinearmodelforthe

log-linearfunction.Themarginsandinteractionbetweenthevariablesshouldbemeasured

inatwo-waytableknownasasaturatedmodel.Equation(17)showstheformulationfor

thesaturationmodel:

ln L ij =ρ+ρ i+ +ρ +j +ρ ij, i(cid:9)=j (17)

whereρ=lnnisthetrueoutcomes,whileρ i+ =lnρ i+, ρ +j =lnρ +j arethebasicoutcomes

ofneuronsS andS,respectively.Accordingto[29],theassociationparameterthatrepre-

i j

sentstheabilitytoadaptthelogexpectedcellfrequencyisexpressedusingonlythepartial

distributionofeachvariableandk .Equation(18)reproducestheobservedfrequencies

ij

f perfectly,knownasasaturatedmodel. G2andthePearsonchisquareχ2areusedto

ij

evaluatethegoodnessoffittoacquirethelikelihoodratio.

(cid:24) (cid:31)

G2=2 ∑ i ∑ j f ln f ij (18)

i=1j=1 ij L ij

χ2= ∑ i ∑ j f (cid:28) ln (cid:11) f −L (cid:12) 2−ln (cid:11) L (cid:12)(cid:29)

ij ij ij ij

i=1j=1

(19)

= ∑ i ∑ j f ln ( fij −Lij )2

i=1j=1 ij Lij

Equations(18)and(19)areemployedtoidentifytheresultsbasedonboththestatistical

samplesizeandtargetedmodel[35]. Additionally,thevaluesofthesetwostatisticsare

computationallythesame.Inthelog-linearanalysis,determinationofthesignificancelevel

132

Mathematics2023,11,2121

requiresassessingboththeparameterandthegoodnessoffit. InG3SATRAμmodel,the

significanceoftheparametersisevaluatedusingapartialassociationtest,whichcalculates

thedifferenceinvaluesfortherelevantdegreesoffreedom(df)inthemodel. Essentially,

thismeansthatifthereisarelationshipbetweenapairofvariables,thenullhypothesis

testcanbeselected[36]. Additionally,thenullhypothesisisrejectedwhentheparameter

valuesofeachindividualvariablearefoundtobesignificantlyassociated.Thealternative

hypothesisassumesthatthereisasignificantdifferencebetweentheobserveddataandthe

populationparameter.Inhypothesistesting,thegoalistorejectthenullhypothesisinfavor

ofthealternativehypothesisbasedonstatisticalevidence[37].Theoutcomesofthevariables

areshownbythegeneratedparameter,byindicatingthebothP andP values.G3SATRAμ

i j

isthenembeddedintotheDHNNandcanbeformulatedusingtheP andP values,whereas

i j

P andP aresignificantp-valuesforattributesS andS,respectively.Additionally,min|P|

i j i j i

representsthelowestsignificantp-valuebetweenS andS.Toguaranteethefinalmodelof

i j

L3SAT,thisworkimplementedalog-linearanalysisandembeddeditintoaDHNNmodel

accordingto[38].ItisimportanttonotethatneitherneuronwasconsideredintheL3SAT

formulationwhenevaluatingtheperformanceofeachneuron.Anotherconsiderationinthis

suggestedmethodisthechangesintraditionalk-SATRAproposedby[24,25]ifEquation

(20)forallvariablescannotreachthethresholdvariablewhen0 ≤ P ≤ α. Furthermore,

i

determiningtheneuronnegativitypresentsthebiggestprobleminEquation(15).Theessence

ofalog-linearanalysisistoremoveanyweakneurons,asindicatedbyEquations(18)and(19).

Inthisstudy,weapplyalog-linearanalysisinthe3-satisfiability-basedreverseanalysismulti-

unitapproachorG3SATRAμinordertodeterminewhichattributesinthedatasetwillbe

selectedtorepresentspecificvariablesintheG3SATRAμ.Inparticular,G3SATRAμutilizes

alog-linearanalysistoselectthebestnineattributesthathavethestrongestinteractions

amongthedatasetoutcomes.Toapplyhigher-orderlogic,theselectednineattributesare

randomlypermuted. Theselectedidealattributewillthenberepresentedasaninduced

logicintheformofa3SAT,whichwillbeembeddedintotheDHNN.Thismethodwasalso

implementedby[30],inworkonthe2SATlogicalrulebasedonasix-attributeselection.This

methodobtainstheoptimalsolutionwhenwecomparethelogicminingmethodintroduced

by[30]with2SATlogicalrules.

5.2.NewObjectiveFunctionwithMulti-UnitDHNN

Inpreviousstudies,suchas[24–29],theobjectivefunctionofthepre-processingphase

istofindthebestlogicLbest thatmaximizesthetruepositiveTP.Afterobtainingthemost

3SAT

optimalLbest ,theDHNNwilllearnthislogicandobtaintheoptimalsynapticweight,

3SAT

whichleadstothefinalinducedlogic. Themainissuewiththisprocedureisthelackof

considerationofanotherimportantvariable,whichisthetruenegativeTN. Aprevious

study[39]failedtoconsidertheTN,whichplaysapivotalroleinobtaininganegative

variableintheinducedlogic. Inthispaper, weproposeanewobjectivefunctionthat

considersL andmaximizesthesummationofTPandTN. Theformulationofthe

3SAT

objectivefunctionisasfollows:

(cid:13)(cid:30) (cid:30) (cid:30) (cid:30)(cid:14)

max (cid:30) P =1 (cid:30)+(cid:30) Q =−1 (cid:30) , j∈N (20)

ij ij

(cid:30) (cid:30)

where (cid:30) TP =1 (cid:30) isthecardinalityofTPinsetjthathasastateequalto1.Notethatjrepresents

ij

theDHNNunit. Inotherwords,Lbest representstheinitialbehaviorofthedatasetbefore

3SAT

beinglearnedbytheDHNN.Equation(20)isdifferentfromtheworkbyZamrietal.[25],

whereonlyLbest withthehighestfrequencywaschosen.Inthispaper,thetopklogicthat

3SAT

satisfiestheconditioninEquation(20)ischosentoproceedtothelearningphase.

5.3.Lbest inMulti-UnitDHNN

3SAT

ThenextstrategytolearnLbest throughtheDHNNisproposingamulti-unitDHNN

3SAT

that processes several Lbest independently. This strategy ensures that the proposed

3SAT

G3SATRAμ can cover more search space during the retrieval phase. This can be im-

133

Mathematics2023,11,2121

plementedbycapitalizingonthesynapticweightfromdifferenttypesofLbest ,which

3SAT

leadstodifferentdirectionsinthefinalneuronstate.Kasihmuddinetal.[18]proposeda

mutationDHNNtoaddressasimilarconcernbyincreasingthesearchspacebymutating

thefinalneuronstate.However,duetothelimitednumberofsynapticweightsproduced

bytheWanAbdullahmethod,thefinalneuronstatetendstoconvergetowardsasimilar

neuronstate.Fromthisperspective,wecanobtaindifferenttypesoffinalneuronstatesjust

byobtainingdifferentlogicduringthelearningphaseoftheDHNN[40].Theequationthat

governsthemulti-unitDHNNisgivenasfollows:

μ j =∧N j= C 1 (A i ∨ B i ∨ C i ), j∈R

m N ax|n[(p=1)∨ (Q=−1)]| (21)

j=1

whereμ referstoamulti-unitDHNNinwhichthestructureleadstoLLearn = (cid:2). After

j 3SAT

obtainingasatisfactoryinterpretation,thesynapticweightofLbest canbeobtainedandis

3SAT

storedasCAMineachmulti-unitDHNN.DuringtheretrievalphaseoftheDHNN,the

finalneuronstateSBisobtainedusingEquation(9)andistransformedintothefollowing

i

inducedlogic. (cid:15)

SInduced= Si, S i B=1 (22)

i Sj, S

i

B=−1

Next,usingtheobtainedinducedlogic,theoutcomeoftheinducedlogiciscompared

withthetestingdata.Inthiscontext,thecomparisonisonlymadewithalloftheproposed

Lbest fromdifferentDHNNunits.Algorithm1showsthepseudocodeoftheproposedwork.

3SAT

Algorithm1:pseudocodeofDHNN−L3SAT.

Input

SetallattributesL1,L2,L3,......LnwithrespecttoL

3

L

S

ea

A

r

T

n=(cid:2)GC,andtrial

Output

ThebestinducedlogicLInduced

3SAT

Begin

Initializealgorithmparameters;

DefinetheattributeforL1,L2,L3,......LnwithrespecttoL

3

B

S

es

A

t

T

Searchthep-valueforeachAttribute;

for(α<p)do

ifEquation(7)issatisfiedthen

AssignLiasSiandcontinue;

while(i≤GC)do

UsingEquation(21)tofindtheLBest

3SAT

ChecktheclausesatisfactionforLBest

3SAT

ComputeHδL3SATusingEquation(12)

ComputethesynapticweightassociatedwithLBest byusingWAapproach:

3SAT

StorethesynapticweightandLBest inCAM;

3SAT

Initializethefinalneuronstate;

for(k≤trial)

ComputehiusingEquation(9);

ConvertSB tothelogicalfromusingEquation(22);

i

CombineSB toforminducedlogicLInduced

i 3SAT

ComparetheoutcomeoftheLInducedwiththeLTest continue;-

3SAT 3SAT

k←k+1

endfor

i←i+1

endfor

End

134

Mathematics2023,11,2121

6.ExperimentalSetup

TovalidatetheperformanceoftheproposedG3SATRAμ,theexperimentsetupmust

beperformedaccordingtothefollowingsetup:

6.1.BenchmarkDataset

TheLinduced for15datasetsisextractedusingthelog-linearanalysisinSection5.1.

i

ThesedatasetsandtheirassignedlabelsareretrievedfromtheUCImachinelearning

repository(https://archive.ics.uci.edu/ml/datasets.php)andKaggleopenset(https://

www.kaggle.com/datasets).Thedatasetwasdownloadedon6November2022fromthe

respectivewebsite.Toavoidpossiblebias,wechosedatasetsfromdifferentfieldsofstudies

(refertoTable1).Table1showsthedetailsofeachselecteddataset.

Table1.Detailsofeachselecteddataset.

Code Dataset DataLink Attribute Instances MissingValue Field Outcomes

UCIMachineLearning

L1 HorseColic 27 300 Yes Zoology Surgery

Repository:HorseColicDataSet

Credit https://achive.ics.uci.edu/ml/

L2 15 690 Yes Finance Class

Approval datasets/credit+approval

https://achive.ics.uci.edu/ml/

L3 Absenteeism 21 740 No Business Timeinhours

datasets/Absenteeism+at+work

https://achive.ics.uci.edu/ml/

Early-Stage

L4 datasets/Early+stage+diabtes+ 17 520 Yes Medical Class

Diabetes

risk+prediction+dataset.

Chronic

https://achive.ics.uci.edu/ml/

L5 Kidney 24 400 yes Medical Classification

datasets/chronic_kidney_disease

Disease

https://achive.ics.uci.edu/ml/

L6 Specheart 22 267 No Medical Diagnosis

datasets/SPECT+Heart

https://achive.ics.uci.edu/ml/

Congressional

L7 datasets/congressional+voing+ 16 435 Yes Social Class

VotingRecords

records

https://achive.ics.uci.edu/ml/

L8 Hepatitis 19 155 Yes Medical Class

datasets/Hepatitis

https://achive.ics.uci.edu/ml/

Autistic

datasets/Autistic+Spectrum+

L9 disorderfor 21 292 Yes Medical Class

Disorder+Screeing+Data+for+

children

Children++

https://achive.ics.uci.edu/ml/

L10 Automobile 26 205 Yes Automotive Price

datasets/Automobilee

https://achive.ics.uci.edu/ml/

L11 PrimaryTumor 17 339 Yes Medical Classification

datasets/primary+tumor

Facebook https://arhive.ics.uci.edu/ml/ Total

L12 19 500 Yes Business

metrics datasets/Facebook+metrics Interactions

UCIMachineLearning

Hungarian

L13 Repostory:HungarianChicken 20 521 No Life Country

ChickenPox

poxCasesDataSet

https://www.kaggle.com/

Alcoholeffect datasets/whenamancodes/

L14 33 395 No Educational Grade

onmathstudy alcohol-effects-on-study?

select=Maths.csv

UCIMachineLearning

Overall

L15 Soybean-Large Repository:Soybean(Large) 35 307 Yes Life

Diagnosis

DataSet

Therearetwomaincriteriaforchoosingdatasets.First,eachdatasetmustcontainat

least15attributes.Thisisimportantforvalidatingthecapabilityofthelog-linearmodel

inextractingthebestattributesduringthepre-processingphase. Inotherwords,ifwe

choosedatasetsthathavelessthan10attributes,theproposedmodelG3SATRAμwould

providethesameresultsastheworkbyZamrietal.[25].Second,thenumberofinstances

mustbemorethan200toavoidoverfittinginG3SATRAμ.Whenthenumberofinstance

isverylow,thereisahighchancethatthelearningdatawillconsistonlyofFPandFN,

whichleadstorandomLBest selection.Inaddition,k-meansclustering[30]willbeusedto

3SAT

135

Mathematics2023,11,2121

convertthevalueofthedatasetintobipolarformS ={−1,1}.Thisconversioniscrucial

i

toensurethattheproposedG3SATRAμcanbecomparedwithotherexistingwork.Since

eachattributeisrepresentedinbipolarform,themissingdataareassignedrandomlyto

1or−1.AccordingtoSathasivam[38],theCAMdismissestheoutlierdatainthebipolar

formasbeingthefaulttoleranceoftheDHNN.

Thecontinuousattributevaluesinthedatasetarestandardizedusingk-meansclus-

teringbyconvertingthemintobipolarrepresentations. Themethodusedfork-means

clusteringwasinspiredbytheworkof[24,25,31].Toaddresstheissueofmissingvalues,

theyarereplacedwitharandombipolarstate(either1or−1),buttheselecteddatasets

shouldhaveveryfewmissingvaluestoensurethatthelearningphaseisnotaffected.

Inaddition,allsimulationsutilizethetrain-split[30]method,wherethetrainingphase

contains60%ofinstancesandthetestingphasecontains40%ofinstances.Thismethod

hasbeenusedinvariousstudies[24–31],whereafurthertestingpercentagewasusedto

confirmtheeffectivenessoftheLinduced.Thisstudyusedkcrossvalidationonthelimited

i

samplinginstancestoestimatehowthedatasetisexpectedtoperforminthetestingphase;

thosesameinstancesarenotusedduringthetrainingphaseforthemodel.

6.2.PerformanceMetrics

Basedonpopularclassificationmetricssuchasaccuracy(Acc),precision(PREC),sen-

sitivity(SEN),F1score(F1),andMatthewscorrelationcoefficient(MCC),theeffectiveness

ofthesuggestedmodelcanbeassessed. Accisappliedtofigureoutthepercentageof

true-positiveandtrue-negativepredictionsoverthetotalnumberofinstances.Thenum-

bersofinstancesaccuratelyanticipatedapositiveandnegativecasesareknownasthe

truepositive(TP)andtruenegative(TN),respectively,whereasfalse-positive(FP)and

falsenegative(FN)instancesarethesumofthenumberoffalselyanticipatednegativeand

positiveoutcomes,respectively. TheAccvaluecanbemeasuredusingEquation(23),as

shownin[41]:

ACC= TP+T T N P+ + T F N P+FN (23)

SEN examinesthepositivetendenciesoftheinstancesaccuratelyanticipatedina

particularsituation,asmentionedby[42].

SEN= TP T + P FN (24)

Accordingto[43],PRECisusedtoanalyzethenumberofpositiveoutcomesamong

thefalse-positiveoutcomesfromthepredictedoutcomes. ThePRECcanbeformulated

asfollows:

PREC= TP T + P FP (25)

F1 is also one of the metrics used to measure accuracy. F1 is the modulation in-

dex of the sensitivity and precision parameters. The F1 formula is presented in the

followingequation:

F1 = 2(TP 2T + P FP) (26)

TheeffectivenessofthelogicminingprocessisevaluatedintheMatthewscorrelation

coefficient(MCC),whichconsidersalltheelementsofaconfusionmatrix.Accordingto[44],

MCCisavalidindicatorforevaluatingthequalityoftheproposedmodelandmaybe

appliedinvarioussizesofclasses.

MCC= #

TPTN−FPFN

(27)

(TP+FP)(TP+FN)(TN+FP)(TN+FN)

136

Mathematics2023,11,2121

6.3.BaselineMethods

TheperformanceoftheG3SATRAμmodeliscomparedwithnumerouswell-known

current works to confirm the efficiency of the suggested methodology. Even though

therearenumerousclassificationalgorithmsthathavebeenintroduced,includingthose

proposedby[43–47],noneofthesestudieshavedemonstratedthatinducedlogicalrules

caneffectivelycategorizeandextractpatternsfromadataset..Notethattheauthorsof[48]

haveproposedlogicminingthatutilizesalog-linearmodel,buttheorderofthelogicis

lowerthanwhatweproposeinthispaper.Inaddition,ourproposedG3SATRAμmodelis

incomparablewiththeworkin[49]duetothestructureoftheradialbasisfunctionneural

network(RBFNN),whichonlyproducedasingleLinduced.Thus,ourproposedG3SATRAμ

i

modeliscomparedwiththefollowingstate-of-the-artlogicminingmethods:

(a) 2SATRA[24]wasthefirstattemptatextractingthebestQinducedfromdatasets.This

i

logicminingmethodutilizessystematicQ2SATasalogicalruleduringtrainingand

testingphase. Asforthepreprocessingphase,2SATRAusesrandomselectionto

choosethebestattribute.IntermsofthebestlogicQbest ,2SATRAusestheobjective

2SAT

functionthatmaximizesthenumberofTP.Inaddition,2SATRAonlyusesasingle-

unitDHNN.

(b) E2SATRA[27]utilizesenergy-basedlogicminingtoensurethattheQinducedalways

i

followsthedynamicoftheLyapunovfunction. Duringtheretrievalphaseofthe

DHNN,theneuronstatethatachievesthelocalminimumenergyisdiscarded. In

thiscontext,thenumberofQinducedistheoreticallylowerthanthoseof2SATRAand

i

P2SATRA.E2SATRAusessimilarobjectivefunctionstothatof2SATRAandonly

utilizesasingle-unitDHNN.

(c) L2SATRAwasinspiredbytheworkof[50],whichemployedthelog-linearmethodto

extractamodelforanovariancystdataset.Thisstandardselectionmethodutilized

characteristicsandincorporatedconventional2SATRAbasedonalog-linearanalysis.

Althoughthelog-linearmethodwasutilizedtoextractthebestattributes,L2SATRA

doesnotcontainapermutationoperator.L2SATRAusesasimilarobjectivefunction

tothatof2SATRAandonlyutilizesasingle-unitDHNN.

(d) P2SATRA[26]isanextensionoftheworkby[51], where Q2SAT wasformulated

withapermutationoperatorandtookintoconsiderationvariousconfigurationsfor

(2)

theliteralsinC . Thepermutationoperatordeterminesallthepossibilitysearch

i

spacesoftheQinducedandleadstothehighestaccuracyvalue.P2SATRAusessimilar

i

objectivefunctionstothatof2SATRAandonlyutilizesasingle-unitDHNN.

(e) RA[23]istheearliestlogicminingthatutilizesHornSATwhenextractingalogical

rulefromadataset.TheinitialRAdoesnotcontainanypre-processingphasesand

generalizedinducedlogic.Inthispaper,theRAisthesystematicsecond-orderlogic

duringthepreprocessingphase.Duringtheretrievalphase,onlyaQinducedthathas

i

thepropertyofHornSATischosen. RAusesasimilarobjectivefunctiontothatof

2SATRAandonlyutilizesasingle-unitDHNN.

(f) A2SATRA was inspired by [30], and its permutation operator investigates every

conceivablesearchspacethatisconnectedonlytotheselectedattributes.Attributes

areselectedbyfocusingonlyonalog-linearanalysisbyselectingsignificantattributes

intheformofacontingencytable.Inthecontextofthelearningandtestingphases,

A2SATRAusesasimilarobjectivefunctiontothatof2SATRAandonlyutilizesa

single-unitDHNN.

6.4.G3SATRAμConfigurationModel

TheconfigurationmodelofG3SATRAμwasbuiltbasedonalog-linearanalysis,which

consistsofamultidimensionalexaminationdatasetintheformofacontingencytablethat

presentstherelationshipbetweenthequalitativeanddiscretescales.However,G3SATRAμ

concentratesononlyone-wayinteractionstoidentifytheminorqualitiesthatcouldpoten-

tiallycausethelogictooverfit.Equation(16)isusedtomeasurethelikelihoodratiotodetect

137

Mathematics2023,11,2121

anysignificanteffectsandtocarryoutaprimaryinteractionanalysis.Significantattributes

aredeterminedusingEquation(18)andthepermutationattributesaredeterminedusing

Equation(19). ThepermutationoperatorinEquation(20)isusedtoexposealltheinter-

connectionsamongthevariablesofG3SATRAμ.Equation(21)determinesthesignificant

attributeapplied.WeincorporatetheconfigurationoftheLBest intoDHNN-3SATusingthe

3SAT

optimalattributewhichleadstoLinducedviaEquation(2).

i

Table2showsthek-Waymodelandhigher-ordereffectscomponentfork=1,whereby

thesaturatedmodelyieldsthesignificanteffectcomponents.Wewanttounderstandhow

thevariablesinteractwithoneanotherratherthanwithalltheattributes;hence,k = 1

isthemostimportantvaluetoobservehowusingG3SATRAμintoDHNNcancreate

interactionsbetweenvariablesbyconcentratingjustononespecificvariableatatime.Due

tothep-valueofthePearsonchisquarebeinglessthan0.05,itispossibletoinferthatthe

numberofiterationsrepresentingthetrialvariablestopsatonepointsignificantlymore

oftenthanexpectedbychance.Table2showsthatthefirst-ordereffectshaveasubstantial

impactonthemodel. EventhoughinTable2itwasindicatedthatthefirst-ordereffect

hadasignificantimpactontheanalysis,westillneedtoconsiderpartialrelationships

amongallthevariables.Asaresult,toobtainthepartialassociationfindings,thevariables

selectedbeforebeingexpressinginthe3SATlogicalstructureareanalyzed.Theparameters

areselectedbasedonthep-valuebyexcludingunimportantqualitiesfromthedatasets

(p-value=0.05).

Table2.Contingencytablewithsignificantvalues.

Dataset LikelihoodRatio Pearson Numberof

df

Code ChiSquare Sig. ChiSquare Sig. Iterations

L1 6560 2577.08 >0.05 29,311.98 >0.05 2

L2 6560 6177.97 >0.05 83,385.89 >0.05 2

L3 2186 6232.99 <0.05 66,353.66 >0.05 2

L4 59,048 6659.89 >0.05 716,016.90 >0.05 2

L5 59,048 5162.86 >0.05 511,554.83 >0.05 2

L6 59,048 3575.83 >0.05 461,730.61 >0.05 2

L7 59,048 6027.20 >0.05 1,159,233.06 >0.05 2

L8 59,048 2037.78 >0.05 144,991.25 >0.05 2

L9 59,048 3460.08 >0.05 150,161.62 >0.05 2

L10 59,048 2944.39 >0.05 352,648.78 >0.05 2

L11 59,048 4531.92 >0.05 402,552.85 >0.05 2

L12 59,048 6618.33 >0.05 791,465.19 >0.05 2

L13 59,048 1635.73 >0.05 780,527.78 >0.05 2

L14 59,048 4592.94 >0.05 181,834.70 >0.05 2

L15 59,048 1448.48 >0.05 177,047.00 >0.05 2

6.5.ExperimentalDesign

Inthisexperiment,weusedIBMSPSSStatisticsversion27toperformalog-linear

analysisoneachdatasetinTable1.ThespecificconcentrationsusedarelistedinTable3,

which provides a comprehensive overview of the experimental parameters and their

respectivevalues.Weusedcross-validationtoidentifythemostimportantattribute,which

wethenusedforlogicmininginDEVC++Version5.11.Thesimulationranonadevice

withanAMDRyzen53500Uprocessor, RadeonVegaMobileGfx, and8GBofRAM

runningonWindows10.Toensureconsistentresults,weranalltrialsonthesamedevice

toavoidanypotentialerrorsduringthesimulation.

138

Mathematics2023,11,2121

Table3.Theparametersforeachstandardlogicminingmethod.

Parameter G3SATRAμ E2SATRA RA(HornSat) L2SATRA A2SATRA 2SATRA P2SATRA 3SATRA

NumberofVariable 9 6 6 6 6 6 6 9

NumberofClauses 3 3 3 3 3 3 3 3

Neuron

100 100 100 100 100 100 100 100

Combination[52]

AttributeSelection LogLinear Random Random LogLinear LogLinear Random Random Random

EnergyTol 0.001 0.001 - 0.001 0.001 - - -

LearningIteration 100 100 100 100 100 100 100 100

Learning

ES ES ES ES ES ES ES ES

Method[26]

Selectionrate 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1

Trial[40] 100 100 100 100 100 100 100 100

CPUtime[49] 24h 24h 24h 24h 24h 24h 24h 24h

Logical

100 100 100 100 100 100 100 100

Permutation(GC)

Activation

HTAF HTAF HTAF HTAF HTAF HTAF HTAF HTAF

Function[53]

p-value 0.05 - - 0.05 0.05 - - -

7.ResultsandDiscussion

Theprimaryaimofthisstudyistoassesstheperformanceoflogicminingwhenusing

apre-processingstructuretoselectattributes.Inthissection,weevaluateitsperformance

bycomparingG3SATRAμwithexistingwork.Theresultsofeachperformancemetricfor

G3SATRAμ(theexistinglogicmining=G3SATRAμ),where+istheexistinglogicmining

lossinG3SATRAμand-istheexistingsurplusbyG3SATRAμ,comparedwithexisting

methods,showedgoodresultsandarediscussedinthissection.

7.1.AccuracyforCurrentandG3SATRAμLogicMiningModels

Table4showstheACCresultsfortheselectedlogicminingmodel.Thereareseveral

variationsintheperformancesfor G3SATRAμ. Theboldvaluesindicatethatthelogic

miningmethodachievedthemaximumvalue.Diff referstothedifferencesbetweenthe

proposedlogicminingmethod(G3SATRAμ)andtheselectedexistinglogicminingmethod.

Table4alsodisplaystheaveragevalueandminimum,maximum,andaverageranksofthe

Friedmantest.TheaccuracyvalueswererecordedfollowingcomputingusingEquation(23).

Table4.AccvalueforG3SATRAμincomparisonwithstate-of-the-artlogicminingmethods.

E2SATRA RA(HornSAT) L2SATRA A2SATRA 2SATRA P2SATRA 3SATRA

Code G3SATRAμ

ACC Diff ACC Diff ACC Diff ACC Diff ACC Diff ACC Diff ACC Diff

L1 0.655 0.567↓ 0.088 0.475↓ 0.180 0.423↓ 0.232 0.602↓ 0.053 0.453↓ 0.202 0.600↓ 0.055 0.602↓ 0.053

L2 0.720 0.474↓ 0.246 0.442↓ 0.278 0.564↓ 0.155 0.686↓ 0.033 0.519↓ 0.201 0.845↑ −0.125 0.670↓ 0.050

L3 0.666 0.566↓ 0.100 0.484↓ 0.182 0.461↓ 0.205 0.597↓ 0.070 0.502↓ 0.164 0.571↓ 0.095 0.566↓ 0.101

L4 0.823 0.534↓ 0.289 0.619↓ 0.204 0.595↓ 0.228 0.855↑ −0.032 0.574↓ 0.249 0.778↓ 0.045 0.677↓ 0.146

L5 0.939 0.763↓ 0.176 0.509↓ 0.430 0.770↓ 0.169 0.923↓ 0.016 0.454↓ 0.485 0.980↑ −0.041 0.576↓ 0.363

L6 0.757 0.553↓ 0.204 0.703↓ 0.054 0.564↓ 0.193 0.665↓ 0.092 0.619↓ 0.138 0.759↑ −0.002 0.684↓ 0.073

L7 0.868 0.431↓ 0.437 0.421↓ 0.447 0.686↓ 0.182 0.869↑ −0.001 0.440↓ 0.428 0.778↓ 0.090 0.786↓ 0.082

L8 0.858 0.384↓ 0.474 0.539↓ 0.319 0.432↓ 0.426 0.826↓ 0.032 0.387↓ 0.471 0.829↓ 0.029 0.671↓ 0.187

L9 0.776 0.723↓ 0.053 0.485↓ 0.291 0.617↓ 0.159 0.762↓ 0.014 0.747↓ 0.029 0.754↓ 0.022 0.651↓ 0.125

L10 0.812 0.737↓ 0.076 0.400↓ 0.412 0.471↓ 0.341 0.671↓ 0.141 0.776↓ 0.037 0.873↑ −0.061 0.739↓ 0.073

L11 0.690 0.557↓ 0.132 0.619↓ 0.071 0.576↓ 0.113 0.613↓ 0.076 0.619↓ 0.071 0.676↓ 0.013 0.572↓ 0.118

L12 0.910 0.497↓ 0.413 0.468↓ 0.442 0.345↓ 0.565 0.771↓ 0.139 0.467↓ 0.443 0.970↑ −0.060 0.567↓ 0.343

L13 0.751 0.646↓ 0.105 0.376↓ 0.375 0.530↓ 0.222 0.708↓ 0.043 0.652↓ 0.100 0.751↓ 0.000 0.641↓ 0.110

L14 0.695 0.547↓ 0.148 0.544↓ 0.151 0.466↓ 0.229 0.638↓ 0.057 0.547↓ 0.148 0.589↓ 0.106 0.668↓ 0.027

L15 0.724 0.607↓ 0.117 0.521↓ 0.203 0.623↓ 0.101 0.624↓ 0.099 0.62↓3 0.101 0.707↓ 0.016 0.626↓ 0.098

+/=/− 9/0/6 15/0/0 15/0/0 15/0/0 13/0/2 15/0/0 10/0/5 15/0/0

Avg 0.776 0.572 0.507 0.542 0.721 0.559 0.764 0.646

Min 0.655 0.384 0.376 0.345 0.597 0.387 0.571 0.566

Max 0.939 0.763 0.703 0.770 0.923 0.776 0.980 0.786

AvgRank 1.600 6.170 6.430 6.500 3.070 5.700 2.230 4.300

Note:Thesymbol↑indicatesthatthelogicmininghasahigheraccuracyvalue,while↓indicatesaloweraccuracy

value.TheboldnumbersunderdiffarecomparisonvaluesforG3SATRAμvs.currentlogicminingmethods.

139

Mathematics2023,11,2121

(a) SeveraldecentperformancesresultedfromtheG3SATRAμ.Theapplicationofthe

log-linearanalysisisassumedtobehighlyeffectiveinpre-processingmethods,as

itidentifiessignificantattributeswithap-valueofp≤0.05.Thisresultsinoptimal

synapticweightvaluesassociatedwiththeresultingattributesforL3SAT[50].Further-

more,sincethelogicalrulesembeddedintheG3SATRAμmodelarewell-structured,

theoutcomeshavethepotentialtoachievehighervaluesforthetruepositives(TPs)

andtruenegatives(TNs).

(b) ThedatasetL11(FacebookMetric)wassignificantbecauseitsaccuracyratingwas

almost1.Therefore,wecanconcludethattheinducedlogicobtainedanaccuracythat

wasverycloseto1forallTPandTN.However,astudyby[26]foundthat,when

comparedwiththelog-linearintegrationmethodusingthenine-attributepermuta-

tionmethod,theP2SATRAmethodwithrestrictionsimprovedidentificationofthe

bestinducedlogicandproducedmoresatisfactoryresultsbasedontruedata.This

indicatesthat,intermsoftheperformanceofthedataset,thelocalfieldcanextract

thebestinducedlogic[54].

(c) AccordingtoTable4,thereareseveralvaluesforourproposedlogicinwhichan

accuracyofAcc>0.8wasachieved.Therefore,wecandeducethattheproposedlogic

miningmethodG3SATRAμseparatetruepositivesfromtruenegativefordatasets.

Therefore,ourworkappliedWanAbdullah’sapproachtoobtainoptimalsynaptic

weight stands [17] to decrease the false negative values that can be produced in

clauses[23].

(d) TheinducedlogicretrievedforL8is L=A←B←C∧D∧E.L8referstosymptoms

ofhepatisdisorder,withattributeA,B,C,D,E,F,G,H,andIrepresentingsteroid,

antivirals,fatigue,malaise,anorexia,liverbig,liverfirm,spleenpalpable,ascites,

andvarices,respectively.Accordingtotheinducedlogic,thesymptomsofhepatis

disorderincreasewhenbilirubinincreasesbyabout60%forfactorsA,C,E,andG.

(e) TheFriedmanranktestwasperformedoneachdatasetw(cid:11)ithα = 0.05(cid:12)anddegree

of freedom (df =7). The Acc p-value is less than 0.05 χ2=69.269 . The null

hypothesis, whichclaimedthatalllogicminingmodelsperformidentically, was

rejected.Asmentionedby[30],thehighestaveragerankisevidenceofthesuperior

performanceofalogicminingmodel. Inthisresearch,theproposedG3SATRAμ

modelachievedameanrankofapproximately1.6amongtheotherlogicmining

models.However,thesecond-highestrankwasachievedbyP2SATRA[21],which

closelycompetedwithourmodel,withanaveragerankofapproximately2.23.

AsshowninFigure3,wecanconcludethatthehighACCvalueisduetotheeffective

trainingphase,whichleadstoanoptimalsynapticweightforthe3SATlogicalrule.This

enablesthenetworktoretrievetheoptimalinducedlogicthroughalocalfield(Equation(9)).

By using a log-linear analysis to select the best attribute, we can further improve the

accuracybyobtainingoptimalsynapticweights,whichleadstohighertruepositive(TP)

and true negative (TN) values. Additionally, the log-linear model can eliminate non-

significantattributes,resultinginlowerfalsepositive(FP)andfalsenegative(FN)values.

ComparingourworkwithRA(HornSAT)[18],weobservethatthenon-flexiblesynaptic

weightoftheirlogicalstructureresultsinlowerTPandTNvalues.Thesuboptimalsynaptic

weightalsoleadstosuboptimalinducedP,whichisfurtherexacerbatedwhenattributes

arerandomlyselectedinRA(HornSAT).ThisfeaturecontributestothelowerTPandTN

valuesinRA(HornSAT).

140

Mathematics2023,11,2121

Figure3.Accuracyoflogicminingmodels.

7.2.PrecisionforCurrentandG3SATRAμLogicMiningModels

ThePRECvaluesforthechosenlogicminingmodelaredisplayedinTable5below.

G3SATRAμshowsseveralvariationsinperformanceforeachdataset.Thevaluesinbold

showthatthespecificlogicminingmethodreacheditsmaximumvalue. Diff denotes

thedifferencesbetweenthechosencurrentlogicminingandtheproposedlogicmining

(G3SATRAμ).Table5alsoshowstheFriedmantest’saveragevalue,minimumandmax-

imumranks,andrangeforranks. Theprecisionvaluesherewerepredicatedbasedon

Equation(25).

Table5.PRECvalueforG3SATRAμincomparisonwithstate-of-the-artlogicminingmethods.

E2SATRA RA(HornSAT) L2SATRA A2SATRA 2SATRA P2SATRA 3SATRA

Code G3SATRAμ

PREC Diff PREC Diff PREC Diff PREC Diff PREC Diff PREC Diff PREC Diff

L1 0.693 0.659↓ 0.034 0.610↓ 0.083 0.518↓ 0.175 0.674↓ 0.019 0.537↓ 0.156 0.628↓ 0.065 0.634↓ 0.059

L2 0.628 0.440↓ 0.188 0.444↓ 0.185 0.451↓ 0.177 0.611↓ 0.017 0.461↓ 0.167 0.751 −0.123 0.604↓ 0.024

L3 0.547 0.410↓ 0.137 0.372↓ 0.175 0.355↓ 0.192 0.286↓ 0.261 0.371↓ 0.176 0.391↓ 0.156 0.443↓ 0.105

L4 0.883 0.634↓ 0.250 0.655↓ 0.229 0.751↓ 0.132 0.910 −0.027 0.648↓ 0.235 0.823↓ 0.060 0.687↓ 0.196

L5 0.917 0.901↓ 0.016 0.606↓ 0.311 0.703↓ 0.213 0.864↓ 0.053 0.568↓ 0.348 0.938 −0.021 0.614↓ 0.303

L6 0.916 0.745↓ 0.171 0.787↓ 0.129 0.850↓ 0.066 0.937 −0.021 0.793↓ 0.123 0.906↓ 0.010 0.788↓ 0.128

L7 0.888 0.442↓ 0.446 0.590↓ 0.297 0.838↓ 0.050 0.915 −0.028 0.552↓ 0.335 0.815↓ 0.073 0.861↓ 0.026

L8 0.898 0.867↓ 0.030 0.842↓ 0.055 0.889↓ 0.009 0.866↓ 0.031 0.718↓ 0.180 0.880↓ 0.018 0.800↓ 0.097

L9 0.720 0.732 −0.012 0.495↓ 0.225 0.580↓ 0.140 0.710↓ 0.010 0.687↓ 0.033 0.700↓ 0.020 0.609↓ 0.112

L10 0.700 0.606↓ 0.094 0.379↓ 0.321 − − 0.599↓ 0.102 0.671↓ 0.029 0.815 −0.115 0.603↓ 0.097

L11 0.676 0.469↓ 0.207 0.462↓ 0.214 0.542↓ 0.134 0.573↓ 0.103 0.462↓ 0.214 0.634↓ 0.042 0.525↓ 0.151

L12 0.790 − − 0.264↓ 0.527 0.279↓ 0.512 0.612↓ 0.178 0.287↓ 0.503 0.950 −0.160 0.405↓ 0.386

L13 0.639 0.521↓ 0.118 0.336↓ 0.303 0.448↓ 0.192 0.582↓ 0.058 0.554↓ 0.085 0.644 −0.005 0.541↓ 0.099

L14 0.668 0.542↓ 0.125 0.545↓ 0.122 0.422↓ 0.246 0.605↓ 0.063 0.542↓ 0.125 0.571↓ 0.097 0.631↓ 0.036

L15 0.739 0.636↓ 0.102 0.581↓ 0.157 0.648↓ 0.090 0.649↓ 0.089 0.650↓ 0.089 0.699↓ 0.040 0.654↓ 0.084

‘+/=/− 6/0/9 13/0/2 15/0/0 14/0/1 12/0/3 15/0/0 10/0/5 15/0/0

Avg 0.753 0.615 0.531 0.591 0.693 0.567 0.743 0.627

Min 0.547 0.410 0.264 0.279 0.286 0.287 0.391 0.405

Max 0.917 0.901 0.842 0.889 0.937 0.793 0.950 0.861

AvgRank 1.6 5.330 6.200 5.470 3.270 5.600 2.530 6.000

Note:Thesymbol↑indicatesthatthelogicminingmethodhashigherprecisionvalues,while↓indicateslowerprecision

values.TheboldnumberunderdiffisacomparisonvalueforG3SATRAμvs.thecurrentlogicminingmethod.

(a) PRECshowsthatG3SATRAμperformsbetterthanotherlogicminingmodelsacross

all15datasets.ThisdemonstratesthecapabilityofG3SATRAμtoextractahighvalue

fortruepositives.G3SATRAμimprovedtheperformanceofthe3SATRAproposed

by[20]byembeddingoptimalattributesinthe3SATandretrievingoptimallyinduced

logicthatisimportanttothedataset.Asaresult,G3SATRAμismorecapablethan

othercurrentlogicminingmodelsatproducingsuccessfuloutcomes.

141

Mathematics2023,11,2121

(b) G3SATRAμachievedaPRECthatisverycloseto1(Precision=1)intwodatasets,L5

andL6.There,itshowsthattheinducedLBest retrievedbyG3SATRAμcanpredict

3SAT

positiveoutcomeswithcertainty.EverydatasetoutputfromtheinducedLBest equals

3SAT

1. TheproposedlogicminingmodelG3SATRAμyieldsaprecisionthatisalmost

equalto1indatasetsL5andL6.Therefore,thefinalneuronstatesobtainedfromthe

localfieldprovideasatisfactoryinterpretationasaresult[25].

(c) IncomparisonwithA2SATRAproposedby[30],theproposedG3SATRAμinthis

paperisabletomoreaccuratelypredictpositiveinstances,withtheexceptionofthree

datasets(L4,L6,andL7).WhileP2SATRAsuggestedby[21]maystillpredictthebest

inducedlogicforfivedatasets(L2,L5,L10,L12,andL13),theG3SATRAμmodelcan

achievehigherpositivevaluesforthesespecificdatasets.

(d) ThisproposedG3SATRAμmodeloutperformsotherlogicminingmodelssuchas

E2SATRA,RA,2SATRA,3SATRA,andL2SATRAintermsofachievinghighervalues

oftruepositives(TPs)andtruenegatives(TNs).Ithasbeendemonstratedthatusinga

log-linearanalysisforattributeselectionandmulti-unittheoryin3SATleadstomore

accurateTPvalues.

(e) TheaveragerankoftheproposedG3SATRAμlogicminingmodelis1.600,which

ishigherthantheaveragerankofothermodels. Theclosestcompetingmethodis

P2SATRA,withanaveragerankof2.530.Thestatisticalanalysisconfirmsthatour

proposedmodelG3SATRAμissuperiortotheothermethods.Thismeansthatour

modelisverygoodatidentifyingbothpositiveandnegativeresults.

InFigure4,theprecisionvalueishighercomparedwithotherexistinglogicmining

methodssuchasRA(HornSAT),E2STRA,2SATRA,andA2SATRA.Theproposedmodel

usingalog-linearanalysisachievedahigherP valuebyselectingtheperfectattribute

best

fromthewholedataset. Thepermutationoperatedwithinaverylargesearchingspace

toreducethecostfunction. Themultidimensionalsolutionintheproposedsystematic

logicalstructureledtoobtainingmoreTNsandlessFPs.Theexistinglogicminingmethods

L2SATRA[50]andA2SATRA[30]obtainedsup-optimalperformancesinthetestingphase,

obtainingmoreFPsthatreducetheprecisionvaluefortheirmodel.

Figure4.Precisionoflogicminingmodels.

142

Mathematics2023,11,2121

7.3.SensitivityforCurrentandG3SATRAμLogicMiningModels

Table6showstheSENresultsfortheselectedlogicminingmodel.Therearevariations

intheperformancesoftheG3SATRAμ.Whereastheboldvaluesindicatethattheparticular

logic mining achieved the maximum value, diff refers to the differences between the

proposedlogicminingmethod(G3SATRAμ)andtheselectedexistinglogicminingmethod.

Table6alsodisplaystheaveragevalueandminimum,maximum,andaverageranksfrom

theFriedmantest.TheseSENvalueswereobtainedusingEquation(24).

Table6.SENvaluesforG3SATRAμincomparisonwithstate-of-the-artlogicminingmethods.

E2SATRA RA L2SATRA A2SATRA 2SATRA P2SATRA 3SATRA

Code G3SATRAμ

SEN Diff SEN Diff SEN Diff SEN Diff SEN Diff SEN Diff SEN Diff

L1 0.769 0.586↓ 0.183 0.389↓ 0.380 0.514↓ 0.255 0.670↓ 0.099 0.562↓ 0.207 0.843↑ −0.074 0.784↑ −0.015

L2 0.643 0.663↑ −0.021 0.522↓ 0.121 0.596↓ 0.047 0.513↓ 0.130 0.809↑ −0.167 0.914↑ −0.271 0.648↑ −0.006

L3 0.516 0.436↓ 0.080 0.610↑ −0.094 0.515↓ 0.001 0.185↓ 0.330 0.506↓ 0.010 0.339↓ 0.177 0.720↑ −0.204

L4 0.777 0.505↓ 0.272 0.774↓ 0.003 0.554↓ 0.223 0.838↑ −0.061 0.524↓ 0.253 0.736↓ 0.041 0.792↑ −0.015

L5 0.937 0.720↓ 0.217 0.834↓ 0.104 0.923↓ 0.015 0.947↑ −0.009 0.676↓ 0.262 0.956↑ −0.019 0.876↓ 0.062

L6 0.755 0.667↓ 0.088 0.859↑ −0.104 0.575↓ 0.180 0.613↓ 0.141 0.678↓ 0.076 0.778↑ −0.023 0.811↑ −0.056

L7 0.901 0.195↓ 0.705 0.384↓ 0.516 0.608↓ 0.293 0.867↓ 0.034 0.516↓ 0.385 0.831↓ 0.070 0.784↓ 0.116

L8 0.921 0.260↓ 0.661 0.522↓ 0.398 0.353↓ 0.568 0.918↓ 0.003 0.428↓ 0.492 0.895↓ 0.026 0.807↓ 0.113

L9 0.921 0.754↓ 0.168 0.700↓ 0.221 0.940↑ −0.019 0.907↓ 0.014 0.926↑ −0.004 0.894↓ 0.027 0.893↓ 0.029

L10 0.860 0.711↓ 0.148 0.900↑ −0.040 0.299↓ 0.561 0.455↓ 0.405 0.802↓ 0.058 0.887↑ −0.027 0.926↑ −0.067

L11 0.596 0.668↑ −0.072 0.507↓ 0.089 0.602↑ −0.006 0.443↓ 0.153 0.507↓ 0.089 0.578↓ 0.018 0.801↑ −0.205

L12 0.933 0.537↓ 0.396 0.519↓ 0.414 0.862↓ 0.071 0.496↓ 0.437 0.586↓ 0.347 0.941↑ −0.008 0.654↓ 0.279

L13 0.759 0.585↓ 0.175 0.727↓ 0.032 0.832↑ −0.072 0.773↑ −0.014 0.755↓ 0.004 0.694↓ 0.066 0.779↑ −0.020

L14 0.855 0.958↑ −0.102 0.814↓ 0.041 0.588↓ 0.267 0.903↑ −0.048 0.958↑ −0.102 0.887↑ −0.031 0.904↑ −0.048

L15 0.852 0.695↓ 0.157 0.697↓ 0.156 0.822↓ 0.031 0.854↑ −0.001 0.827↓ 0.026 0.912↑ −0.060 0.810↓ 0.043

‘+/=/− 2/0/13 12/0/3 12/0/3 12/0/3 10/0/5 12/0/3 8/0/7 6/0/9

Avg 0.800 0.596 0.651 0.639 0.692 0.671 0.806 0.799

Min 0.516 0.195 0.384 0.299 0.185 0.428 0.339 0.648

Max 0.937 0.958 0.900 0.940 0.947 0.958 0.956 0.926

AvgRank 2.97↑ 5.87 5.33 5.2 4.53 4.8 3.13 4.17

Note:Thesymbol↑indicatesthatthelogicminingmethodhasahighersensitivityvalue,while↓indicatesa

lowersensitivityvalue.TheboldnumberunderdiffisacomparisonvalueforG3SATRAμvs.currentlogicmining

methods.

(a) Our proposed logic mining method G3SATRAμ outperformed the 3SATRA and

P2SATRA.Thisdemonstratestheimportanceofthelog-linear-approach-chosenfea-

turesforagivendatasetnotbeingsignificantforthedataset.Therandomselection

proposedby[26]successfullyretrievedQtest =1foralloutcomes.

2SAT

(b) OurG3SATRAμmodelachievedaSENcloseto1(0.937),indicatingitsabilityto

predictpositiveoutcomesintheretrievalphaseoftheDHNNfortheL5dataset.For

theotherdatasets,ourmodeldemonstratedhighTNandTPvaluescomparedwith

otherlogicminingmodels.Infact,fortheL7andL8datasets,ourproposedmodel

achievedhigherTNandTPvaluesthanothermodels.

(c) Therearesomeinstanceswherethesensitivitywasnotrecordedduetothelack

ofapositiveoutcomeforthatdatasetinthelogicminingmethodsE2SATRAand

L2SATRA.Furthermore, thereisagoodlikelihoodthatthedatasetrepresentsan

actualsituationandthatthetestingdataonlycontainsnegativeclasses.Itfollowsthat

theinducedQBestisbiastowardstothenegativeclass.

(d) Forallofthedatasets,theFriedma(cid:11)nranktestwa(cid:12)sperformedwithα=0.05anddf =7.

Thep-valueforSenis<0.05,and χ2=18.698 .Asaresult,thenullhypothesisthat

alllogicminingmodelsperformequallywellwasrejected. AccordingtoTable6,

G3SATRAμ’sperformancestilldisplaysacompetitiveSenvaluewhencompared

withotherpublishedworksuchas3SATRA,P2SATRA,andA2SATRA.Thelowest

statisticalaveragerankachievedinthelogicminingmethodE2SATRAwas5.80.This

staticaltestcanpredictthatA3SATRAcanstillreachtheLinducedwhenaddinganother

Best

optimizationlayer,whichwouldincreasetheDHNN’scomplexity.

Similarly,totheprecisionmetrics,theconfusionmetricforsensitivityalsoachievesa

higherTPvalueintheproposedlogicalstructureG3SATRAμwhencomparedwithother

logicalstructures,exceptP2SATRA[26].Figure5showstheselectionofrandomattributes

andthepermutationoperatorobtaininganaccuratelocalfieldtoachievethebestoptimal

143

Mathematics2023,11,2121

solution.TheG3SATRAμisnotbadintermsoftheoptimalsolutionwhenweusedthe

Friedmanranktest.Itsrankingvaluewasstillofahigherordercomparedwiththeother

currentlogicminingmethods.

Figure5.Sensitivityoflogicminingmodels.

7.4.F1forCurrentandG3SATRAμLogicMiningModels

Table7showstheF1resultfortheselectedlogicminingmodel.Thereisvariationin

theperformancesfortheG3SATRAμ.Whereastheboldvaluesindicatethattheparticular

logicminingmethodachievedthemaximumvalue,diff referstothedifferencesbetween

theproposedlogicminingmethod(G3SATRAμ)andtheselectedexistinglogicmining

method.Table7alsodisplaystheaveragevalueandminimum,maximum,andaverage

ranksfromtheFriedmantest.TheseF1valueswerecomputedusingEquation(26).

Table7.FIvalueforG3SATRAμincomparisonwithstate-of-the-artlogicminingmethods.

G3SATRAμ E2SATRA RA(HornSAT) L2SATRA A2SATRA 2SATRA P2SATRA 3SATRA

Code FIScore

Sc

F

o

I

re

Diff

Sc

F

o

I

re

Diff

Sc

F

o

I

re

Diff

Sc

F

o

I

re

Diff

Sc

F

o

I

re

Diff

Sc

F

o

I

re

Diff

Sc

F

o

I

re

Diff

L1 0.726 0.610↓ 0.116 0.461↓ 0.265 0.512↓ 0.214 0.666↓ 0.060 0.549↓ 0.178 0.712↓ 0.014 0.700↓ 0.026

L2 0.630 0.504↓ 0.127 0.423↓ 0.207 0.508↓ 0.122 0.546↓ 0.085 0.569↓ 0.061 0.820↑ −0.190 0.607↓ 0.023

L3 0.529 0.415↓ 0.114 0.455↓ 0.074 0.411↓ 0.118 0.195↓ 0.334 0.425↓ 0.104 0.354↓ 0.175 0.547↑ −0.018

L4 0.826 0.548↓ 0.278 0.684↓ 0.142 0.625↓ 0.202 0.870↑ −0.044 0.569↓ 0.257 0.776↓ 0.050 0.722↓ 0.104

L5 0.919 0.759↓ 0.160 0.617↓ 0.303 0.739↓ 0.181 0.886↓ 0.034 0.553↓ 0.366 0.947↑ −0.027 0.663↓ 0.257

L6 0.827 0.698↓ 0.129 0.816↓ 0.011 0.667↓ 0.160 0.741↓ 0.086 0.722↓ 0.105 0.835↑ −0.008 0.796↓ 0.031

L7 0.893 0.259↓ 0.634 0.448↓ 0.445 0.702↓ 0.191 0.890↓ 0.003 0.522↓ 0.371 0.820↓ 0.073 0.817↓ 0.075

L8 0.909 0.392↓ 0.517 0.635↓ 0.274 0.467↓ 0.442 0.891↓ 0.018 0.509↓ 0.400 0.886↓ 0.022 0.787↓ 0.122

L9 0.807 0.735↓ 0.072 0.577↓ 0.230 0.716↓ 0.091 0.795↓ 0.012 0.788↓ 0.019 0.785↓ 0.023 0.723↓ 0.084

L10 0.770 0.639↓ 0.130 0.531↓ 0.239 0.250↓ 0.520 0.504↓ 0.266 0.727↓ 0.043 0.839↑ −0.069 0.726↓ 0.044

L11 0.618 0.515↓ 0.103 0.463↓ 0.155 0.554↓ 0.064 0.410↓ 0.208 0.463↓ 0.155 0.539↓ 0.079 0.626↑ −0.008

L12 0.854 0.302↓ 0.552 0.334↓ 0.520 0.419↓ 0.435 0.546↓ 0.308 0.348↓ 0.506 0.946↑ −0.092 0.479↓ 0.374

L13 0.686 0.511↓ 0.175 0.456↓ 0.230 0.564↓ 0.122 0.655↓ 0.031 0.621↓ 0.065 0.665↓ 0.021 0.619↓ 0.067

L14 0.747 0.690↓ 0.056 0.652↓ 0.095 0.464↓ 0.283 0.724↓ 0.023 0.690↓ 0.056 0.694↓ 0.053 0.740↓ 0.007

L15 0.787 0.633↓ 0.154 0.622↓ 0.164 0.719↓ 0.068 0.728↓ 0.059 0.722↓ 0.065 0.789↑ −0.002 0.723↓ 0.064

‘+/=/− 6/0/9 15/0/0 15/0/0 15/0/0 14/0/1 15/0/0 8/0/7 13/0/2

Avg 0.769 0.547 0.545 0.555 0.670 0.585 0.760 0.685

Min 0.529 0.259 0.334 0.250 0.195 0.348 0.354 0.479

Max 0.919 0.759 0.816 0.739 0.891 0.788 0.947 0.817

AvgRank 1.53 5.930 6.330 5.870 3.800 5.000 2.400 5.130

Note:Thesymbol↑indicatesthatthelogicminingmethodhasahigherFIScore,while↓indicatesalowerFI

score.TheboldnumberunderdiffisacomparisonvalueforG3SATRAμandcurrentlogicminingmethods.

144

Mathematics2023,11,2121

(a) Themulti-unitG3SATRAμformsquiteagoodnumberofpositiveoutcomeswhen

learningfromallthedatasets[41].WhenwecompareP2SATRAwiththeproposed

G3SATRAμ,performanceislackingintermsofretrievedpositiveoutcomes.There-

fore,theauthorsof[29]statedthattheoptimalvalueforsynapticweightiskeptinthe

contentaddressablememory,andLBest canenhancethelocalfieldwhencomputing

3SAT

theidealfinalneuronstate.

(b) Onedataset,L5,obtainedanF1scoreof0.921,whichiscloseto1,intheproposed

modelG3SATRAμ.ThisshowsthatourproposedG3SATRAμproducedthecorrect

numberofTPsduringtheretrievalphaseoftheDHNN,andasweknowthrough

previous work [43], if F1 = 1, the model has perfect precision and recall (correct

positivepredictionsrelativetototalactualpositives)efficiency.

(c) ThereisnoinstancewhereourdatareturnanF1score=0;therefore,ourproposed

logicwasabletoproduceTPs. TheLinducedthatwasdeterminedbycomputingthe

Best

localfieldissensitivetocorrectlyforecastedpositivesituations. Themajorityof

LinducedleanedtowardsLtest =1,reachingthevalueofF1.Theinducedlogicledto

Best 3SAT

LLearn=1

3SAT

(d) Alldatasetswithα=0.05andsevendegrees(cid:11)offreedomu(cid:12)nderwenttheFriedmantest

accurately.TheF1p-valueisα ≤ 0.05,and χ2=54.089 .Thus,thenullhypothesis

thatalllogicminingmodelswillperformequallywellwasrejected.However,com-

paredwiththeotherworks,G3SATRAμobtainedagreataveragerankequalto1.53.

ThisistheoutcomeofG3SATRAμ’sabilitytoanticipatewhichattributesmaximise

TPduringtheDHNNretrievalphase.

InFigure6,wecontinueanalyzingtheFIvaluewithallofthehigher-orderlogical

structures;3SAThasahigherprobabilityofbeingasatisfiedlogic.Itshigher-orderlogical

ruleobtainsthecorrectsynapticweighttoachieveanideallocalfield,whichincreases

accuracy. G3SATRAμisstillhasthehighestFIvaluecomparedtootherlogicmining

methods,whicharesecond-orderlogicalstructureswithahighprobabilityofbeingan

unsatisfiedcondition.AsuccessfullyselectedrandomattributeobtainsmoreFPvaluesin

the15selecteddatasets.Aswecansee,the3SATRAproposedby[25]stillcanachievean

optimalvalueclosetothatofG3SATRAμduetobothbeinghigher-orderlogicalstructures.

Figure6.FIScoreoflogicminingmodels.

145

Mathematics2023,11,2121

InFigure6,wecontinueanalyzingtheFIvaluewithallofthehigherorderlogical

structures;3SAThasahigherprobabilityofbeingasatisfiedlogic.Ithigher-orderlogical

ruleobtainthecorrectsynapticweighttoachieveanideallocalfield,whichincreasesits

accuracy.G3SATRAμisstillintheleadintermsofFIvaluecomparedwiththeotherlogic

miningmethodsthataresecond-orderlogicalstructureswithveryhighchancesofbeing

anunsatisfiedcondition.AsuccessfullyselectedrandomattributeobtainsmoreFPvalues

inthe15selecteddatasets.Aswecansee,the3SATRAproposedby[25]canstillachievean

optimalvalueclosetothatofG3SATRAμduetobothbeinghigher-orderlogicalstructures.

7.5.MatthewsCorrelationCoefficientforCurrentandG3SATRAμLogicMiningModels

TheMCCresultforthechosenlogicminingmodelcanbeseeninTable8.G3SATRAμ

displaysavarietyoflinearcapabilities.Theboldnumbers,ontheotherhand,showthata

givenlogicminingapproachhasreacheditsmaximumvalue.Diffrepresentsthedifferences

betweenthechosenexistinglogicminingmethodandthesuggestedlogicminingmethod

(G3SATRAμ). Theaveragevalueandminimum,maximum,andaverageranksofthe

FriedmantestareshowninTable8.TheseMCCvalueswereobtainedusingEquation(27).

Table8.MCCvalueforG3SATRAμincomparisonwithstate-of-the-artlogicminingmethods.

G3SATRAμ E2SATRA RA(HORNSAT) L2SATRA A2SATRA 2SATRA P2SATRA 3SATRA

Code

MCC MCC Diff MCC Diff MCC Diff MCC Diff MCC Diff MCC Diff MCC Diff

L1 0.272 0.102↓ 0.170 −0.010↓ 0.282 −0.196↓ 0.468 0.154↓ 0.118 −0.145↓ 0.417 0.076↓ 0.196 0.114↓ 0.158

L2 0.337 −0.018↓ 0.356 −0.016↓ 0.353 0.005↓ 0.332 0.257↓ 0.080 0.074↓ 0.263 0.623↑ −0.286 0.298↓ 0.039

L3 0.267 0.065↓ 0.201 0.022↓ 0.245 −0.078↓ 0.345 −0.004↓ 0.271 0.005↓ 0.262 0.042↓ 0.225 0.189↓ 0.077

L4 0.530 0.045↓ 0.485 0.148↓ 0.382 0.211↓ 0.319 0.611↑ −0.081 0.069↓ 0.461 0.441↓ 0.089 0.214↓ 0.316

L5 - - - - - - - - - - - - - - -

L6 - - - - - - - - - - - - - - -

L7 0.724 −0.060↓ 0.784 −0.144↓ 0.868 0.413↓ 0.310 0.730↑ −0.006 −0.186↓ 0.910 0.535↓ 0.189 0.567↓ 0.157

L8 0.486 0.054↓ 0.432 0.071↓ 0.415 0.146↓ 0.340 0.331↓ 0.155 −0.177↓ 0.662 0.354↓ 0.132 0.062↓ 0.424

L9 0.573 0.461↓ 0.113 −0.051↓ 0.624 0.269↓ 0.304 0.541↓ 0.032 0.523↓ 0.050 0.523↓ 0.050 0.327↓ 0.246

L10 0.624 0.454↓ 0.170 −0.002↓ 0.625 - - 0.269↓ 0.355 0.547↓ 0.077 0.750↓ −0.126 0.546↓ 0.078

L11 0.284 −0.049↓ 0.334 −0.074↓ 0.359 0.057↓ 0.228 0.060↑ 0.225 −0.074↓ 0.359 0.078↓ 0.207 0.090↓ 0.194

L12 0.797 - - −0.054↓ 0.851 - - 0.400↓ 0.397 - - 0.925↑ −0.128 0.186↓ 0.611

L13 0.497 0.290↓ 0.207 −0.116↓ 0.613 - - 0.434↓ 0.062 0.360↓ 0.136 0.467↓ 0.030 0.361↓ 0.136

L14 0.404 - - 0.073↓ 0.330 −0.107↓ 0.510 0.299↓ 0.105 - - 0.180↓ 0.223 0.372↓ 0.032

L15 0.399 - - −0.016↓ 0.415 - - - - - - 0.361↓ 0.038 0.141↓ 0.258

‘+/=/− 13/0/2 13/0/2 15/0/0 14/0/1 12/0/3 15/0/0 10/0/5 15/0/0

Avg 0.476 0.134 −0.013 0.080 0.340 0.100 0.412 0.267

Min 0.267 −0.060 −0.144 −0.196 −0.004 −0.186 0.042 0.062

Max 0.797 0.461 0.148 0.413 0.730 0.547 0.925 0.567

AvgRank 1.87↑ 5.670 6.130 5.900 3.430 5.800 2.800 4.400

Note:Thesymbol↑indicatesthatthelogicminingmethodhasahigherMCCvalue,while↓indicatesalower

MCCvalue.TheboldnumberunderdiffisacomparisonvalueforG3SATRAμvs.currentlogicminingmethods.

(a) Ourproposedlogicminingmethod,themulti-unitG3SATRAμ,managedtoobtain

optimalresultsforMCC,about10outof15, foralldatasets. Theauthorsof[51]

mentionedthatastheMCCvalueapproaches0,thevaluesareabletopredictwhich

attributeswillberandomlyselected.Inthisaspect,theMCCvalueanalysisassistsin

determiningtheeffectivenessoftheconfusionmatrixderivedfromtheinducedlogic

extractedbyG3SATRAμ.

(b) Thelog-linearanalysisproposedby[30]isabletoproducethebestattributeselectionin

A2SATRAandG3SATRAμtoobtaininstancesofpositiveoutcomes,withMCC=>0.5in

thisresearchanalysis.Asaresult,theMCCvaluesofthefivedatasetsintheG3SATRAμ

modelaremorethan0.5amongthe15dataset(L4,L7,L9,L10,andL12).

(c) DatasetsL5andL6obtainedvaluesofzero,astheMCCwasnotregisteredbecause

nopositiveoutcomewasregisteredthroughoutthedataset. Thisindicatesinthe

G3SATRAμmodel,Ltest isnotreliable. Insometheotherlogicminingmethods,

3SAT

thefalsevaluesofzeroinlogicminingmethodsE2SATRA,L2SATRA,and2SATRA

Ltest arenotreliableincertaindatasets.

3SAT

(d) Alldatasetswithα=0.05and(cid:11)df=7were(cid:12)subjectedtoaFriedmanranktest. The

MCCp-valueisα ≤ 0.05,and χ2=51.854 .Asaresult,thenullhypothesisthatall

logicminingmodelsperformequallywellwasrejected. Thehighestaveragerank

146

Mathematics2023,11,2121

amongthecurrentlyusedmethodsis1.87,forG3SATRAμ.Atthesametime,notice

thatP2SATRA,withanaveragerankof2.800,isthemethodthatmostcloselyrivals

G3SATRAμ.Asaresult,itindicatesthatalltheconfusionmatricesproposedinthis

studystatisticallysupportG3SATRAμ’ssuperiorityoverthoseinpreviousstudies.

AccordingtothefindingsinFigure7, G3SATRAμhasagreaterMCCvaluethan

theotheravailablemethods.Thismodelcapitalizesonhigher-orderk-satisfiabilitylogic

asopposedtothemodelputforthby[26],whereonlysecond-orderlogicwasusedto

representthedataset.Throughoutthiscondition,G3SATRAμhasagreaterlogicalcapacity

toreflectthedataset’sdimensionality.Theproposedlog-linearanalysisinEquation(20)

canfilteragreaternumberofnon-significantattributesusinghighervaluesofk,which

resultsinwell-balancedTPsandTNs.ForlearningintheHNN,G3SATRAμadditionally

obtainsmorethanoneLBest ,preventingthenetworkfrombecomingoverfitwithasingle

3SAT

LInduced. Asaresult,theLBest intheG3SATRAμhasagreaterMCCvalue,preventing

3SAT 3SAT

itfrombecomingarandomclassifier. E2SATRAwasfoundtohaveseveraldrawbacks

E2SATRAuses2SATpoorcapacityinasatisfiedlogicalrule. Thelower-orderlogical

structureretrievesworseCAMthanhigher-orderlogic,whichcanminimizetheenergy

(PBest =P

induced

). L

3

In

S

d

A

u

T

cedsignificantlyachievesasmallersearchspace.Thereisahigher

chancethatonlyoneinducedlogicwasdiscoveredduringthelearningphase,whichcaused

theMCCvaluetobeclosetozero,convergingtotherandomclassifier.

Figure7.MCCoflogicminingmodels.

FromFigure8,wecanconcludethattheFriedmantestisastatisticaltestthatdoes

notrelyonspecificassumptionsaboutthedata,anditiscommonlyusedtocomparethree

ormorerelatedgroupsorconditions. Thistestispreferredwhenthedatadonotmeet

thecriterianeededforparametrictests,suchasanormaldistributionorhomogeneity

ofvariances. IntheFriedmantest,thehighestrankreferstothelogicminingmethod

withthehighestmedianrankacrossallthelogicminingincludedinthestudy,which

indicatesthatitperformedthebestorhadthemostfavorableoutcomecomparedwithall

theotherlogicminingmethodscompared.Similarly,thelowerrankingisacrucialelement

ininterpretingtheresultsoftheFriedmantestasithelpstoidentifywhichtreatmentor

conditionperformedtheworstandsuggeststhatitmayrequireimprovementorelimination

infuturestudies.

147

Mathematics2023,11,2121

Figure8.Friedmantestresultsforlogicminingmodels.

Accordingtotheresultsofthetest,theG3SATRAμmodelachievedthehighestav-

eragerankamongallthelogicminingmodelsthatwerediscussed. Thismeansthatthe

G3SATRAμmodelperformedbetterthantheothermodels. Thesecondhighestaver-

agerankamongthelogicminingmodelswasachievedbytheP2SATRAmodel. The

permutationoperatorusedintheP2SATRAmodelhadasignificantimpactonitsperfor-

manceduringthestatisticaltest. Overall,theresultsoftheFriedmantestindicatethat

theG3SATRAμmodelisthebestperforminglogicminingmodelamongthoseevaluated.

However,itisimportanttonotethatthetestonlyevaluatedaspecificsetofmodelsand

maynotnecessarilygeneralizetoothermodelsorscenarios.Incontrast,theRA(HornSAT)

achievedthelowestrankinaFriedmantestresult.Thisindicatesthatithadthelowestme-

dianrankamongalltheproposedlogicminingapproachesinthestudyandperformedthe

worstorhadtheleastfavorableoutcomeamongallthelogicminingmethodscompared.

Insummary,theproposedlogicalstructureG3SATRAμdemonstratessuperiorper-

formancecomparedwithotherlogicminingmethods,accordingtothetechnicalanalysis.

TheG3SATRAμusesalog-linearanalysistoselectthebestattributes,whichresultsin

optimalsynapticweights,leadingtohighertruepositivesandtruenegativesandlower

falsepositivesandfalsenegatives. Thedifferentperformancemetricssuchasaccuracy,

precision,sensitivity,MCC,andF1scoreshowedthattheproposedmethodoutperforms

theotherlogicalminingmethods,exceptforP2SATRAinsensitivity,whichachievedmore

truepositives.Additionally,thestatisticaltestresultsrankedtheproposedmethodasthe

bestamongtheothermethods.Thegoalofthisstudywastoassesstheeffectivenessofthe

proposedmethodrelativetootherlogicminingtechniquesusingarangeofperformance

metricsandstatisticaltests. Thisevaluationaimedtodeterminewhethertheproposed

methodperformsbetterthanothermethodsand,ifso,towhatdegree.

8.LimitationofG3SATRAμ

Theaimoflogicminingistoextractrulesandpatternsfromdatathatcanbeusedto

makepredictionsortogaininsightsintotheunderlyingstructureofthedata.However,

likeanyotherscientificmethod,logicmininghasitslimitations.Theremaybecaseswhere

thedataaretoonoisyorwherethepatternsaretoocomplexforthemethodtoeffectively

identifyusefulrules.Theremayalsobesituationswherethemethodistoocomputationally

expensiveorrequirestoomuchdatatobepractical.

148

Mathematics2023,11,2121

Therefore,inthisstudy,weaimtoexploretheselimitationsinmoredetail.Byidentify-

ingandunderstandingthelimitationsoflogicmining,wecanfindwaystoenhancethe

effectivenessoflogicminingtechniques.

(a) Onlyfocusingthelog-linearapproachonselectingsignificantattributes.Firstly,by

removinginsignificantattributesfromthedatasetbeforetranslationintohigher-order

logicalrules,thecomplexityofthelogicminingprocesscanbereduced,whichcan

leadtoafasterandmoreefficient G3SATRAμ modelinthetrainingphase. The

selectedattributethatbestrepresentsthedatasetcanimprovetheoverallaccuracy

andperformanceofthelogicminingmodelandcanreducetheriskofoverfitting,

whichcanimprovethegeneralizabilityandapplicabilityoftheG3SATRAμ.

(b) Selectingmulti-unitoptimal3-satisfiabilitylogicalrulesisdependentontheselectionof

truepositiveandtruenegativevalues.Relyingonasinglesetofvaluesfortruepositives

andtruenegativesmaynotbesufficientincapturingtheintricaciesofthedataset,thus

resultinginsuboptimalsolutions. However,usingmulti-unitoptimallogicalrulesmay

leadtoasubstantialexpansionofthesearchspaceforthediscreteHopfieldneuralnetwork,

particularlywhendealingwithhighlycomplexornoisydatasets.

(c) The multi-unit discrete Hopfield neural network may not always be effective in

learningandderivingthebestlogicfromthedataset.Theaccuracyandperformance

ofthenetworkmaybeaffectedbythequalityandquantityofthedatausedinthe

analysis.Therefore,theuseofWanAbdullah’smethodtoderivesynapticweightscan

beeffectiveforhighlycomplexornoisydatasets.Usingamulti-unitneuralnetwork,

theamountofinducedlogicthatrepresentsthebehaviorofthedatasetsincreases.

(d) Theproposedpermutationoperatorfor3-satisfiabilitylogicinadiscreteHopfield

neuralnetworkenablestheidentificationoftheoptimalattributeconfigurationfor

eachlogicalclause,whichcanleadtothegenerationofmoreaccurateandefficient

inducedlogic.Additionally,theuseofpermutationprovidesflexibilityintheiden-

tificationofthehighestperforminginducedlogicintermsofaconfusionmatrix,

whichcanimprovetheoverallaccuracyandperformanceofthemodel.Moreover,the

abilitytoidentifythehighestperforminginducedlogicthroughpermutationenables

theselectionofthemostrelevantandsignificantattributes,whichcanleadtomore

meaningfulandinterpretableresults.

9.FutureWork

Inselectinganetworkforourneeds,weoptedforDHNNoverRBFNNandothers

duetotheneedforanadditionaloptimizationlayerwhenadjustingparameters. The

RBFNNrequiresmultipletrainingphases(no-training,half-training,andfulltraining)to

evaluaterelevantparameterssuchaswidthandcenter.Evenwiththerightparameters,

thefeedforwardRBFNNonlycreatesasinglepieceofinducedlogic,whichisusuallya

simplifiedlinearclassifierwithnoutility.However,thisworkdoesnotcompareDHNN

options,suchastheonepresentedby[48].Instead,thisexperimentexaminestheimpactof

attributeselectiononlogicmining.ItisimportanttonotethatintheG3SATRAμmethod,

theinteractionindicatedbyalog-linearanalysisonlydependsontheintegrationofthe

attributesandthesolution.Themethodisbiologicallyinspiredandbasedonthepremise

thatthehumanbrainiseffectiveatremovingunwanteddetailswhentheoutcomeisvisible.

Selectingtruepositiveandtruenegativevaluesfromtheperformanceofthelogic

mininganddiscreteHopfieldneuralnetworkinvolvesexperimentingwithvariousselection

strategies,suchasusingdifferentthresholdsorweightsforeachvalueandevaluating

their impact on the quality of the induced logics and the overall performance of the

network [55,56]. Another idea could be to explore the use of other machine learning

techniquesinconjunctionwiththeproposedhybridlogicminingapproach,suchasdeep

learningorreinforcementlearning.Thiscouldinvolveinvestigatinghowthesetechniques

canbeintegratedwiththediscreteHopfieldneuralnetworktofurtherenhancetheaccuracy

andefficiencyofthelogicminingprocess,particularlywhendealingwithlargeandcomplex

datasets. Finally, other potential studies can apply the proposed hybrid logic mining

149

Mathematics2023,11,2121

methodtospecificreal-worldproblemsorapplications,suchasfrauddetectionormedical

diagnoses. Thiscouldinvolveadaptingtheapproachtothespecificrequirementsand

characteristicsoftheproblemdomainandevaluatingitsperformanceandeffectivenessin

comparisonwithexistingsolutions.

10.Conclusions

Inthispaper,weproposedanewlogicminingG3SATRAμthatutilizesseveralfresh

perspectives.First,weformulatedalog-linearapproachbyselectingsignificanthigher-order

attributeswithrespecttothefinallogicaloutcome. Usingthisapproach,wereducedthe

numberofinsignificantattributesinthedatasets. Second,anewobjectivefunctionthat

utilizesbothtruepositivesandnegativesduringthepre-processingphasewasproposed.The

newobjectivefunctionconsidersnegativeoutcomes,whichwerenotconsideredinprevious

state-of-the-artmethods. Third, thispaperproposedthefirstmulti-unitDHNNwhere

eachunitlearnsfromindividualLBest ,whichleadstodiversificationoftheinducedlogic.

3SAT

Fourth,theproposedlogicmininginthispaperutilizesapermutationoperatortoensurethe

optimalarrangementoftheattributewasusedduringthelearningphaseofaDHNN.Finally,

extensiveexperimentationusingvariousreal-lifedatasetswasperformedinG3SATRAμ

andwascomparedwithotherstate-of-the-artlogicminingmethods.Basedontheseresults,

ourproposedG3SATRAμwasobservedtooutperformthestate-of-the-artlogicmining

methodsintermsofvariousperformancemetricsandstatisticalvalidation. Ultimately,

thissignifiestherobustnessoftheG3SATRAμinextractingthemostoptimallogicalrule.

Asforfuturework,theproposedG3SATRAμcanbeimplementedusingnon-satisfiable

logicsuchasmaximumsatisfiability.Thisstudyprovidesanewperspectiveinextracting

datasetsthathavenegativeoutcomesinnature.Inaddition,metaheuristicsalgorithmssuch

asreinforcementlearningandsimulatedannealingcanbeimplementedduringthelearning

phaseofaDHNNtoensureonlythatcorrectsynapticweightsareobtained.

AuthorContributions:Conceptualization,methodology,software,writing—originaldraftprepara-

tion,G.M.;formalanalysis;S.N.F.M.A.A.;validation,N.‘A.R.;supervisionandfundingacquisition,

M.S.M.K.;writing—reviewandediting,S.A.;visualization,N.‘A.R.;projectadministration,M.A.M.

Allauthorshavereadandagreedtothepublishedversionofthemanuscript.

Funding: ThisresearchisfullyfundedandsupportedbyUniversitiSainsMalaysia,ShortTerm

Grant,304/PMATHS/6315655.

DataAvailabilityStatement:Notapplicable.

Acknowledgments:TheauthorsexpressspecialthankstoallresearchersintheArtificialIntelligence

ResearchDevelopmentGroup(AIRDG)fortheircontinuedsupport.Wealsoacknowledge“Universiti

SainsMalaysia,ShortTermGrant,304/PMATHS/6315655”forthesupportandfunding.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

References

1. Witten,I.H.;Frank,E.Datamining:PracticalmachinelearningtoolsandtechniqueswithJavaimplementations.AcmSigmodRec.

2002,31,76–77.[CrossRef]

2. Li,H.;Li,T.Areviewofdataminingtechniquesandtheirapplicationsinhealthcare.Int.J.Med.Inform.2022,158,104618.

3. Wu,X.;Zhu,X.;Wu,G.Q.;Ding,W.Dataminingwithbigdata.IEEETrans.Knowl.DataEng.2014,26,97–107.

4. Wang,X.;Yao,X.;Sun,Y.Applicationofdataminingtechniquesinthefieldofbusiness:Asystematicreview.Electron.Commer.

Res.Appl.2019,34,100827.

5. Aslani,N.;Galehdar,N.;Garavand,A.Asystematicreviewofdataminingapplicationsinkidneytransplantation.Inform.Med.

Unlock.2023,37,101165.[CrossRef]

6. DaSilveiraBarcellos,D.;deSouza,F.T.Optimizationofwaterqualitymonitoringprogramsbydatamining.WaterRes.2022,221,118805.

[CrossRef]

7. Kaur,J.;Dharni,K.Applicationandperformanceofdataminingtechniquesinstockmarket:Areview. Intell.Syst. Account.

Financ.Manag.2022,29,219–241.[CrossRef]

8. Sunhare,P.;Chowdhary,R.R.;Chattopadhyay,M.K.Internetofthingsanddatamining:Anapplicationorient-edsurvey.J.King

SaudUniv.Comput.Inf.Sci.2022,34,3569–3590.[CrossRef]

150

Mathematics2023,11,2121

9. Miao,F.;Xie,X.;Wu,Y.;Zhao,F.DataMininganddeeplearningforpredictingthedisplacementof“Step-like”landslides.Sensors

2022,22,481.[CrossRef]

10. Shafiq,D.A.;Marjani,M.;Habeeb,R.A.A.;Asirvatham,D.StudentRetentionUsingEducationalDataMiningandPredictive

Analytics:ASystematicLiteratureReview.IEEEAccess2022,10,72480–72503.[CrossRef]

11. Izonin,I.;Tkachenko,R.;Shakhovska,N.;Ilchyshyn,B.;Singh,K.K.ATwo-StepDataNormalizationApproachforImproving

ClassificationAccuracyintheMedicalDiagnosisDomain.Mathematics2022,10,1942.[CrossRef]

12. Wang,Y.;Yang,L.;Wu,J.;Song,Z.;Shi,L.MiningCampusBigData:PredictionofCareerChoiceUsingInterpretableMachine

LearningMethod.Mathematics2022,10,1289.[CrossRef]

13. Montisci,A.;Porcu,M.C.ASatelliteDataMiningApproachBasedonSelf-OrganizedMapsfortheEarlyWarn-ingofGround

SettlementsinUrbanAreas.Appl.Sci.2022,12,2679.[CrossRef]

14. Ferandez,D.M.;Cernadas,E.;Barro,S.;Amorim,D.Explainableartificialintelligence(XAI):Concepts,taxonomies,opportunities,

andchallengestowardresponsibleAI.Inf.Fusion2020,58,82–115.

15. Kumar,A.;Tanwar,S.ExplainableAIfordata-drivendecision-makinginhealthcare.J.Ambient.Intell.Humaniz.Comput.2021,

2021,1–13.

16. Hopfield,J.J.;Tank,D.W.“Neural”computationofdecisionsinoptimizationproblems.Biol.Cybern.1985,52,141–152.[CrossRef]

17. Abdullah,W.A.T.W.Logicprogrammingonaneuralnetwork.Int.J.Intell.Syst.1992,7,513–519.[CrossRef]

18. MohdKasihmuddin,M.S.;Mansor,M.A.;MdBasir,M.F.;Sathasivam,S.DiscretemutationHopfieldneuralnetworkinproposi-

tionalsatisfiability.Mathematics2019,7,1133.[CrossRef]

19. Sathasivam,S.;Mansor,M.A.;Ismail,A.I.M.;Jamaludin,S.Z.M.;Kasihmuddin,M.S.M.;Mamat,M.Novelrandomksatisfiability

fork≤2inhopfieldneuralnetwork.SainsMalays2020,49,2847–2857.[CrossRef]

20. Zamri,N.E.;Azhar,S.A.;Mansor,M.A.;Alway,A.;Kasihmuddin,M.S.M.Weightedrandomksatisfiabilityfork=1,2(r2SAT)in

discreteHopfieldneuralnetwork.Appl.SoftComput.2022,126,109312.[CrossRef]

21. Guo,Y.;Kasihmuddin,M.S.M.;Gao,Y.;Mansor,M.A.;Wahab,H.A.;Zamri,N.E.;Chen,J.YRAN2SAT:Anovelflexiblerandom

satisfiabilitylogicalruleindiscretehopfieldneuralnetwork.Adv.Eng.Softw.2022,171,103169.[CrossRef]

22. Mansor,M.A.; Kasihmuddin,M.S.M.; Sathasivam,S.ArtificialImmuneSystemParadigmintheHopfieldNetworkfor3-

SatisfiabilityProblem.PertanikaJ.Sci.Technol.2017,25,1173–1188.

23. Sathasivam,S.;WanAbdullah,W.A.T.Logicmininginneuralnetwork:Reverseanalysismethod.Computing2011,91,119–133.

[CrossRef]

24. Kho,L.C.;Kasihmuddin,M.S.M.;Mansor,M.;Sathasivam,S.LogicMininginLeagueofLegends.PertanikaJ.Sci.Technol.2020,

28,211–215.

25. Zamri,N.E.;Mansor,M.A.;MohdKasihmuddin,M.S.;Alway,A.;MohdJamaludin,S.Z.;Alzaeemi,S.A.Amazonemployees

resourcesaccessdataextractionviaclonalselectionalgorithmandlogicminingapproach.Entropy2020,22,596.[CrossRef]

26. Jamaludin,S.Z.M.;Mansor,M.A.;Baharum,A.;Kasihmuddin,M.S.M.;Wahab,H.A.;Marsani,M.F.Modified2satisfiability

reverseanalysismethodvialogicalpermutationoperator.Comput.Mater.Contin.2023,74,2853–2870.

27. MohdJamaludin,S.Z.;MohdKasihmuddin,M.S.;MdIsmail,A.I.;Mansor,M.A.;MdBasir,M.F.Energybasedlogicmining

analysiswithhopfieldneuralnetworkforrecruitmentevaluation.Entropy2020,23,40.[CrossRef]

28. Li,S.;Li,Y.;Li,R.;Li,X.;Liu,Y.Anovelhybridalgorithmforsolvinglarge-scale2-SATproblems.Appl.SoftComput.2021,100,106997.

29. Kasihmuddin,M.S.M.;Jamaludin,S.Z.M.;Mansor,M.A.;Wahab,H.A.;Ghadzi,S.M.S.Supervisedlearningperspectiveinlogic

mining.Mathematics2022,10,915.[CrossRef]

30. Jamaludin,S.Z.M.;Romli,N.A.;Kasihmuddin,M.S.M.;Baharum,A.;Mansor,M.A.;Marsani,M.F.Novellogicminingincorporat-

ingloglinearapproach.J.KingSaudUniv.Comput.Inf.Sci.2022,34,9011–9027.[CrossRef]

31. Alway,A.;Zamri,N.E.;MohdKasihmuddin,M.S.;Mansor,A.;Sathasivam,S.PalmOilTrendAnalysisviaLogicMiningwith

DiscreteHopfieldNeuralNetwork.PertanikaJ.Sci.Technol.2020,28,967–981.

32. Wu,X.;Zhang,X.;Wei,X.AdynamicHopfieldneuralnetworkforconstrainedoptimizationproblems.NeuralNetw.2017,87,43–54.

33. Cook,S.A.Shortpropositionalformulasrepresentnon-deterministiccomputations.Inf.Process.Lett.1988,26,269–270.[CrossRef]

34. Zollanvari,A.;James,A.P.;Sameni,R.Atheoreticalanalysisofthepeakingphenomenoninclassification.J.Classif.2020,37,

421–434.[CrossRef]

35. Gardini,F.;Trivisano,C.;Lanciotti,R.;Maffei,M.;Guerzoni,M.E.Suitabilityoflog-linearmodelstoevaluatethemicrobiological

qualityofbabyclams(ChameleagallinaL.)harvestedintheAdriaticSea. Int. J.FoodMicrobiol. 2000,54,63–74. [CrossRef]

[PubMed]

36. Haque,M.M.;Chin,H.C.;Debnath,A.K.Aninvestigationonmulti-vehiclemotorcyclecrashesusinglog-linearmodels.Saf.Sci.

2012,50,352–362.[CrossRef]

37. Cumming,G.Thenewstatistics:Whyandhow.Psychol.Sci.2014,25,7–29.[CrossRef]

38. Sathasivam,S.;Mamat,M.;Kasihmuddin,M.S.M.;Mansor,M.A.Metaheuristicsapproachformaximumksatisfiabilityin

restrictedneuralsymbolicintegration.PertanikaJ.Sci.Technol.2020,28,545–564.

39. Lloyd,S.LeastsquaresquantizationinPCM.IEEETrans.Inf.Theory1982,28,129–137.[CrossRef]

40. Sathasivam,S.UpgradinglogicprogramminginHopfieldnetwork.SainsMalays.2010,39,115–118.

41. Jha,K.;Saha,S.Incorporationofmultimodalmultiobjectiveoptimizationindesigningafilter-basedfeatureselectiontechnique.

Appl.SoftComput.2021,98,106823.[CrossRef]

151

Mathematics2023,11,2121

42. Ahmad,S.;Ullah,T.;Ahmad,I.;Al-Sharabi,A.;Ullah,K.;Khan,R.A.;Ali,M.A.Novelhybriddeeplearningmodelformetastatic

cancerdetection.Comput.Intell.Neurosci.2022,2020,8141530.[CrossRef][PubMed]

43. Luque,A.;Carrasco,A.;Martin,A.;Heras,A.Theimpactofclassimbalanceinclassificationperformancemetricsbasedonthe

binaryconfusionmatrix.PatternRecognit.2019,91,216–231.[CrossRef]

44. Chicco,D.;Starovoitov,V.;Jurman,G.ThebenefitsoftheMatthewscorrelationcoefficient(MCC)overthediagnosticoddsratio

(DOR)inbinaryclassificationassessment.IEEEAccess2021,9,47112–47124.[CrossRef]

45. Shi,J.;Li,Z.;Zhao,H.FeatureSelectionviaMaximizingInter-classIndependenceandMinimizingIntra-classRedundancyfor

HierarchicalClassification.Inf.Sci.2023,626,1–18.[CrossRef]

46. Shang,R.;Kong,J.;Wang,L.;Zhang,W.;Wang,C.;LiYJiao,L.Unsupervisedfeatureselectionviadiscretespectralclusteringand

featureweights.Neurocomputing2023,517,106–117.[CrossRef]

47. Wang,P.;Xue,B.;Liang,J.;Zhang,M.FeatureSelectionUsingDiversity-BasedMulti-objectiveBinaryDifferentialEvolution.Inf.

Sci.2023,626,586–606.[CrossRef]

48. Jeon,Y.;Hwang,G.FeatureselectionwithscalablevariationalgaussianprocessviasensitivityanalysisasedonL2divergence.

Neurocomputing2023,518,577–592.[CrossRef]

49. Alzaeemi,S.A.S.;Sathasivam,S.ExaminingtheforecastingmovementofpalmoilpriceusingRBFNN-2SATRAmetaheuristic

algorithmsforlogicmining.IEEEAccess2021,9,22542–22557.[CrossRef]

50. Jamaludin,S.Z.M.;Ismail,M.T.;Kasihmuddin,M.S.M.;Mansor,M.A.;Antony,S.N.F.M.A.;Makhul,A.A.Modellingbenign

ovariancystriskfactorsandsymptomsvialog-linearmodel.Pertanika2021,29,99–2216.[CrossRef]

51. Singh,N.;Singh,P.Ahybridensemble-filterwrapperfeatureselectionapproachformedicaldataclassification.Chemometr.Intell.

Lab.Syst.2021,217,104396.[CrossRef]

52. Sidik,S.S.M.;Zamri,N.E.;MohdKasihmuddin,M.S.;Wahab,H.A.;Guo,Y.;Mansor,M.A.Non-systematicweightedsatisfiability

indiscretehopfieldneuralnetworkusingbinaryartificialbeecolonyoptimization.Mathematics2022,10,1129.[CrossRef]

53. Mansor,M.A.;Sathasivam,S.Acceleratingactivationfunctionfor3-satisfiabilitylogicprogramming.Int.J.Intell.Syst.Appl.

2016,8,44–50.[CrossRef]

54. Karim,S.A.;Zamri,N.E.;Alway,A.;Kasihmuddin,M.S.M.;Ismail,A.I.M.;Mansor,M.A.;Hassan,N.F.A.Randomsat-1125

isfiability:Ahigher-orderlogicalapproachindiscreteHopfieldNeuralNetwork.IEEEAccess2021,9,50831–50845.[CrossRef]

55. Kudenko,D.;Kazakov,D.Logic-basedreinforcementlearning.Mach.Learn.2009,75,47–88.

56. Chen,J.;Chen,Y.;Hu,Y.ImproveddiscreteHopfieldneuralnetworkforsolvingoptimizationproblems.Neurocomputing2018,

312,257–267.

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

152

mathematics

Article

Securing IoT Devices Running PureOS from Ransomware

Attacks: Leveraging Hybrid Machine Learning Techniques

TariqAhamedAhanger1,*,UsmanTariq1,*,FadlDahan2,ShafiqueA.Chaudhry3andYasirMalik4

1 ManagementInformationSystemDepartment,CollegeofBusinessAdministration,

PrinceSattamBinAbdulazizUniversity,Al-Kharj16278,SaudiArabia

2 DepartmentofManagementInformationSystems,CollegeofBusinessAdministration-HawtatBaniTamim,

PrinceSattamBinAbdulazizUniversity,Al-Kharj11942,SaudiArabia;f.naji@psau.edu.sa

3 RehSchoolofBusiness,ClarksonUniversity,Potsdam,NY13699,USA;schaudhr@clarkson.edu

4 DepartmentofComputerScience,FacultyofScience,BishopsUniversity,2600RueCollege,

Sherbrooke,QCJ1M1Z7,Canada;ymalik@ubishops.ca

* Correspondence:t.ahanger@psau.edu.sa(T.A.A.);u.tariq@psau.edu.sa(U.T.);Tel.:+966-(11)-5887080(T.A.A.&U.T.)

Abstract:Internet-enabled(IoT)devicesaretypicallysmall,low-powereddevicesusedforsensing

andcomputingthatenableremotemonitoringandcontrolofvariousenvironmentsthroughthe

Internet.Despitetheirusefulnessinachievingamoreconnectedcyber-physicalworld,thesedevices

arevulnerabletoransomwareattacksduetotheirlimitedresourcesandconnectivity.Tocombatthese

threats,machinelearning(ML)canbeleveragedtoidentifyandpreventransomwareattacksonIoT

devicesbeforetheycancausesignificantdamage.Inthisresearchpaper,weexploretheuseofML

techniquestoenhanceransomwaredefenseinIoTdevicesrunningonthePureOSoperatingsystem.

Wehavedevelopedaransomwaredetectionframeworkusingmachinelearning,whichcombines

theXGBoostandElasticNetalgorithmsinahybridapproach.Thedesignandimplementationof

ourframeworkarebasedontheevaluationofvariousexistingmachinelearningtechniques.Our

approachwastestedusingadatasetofreal-worldransomwareattacksonIoTdevicesandachieved

highaccuracy(90%)andlowfalse-positiverates,demonstratingitseffectivenessindetectingand

preventingransomwareattacksonIoTdevicesrunningPureOS.

Citation:Ahanger,T.A.;Tariq,U.; Keywords:ransomwaredetection;machinelearning;malwareanalysis;featureextraction;Internet

Dahan,F.;Chaudhry,S.A.;Malik,Y. ofThings(IoT)

SecuringIoTDevicesRunning

PureOSfromRansomwareAttacks:

MSC:68M25

LeveragingHybridMachine

LearningTechniques.Mathematics

2023,11,2481. https://doi.org/

10.3390/math11112481 1.Introduction

AcademicEditor:WeiFang 1.1.BackgroundonRansomwareAttacks

TheInternetofThings(IoT)iscausingasignificanttransformationinthewaypeople

Received:17April2023

liveandwork.Theprevalenceofinternet-connecteddevicesinhouseholdsisrising,includ-

Revised:20May2023

Accepted:25May2023 ingbutnotlimitedtosmartthermostats,lightbulbs,speakers,andvirtualassistants,which

Published:28May2023 canberemotelycontrolledthroughmobiledevices.IoTdevicesareusedextensivelyacross

variousindustries,e.g.,mining,utilities,agriculture,automotive,discretemanufacturing,

etc.,tocollectdataatvariousstagesofoperationstoleverageartificialintelligence(AI)and

predictiveanalytics[1].Incorporatingthesesensorsenablesmonitoringandcontrolofa

Copyright: © 2023 by the authors. processorenvironmentinreal-time,resultinginfasterandmorerationaldecision-making.

Licensee MDPI, Basel, Switzerland. AlthoughIoTdeviceshaveimmensepotential,theirvulnerabilitytonetworkattacks

Thisarticleisanopenaccessarticle remainsasignificantconcern.Networkthreats,suchasdatatheft,phishingattempts,spoofing,

distributed under the terms and anddenialofservice,canaffectIoTdevices.Theseattackscanleadtoadditionalcybersecurity

conditionsoftheCreativeCommons risks,suchasransomware,whichcanbeincrediblyexpensiveandtime-consumingtofix

Attribution(CCBY)license(https://

forenterprises.Thenumberofransomwareattackshassurgedinrecentyears.Onenotable

creativecommons.org/licenses/by/

incidentwastheWannaCryransomwareattackin2017,whichaffectedalargenumberof

4.0/).

Mathematics2023,11,2481.https://doi.org/10.3390/math11112481 https://www.mdpi.com/journal/mathematics

153

Mathematics2023,11,2481

computersglobally,includingmanyIoTdevices[2].Anotherincidentin2019targetedasmart

buildinginFinland,whichcausedconsiderabledamage[3].In2020,aGermanhospitalwas

alsoaffectedbyransomwarethattargetedanIoTdevice,resultingintheshutdownofcritical

systems,includingemergencyservices.AreportrecentlypublishedbySonicWallhighlighted

a77%increaseinmalwareattacksonIoTdevicesduringthefirsthalfof2022[4].According

tothereport,ransomwareattackshaddecreasedby23%,whereascryptojackingattackshad

increasedby30%,andintrusionattemptshadincreasedby19%. Thesenumberspointto

thegrowingthreatofransomwareattacksonIoTdevicesandunderscoretheneedformore

robustsecuritymeasurestohandlesuchattacks.

1.2.TheNeedforEffectiveDefenseMechanismsagainstRansomwareAttacks

WeassertthatIoTdevicesrequireeffectiveprotectionmeasuresduetotheircharacter-

isticsaswellastheirapplications.Thefollowingaresomeofthereasonsthatsupportour

assertion:

(a) Duetotheircompactandlow-costformfactors,manydevicesintheIoTsufferfrom

processingpowerandmemoryconstraints. Theymaynothavetheresourcesto

runcomputer-intensivesecurityprogramsorcommunicateatahighbandwidth.

Therefore, theybecomeincreasinglysusceptibletoransomwareanomaliesasthe

numberoflinkeddevicesgrows.

(b) Becauseofalackofrobustsecuritymeasuresandstandards,manyIoTdevicesare

vulnerabletoattacks.Thisisarealconcern,especiallyforolderdevicesthatwerenot

alwaysbuiltwithsafetyinmind.

(c) Sensitiveinformation,suchasmedicalrecords,financialrecords,andpersonalprefer-

ences,isfrequentlycollectedbyIoTdevices.Thesesensors’datacouldbestolenand

utilizedfornefariouspurposesiftheywerehacked.

(d) Thehardware,software,andnetworkarchitecturethatmakeupanIoTsystemcanbe

rathercomplicated.Becauseofthiscomplexity,proactivelyspottingandpreventingran-

somwareischallenging.Duetoheterogeneousoperationalandfunctionalrequirements,

integratingIoTequipmentintoolder,lesssecuresystemsiswidespread.Therefore,it

couldbechallengingtoprotectthesesystemswithoutcausingoperationaldisruptions.

Despiteallthesechallenges,puttingsecurityfirstisessentialfortheIoTdevicesto

realizeasecureIoTparadigm.

1.3.TheRoleofMachineLearninginRansomwareDefense

Machinelearning(ML)canplayanimportantroleinransomwaredefenseinIoTby

helpingtodetectandpreventransomwareattacksbeforetheycancausesignificantdamage.

Forexample,MLalgorithmscanbetrainedtorecognizepatternsinIoTnetworktrafficthat

mayindicatethatamalwareattackispotentiallyunderway. Thiscanincludedetecting

unusualnetworkbehavior,suchasasuddensurgeintrafficoralargenumberofrequests

foraparticulartypeofdata.MLmodelscanbetrainedontheexistingattacksdataandbe

usedtopredict/identifysimilarattacksinthefuture.Severalpredictivemodelingsystems

havebeendevelopedformalwaredetectionsuchas:

(a) RandomForestalgorithmwithanensembleofdecisiontreeswasusedtoclassify

malwaresamplesin[4].

(b) SupportVectorMachine(SVM)isasupervisedlearningalgorithmthathasbeenused

forclassificationandregressionanalysis[5,6].

(c) Inprobabilitytheory,Bayes’theoremisthebasisfortheNaiveBayesalgorithmand

hasbeenusedinspamdetectiontoidentifymalware[6].

(d) Decisiontrees[7]areanotherMLtechniquethathasbeenfrequentlyemployedin

combinationwithothersupportivealgorithmsformalwaredetection.

(e) Logisticregression[8]isastatisticalmethodusedtofigureouthowlikelyabinary

outcomeistohappen.Ithasbeenusedsuccessfullyinprogramsthatlookformalware.

(f) NeuralNetworks[9]havealsobeenusedsuccessfullyinmalwaredetectionapplications.

154

Mathematics2023,11,2481

Traditionally,researchersusevariousfeaturestotrainmachinelearningmodelsto

identifythesignaturesorbehaviorsofmalware. Thesemodelsarethenusedtocreate

aframeworkthatcouldidentifyandmitigatespecificanomaliessuchasransomware.

ThefollowingaresomeofthewidelyusedfactorsthatareusedtotrainMLmodelsfor

malware-detectingsystems:

(a) Unusualorhigh-volumenetworktraffic[10],aswellastrafficfromunknownsources,

ports,orprotocols,arejustsomeoftheindicatorsthatwereuncoveredbyMLmodels

monitoringnetworkactivity.

(b) Systemcallsareusedbymalwaretocommunicatewiththeoperatingsystemand

wereatelltalesignofmalicioussoftware[11]. ModelstrainedwithMLwerevery

vigilantonsystemcallsforsignsofmaliciousactivity.

(c) Resourceuseanomalies[12]causedbymalware,suchashighcentralprocessingunit

(CPU)ormemoryusage,wereeasilydetectablebyMLmodels.

(d) Anomalousactivity,suchaschangestosystemsettings[13]oruserbehaviorthatdoes

notmakesense,mightbeatelltalesignofmalwareandwasdetectedusingMLmodels.

(e) ThesoftwareonIoTdeviceswasanalyzedbyMLmodelsforthepresenceofrecog-

nizedmalwaresignaturesordangerouspatterns.

1.4.PureOS

PureOSisanopen-sourceoperatingsystembasedontheLinuxkernelandincludes

pre-installedprivacy-enhancing tools, suchas theTor Browserandhypertexttransfer

protocolsecure(HTTPS-Everywhere)andhasstrongdefaultencryptionforuserdata.

PureOShasabuilt-infeature.“PureBoot”,thatusesa“Heads”firmwarepayloadtoenable

ausertobootthesystemfromatrustedsourceandchecktheintegrityofthesystem’s

firmwareandbootprocess.PureBootisagreatwaytoestablishaneffectivemeasurefor

preventingmalwareinstallationonadevice.

Likeanyoperatingsystem,PureOSisalsoatargetof“unpatchedsecurityflaws”,

“misconfiguredsettings”,“weakauthentication”,“socialengineeringvulnerabilities(e.g.,

fakesoftwareupdates,etc.)”,and“supply-chainattack(e.g.,insertingbackdoorsorother

maliciouscodeduringthemanufacturingordistributionprocess)”.Ultimately,anysuccess-

fulanomalousattemptcantriggeranenterprise-wideimpactthatmayreflectthehorrific

consequencesofransomware.

Themainobjectiveofthispaperistoputforwardandinvestigatesolutionstomiti-

gatetheimpactofransomwarevulnerabilitiesonIoTdevicesthatrunPureOS[14].The

followingarethemaincontributionsofthiswork:

i. Weinvestigated15,000samples(i.e.,ransomwareandbenign)instances,detailing

hithertounreportedfacetsofransomwareattackswithanemphasisonsharedtraits

amongstmalwarefamilies.

iii. Weoutlinedthedesignprocessbehindthefundamentalcomponentsofransomware

samplesanddiscussedhowthisknowledgecanbeleveragedtopreventfutureintru-

sion.Indevastatingransomwarecyberattacksofvaryingdegreesofcomplexity,our

researchdemonstratedthataberrantcontroleffortsshouldbereliablymonitored.

iii. Weproposedmethodstocounterthewidespreadthreatofdissimilarransomware

attacks. Wehavesuggestedagenericapproachtodetectingsuchrisks, onethat

makesnopresumptionsaboutthespecificmethodsthroughwhichuserrecordsare

maliciouslymadeunavailable.

Therestofthepaperisorganizedasfollows.Section2isdedicatedtopresentinga

comprehensiveliteraturereview,whileSection3delvesintotheintricatedetailsofdata

collection,augmentation,balancing,andprocessingtechniques.InSection4,wepresent

ourapproach,whileSection5expoundsuponthepracticalimplementationandrigorous

testingofourproposedransomwareanalysisandidentificationarchitecture.Ultimately,

thepaperculminatesinSection6,whereaconclusionisreached.

155

Mathematics2023,11,2481

2.LiteratureReview

TheNIST2018framework[15]proposestheadoptionofaFrameworkCoreconsisting

offivefundamentalfunctions, i.e., Identify, Protect, Detect, Respond, andRecover, to

structurecybersecurityactivitiesoptimally. Theseelementsaidorganizationsinformu-

latingtheircybersecurityriskmanagementstrategybyarrangingdata,supportingrisk

managementdecisions,reducingrisks,andenhancingperformancethroughtheintegration

ofpreviousexperiences.

OrganizationsaremandatedbytheNISTguidelinestoimplementtargetedstrategies

tocombatmalwareeffectively.Thesestrategiesencompassvariousaspects,includingthe

timelyidentificationandcharacterizationofincidents,theswiftdisseminationofpertinent

information, evaluation of actions that may hinder recovery efforts, reinforcement of

informationsharingwithinnetworkenvironments,implementationofcorrectivemeasures

topreventarecurrence,monitoringofprecursoreventsorindicatorsforfutureincident

detection,andtheacquisitionofsupplementarytoolsandresourcesforincidentdetection,

analysis, and mitigation. By proactively adopting these measures, organizations can

fortify their systems against potential threats and maintain their resilience in the face

ofcyber-attacks. Fromtheearliestextensiveanalysesofransomwarebehavior[16,17],

scholarshaveadvanceddiverseperspectivesandmultifarioustoolsandtechniquesto

detectransomwarebehavior,includingbutnotlimitedtofilesystemactivitymonitoring

andapplicationprogramminginterface(API)hooking.Itissignificanttonotethatwhile

staticanalysis,particularlysignature-baseddetection,retainsitsstatusasaconventional

methodfordetectingmalwareingeneral, itisnotaswidelyutilizedinthecontextof

ransomwaredetection.Despitemanyantivirustoolsincorporatingransomwaresignatures

intotheirdatabases,currentresearchprimarilyaccentuatesthesignificanceofbehavioral

approaches,potentiallyinresponsetotheubiquitousadoptionofransomware-as-a-service

(RaaS)andtheinclinationofransomwareauthorstoimitateoneanother,resultinginthe

emergenceofaprofusionofdissimilarandtransientvariations.

Theincreasingprevalenceofransomwareamongattackershasledtoasurgeinits

popularitywithintherealmofcybersecurityresearch.Upadhyayaetal.[18]conducteda

comprehensiveanalysisoftheanatomyandfeaturesofransomware,atypeofmalicious

softwarethatfrequentlyblocksaccesstotaskmanager, commandprompts, andother

executablefiles,renderingtheinfectedsystemunusable.Nevertheless,thepresentstudy

focusesexclusivelyonCTBLocker,aspecifictypeofransomware,andexploresitsmodus

operandiintermsofinfiltration,itsprocessofgeneratingaBitcoinwalletforeachtarget,

anditspaymentsystemfacilitatedthroughtheTornetwork.Meanwhile,certainphysicists

havesuggestedtheimplementationofquantumcryptographysystemsthatareimpervious

toloopholes,whichhavebeencomparedtoillusorymirages.Conversely,othersadvocate

takingproactivemeasuressuchassafeguardingdigitalassetsandmaintainingroutine

backupsinpreparationforanyfutureattacks.InGagneja’s[19]analysis,severalmethods

areidentifiedbywhichransomwareinfiltratesasystembyexploitingsecurityvulnera-

bilitieswithinoutdatedapplicationsonavictim’scomputer. Asaconsequenceofsuch

anattack,backupfilesanddirectoriesaredeliberatelyremovedtoobstructthesystem’s

restorationprocess,leadingtotheeventualencryptionofvitalsystemfiles.Tocounteract

thesemaliciousactivities,itwasrecommendedtoprovidecomprehensivetrainingtoper-

sonnelonallmattersrelatedtosystemsecurity,ensuringthetimelyinstallationofpatches

toaddressanypotentialsecurityweaknesses,implementingfirewallprotection,conducting

regularemailscanning,andemployingonlylicensedoperatingsystemsaspreventative

measuresagainstthepossibilityofransomwareattacks.

CeldránandMoon,intheirrespectiveworks[20,21],presentanevaluationofthe

impactofvarioustechniquessuchashash-codedstringextraction,fileformatanalysis,file

fingerprinting,packerdetection,anddisassemblyontheefficacyofstaticanddynamic

analysis.Theprimaryobjectiveofthisanalysiswastoyieldtwocriticaladvantages.The

first advantage is the safety that static analysis affords during the evaluation process,

giventhatthereisnoneedtoexecutethemalware.Secondly,themethodprovidesmore

156

Mathematics2023,11,2481

profoundinsightsintotheexecutionpathwaysofmalware,enablingamorecomprehensive

understandingofitsoperations. Furthermore,theresearchillustratedthatintherealm

ofbinaryanalysis,twoprimarymethodologiescanbeemployedformalwareanalysis:

static analysis and dynamic analysis. Static analysis involves scrutinizing the binary

withoutexecutionasapreliminarystep.Thisapproachdoesnotnecessarilynecessitatethe

utilizationofavirtualenvironmentandcanbechallengingtoutilizewithpackedbinaries

unlesstheyareunpackedmanually. However,staticanalysisiscapableofrenderingan

extensiveandall-encompassingviewofthecodecoveragewithalowfalsepositiverate.

Conversely,dynamicanalysisrequiresthebinarytobeexecutedfirstbeforebeinganalyzed.

Tostarttheanalysisprocess,avirtualenvironmentmustbeconfigured,andpackedbinaries

areautomaticallyunpacked. Whiledynamicanalysisprovidesinsightintothepathof

executionofrunningmodules,itsfalsepositiverateisnotablyhigh.

Dargahietal.[22]formulatedasystematicclassificationofthedistinguishingattributes

ofransomwarefromtheperspectiveofcybercriminalsusingtheCyberKillChain(CKC)

model.Thisworkexplorestheinterconnectednessbetweenvariousransomwarecharac-

teristicsandthedifferentstagesoftheCyberKillChain(CKC).Itfocusesonhowfactors

suchaspayloaddeliveryandaccesspreventionplayarolethroughouttheCKC,starting

fromtheweaponizationphaseandprogressinguntilthedesiredobjectivesareachieved.

AlthoughDargahietal.’sapproachisinnovative,itsscopewasnarrow.Theauthorssolely

analyzedcrypto-ransomwarethattargetsdesktopsystemsanditsmalevolentattributes,

suchasthepotentialityofbotnetdeployments. Theauthorsdidnotassesstheefficacy

orfeasibilityofalternativestrategiesnorexploremobileorIoTplatforms,whichcanbe

susceptibletoransomwareattacks.

Furthermore,itisessentialtonotethatthetaxonomyproposedbyDargahietal.[22]

isonlyoneofseveralapproachestocategorizingransomware. Otherresearchershave

proposedalternativetaxonomiesthatfocusondifferentaspectsofransomwarebehavior,

suchastheanalysisofnetworktrafficortheidentificationofransomwarefamiliesbasedon

codesimilarities.WhileDargahietal.’smethodwasvaluableinidentifyingtheobjectives

andmotivesofransomwareattackers,itdidnotprovideinsightsintothebestpracticesfor

preventingormitigatingransomwareattacks.

Table1providesacomprehensiveoverviewofdifferentransomwaredetectiontech-

niques,presentedinexistingworks,andtheirrespectivefeatures,advantages,anddisad-

vantages. Signature-basedtechniquesarewell-establishedandeffectiveagainstknown

ransomwarevariants,butcanbeineffectiveagainstneworpolymorphicvariants.Heuristic-

basedtechniquescandetectneworunknownvariants,butmayhaveahigherfalse-negative

rateandlimitedabilitytodifferentiatebetweenbenignandmaliciousactivity.Machine-

learning-basedtechniquesoffertheabilitytolearnandadapttonewvariants,butrequire

significantamountsofrepresentativedataandmayproducefalsepositives. Hybridap-

proaches provide a combination of signature and machine-learning-based techniques

forimprovedaccuracy,butcanberesource-intensive. It’simportanttonotethattheef-

fectivenessofeachtechniquemayvarydependingonthespecificimplementation,the

ransomwarebeingtargeted,andthecontextinwhichthedetectionistakingplace.

Overall,wehavereviewed298researchpapersthatweresearchedwiththekeyword

“Ransomware”onGoogleScholarthatwerepublishedfromtheyear2010toApril2023,

andwehavefoundafewissuesthathavenotbeenproperlycoveredinexistingresearch.

Thefirstissueweencounteredpertainstothewidespreadandinterchangeableusageofthe

term“ransomware”and“crypto-ransomware”,whichmayindicatealackofconsensus

amongresearchersastowhetherthesetwotermsaretechnicallyequivalentorwhether

non-crypto-ransomwarecanbeclassifiedasransomwareatall.

Anotherissueweidentifiedisthelackofauniversalstandardfordefiningbenignor

malicious(ransomware-like)behaviors.Ransomwareisatypeofmalwarethatisprimarily

designedtoextortransompaymentsfromusers, andwhileitisgenerallyagreedthat

differentvariantsofransomwaresharetwocommonfeatures,namely,blockinguseraccess

toresources(oftenfiles)andattemptingtoextortransompayments, researchershave

157

Mathematics2023,11,2481

divergentviewsonwhichadditionalfeaturesorfeaturecombinationsareindicativeof

maliciousbehavior.

Table1.Comparisonofransomwaredetectiontechniquesandtheirfeatures,advantages,andisadvantages.

DetectionTechnique Features Advantages Disadvantages

Inabilitytodetectnew,unknown

Hashvalues,filenames, Highaccuracy,lowfalse

Signature-based ransomwarevariants,ineffective

behaviorpatterns positiverate

againstpolymorphicransomware

Abilitytodetectnew,

unknownransomware Higherfalsenegativerate,limited

Behaviorpatterns,fileaccess

Heuristic-based variants,lowfalsepositive abilitytodifferentiatebetween

patterns,networktraffic

rate,effectiveagainst benignandmaliciousactivity

polymorphicransomware

Abilitytodetectnew,

Requireslarge,representative

unknownransomware

datasetsfortraining,maybe

Dynamicbehavioranalysis, variants,abilityto

susceptibletoadversarialattacks,

Machinelearning-based systemcalls,networktraffic, differentiatebetweenbenign

mayproducefalsepositives

entropy,headerinformation andmaliciousactivity,high

duetobenignsoftwarewith

accuracy,effectiveagainst

similarbehavior

polymorphicransomware

Improvedaccuracyandability

Combinationof Maybemorecomplexand

todetectnew,unknown

signature-basedand resource-intensive,may

Hybridapproach ransomwarevariants,

machine-learning-based stillmissnew,unknown

effectiveagainstpolymorphic

techniques ransomwarevariants

ransomware

Furthermore,weobservedalackofuniformusageofterminologiesinthecontextof

mitigationstrategies,whichcouldpotentiallyleadtoconfusionandmisunderstandings.

Finally,wefoundthatthereisnouniversallyacceptedstandardforevaluatingandcompar-

ingtheeffectivenessofdifferentstrategies,furtherunderscoringtheneedforadditional

researchinthisarea.

3.DataCollectionandPreparation

3.1.DataCollectionandProcessingTechniques

Inthissection,wediscussourprocedureforselectingransomwaresamples,whichplayed

avitalroleinourstudy’smalwaredatasetcollection.Toassembletheransomwaredatasets,we

utilizedthewidelyusedmalwareanalyzerAnubisandESETNOD32[23],aswellasaplethora

ofpubliclyavailablemalwarearchivesandanecdotalresearchinonlinesecurityforums.

Wecompiledandanalyzedadatasetcomprisingmorethan15,000ransomwaresamples.

Ouranalysisaimedtouncovernovelinsightsintopreviouslyundocumentedaspectsof

ransomwareattacksandidentifycommonalitiesamongdifferentmalwarefamilies.Toensure

thevalidityandprecisionofthedataset,weconductedarigorousexaminationofmultiple

factors.Theseincludedassessingthereliabilityanddiversityofthedatasources,evaluating

the size and diversity of the dataset, verifying the accuracy of pre-labeled ransomware

classifications,performingmeticulousdatapreprocessingandnormalization,ensuringthe

integrityofthedata,andconsideringthetimeframeduringwhichthedatawerecollected.The

validationprocessinvolvedmeticulouschecksforinconsistencies,errors,andbiaseswithin

thedataset.Furthermore,wecomparedourdatasetwithotherpubliclyavailabledatasetsor

groundtruthdatatofurthervalidateitsreliability.

Wehaveadoptedthedynamicanalysistechniquethatinvolvedrunningransomware

inacontrolledenvironmentsuchasasandboxandvirtualmachinetoobserveitsbehavior

andcapturerelevantdatasuchassystemcalls,networktraffic,andregistrymodifications.

Thedynamicanalysishelpedusunderstandthedissimilarcharacteristicsoftheransomware

dataset. Ransomwarecharacteristicsinclude,butarenotlimitedto,metadata,behavior

158

Mathematics2023,11,2481

logs,networktraffic,malwarelandscape,representativeness(i.e.,ransomwarefamilies,

types,andvariants),transferabilityofthreatmodels,imbalance(i.e.,datanoiseanderrors),

andtemporality(i.e.,time-periodandfrequencyofmalwaresamplecollection).

3.2.PreprocessingandFeatureEngineering

Fordatapreprocessingandfeatureengineeringofransomware,wehaveremoved

duplicateandirrelevantdata,handledmissingvalues,andscaledtheransomwarelogdata

toensurethatfeaturesarecomparable.Effectivedatapreprocessingandfeatureengineering

improvetheaccuracyofransomwaredetectionandfacilitatethedevelopmentofarobust

securityframework.Featureengineeringinvolvedtheexaminationoffilesize,filetype,

fileentropy,APIcalls,codeobfuscation,codeanalysis,sandboxanalysis,andevaluationof

digitalsignaturesiffilesaredigitallysignedbythecreatorforfeaturedetectionofmalware.

3.3.DataAugmentationandBalancingTechniques

Forransomwaredataaugmentation,weappliedtwotechniques:(a)randomnoise

(i.e.,addingrandomnoise(e.g.,irrelevantfeatures,redundantfeatures,missingcodes,and

significantlydifferentdatapoints)tothemalwaresamplestomakethemmorerobustto

variationsinthedata),and(b)randomcropping(i.e.,croppingthemalwaresamplesto

asmallersize). Thepurposeofdataaugmentationforransomwarewastoincreasethe

sizeandvariabilityofthemalwaredatasetusedtotraintheappliedmachinelearning

model.Bygeneratingnewsamplesfromtheexistingdatasetthroughdataaugmentation

techniques,wewereabletocreateamorediverseandrepresentativetrainingset,which

ledtotheproposedmethodtoimprovemodelperformanceandgeneralization.

Consequently,dataaugmentationhelpedtoaddresstheproblemofimbalanceddatasets,

wherethenumberofsamplesineachclasswasnotequal.WeemployedtheSyntheticMinority

Over-samplingTechnique(SMOTE)tobalancethedataset,bygeneratingsyntheticsamples

thatincreasedthenumberofminorityclasssamples.Thishelpedustackletheproblemof

classimbalance,wherethereweresignificantlyfewersamplesintheminorityclasscompared

tothebenignclass.SMOTEalsopreventedoverfitting,asitincreasedthesizeoftheminority

class,leadingtoabettergeneralizationofthemodeltonewdata.Consequently,SMOTEwas

instrumentalinaccuratelyclassifyingnewmalwaresamples.

Table2exhibitsthepseudocodethatoutlineshowSyntheticMinorityOver-sampling

Technique(SMOTE)canbeappliedtoidentifyransomwareinadataset.

Table2.AssessingthefeasibilityofSMOTEforransomwaredetectioninadataset.

SMOTEApplicabilitytoIdentifyRansomwareinaDataset

(1) Loadtheransomwaredataset.

(2) Splitthedatasetintotrainingandtestingsets.

(3) Determinetheminorityclass(i.e.,ransomwaresamples).

(4) ApplySMOTEtothetrainingsettogeneratesyntheticsamplesfortheminorityclass:

(a) Determinethenumberofsyntheticsamplestogeneratebasedonthedesiredratioofminoritytomajoritysamples.

(b) Selectarandomminoritysample.

(c) Identifyitsknearestneighbors.

(d) Randomlyselectoneoftheknearestneighborsanduseittocreateanewsyntheticsamplebyinterpolatingbetween

theselectedsampleanditsneighbor.

(e) Repeatstepsb–duntilthedesirednumberofsyntheticsamplesisgenerated.

(5) Combinetheoriginaltrainingsetwiththegeneratedsyntheticsamplestocreateanew,balancedtrainingset.

(6) Trainamachinelearningmodelonthenewtrainingset.

(7) Evaluatethemodel’sperformanceonthetestingset,usingmetricssuchasprecision,recall,andF1-score.

Ifthemodel’sperformanceissatisfactory,useittopredictwhethernewsamplesareransomwareornot.

159

Mathematics2023,11,2481

3.4.FocusedRansomwareVariants

Toevaluatetheeffectivenessofourproposedransomwaredetectionframeworkin

areal-worldscenario,weneededtotestitonactualransomwaresamples.However,the

ransomwarevariantswehadaccesstowerenotcompatiblewiththePureOSoperating

environment. Therefore, we re-implemented the ransomware variants to make them

suitable for the PureOS environment. This process involved analyzing the following

ransomwarecodeandmodifyingittoensurethatitcouldbeexecutedandstudiedwithin

thePureOSenvironment.

i. TheKryptik[24]ransomwareisatypeofmalwarethatisoftendisseminatedthrough

emailphishingcampaignsandexploitkits.Thisadvancedformofransomwareuses

encryptionalgorithmstolockdownthevictim’sfiles,renderingtheminaccessible.

Kryptikransomwarewasre-designedtoevadedetectionbyantivirussoftware(i.e.,

VirusChaser[25])andusescommand-and-control(C&C)serverstoobtaininstruc-

tionsfromtheattacker.Itemploysencryptionalgorithms(i.e.,RSA-2048andAES-256)

toencryptthevictim’sfiles,renderingtheminaccessible.Itutilizesobfuscationtech-

niquestoconcealitsactivities.TheimpactofKryptikransomwarecanbecatastrophic,

resultingincriticaldatalossanddisruptingbusinessoperations.

ii. Wehavere-implementedtheCloudSnooper[26]ransomwaretotargetcloud-based

systemsandservices(i.e.,Tonidocloudplatform[27]throughtheNautilusfilemanager

plugin).Itexploitedtheweaknessesincloudinfrastructuretogainunauthorizedaccess

tothevictim’snetwork. SomeofthenotablefeaturesofCloudSnooperransomware

includeitsabilitytobypassfirewallsandintrusiondetectionsystemsandencryptfiles.

Itoperatedcovertlytoevadedetectionandcausedseveredamagetothevictim(i.e.,

sandboxexperimentalsetup.TheimpactofCloudSnooperransomwarewasparticularly

devastating,asitresultedinthelossofsensitiveinformationanddisruptionofnormal

OSoperations(i.e.,encryptingorlockingfiles,modifyingsystemsettings,andinterfering

withthenormalfunctioningofapplicationsandsystemprocesses).

iii. TheWannaCry[28]ransomwarewasfirstidentifiedinMay2017. Itspreadrapidly,

infectingover230,000computersinover150countrieswithinjustafewdays.Originally,

theransomwareusedavulnerabilityinMicrosoftWindowsknownasEternalBlueto

spreadfromonecomputertoanother,makingitparticularlydangerous.Keyfeaturesof

WannaCrywereasfollows:

a. ItencryptsfilesontheinfectedsystemusingtheAESencryptionalgorithm,

makingtheminaccessibletotheuser.

b. Itcanspreadrapidlyacrossanetwork,infectingothervulnerablecomputers

withoutanyuserinteraction.

c. A“killswitch”wasbuiltintothecodeofWannaCry,allowingresearcherstohalt

thespreadoftheransomwarebyregisteringadomainnamethatthemalware

checkedbeforeencryptingfiles.

WannaCrywasalteredandreprogrammedtoaccommodatethePureOSfunctionalre-

quirementsthatwereoriginallyimplementedtospecificallytargetedsystemsrunning

MicrosoftWindowsoperatingsystems,withaparticularfocusonolder,unsupported

versionssuchasWindowsServer2003andServer2022. Theransomwarepayload

wasdeliveredasaPureOSexecutablefiledisguisedasasoftwareupdate.Oncethe

filewasexecuted,itinstalledransomwareonthesystemandbeganencryptingfiles.

WehaveusedAESencryptiontoencryptfilesontheinfectedsystem,withaunique

keygeneratedforeachsystem.There-implementedransomwarealsoencryptedthe

keyitselfusingRSAencryption,makingitintolerabletodecryptthefileswithoutthe

privatekeypresumablyheldbytheattackers.

iv. LockBit[29]isafile-encryptingransomwarethatusesacombinationofRSAand

AESencryptionalgorithmstoencryptthevictim’sfiles.Oncethefilesareencrypted,

theransomwaredisplaysaransomnote,demandingpaymentinexchangeforthe

decryptionkey.Were-designedthemalwarebygrantingittheabilitytospreadacross

160

Mathematics2023,11,2481

anetworkandinfectmultipledevicesconnectedtoit.Revisedimplementationwas

equippedwithatimerfeaturethatdeletesfilesafterasetamountoftime,whichmeans

thattheanomalymustbecounter-measuredtodiminishtheimpact.Thisransomware

waskeentotargetcriticalfiles,suchasdocuments,images,anddatabases.

v. Re-programmedBlackBasta[30]ransomwareusedAES-256encryptiontoencrypt

filesonthevictim’sPureOSmountedcomputer(i.e.,includingdesktops,laptops,and

servers).Itappendedauniqueextensiontoencryptedfiles,makingthemunusable

untiltheyaredecrypted. Theencryptionprocesstookseveralminutesorinsome

iterationsevenhours,dependingonthesizeofthefiles.

vi. Revised Hive [31] ransomware used a combination of RSA and AES encryption

algorithmstolockthevictim’sfiles(i.e.,experimentalsetup).Itenteredthesystem

throughanexploitkitandcouldspreadtootherconnecteddevicesonthesandbox

network.Theransomwarecoulderaseshadowcopiesandbackupfilestoobstructthe

victim’seffortstorecovertheirencrypteddata.

vii. ALPHV,BlackCat,andNoberus[31]arethreedistinctransomwarefamilieswith

theirownuniquefeatures,systemandnetworktargets,technicaldetails,andimpact.

Commonfeaturesincludeditsuseofdoubleextortiontactics, whichinvolvenot

onlyencryptingavictim’sfiles(i.e.,AES-256,andRSA),butalsostealingsensitive

data.Were-implementedtheseransomwarevariantsbyusingmultipletechniques

toevadedetection,includingcodeobfuscation,anti-debuggingtechniques,andpro-

cessinjection.Duringcertainexperimentaliterations,weappendedthe“.noberus”

extensiontoencryptedfiles.Wehaveobservedthatransomwaretypicallyappendsa

uniqueextensiontoencryptedfilesasawaytodifferentiatethemfromtheiroriginal

unencryptedstate.

viii. PureOS-focusedAvosLocker[32]usedstrongencryptionalgorithms(suchasAES-256

andRSA)toencryptfilesonavictim’scomputerornetwork.AvosLockertargeted

thehoneypotcomputerandnetworkthatwasvulnerabletoitsdistributionmethod

(suchasoutdatedRemoteDesktopProtocol(RDP))andcontainsvulnerabilitiesthat

canbeexploited. Intherevisedimplementation,AvosLockergeneratedaunique

encryptionkeyforeachinfectedcomputer,whichwasstoredontheattacker’s(i.e.,

anomaly)server.Theimpactofthisransomwarewassevere,asitcausedthevictimto

loseaccesstoimportantfilesanddata.

ix. TheConti[33]ransomwareisahighlyadvancedandcomplexmalwarethatusesa

sophisticatedencryptionalgorithmtoencryptfilesonavictim’scomputersystem.It

canspreadthroughanetwork,infectingotherconnectedsystems.Thevulnerabilities

thatContiexploitsinPureOSincludeexploitingweaknessesintheRDPprotocol

togainaccesstointernet-connectedsystems,exploitingvulnerabilitiesinVPNand

remoteaccesssoftwaresuchasPulseSecureVPN,FortinetVPN,andCitrixADC,and

exploitingvulnerabilitiesinwebserverssuchasApacheandNginxtogainunautho-

rizedaccesstovictims’systems. Toachieveourgoal,wehaveensuredthatConti

ransomwareusesacombinationofsymmetricandasymmetricencryptiontechniques

toencryptthefilesofitsvictims(i.e.,random256-bitChaChasymmetrickeyforeach

file’sencryptionandanasymmetricencryptionalgorithmRSAcryptographyforthe

encryptionoftheChaChakey).Furthermore,itcommunicatedwithitsC&Cserver

usinganencryptedchannel,makingitdifficulttotrackitsactivities.

x. WeimplementedREvil[34]ransomwaremorepowerfullybyusingstrongerencryp-

tionalgorithmssuchasRSA-2048andAES-256. Thisallowedtheransomwareto

encryptnotonlylocalfilesbutalsofilesonnetworksharesandmappeddrives.As

aresult,anyPureOS-basedcomputingsystem,includingtheLibremServer,work-

stations(suchastheLibrem14andLibremMini),andcellulardevices(suchasthe

Librem5)couldpotentiallybetargeted[35].Afterinfectingavictim’scomputer,the

ransomwarewasdesignedtoremaintherebycreatingascheduledtaskormodifying

theregistry.Furthermore,wemadetheransomwareevenmoremaliciousbyadding

theabilitytoexfiltratesensitivedatabeforeencryptingit.

161

Mathematics2023,11,2481

xi. WeimplementedDarkSide[35]ransomwarebyenforcingstrongencryptionalgo-

rithms,suchasRSAandAES,toencryptfilesonavictim’scomputerandprevent

themfrombeingaccessedwithoutmeetingtheadversarycriteria.Variousobfuscation

techniques(i.e.,(a)codeencryptionandobfuscation,(b)applyingthepolymorphic

code,(c)applyingthedynamicallylinkedtosystemlibraries,(d)malwarecodecom-

pression,and(e)equippingitwithananti-debuggingcapacitytodetectwhenitis

beinganalyzedordebuggedandtakesactionstoevadeordisabletheanalysis)were

introducedtoevadedetection.

xii. TheBabuk[36]ransomwarewasre-designedtouseacombinationofsymmetric

andasymmetricencryptionalgorithmstoencryptdataonthetargetsystem.Itused

aper-filerandom256-bitChaChasymmetrickeyforeachfile’sencryption,andan

asymmetricencryptionalgorithmsuchasRSAcryptographyfortheencryptionofthe

ChaChakey.Theasymmetricencryptionalgorithmisusedtosecurelytransmitthe

ChaChakeytotheransomwareoperator,allowingthemtodecryptthefiles.Babuk’s

featureallowedittostealdatafrominfectedsystems.Thesedatawerethenencrypted

andsenttotheransomwareoperator(i.e.,adversarialprocess).Itwasalsocapable

ofterminatingrunningprocesses,deletingshadowvolumecopies,anddisablingthe

PureOSSystemRestorefeature.

xiii. Tosatisfytheexperimentalrequirement,weredesignedtheEgregor[37]ransomware

thatenabledittouseamixofsymmetricandasymmetricencryptionalgorithmsto

encryptfilesonthetargetedcomputer. Theprocessinvolvedgeneratingaunique

256-bitChaChasymmetrickeyforeachfileandusingtheRSAalgorithmtoencrypt

theChaChakeyforsecuretransmissiontotheattacker(i.e.,automatedprocess),which

couldthendecryptthefiles.Moreover,theransomwarehadvariouscapabilitiessuch

asappendingarandomextensiontotheencryptedfiles,exploitingvulnerabilitiesin

RDPconnectionsandexploitkits,stealingdatafrominfectedcomputers,terminat-

ingprocesses,removingshadowvolumecopies,anddisablingthePureOSSystem

Restorefunction. Uponinfectingthecomputer, theransomwarecompressedthe

encryptedfilesintoasinglearchiveusinganencryptionandcompressiontechnique

(i.e.,“Lossless”and“Huffmancoding”[35]compression).

xiv. Theupdated/re-designedversionoftheAvaddon[37]ransomwarehadnumerous

functions,suchasemployingbothsymmetricandasymmetricencryptionmethodsto

encryptfiles.ItusedtheRSAalgorithmtoencryptfilesandusedanexclusiveAES-256

keyforeachfile,makingitchallengingtodecryptwithoutthekey.Theransomware

alsoaddedadistinctextensiontoeachencryptedfile,makingithardtorecognizeand

retrievethefiles.Moreover,themalwarewasequippedwithanextendedcapacityto

extractsensitivedatafromtheinfectedsystemandforwardittotheattackernode(i.e.,

anautomatedprocess).Itcouldterminateongoingprocessesanddeactivatevarious

operatingsystemsecurityfeatures,includingPureBoot[38].

4.AppliedMachineLearningModelsforRansomwareDefense

4.1.OverviewofDifferentMachineLearningModels

Detectingmalwareusingmachinelearningisacomplexundertakingthathasbeena

focusofresearchformanyyears.Withtheincreasingsophisticationofransomware,there

isaconstantracebetweensecurityresearchersandmalwarecreatorstostayaheadofeach

other. Thismeansthatresearchinthisfieldwillalwaysremainimportantandrelevant.

Evenifanewmachinelearningmethodisdevelopedthatiscapableofidentifyingalltypes

ofransomwares,itislikelythatmalwarecreatorswilleventuallydevelopnewtechniques

toevadedetection.Asaresult,thepursuitofimprovingmalwaredetectionmethodsisan

ongoingprocessthatrequirescontinuousinnovationandadaptationtokeepupwiththe

evolvingthreatlandscape.

OurstudyaimedtoidentifythemosteffectiveMLapproach(es)fordetectingransomware

andbenignexecutablefiles.Toachievethis,wehaveadoptedathree-stepmethodology.

162

Mathematics2023,11,2481

Firstly,weconductedathoroughreviewofstate-of-the-artmachinelearningmethods

(randomforest,supportvectormachine(SVM),decisiontree,naïveBayes,AdaBoost,etc.)

andexaminedthedatasetsanddatacollectionmethodsusedinrecentresearchtoidentify

themostpromisingtechniques.

Secondly,were-implementedandtrainedthethreemosteffectivemethodsidentified

inthefirststepusingourcollecteddataset.Byre-implementingandtrainingthesemethods,

weaimedtoassesstheirperformanceonourspecificdatasetandcomparetheiraccuracyin

detectingmalicioussoftware.

Ultimately, by using real-world samples, we evaluated the effectiveness of each

method in identifying malware and determining which approach offers the best per-

formancefordetectingmalicioussoftware.Overall,ourresearchendeavoredtocontribute

tothedevelopmentofamoreaccurateandreliableransomwaredetectionmethodthatcan

enhancecybersecurityandprotectagainstevolvingthreats.

Toaccomplishourgoalofachievingthedesiredimpact,weperformedacomparative

analysis of a hybrid-supervised learning approach in three different scenarios. These

scenariosweredesignedtorepresentdifferentlevelsofstringencywhenitcametothe

samplesconsidered.

(a) Thefirstscenariowasverystrict,andonlyaverywell-characterizedsetofsamples

wereincluded.

(b) Thesecondscenariowaslessstrictandincludedabroaderrangeofwell-studiedsamples.

(c) Thethirdscenariowasthemostrealistic,representingtheactualconditionsfacedby

vendorsofransomwaredetectionsolutions.

Bydesigningthesethreescenarios,wegainedinsightintohowtheuseofasmaller,

moredistinctdatasetcomparedtoalarger, morevariedonecanimpacttheproposed

framework. Thisanalysishelpedusunderstandtheeffectsoftheframeworkinamore

nuancedway,leadingtoabetteraccomplishmentofourgoal.Overall,ourcomparative

analysisandexperimentaloutcomeprovidedvaluableinformationthathelpedusmake

moreinformeddecisionswhenitcomestoimplementingsupervisedlearningapproaches

inreal-worldscenarios.

4.2.SelectionofAppropriateMachineLearningModels

(a) Wewantedtofindthebestmachine-learningmodelfordetectingransomware.There-

fore,wecreatedasetofcriteriaforoursearch. Thecriteriaarenotexhaustivebut

includethefollowing: theselectedmodelshouldhavehighaccuracyindetecting

ransomwareandbeabletominimizefalsepositivesandfalsenegatives.

(b) Themodelshouldbescalableandperformwellevenwhendealingwithsmallor

largedatasets.

(c) Itshouldbeabletogeneralizewelltonewandunseenransomwaresamples.

(d) Themodelshouldberobustandabletoperformwellinthepresenceofnoise,adver-

sarialattacks,andotheranomalies.

(e) Themodelshouldprovideclearandinterpretableexplanationsforitsdecisionsand

predictions.

(f) Itshouldbeefficientintermsofcomputationtime,memoryusage,andpowerconsumption.

(g) Themodelshouldbeflexibleandeasilyadaptabletochangingransomwareattack

patternswiththeabilitytoincorporatenewdata.

Wehaveexploredtherelevanceofusingregressionmodelsfordetectingransomware,

astheypossessthecapabilitytoestimatethelikelihoodofafileorbehaviorbeingmalicious.

Thisisimportant,especiallybecauseconventionaltechniquessuchassignature-based

detection may not be effective in detecting new or unknown malware variants. The

regressionmodel(XGBoost(i.e.,usefulfordealingwithlargedatasetsandisknownfor

itsspeedandscalability)[39],andElasticNet(i.e.,toachieveabalancebetweensparsity

andaccuracy))[40]wastrainedonadatasetoflabeledinstances,whereeachexample

wasafileorbehaviorthatwaseither“malicious”or“benign”.Byanalyzingthefeatures

163

Mathematics2023,11,2481

oftheseinstances,themodelcouldthenpredicttheprobabilityofanewfileorbehavior

beingmalicious.Someoftheinitialfeaturesthatwereleveragedforransomwaredetection

includedfilesizeandentropy,thepresenceofspecificstringsorsignatures,APIcallsand

theirarguments,andnetworktrafficpatterns.ItisworthnotingthatbothXGbBoostand

ElasticNetregressionhavebeenproventobeusefulinmachinelearningapplicationswhere

theinputdatahavemanyfeaturesandsomeofthemarecorrelated.Byidentifyingthekey

featuresthatareessentialforpredictingthetargetoutcome,theprocessoffeatureselection

enhancesthepracticalityoftheapplication.

ReferringtoFigure1,inthepseudocodeprovidedabove(Table3),thefunctionscol-

lect_data()andpreprocess_data(data)servethepurposesofdatacollectionanddataprepro-

cessing,respectively. Thefunctionsplit_data(preprocessed_data,test_size=0.2)splitsthe

preprocesseddataintotrainingandtestingsets,perform_elasticnet(train_data)identifiesthe

mostimportantfeaturesforpredictingransomwareusingElasticNet,andselect_features(data,

important_features)selectsonlytheimportantfeaturesfromthedata.Similarly,thefunction

train_xgboost(train_data_selected)trainstheXGBoostmodelontheselectedfeaturesand

validate_model(model,test_data_selected)validatesthemodel’sperformanceonthetesting

data.Weusedtune_hyperparameters(model,train_data_selected)tofine-tunethemodel’s

hyperparametersandevaluate_model_performance(tuned_model_performance)toobtain

theperformanceevaluationofthetunedmodel. Finally,deploy_model(tuned_model)is

usedtodeploythetunedmodelforuseinaproductionenvironment.

Table3.DetectingransomwareusingXGBoostandElasticNet.

PseudocodeforDetectingRansomwareUsingXGBoostandElasticNet

(1) Collectandpreprocessthedata:

(a) data=collect_data()

(b) preprocessed_data=preprocess_data(data)

(2) Splitthedata:

(a) train_data,test_data=split_data(preprocessed_data,test_size=0.2)

(3) Featureselection:

(a) important_features=perform_elasticnet(train_data)

(b) train_data_selected=select_features(train_data,important_features)

(c) test_data_selected=select_features(test_data,important_features)

(4) Trainthemodel:

(a) model=train_hybrid_xgboost_elasticnet(train_data_selected)

(b) model_performance=validate_model(model,test_data_selected)

(5) Tunethemodel:

(a) tuned_model=tune_hyperparameters(model,train_data_selected)

(b) tuned_model_performance=validate_model(tuned_model,test_data_selected)

(6) Evaluatethemodel:

(a) evaluate_model_performance(tuned_model_performance)

(7) Deploythemodel:

(a) deploy_model(tuned_model)

Thus,detectingransomwareusingXGBoostinvolvedtrainingamachinelearning

modelusingfeaturesthathelpedtodistinguishbetweennormalandransomwarebehavior.

Datarelatedto“fileaccesspatterns”wasformulatedas:

XGBoost(Ransomware + ) w = 3 w ∗ 1 n ∗ um nu _ m of _ _ o fi f l _ es fi _ le r s e _ n c a r m ea e t d ed + + w w 4 ∗ 2 ∗ nu n m um _o _ f o _ f fi _ l fi e l s e _ s r _ e d a e d le + ted b (1)

wherew1,w2,w3,andw4aretheweightsassignedtothenumberoffilescreated,deleted,

renamed,andread,respectively,and“b”isthebiasterm.

164

Mathematics2023,11,2481

Datarelatedto“networktrafficpatterns”wasformulatedas:

XGBoost(Ransomware)=w1 ∗num_of_outgoing_connections+w2 ∗

num_of_incoming_connections+w3 ∗num_of_data_packets_sent+w4 ∗ (2)

num_of_data_packets_received+b

wherew1,w2,w3,andw4aretheweightsassignedtothenumberofoutgoingconnections,

incomingconnections,datapacketssent,anddatapacketsreceived,respectively,andbis

thebiasterm.Datarelatedto“systemcallpatterns”wasformulatedas:

XGBoost(Ransomware) n = um w _ 1 o ∗ f_ n s u u m sp _ i o ci f o _ u s s y _ s s te y m st _ em ca _ ll c s a + lls w + 2 ∗ b (3)

wherew1andw2aretheweightsassignedtothetotalnumberofsystemcallsandsuspicious

systemcalls,respectively,andbisthebiasterm.

Figure1.FlowdiagramofransomwaredetectioncriteriausingXGBoostandElasticNet.

165

Mathematics2023,11,2481

TheexperimentwasrevisedwithauniquedatasetusingElasticNetmethodologyby

followingconventionalsteps(i.e.,collectionofanindicativedataset,processingthedatafor

featurenormalization,splittingdataintotrainingandtestingsets,trainingtheMLmodel,

andtestingthemodelusingametricsuchasaccuracy,precision,orrecall.

ElasticNetlossfunctionwasevaluatedas:

(cid:2) (cid:2) (cid:3) (cid:3)

min 1/ 2∗n ||y−Xw||2+alpha∗l4 ∗||w|+0.5∗alpha∗(1−l4 )∗||w||2 (4)

samples 2 ratio ratio 2

where

i. “n_samples”isthenumberofsamplesinthedataset.

ii. “y”isthetargetvariableinthedataset.

iii. “X”isthematrixoffeaturesinthedataset.

iv. “W”isthevectorofcoefficientsthatarelearnedbythemodel.

v. “14_ratio”isahyperparameterthatcontrolsthebalancebetweenpurportedlyL1and

L2regularization.Asasserted,theL1regularizationpromotessparsityinthelearned

coefficients,whileL2regularizationpromotessmall,non-zerocoefficients.

vi. “Alpha”isahyperparameterthatcontrolsthestrengthoftheregularization.Higher

valuesofalphaleadtomoreregularization.

Inthisscenario,theElasticNetlossfunctionisreferredtoasacombinationofL1and

L2regularization.TheL1regularizationtermisgivenby alpha∗l4

ratio

∗||w|| 1,whichisthe

sumoftheabsolutevaluesofthecoefficientsmultipliedbyascal(cid:30)ingfactoralpha∗l4_ratio.

TheL2regularizationtermisgivenby0.5∗alpha∗(1−l4

ratio

)∗(cid:30)|w||2

2

,whichisthesumof

thesquaresofthecoefficientsmultipliedbyascalingfactor0.5∗alpha∗(1−l4 ).The

ratio

L1scalingfactorsaredesignedtobalancethestrengthofthetworegularizationterms.

4.3.FeatureSelectionandModelTuning

Todevelopeffectiveransomwaredetectionmethods,itwasnecessarytoextractrel-

evantfeaturesfromtheransomware. Thisprocessinvolvedcloselyanalyzingtheran-

somware’scodeandbehaviortoidentifyspecificcharacteristicsorpatternsthatcandis-

tinguishitfromothertypesofmalwares.Reimplementedransomwarepossessesdistinct

featuresthatareusefulinidentifyinganddetectingthem. Thesefeaturesareuniqueto

ransomwareandcandifferentiateitfromothertypesofmalwares.Someoftheessential

ransomwarefeaturesinclude,butarenotlimitedto:

i. Atypicalnetworkactivitythatisnottypicalforthesystem.

ii. Alterationstofileextensionsarenottypicalforthesystem.

iii. Suspiciousprocesseswithnamesthatarerandomorlocatedinunusualdirectories.

iv. Changestotheregistry.

v. UnusualCPUordiskusagethatisnottypicalforthesystem.

vi. Pop-upmessagesorwarnings.

vii. Atypicalsystemcrashesorerrors.

viii. Encryptionkeygenerationbymalware.

ix. Usageofnon-standardencryptionalgorithms.

x. Unusualbehavior,suchasmodificationoffiletimestampsorthecreationofdecoy

filestodeceivethevictim.

xi. Atypicalfileaccesspatternsthatarenottypicalforthesystem.

xii. Largenumbersoffiledeletions.

xiii. Changestofilepermissionsthatarenottypicalforthesystem.

xiv. Randomfilenamesonlargefiledatasets,allatonce.

xv. Largenumbersoffailedloginattempts.

xvi. Unusualfilesizesthatarenottypicalforthesystem.

Oncetherelevantfeatureswereextracted,theywereusedtotrainthemachinelearning

modelfordetectingandclassifyingransomwareinreal-worldscenarios.Thisapproach

allowedformoreeffectiveransomwaredetection,asitleveragestheuniquecharacteristics

ofransomwaretoidentifyandmitigatethreats. Furthermore,bycontinuallyupdating

166

Mathematics2023,11,2481

thefeatureextractionprocess,thedetectionmodelwasadaptedtotheevolvingthreat

landscapeofransomwareattacks.

4.4.EvaluationofModelPerformance

ToevaluatetheperformanceofourmodelfordetectingransomwareusingXGBoostand

ElasticNet,weusedwell-knownMLmodelevaluationmetrics,i.e.,accuracy,precision,recall,

andF1-score.Thefollowingsarethemainstepsperformedfortheperformanceevaluation:

1. Splitthedataintotrainingandtestingsets.

2. PerformfeatureselectionusingElasticNettoidentifythemostimportantfeaturesfor

predictingransomware.

3. TrainanXGBoostmodelontheselectedfeaturesusingthetrainingset.

4. Predictthelabelsofthetestsetusingthetrainedmodel.

5. Evaluatetheperformanceofthemodel.

Table4depictsthemodelcodeinwhichXandyarethefeaturesandlabelsofthe

data,respectively.train_test_split()wasusedtosplitthedataintotrainingandtestingsets.

perform_elasticnet()identifiestheimportantfeaturesusingElasticNet.select_features()

selectstheimportantfeaturesfromthedata.train_xgboost()trainstheXGBoostmodelon

theselectedfeatures.predict()predictsthelabelsofthetestset.Ultimately,theevaluation

metricsarecomputedusingtheappropriatefunctionsfromscikit-learn(accuracy_score(),

precision_score(),recall_score().Itisworthhighlightingthattheimportanceofemploying

parameterstest_sizeandrandom_stateisasfollows:

i. Thetest_sizeparameterspecifiestheproportionofthedatathatwillbeusedfortesting,

whiletheremainingdataareusedfortraining.Forexample,atest_sizeof0.2meansthat

20%ofthedatawillbeusedfortesting,and80%willbeusedfortraining.

ii. Therandom_stateparameterisusedtosettheseedfortherandomnumbergenerator,

whichensuresthattheresultsarereproducible.Thisisimportantbecausetherandom

samplingofdatafortrainingandtestingcanaffecttheperformancemetricsofthe

model.Bysettingtherandom_stateparametertoaspecificvalue,thesamerandom

samplingwilloccureverytimethecodeisrun,ensuringthattheresultsareconsistent

andreproducible.

Table4.Algorithmicoutlineforassessingmodelperformance.

PseudocodeforEvaluatingthePerformanceoftheModel

#Splitthedataintotrainingandtestingsets

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#PerformfeatureselectionusingElasticNet

important_features=perform_elasticnet(X_train,y_train)

#Selecttheimportantfeatures

X_train_selected=select_features(X_train,important_features)

X_test_selected=select_features(X_test,important_features)

#TrainanXGBoostmodelontheselectedfeatures

model=train_xgboost(X_train_selected,y_train)

#Predictthelabelsofthetestset

y_pred=model.predict(X_test_selected)

#Computetheevaluationmetrics

accuracy=accuracy_score(y_test,y_pred)

precision=precision_score(y_test,y_pred)

recall=recall_score(y_test,y_pred)

f1=f1_score(y_test,y_pred)

167

Mathematics2023,11,2481

Tocomputetheaccuracy,precision,recall,andF1-scorefordetectingransomware

usingXGBoostandElasticNet,itwasnecessarytoobtainasetoftruepositive(TP),true

negative(TN),falsepositive(FP),andfalsenegative(FN)valuesfortheproposedmodel.

These values were obtained by comparing the predictions made by the XGBoost and

ElasticNetmodelstotheactuallabelsofthedata.

OncethemodelhadtheTP,TN,FP,andFNvalues,itcalculatedthefollowingmetrics:

Accuracy=(TP+TN)/(TP+TN+FP+FN).:Theproportionofcorrectly

(5)

classifiedinstancesamonginstances.

Precision=TP/(TP+FP).:Theproportionofcorrectlyidentifiedpositiveinstances

(6)

amongallpositiveinstances.

Recall=TP/(TP+FP).:Theproportionofcorrectlyidentifiedpositiveinstances

(7)

amongallactualpositiveinstances.

F1-score=2∗(Precision∗Recall)/(Precision+Recall).:Theharmonicmeans

(8)

ofprecisionandrecall,whichgivesabalancedmeasureofbothmetrics.

Table5presentstheperformanceoftheransomwaredetectionmodelinaccurately

identifyingdistincttypesofransomware. Thetablealsoshowsthemodel’sabilityto

minimizefalsepositivesandfalsenegatives.Falsepositivesrefertocaseswhenthemodel

indicatesthatasystemorfilehasransomware,wheninfactitdoesnot,whilefalsenegatives

occurwhenthemodelfailstodetectthepresenceofransomwarethatisthere.Byproviding

thisinformation,thedatasetenabledustoassessthemodel’sabilitytoaccuratelyidentify

diversetypesofransomwares.Furthermore,thedatasetincludeskeyperformancemetrics

suchasAccuracy,Precision,Recall,andF-Score,whichwerefrequentlyemployedtogauge

theeffectivenessofthemodel.Thesemetricsenabledustocomparetheeffectivenessof

variousransomwaredetectionvariablesintermsoftheiraccuracyinidentifyingdifferent

typesofransomwarewhileminimizingthenumberoffalsepositivesandfalsenegatives.

Table5.Testingtheproposedmethodonalimiteddatasetofransomwareanomaliestodetermineits

averageperformance.

Ransomware False/Positive False/Negative Accuracy Precision Recall F-Score

Kryptik 3.21 1.95 85 0.823 0.853 0.869

CloudSnooper 1.67 2.84 92 0.882 0.830 0.863

WannaCry 0.95 2.18 81 0.854 0.818 0.861

LockBit 3.53 3.34 88 0.801 0.846 0.832

BlackBasta 2.47 1.17 84 0.888 0.839 0.854

RevisedHive 1.92 2.53 89 0.820 0.817 0.829

ALPHV/BlackCat/Noberus 2.99 2.28 95 0.847 0.856 0.844

AvosLocker 1.42 1.11 83 0.897 0.824 0.819

Conti 3.76 3.89 87 0.876 0.811 0.876

REvil 1.08 3.48 80 0.815 0.857 0.877

DarkSide 2.27 1.73 91 0.809 0.814 0.816

Babuk 0.85 3.29 94 0.865 0.847 0.823

Egregor 3.94 3.747 82 0.839 0.819 0.881

Avaddon 2.04 1.09 90 0.896 0.862 0.858

168

Mathematics2023,11,2481

Theeffectivenessofourfeatureselectioncriteriawasevaluatedbycomparinginfor-

mationgainandchi-squaremethodsusingtheNaïveBayesclassifier.Thefeaturesetswere

createdusing28,56,84,122,and140features. Table6presentsthesimilaritiesbetween

thetwoapproachesandtheirclassificationperformanceusingfourmetrics:TruePositive,

FalsePositive,Precision,andF-Score.TheBayesianpredictorwithattributesselectedvia

informationgainandchi-squaretechniqueswasusedtogeneratetheresultsofthedetection

process.Theresultsindicatedapositivecorrelationbetweenthenumberoffeaturesused

andanomalydetectioninbothmethods,suggestingthataccuracyimprovedwhenthe

featureswereoptimized.

Table6.Thelevelofaccuracyachievedbythehybrid“XGBoostandElasticNet”methodindetecting

aspecificransomwarevariant.

FeatureOptimization AppliedFeatureCount TPRate(%) FPRate Precision F-Score

140 82.96 2.74 0.928 0.844

112 86.02 2.12 0.867 0.804

InformationGain 84 81.75 3.14 0.923 0.823

56 85.14 2.58 0.849 0.862

28 83 1.98 0.882 0.818

140 91.94 2.54 0.798 0.844

112 92.13 3.10 0.826 0.804

Chi-Square 84 91.56 2.28 0.771 0.823

56 92.01 3.30 0.793 0.862

28 92.32 1.99 0.810 0.818

WehavealsousedInformationGainasametrictomeasuretheusefulnessofafeature

insplittingthedataintodifferentclasses.Itcalculatedthereductioninentropyachieved

bysplittingthedataonaparticularfeature. ThehighertheInformationGain,themore

usefulthefeatureisintheclassificationprocess.Similarly,Chi-Squareisusedtodetermine

whethertherewasasignificantassociationbetweentwocategoricalvariables.Inthecontext

offeatureselection,Chi-Squarewasemployedtoidentifyfeaturesthatweresignificantly

associatedwiththetargetvariable.ThehighertheChi-Squarescore,themoresignificant

theassociationbetweenthefeatureandthetargetvariable.

Tousethesemetricstodetectransomware,weselectedthefeatureswiththehighest

InformationGainorChi-Squarescoreandusedthemtotraintheprojectedmodel. The

selected features were able to distinguish between ransomware and non-ransomware

sampleswithhighaccuracy. Furthermore, toselectthebestfeaturecountandmetric

fordetectingransomware,wecomparedtheTPrate,FPrate,Precision,andF-Scorefor

eachcombinationoffeaturecountandmetric. Weplottedtheresultstovisualizethe

performanceofeachcombination.

WehaveformulatedInformationGainas:

InformationGain=Entropy(S)−∑ [p(v)×Entropy(Sv)] (9)

where,

• Sistheoriginaldataset.

• visaspecificvalueofthefeaturebeingconsidered.

• p(v)istheproportionofthenumberofelementsinSthathavethevaluevtothe

numberofelementsinS.

• SvisthesubsetofSwherethefeaturehasthevaluev.

169

Mathematics2023,11,2481

• Entropy(S)istheentropyoftheoriginaldatasetS.

• Entropy(Sv)istheentropyofthesubsetSv.

TheentropyEntropy(S)fortheoriginaldatasetSiscalculatedusingthefollowingprinciple:

Entropy(S)=−∑ [p(c)×log2(p(c))]. (10)

wherecisaclasslabelinS,andp(c)istheproportionofthenumberofelementsinSthat

belongtoclassctothenumberofelementsinS.Thisformulagivestheentropyofthe

originaldatasetSbasedontheclasslabelsinthedataset.

OncetheentropyoftheoriginaldatasetSiscalculated,wethenusedtheformulafor

informationgaintodeterminetheimportanceofeachfeatureinS.Theinformationgain

measuresthereductioninentropyachievedbysplittingthedatabasedonaparticularfeature.

ToestimatetheChi-Square,thefollowingformulawasemployed:

χ2= ∑ [(O−E)2/E] (11)

where,

• Oistheobservedfrequencyforagivenfeatureandthepresenceofransomware.

• Eistheexpectedfrequencyforthesamefeatureandransomwarepresence.

• ∑isthesummationoverallpossiblevaluesofthefeatureandransomwarepresence.

Theexpectedfrequencywascalculatedbasedontheassumptionthatthefeatureand

thepresenceofransomwarewereindependent. Iftheobservedfrequencysignificantly

differsfromtheexpectedfrequency,itsuggeststhattherewasacorrelationbetweenthe

featureandthepresenceofransomware. Intheproposedransomwaredetection,Chi-

Squarewasusedtoidentifyfeaturesthataresignificantlycorrelatedwithransomware.

Thesefeatureswerethenusedasinputfortheappliedmachinelearningmodel(i.e.,hybrid

XGBoostandElasticNet)todetectransomware.

5.ImplementationandTesting

Ourmodelwastrainedusingdifferentconfigurations:

1. ThefirstoneinvolvedaLibrem14laptopequippedwithanIntelCorei710710Uprocessor

with6coresand12threads,DDR4RAMof64GB,IntelUHDGraphics620GPU,M.2SSD

storageof2TB(NVMe),PureBootfirmware,andaPureOSoperatingsystem.

2. ThesecondconfigurationusedaLibrem5smartphone,whichhadanNXP®i.MX8M

QuadcoreCortexA53processorwith64-bitARMarchitecturerunningatamaximumof

1.5GHz(alongwithanauxiliaryCortexM4),VivanteGC7000LiteGPU,3GBofRAM,

32GBeMMCinternalstorage,andaPureOSoperatingsystem.

Themodelwastrainedwith15,000instancesobtainedfromanexperimentalsetup.The

datasetcomprised27%legitimateinstances,15%cryptominers,13%memorydumps,4%

RAT-ratedfiles,and41%ransomwaresamples,whichwerecustomizedversionsofKryp-

tik,CloudSnooper,WannaCry,LockBit,BlackBasta,Hive,ALPHV/BlackCat/Noberus,

AvosLocker,Conti,REvil,DarkSide,Babuk,andAvaddon.Thedatawereupdatedasof23

March2023.WeutilizedasimulationmodelintheVMwareNSXsandbox[41]togenerate

ransomwaresamplestrings.ByemployingFull-systemMirroringalongsideNSXSandbox,

weensuredprecisedetectioncapabilities.Togainadeeperunderstandingofthesandbox’s

configurations, weadditionallyexecutedourscriptintheCuckooSandbox[42]. This

allowedustoobservethebehaviorofthefilewithinapracticalandisolatedenvironment.

Thedecisionwasmadetotrusttheactualbehaviorofthefiles,monitoredbythesandbox,

allowingustoidentifyspecificfeaturesextractedthroughthesandbox’smonitoring.

Toidentifythenecessaryprerequisitesforaspecificaction,weemployedtwoseparate

testing environments. The feature set comprised 140 characteristics, with 30 of them

consistingofcallstoAPIpackagesthatencompassedallPureOSapplicationprogramming

interfaces. Anoutlineoftheransomwareversionsemployedintheevaluationstageis

providedinTable7.

170

Mathematics2023,11,2481

Table7.Ahigh-levelviewoftheanalyzedransomwarevariants.

Ransomware Encoding Lock RemoteAccessTrojan SampleSize(%)

Kryptik (cid:3) (cid:3) (cid:3) 4

CloudSnooper (cid:3) (cid:3) (cid:3) 9

WannaCry (cid:3) - - 7

LockBit (cid:3) (cid:3) - 5

BlackBasta (cid:3) - - 11

RevisedHive (cid:3) (cid:3) - 8

ALPHV/BlackCat/Noberus (cid:3) - - 10

AvosLocker (cid:3) (cid:3) (cid:3) 6

Conti (cid:3) - (cid:3) 12

REvil (cid:3) - (cid:3) 3

DarkSide (cid:3) - (cid:3) 8

Babuk (cid:3) (cid:3) - 2

Egregor (cid:3) (cid:3) (cid:3) 9

Avaddon (cid:3) (cid:3) - 6

Cuckoosandboxwascapableofanalyzingawiderangeoffileextensionsincluding

.js,.hta,.psi,.pdf,.ppt,.ps1,.python,.vbs,.zip,etc.Furthermore,applets,classes(e.g.,bin,

cpl,dll,etc.),functions(e.g.,DllMain,arguments,loader,etc.),dumps(e.g.,memory.dump,

dump.pcap,tlsmaster.txt,andfiles.jsonformetadataextraction),.bson,shots,andmore

werealsoexamined.

TheAPIsthatwereusedtofacilitateortriggerransomwareoperationsincludeda

varietyoftypesfromvariouscategories.Theseinclude,butarenotlimitedto,ShellExe-

cute,CreateProcess,WriteProcessMemory,VirtualAllocEx,RegOpenKey,RegCreateKey,

RegSetValue,HttpSendRequest,andLoadLibrary.TheseAPIsbelongtoarangeofdifferent

categoriessuchassystemcalls,networking,input/output,filesystem,cryptography,and

userinterface.ItisimportanttonotethattheseAPIswereutilizedmaliciouslybythreat

actors(i.e.,pre-fabricatedanomalies)tocarryoutransomwareattacks.

Theransomwareweusedforencryptingthedata(i.e.,filesofvaryingsizesranging

from100KBto1GB)onthehackedsystememployedRSA-2048,AES-256,andChaCha-256

encryptionalgorithms.Wecarriedoutathoroughinvestigationofthetimetakenbythese

algorithmsandfoundthattheChaCha-256hadthefastestencryptionspeedamongthe

three,makingitamoreefficientoptionforuseinransomwareattacks. Thetime-based

encryptioncomparisonisshowninFigure2andcanbesummarizedas:

(a) RansomwareattackersareusingadvancedencryptionalgorithmssuchasRSA-2048,

AES-256,andChaCha-256toencryptvictimdata,makingitinaccessiblewithoutthe

decryptionkey.

(b) Thespeedatwhichencryptionalgorithmsoperatecanimpactthesuccessofaran-

somwareattack.Inthiscase,ChaCha-256wasfoundtobethefastestamongthethree

encryptionalgorithms,makingitapotentiallymoreeffectivechoiceforattackers.

(c) Asaresultofthefasterencryptionspeed,ChaCha-256maybecomemoreprevalentin

futureransomwareattacks.

171

Mathematics2023,11,2481

Figure2.TheuseofRSA-2048,AES-256,andChaCha-256fortime-basedencryptioncomparisons.

Figure3showstheeffectofselectingasubsetoffeaturesfromadatasetofransomware

characteristicsbasedontheirvariance. Thevariancethresholdisavaluethatissetto

determinetheminimumvarianceafeaturemusthavetobeincludedinthesubset.During

theoptimizationprocess,wenoticedthatbyvaryingthevariancethreshold,itispossibleto

selectdifferentnumbersoffeaturesforthesubset.Bysettingavariancethresholdforeach

feature,onlythosethatsignificantlydifferacrossthedatasetwillbeincludedinthesubset.

Ifthevariancethresholdissethigh,onlyfeatureswithhighvarianceareincludedinthe

subset,leadingtoasmallernumberofransomwarefeatures. Incontrast,ifthevariance

thresholdissetlow,morefeatureswithlowervarianceareincluded,resultinginalarger

numberofransomwarefeatures.

Itisimportanttonotethatthenumberofransomwarefeaturesselectedforthesubset

canhaveasignificantimpactontheperformanceofappliedmachinelearningmodels(i.e.,

XGBoostandElasticNet).Therefore,selectingtheoptimalnumberofransomwarefeatures

withvaryingvariancethresholdsisacrucialstepindevelopingeffectiveransomware

detectionandpreventionsystems.

Thestudyconductedtestsontheentiredataset,usingacross-validationtechniquethat

involved25folds,andsplittingthedataintotrainingandtestingsubsetsrandomly,with

60%ofthedatausedfortrainingand40%fortesting.Table8presentstheperformanceof

sixdifferentmachinelearningalgorithmsindetectingandpreventingransomwareattacks.

Themetrics(i.e., accuracy, precision, recall, andF-score)wereevaluatedusingbotha

25-foldcross-validationtechniqueanda60%splittraining/testsetapproach.Theproposed

algorithm,thehybridXGBoostandElasticNet,hasthehighestroutineacrossevaluation

techniques,indicatingthatitoutperformstheotheralgorithms.Theresultshighlightthe

potentialofmachinelearningalgorithmsindetectingandpreventingransomwareattacks

andprovideinsightsintowhichalgorithmsperformbetterinthiscontext.

172

Mathematics2023,11,2481

Figure3.Dimensionalityinthenumberofcharacteristicswithvariousthresholdsforvariance.

Table8.TheoutcomesoftheAccuracy,Precession,Recall,andF-Score.

Accuracy Precession Recall F-Score

Sr# MLAlgorithm

25Folds 60%Split 25Folds 60%Split 25Folds 60%Split 25Folds 60%Split

Reinforcement

learning(Markovic

1 0.867 0.865 0.867 0.865 0.845 0.842 0.874 0.872

DecisionProcess+

Q-Learning)[43]

K-NearestNeighbors

2 0.872 0.870 0.872 0.871 0.855 0.853 0.880 0.882

Algorithm[44]

SupportVector

3 0.845 0.846 0.846 0.842 0.803 0.806 0.845 0.842

Machine[45]

StochasticGradient

4 0.811 0.816 0.813 0.817 0.733 0.725 0.804 0.818

Descent[46]

5 NaiveBayes[44] 0.512 0.532 0.672 0.666 0.551 0.533 0.865 0.847

HybridXGBoostand

6 0.901 0.907 0.921 0.917 0.920 0.933 0.921 0.927

ElasticNet

Limitations

Theproposedresearchhasprimarilyfocusedonexploringtherobustnessofclassifiers

thatsolelyexaminethestructureofbinaryprograms(i.e., ofbenignandransomware

samples).However,themethods(i.e.,hybridXGBoostandElasticNet)wehaveapplied

would not affect classifiers that consider the execution of such programs, and extract

featuressuchasthesequenceofsystemcalls. Thereasonforthislimitationisthatthe

dataweintroduceandmodifyarenotexecutedduringtheprogramruntime. Todeal

withactivefeatures,anattackerwouldhavetoresorttousingbinaryrewritingtechniques,

whicharepracticalmodificationsspecificallydesignedforthispurpose.Thesealterations

involvemanipulatingtheprogram’sanomalouscodebyaddingnewbranchesorreplacing

semanticallyequivalentinstructions,whichcanbeusedtoencoderansomwareinaway

thathasbroadapplicability.

173

Mathematics2023,11,2481

6.ConclusionsandFutureWork

Itcanbeassertedwithahighdegreeofcertaintythatmachinelearningalgorithms

haveproventobeefficacioustoolsinidentifyinganddetectingmalicioussoftware.How-

ever,designingsuchsystemsisoftendifficultbecausetheyinvolvecomplexfeaturesthat

canmakeithardtounderstandhowthemodelslearnandaccuratelyidentifythereal

characteristicsofmalware.Consequently,systemsthathavetheseweaknessescanuninten-

tionallyincorporatefalsepatterns,whichmaymakethemmorevulnerabletoattacksfrom

maliciousactors.

ThefocalpointofthisarticleisthedetectionofPureOS-specificransomware,aperni-

ciousandinsidiousthreatthathasproliferatedwithunprecedentedvelocityinrecentyears.

Weconductedacomprehensiveexaminationoftheefficacyofvarioussinglefeaturetype

setsinidentifyingthistypeofransomware,whilealsoconsideringthecustomarytactics

employedbymalevolentactorstocamouflagetheirnefariousactivities.

Tofurtherrefineandoptimizethesetechniques,weexploitedhybridmachinelearning

methodologies,suchasXGBoostandElasticNet,toscrutinizeandassessthestrengthand

validityofthedevelopedsystems.Theultimategoalwastoproposeeffectivemethodolo-

giesforthejudiciousimplementationofthesetechniques.Accordingly,experimentalwork

wasconductedtoevaluatethepotentialimpactofthesemethodologiesonthedetectionof

ransomwareandtoenhancethedesignprocessofhybridmachine-learning-basedsystems.

Itisclearfromtheresultsthatourapproachperformsexceptionallywellindetecting

ransomwarepatternswithhighaccuracyandalowfalse-negativerate.Thisworkshows

thatMLtechniquescanbeusedtosignificantlyimprovetheeffectivenessandefficiencyof

cybersecuritydefensesagainstransomwareattacks.

Weassertthatcombiningmultiplemachinelearningmodelscanimprovetheoverall

detectionaccuracyandreducefalsepositives.Thisworkmightprovideaboosttoensemble

learningtechniques,especiallyintheareaofcybersecurity.

AuthorContributions: Conceptualization,U.T.andT.A.A.; methodology,F.D.,U.T.andS.A.C.;

software,U.T.andY.M.;validation,U.T.andT.A.A.;formalanalysis,U.T.;investigation,S.A.C.and

U.T.;resources,U.T.andT.A.A.;datacuration,Y.M.andU.T.;writing—originaldraftpreparation,

T.A.A.,U.T.andF.D.;writing—reviewandediting,Y.M.,U.T.andS.A.C..;visualization,Y.M.and

U.T.;supervision,T.A.A.;projectadministration,S.A.C.andY.M.;fundingacquisition,S.A.C.All

authorshavereadandagreedtothepublishedversionofthemanuscript.

Funding: TheauthorsextendtheirappreciationtotheDeputyshipforResearchandInnovation,

MinistryofEducationinSaudiArabiaforfundingthisresearchworkthroughprojectnumber

2022/01/22636.

InstitutionalReviewBoardStatement:Thestudywasconductedaccordingtotheguidelinesofthe

DeclarationofDeanshipofScientificResearch,PrinceSattamBinAbdulazizUniversity,SaudiArabia.

InformedConsentStatement:Notapplicable.

DataAvailabilityStatement:Notapplicable.

Acknowledgments:ThisstudyissupportedviafundingfromPrinceSattamBinAbdulazizUniversity.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

References

1. Lawal,K.;Rafsanjani,H.N.Trends,benefits,risks,andchallengesofIoTimplementationinresidentialandcommercialbuildings.

EnergyBuiltEnviron.2022,3,251–266.[CrossRef]

2. RansomwareatColoradoITProviderAffects100+DentalOffices—KrebsonSecurity.7December2019.Availableonline:https:

//krebsonsecurity.com/2019/12/ransomware-at-colorado-it-provider-affects-100-dental-offices/(accessedon27March2023).

3. NATOCountriesHitwithUnprecedentedCyberAttacks.GovTech.4September2022.Availableonline:https://www.govtech.

com/blogs/lohrmann-on-cybersecurity/nato-countries-hit-with-unprecedented-cyber-attacks(accessedon28March2023).

4. Cui,J.MalwareDetectionAlgorithmforWirelessSensorNetworksinaSmartCityBasedonRandomForest.J.Test.Eval.2022,

51,20220100.[CrossRef]

174

Mathematics2023,11,2481

5. Singh,T.;DiTroia,F.;Corrado,V.A.;Austin,T.H.;Stamp,M.SupportVectorMachinesandMalwareDetection.J.Comput.Virol.

HackingTech.2015,12,203–212.[CrossRef]

6. Yilmaz,A.B.;Taspinar,Y.S.;Koklu,M.ClassificationofMaliciousAndroidApplicationsUsingNaiveBayesandSupportVector

MachineAlgorithms.Int.J.Intell.Syst.Appl.Eng.2022,10,269–274.Availableonline:https://ijisae.org/index.php/IJISAE/

article/view/2010(accessedon29March2023).

7. AbuAl-Haija,Q.;Odeh,A.;Qattous,H.PDFMalwareDetectionBasedonOptimizableDecisionTrees.Electronics2022,11,3142.

[CrossRef]

8. Gao,Y.;Hasegawa,H.;Yamaguchi,Y.;Shimada,H.MalwareDetectionUsingLightGBMwithaCustomLogisticLossFunction.

IEEEAccess2022,10,47792–47804.[CrossRef]

9. Xie,N.Andro_MD:AndroidMalwareDetectionbasedonConvolutionalNeuralNetworks.Int.J.Perform.Eng.2018,14,547–558.

[CrossRef]

10. Liu,T.;Li,Z.;Long,H.;Bilal,A.NT-GNN:NetworkTrafficGraphfor5GMobileIoTAndroidMalwareDetection.Electronics

2023,12,789.[CrossRef]

11. Manoharan,S.;Sugumaran,P.;Kumar,K.MultichannelBasedIoTMalwareDetectionSystemUsingSystemCallsandOpcode

Sequences.Int.Arab.J.Inf.Technol.2022,19,261–271.[CrossRef]

12. Sun,H.;Wang,X.;Buyya,R.;Su,J.CloudEyes:Cloud-basedmalwaredetectionwithreversiblesketchforresource-constrained

internetofthings(IoT)devices.Softw.Pract.Exp.2016,47,421–441.[CrossRef]

13. Ahmed,U.;Lin,J.C.W.;Srivastava,G.Mitigatingadversarialevasionattacksofransomwareusingensemblelearning.Comput.

Electr.Eng.2022,100,107903.[CrossRef]

14. Ibrahim,A.;Tariq,U.;AhamedAhanger,T.;Tariq,B.;Gebali,F.RetaliationagainstRansomwareinCloud-EnabledPureOS

System.Mathematics2023,11,249.[CrossRef]

15. Barrett, M.P.FrameworkforImprovingCriticalInfrastructureCybersecurityVersion1.1. NIST.16April2018. Available

online:https://www.nist.gov/publications/framework-improving-critical-infrastructure-cybersecurity-version-11(accessedon

27March2023).

16. Hull,G.;Jhon,H.;Arief,B.Ransomwaredeploymentmethodsandanalysis:Viewsfromapredictivemodelandhumanresponses.

CrimeSci.2019,8,2.[CrossRef]

17. Kharraz,A.;Robertson,W.;Kirda,E.ProtectingagainstRansomware:ANewLineofResearchorRestatingClassicIdeas?IEEE

Secur.Priv.2018,16,103–107.[CrossRef]

18. Upadhyaya,R.;Jain,A.Cyberethicsandcybercrime:Adeepdwelvedstudyintolegality,ransomware,undergroundweband

bitcoinwallet.InProceedingsofthe2016InternationalConferenceonComputing,CommunicationandAutomation(ICCCA),

GreaterNoida,India,29–30April2016;pp.143–148.[CrossRef]

19. Gagneja,K.K.Knowingtheransomwareandbuildingdefenseagainstit—Specifictohealthcareinstitutes.InProceedingsofthe2017

ThirdInternationalConferenceonMobileandSecureServices(MobiSecServ),MiamiBeach,FL,USA,11–12February2017;pp.1–5.

[CrossRef]

20. Celdrán,A.H.;Sánchez,P.M.S.;Castillo,M.A.;Bovet,G.;Pérez,G.M.;Stiller,B.Intelligentandbehavioral-baseddetectionof

malwareinIoTspectrumsensors.Int.J.Inf.Secur.2022,22,541–561.[CrossRef]

21. Moon,D.;Lee,J.;Yoon,M.Compactfeaturehashingformachinelearningbasedmalwaredetection.ICTExpress2022,8,124–129.

[CrossRef]

22. Dargahi,T.;Dehghantanha,A.;Bahrami,P.N.;Conti,M.;Bianchi,G.;Benedetto,L.ACyber-Kill-Chainbasedtaxonomyof

crypto-ransomwarefeatures.J.Comput.Virol.HackingTech.2019,15,277–305.[CrossRef]

23. ESET:ThreatReportQ22020.Comput.Fraud.Secur.2020,2020,4.[CrossRef]

24. Yang,W.;Gao,M.;Chen,L.;Liu,Z.;Ying,L.RecMaL:Rectifythemalwarefamilylabelviahybridanalysis.Comput.Secur.2023,

128,103177.[CrossRef]

25. VirusChaser: AComprehensiveAntivirusSolutionEquippedwithPowerfulSystemProtectionFeatures. VirusChaser. 18

February2023.Availableonline:https://www.ncloud.com/marketplace/viruschaser(accessedon16April2023).

26. FKIE,F.CloudSnooper(MalwareFamily).CloudSnooper(MalwareFamily).21December2020.Availableonline:https://malpedia.

caad.fkie.fraunhofer.de/details/elf.cloud_snooper(accessedon1March2023).

27. Tonido—RunYourPersonalCloud.AFreePrivateCloudServer.(n.d.).Tonido—RunYourPersonalCloud.AFreePrivateCloud

Server.Availableonline:https://www.tonido.com/(accessedon2March2023).

28. Ghafur,S.;Kristensen,S.;Honeyford,K.;Martin,G.;Darzi,A.;Aylin,P.AretrospectiveimpactanalysisoftheWannaCry

cyberattackontheNHS.npjDigit.Med.2019,2,98.[CrossRef]

29. Eliando,E.;Purnomo,Y.LockBit2.0Ransomware:Analysisofinfection,persistence,preventionmechanism.CogIToSmartJ.2022,

8,232–243.[CrossRef]

30. Kajave,A.;Nismy,S.A.H.HowCyberCriminalUseSocialEngineeringtoTargetOrganizations.arXiv2022,arXiv:2212.12309.

[CrossRef]

31. Tanner,D.A.;Hinchliffe,A.;Santos,D.ThreatAssessment:BlackcatRansomware.2022.Availableonline:https://shorturl.at/

cdV37(accessedon2March2023).

32. Kara,I.;Aydos,M.Theriseofransomware:Forensicanalysisforwindowsbasedransomwareattacks.ExpertSyst.Appl.2022,

190,116198.[CrossRef]

175

Mathematics2023,11,2481

33. Umar,R.;Riadi,I.;Kusuma,R.S.AnalysisofContiRansomwareAttackonComputerNetworkwithLiveForensicMethod.IJID

Int.J.Inform.Dev.2021,10,53–61.[CrossRef]

34. Datta,P.M.;Acton,T.Fromdisruptiontoransomware:Lessonsfromhackers.J.Inf.Technol.Teach.Cases2022.[CrossRef]

35. PurismProducts.Availableonline:https://puri.sm/products/(accessedon3March2023).

36. Zou,S.;Zhang,J.;Jiang,S.;Cheng,Y.;Ji,X.;Xu,W.OutletGuarder:DetectingDarkSideRansomwarebyPowerFactorCorrection

SignalsinanElectricalOutlet.InProceedingsofthe2022IEEE28thInternationalConferenceonParallelandDistributedSystems

(ICPADS),Nanjing,China,10–12January2023;pp.419–426.[CrossRef]

37. Lin,C.;Kimberly,G.;Daniel,R.;Henry,U.BlockchainForensicsandCrypto-RelatedCybercrimes.SSRN2023.[CrossRef]

38. PureBoot&Ndash;Purism.(n.d.).Purism.Availableonline:https://puri.sm/projects/pureboot/(accessedon1March2023).

39. Palša,J.;Ádám,N.;Hurtuk,J.;Chovancová,E.;Madoš,B.;Chovanec,M.;Kocan,S.MLMD—AMalware-DetectingAntivirus

ToolBasedontheXGBoostMachineLearningAlgorithm.Appl.Sci.2022,12,6672.[CrossRef]

40. Srinivasan,S.;Deepalakshmi,P.ENetRM:ElasticNetRegressionModelbasedmaliciouscyber-attackspredictioninreal-time

server.Meas.Sens.2023,25,100654.[CrossRef]

41. VMware. NSXSandbox|VMware. Availableonline: https://www.vmware.com/products/nsx-sandbox.html(accessedon

4March2023).

42. Wahidin,G.W.;Syaifuddin,S.;Sari,Z.AnalisisRansomwareWannacryMenggunakanAplikasiCuckooSandbox.J.Repos.2022,

4,83–94.[CrossRef]

43. Lee,C.;Han,S.M.;Chae,Y.H.;Seong,P.H.Developmentofacyberattackresponseplanningmethodfornuclearpowerplantsby

usingtheMarkovdecisionprocessmodel.Ann.Nucl.Energy2022,166,108725.[CrossRef]

44. Sahin,D.O.;Akleylek,S.;Kilic,E.LinRegDroid:DetectionofAndroidMalwareUsingMultipleLinearRegressionModels-Based

Classifiers.IEEEAccess2022,10,14246–14259.[CrossRef]

45. Singh,P.; Borgohain,S.K.; Kumar,J.PerformanceEnhancementofSVM-basedMLMalwareDetectionModelUsingData

Preprocessing. InProceedingsofthe20222ndInternationalConferenceonEmergingFrontiersinElectricalandElectronic

Technologies(ICEFEET),Patna,India,24–25June2022;pp.1–4.[CrossRef]

46. Mowri,R.A.;Siddula,M.;Roy,K.InterpretableMachineLearningforDetectionandClassificationofRansomwareFamiliesBased

onAPICalls.arXiv2022,arXiv:2210.11235.[CrossRef]

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

176

mathematics

Article

Multi-Country and Multi-Horizon GDP Forecasting Using

Temporal Fusion Transformers †

JuanLaborda1,*,SoniaRuano2andIgnacioZamanillo2

1 DepartmentofBusinessAdministration,UniversidadCarlosIII,Getafe,28903Madrid,Spain

2 BancodeEspaña,C/Alcalá48,28014Madrid,Spain;sonia.ruano@bde.es(S.R.);

ignacio.zamanillo@bde.es(I.Z.)

* Correspondence:jlaborda@emp.uc3m.es;Tel.:+34-655-019-700

† Theopinionsandanalysesexpressedinthispaperaretheresponsibilityoftheauthorsand,therefore,donot

necessarilyreflectthoseoftheBancodeEspañaortheEurosystem.

Abstract:Thispaperappliesanewartificialintelligencearchitecture,thetemporalfusiontransformer

(TFT),forthejointGDPforecastingof25OECDcountriesatdifferenttimehorizons. Thisnew

attention-basedarchitectureofferssignificantadvantagesoverotherdeeplearningmethods.First,

resultsareinterpretablesincetheimpactofeachexplanatoryvariableoneachforecastcanbe

calculated.Second,itallowsforvisualizingpersistenttemporalpatternsandidentifyingsignificant

eventsanddifferentregimes.Third,itprovidesquantileregressionsandpermitstrainingthemodel

onmultipletimeseriesfromdifferentdistributions.ResultssuggestthatTFTsoutperformregression

models,especiallyinperiodsofturbulencesuchastheCOVID-19shock. Interestingeconomic

interpretationsareobtaineddependingonwhetherthecountryhasdomesticdemand-ledorexport-

ledgrowth.Inessence,TFTisrevealedasanewtoolthatartificialintelligenceprovidestoeconomists

andpolicymakers,withenormousprospectsforthefuture.

Keywords:GDP;deeplearning;timefusiontransformers;multi-horizonforecasting;interpretability

MSC:37M10

Citation:Laborda,J.;Ruano,S.;

1.Introduction

Zamanillo,I.Multi-Countryand

TheGreatRecession,theCOVID-19pandemic,andthewarinUkraineincreasedthe

Multi-HorizonGDPForecasting

UsingTemporalFusionTransformers. uncertaintysurroundingtheeconomiccycle.Precedingthesecrises,theworldeconomy

Mathematics2023,11,2625. https:// underwentaprocessoffinancializationovertheprecedingtwodecades,characterized

doi.org/10.3390/math11122625 byabroadrangeofshiftsintherelationshipbetweenthefinancialandrealsectors.This

phenomenonelevatedthesignificanceoffinancialactorsintheeconomy([1]).Italteredthe

AcademicEditor:WeiFang

aspectsofmicroandmacrodynamics.Thistranslatedthedynamicsoffinancialmarkets,

Received:3May2023 inparticular,nonlinearitiesandlong-termdependencies([2,3]),intofeaturesofdifferent

Revised:2June2023 businesscycleindicators,includingrealGDP.Consequently,forecastingmacroeconomic

Accepted:7June2023 data,suchasrealGDPgrowth,becameamorecomplextask.

Published:8June2023 TheeffectofanexplanatoryvariableonrealGDPdependsonhowitisinterrelated

withotherexplanatoryvariables,which,inaddition,canvaryovertime.Anexampleof

thatistheevidencethatweobtaininthisstudyonthelossofthepredictivepowerofthe

slopeoftheyieldcurvetoanticipatethebusinesscycle.Indifferentpreviousstudies,the

Copyright: © 2023 by the authors.

yieldcurvewasrevealedasanextremelypowerfulpredictorofrecessions([4–9]).

Licensee MDPI, Basel, Switzerland.

Theexistenceoflong-rangedependenceandnon-linearitiesinabusinesscycletime

Thisarticleisanopenaccessarticle

series([10–13])opensthedoortotheuseofartificialintelligence(AI)techniquestoforecast

distributed under the terms and

realGDP.AIisthedevelopmentofcomputer-basedalgorithmsthatcanperformtasks

conditionsoftheCreativeCommons

similartohumanintelligencebeingabletomodifytheiractions,thusmaximizingtheir

Attribution(CCBY)license(https://

chancesofsuccess.Suchalgorithmsareincreasinglycapableofsolvingextremelycomplex

creativecommons.org/licenses/by/

4.0/).

Mathematics2023,11,2625.https://doi.org/10.3390/math11122625 https://www.mdpi.com/journal/mathematics

177

Mathematics2023,11,2625

problems,suchashelpingindecision-makingprocesses;includingtheclassificationand

evaluationoflargeamountsofdata.

ThispapercontributestotherealGDPforecastingliteraturebyproposingtheap-

plicationoftemporalfusiontransformers(TFTs).Thisstate-of-the-arttimeseriesmodel,

developed by [14], is encompassed within deep neural networks (DNNs). This new

attention-basedarchitectureofferssignificantcomparativeadvantagesoverregression

modelsandotherdeeplearningmethods.First,itcanbeappliedtounivariateandmulti-

variatetimeseries.Second,threetypesofexplanatoryvariablescanbeused:temporaldata

knownonlyuptothepresent,temporaldatawithknowninputsintothefuture,and/or

exogenousstatic/categoricalvariables.Third,itallowsworkingwithheterogeneoustime

series,sothatitcantrainonmultipletimeseriesfromdifferentdistributions.Fourth,the

TFTarchitecturesplitsprocessingintolocalpreprocessingandglobalprocessing.Thefirst

onecapturesspecificeventsandthesecondonethecommonfeaturesofallthetimeseries.

Fifth,theresultsareinterpretablesincetheimpactofeachexplanatoryvariableoneach

forecastcanbecalculatedbyanalysingthevariableselectionweights.Sixth,itallowsfor

visualizingpersistenttemporalpatternsandidentifyingsignificanteventsanddifferent

regimes. Finally, it provides quantile regressions and permits computing simulations

basedonaknowninputintothefuture. Thisfeatureisespeciallyvaluabletoevaluate

macroeconomicpolicies.

WeapplyTFTsforthejointGDPforecastingof25OECDcountriesusingmacroeco-

nomicandfinancialvariables.SinceTFTsallowmulti-horizonforecasts,wewillforecastat

differenttimehorizons:one,two,three,andfourquarters.Itrequiresthedatasampleto

bepartitionedintothreedatasets:thetrainingdataset,thevalidationdataset,andfinally

thetestdataset. TheobtainedresultsarecomparedwiththoseofabenchmarkARIMA

modelusingtwostandardmetrics, meanabsoluteerror(MAE)androotmeansquare

error(RMSE).

TFToutperformsthestandardARIMAinthetwoproposedmetrics,MAEandRMSE.

TheperformanceofTFTforecastswascomparedtothatoftheARIMAmodelseparately,

inrecessionandexpansionsub-periods,inordertogivegreaterrobustnesstotheresults

obtainedatagloballevel.TFToutperformsARIMAinperiodsofeconomicslowdownor

globalrecessionaswellasinperiodsofstablegrowth;inthiscase,theimprovementis

marginal.ResultssuggestthatTFTsoutperformregressionmodels,especiallyinperiodsof

turbulence,suchastheCOVID-19shock.Interestingeconomicinterpretationsareobtained

dependingonwhetherthecountryhasdomesticdemand-ledorexport-ledgrowth.The

obtainedresultsshowthattheTFTforecastsimprovementsaresignificantlygreaterin

demand-drivengrowthcountries.

TheuseofTFTstopredictrealGDPyieldsveryinterestingresultsregardingthe

importanceoftheexplanatoryvariables.Whiletheslopeofthecurvehaslimitedpredictive

power,itisworthnotingthatthevariablemeasuringtheindebtednessofthenon-financial

privatesectorsdemonstratesaremarkableabilitytoanticipatefuturetrends.Thisvariable

playedacatalyticroleintheGreatRecessiononcethevalueofcollateralbegantodeteriorate,

inaccordancewithHymanMinsky’sfinancialinstabilityhypothesis([15,16]).Inthisregard,

recentstudiesshowthehighpersistenceoftheratioofprivatedebttoGDPfordifferent

OECDcountries,andthekeyimportanceofmacroprudentialpolicy,asoneofthepillars

ofmacroeconomicpolicy([17]). Finally, itshouldbenotedthattheimportanceofthe

explanatoryvariablesinpredictingrealGDPmightvarysomewhatdependingonthe

phaseoftheeconomiccycleortheforecasttimehorizon.TFTsarecapableofcapturingthis.

The rest of the paper is organized as follows: Section 2 discusses the theoretical

frameworkthatallowsustousefinancialvariables, compositeleadingindicators, the

creditcycle,andinternationaltradeaspredictorsofeconomicgrowth.Section3reviews

theliteratureonforecastingeconomicgrowthusingdeeplearningandregressionmodels.

Section4formulatesthemethodologydesigned,usingTFTs,forthejointforecastingofthe

GDPsofasubstantialnumberofcountries,anddetailsthedescriptionofthesampleand

178

Mathematics2023,11,2625

thevariablesused. Section5discussestheempiricalresultsobtained. Finally,Section6

presentstheconclusions,pointingoutfuturelinesofresearch.

2.PredictorsofGDPGrowth:ALiteratureReview

Overdecades,economistsdevotedasubstantialamountofefforttomodeleconomic

growth. Thereexistsawideliteraturethatsupportstheimportanceofdifferentkinds

ofvariablestopredicttheevolutionofGDP.Throughoutthissection,wereviewalist

ofvariablesfromabroadarrayofcandidatesanddescribehowtheyarerelatedtothe

businesscycle.

2.1.FinancialVariablesandLeadingIndicators

Financialvariables,suchasthepricesoffinancialinstruments,interestrates,interest

ratespreads,stockpriceindexes,andmonetaryaggregates,havesignificantpredictive

contentforeconomicactivitysincetheyareforward-lookingvariables,andtherefore,are

usefulindicatorsinmacroeconomicprediction. Foracomprehensiveliteraturereview,

see[18].

1.TheYieldCurve.Thespreadsbetweeninterestratesfordifferentmaturitiestend

tobeinterpretedasthemarketexpectationsoffutureratescorrespondingtotheperiod

betweenthetwomaturities. Intuitively,long-termratesincorporatetheexpectationsof

financialmarketsonfutureshort-termrates.Consequently,anegative-slopedorflatcurve

meansthatmarkets’prospectsinvolveadecreaseinfuturerealinterestrates,whichis

associatedwithweakeconomicactivityordownturn.

Evidenceonthepredictivepowerofthespreadbetweenlong-termandshort-term

governmentbondrates,calledtheslopeoftheyieldcurve,forinflationandrealeconomic

activityiswideandrobustacrosscountriesandtimeperiods([4,5,19–23]).

Ref.[6]providesthetheoreticalbasisforthisstatisticalevidence. Inparticular,the

mainimplicationoftheanalyticalrationalexpectationsmodelisthattherelationshipsare

notstructuralsincetheyareinfluencedbythemonetarypolicyregime.Inotherwords,the

extenttowhichtheyieldcurveisagoodpredictordependsontheformofthemonetary

policyreactionfunction,which,inturn,maydependonexplicitpolicyobjectives.Theyield

curvehaspredictivepower,forexample,ifthemonetaryauthorityfollowsstrictorflexible

inflationtargetingorifpolicyfollowsthe[24]rule.

We hypothesize that the impact of the yield curve on economic growth will de-

pendonhowitinteractsnon-linearlywiththeglobalcreditspreadcycleandtheofficial

interestrates.

2.CorporateBondSpreads.Assetpurchaseprograms,forwardguidance,andother

unconventionalmonetarypoliciescanlowerlong-terminterestrates,alteringtheinforma-

tioncontentoftheyieldcurve.However,eveninsuchcircumstances,thebehaviorofthe

corporatebondcreditspreadcurvevariesoverthebusinesscycle,potentiallycontaining

moreinformationaboutthefuture.

Manystudiesfocusedoncorporatebondspreads([25–31]),providingstrongevidence

forthelinkbetweenthisspreadandtheeconomicactivity.

WeincludeinourmodeltheratiooftheMoody’sU.S.Baacorporatebondyieldsto

thatofAaaasaglobalproxyforcreditspread.

3.TheCompositeLeadingIndicator.Thecombinationofmultipleleadingvariablesin

compositeleadingindicators(CLIs)pursuesamoreaccuratepredictionofthedevelopment

ofthereferenceseries.CLIsaredesignedtopredictthedevelopmentofthebusinesscycle,

focusingontheidentificationofturningpointsthatoccurwhenthegrowthratemovesfrom

anexpansionperiodtoacontractionperiodorviceversa.Empiricalevidencesupporting

theusefulnessoftheCLI,bothin-sampleandout-of-samplereal-time,inarealtimecontext,

iswide.Someexamplesare[4,32–35].

WeincludeinourmodeltheCLIbuiltbyOECD(see[36]),whichcapturesfluctuations

oftheeconomicactivityarounditslong-termpotentiallevel.ThisCLIshowsshort-term

179

Mathematics2023,11,2625

economicmovementsinqualitativeratherthanquantitativeterms.ACLIreadingabove

(below)100precedeslevelsofGDPabove(below)itslong-termtrend.

4. TheIndustrialsCommodityPriceIndex. TheCRBRawIndustrialsSpotIndex,

drawnfromBloomberg,isasyntheticmeasureofpricemovementsof13sensitivebasic

commoditieswhosemarketsarepresumedtobeamongthefirsttobeinfluencedbychanges

ineconomicconditions.Assuch,itservesasoneearlyindicationofimminentchangesin

businessactivity.

Thecriteriafortheselectionofcommoditiesare:(i)wideuseforfurtherprocessing

(basic);(ii)freelytradedinanopenmarket;(iii)sensitivetochangingconditionssignificant

inthosemarkets;and(iv)sufficientlyhomogeneousorstandardizedsothatuniformand

representativepricequotationscanbeobtainedoveraperiodoftime.

Then,theSpotMarketIndexisdefinedastheunweightedgeometricmeanofthe

individual commodity price relatives (i.e., the ratios of the current prices to the base

periodprices).

Differentpapersempiricallyexaminetheinteractionsbetweencommodityprices,

money,interestrates,goods,andeconomicgrowth([37–41]). Inparticular,Ref.[41]ex-

ploreshowthecommoditymarketcanpredictGDPgrowthforcountriesworldwide,rather

thanafewspecificcountriesorregions. Theyfindcommodityreturnssignificantlypre-

dictthenextquarter’sGDPgrowth,andthuscanbeconsideredasleadingindicatorsof

economicgrowth.

2.2.TheCreditCycle

Thecreditcycleandtheeconomiccyclearecloselyrelated. Manystudiesprovide

empiricalevidencesupportingthatendogenouscreditsupplyexpansionsprecedeadecline

inrealGDP(see[42],forareview). Theintuitionisthat,inthesupplysideoffinancial

markets,riskappetiteandthedebtaccumulationevolveoverthebusinesscyclefollowing

aregularprocess,andultimately,thiscreditcycletranslatestotherealeconomythrough

defaultsthatmaterializecreditrisk,andtheend,financialconstraintsaffectingthereal

economy.Inparticular,theMinsky’sfinancialinstabilityhypothesis([15,16,43,44])predicts

that, for a given microeconomic condition, the likelihood of facing credit constraints

decreasesinperiodsofGDPexpansionandincreasesinperiodsofcontraction.

Weincludeinourmodelthemeasurementofprivateindebtednessatthecountrylevel

developedandpublishedbytheBankforInternationalSettlements(BIS).Specifically,itis

definedastheratioofthetotaldebtofnon-financialprivatesectorsatmarketvalueofone

countryoveritsnominalGDP.

2.3.WorldTradeandEconomicIntegrationacrossCountries

Aswasfirststressedbytheclassics,AdamSmithandDavidRicardo,tradepromotes

growth by allowing the optimal use of resources. Empirical evidence is profuse and

supportsthattradetendstofavordevelopment,giventhatitstimulatestechnicalprogress,

whichisspreadacrosscountriesthroughtheimportationofcapitalgoodsthatincorporate

innovations(forasurvey,see[45]).

Particularly,exportspromoteeconomicgrowththroughseveralchannels: theyen-

hanceabetterallocationofresourcesthroughspecializationongoodsthathaveanim-

provedcomparativeadvantage,favoringproductivitygainsthrougheconomiesofscale,

spillovereffects,andlearning-by-doing.Inthissense,tradeintegrationenablesahigherex-

ternaldemandthatincreasestheprobabilityand/orintensityofexporting,andtherefore,of

economicgrowth,especiallyinperiodswheredomesticdemandisunderpressure([46–48]).

Internationaltradewasalsoidentifiedasachannelthroughwhichshocksareinterna-

tionallytransmitted,contributingtothesynchronizationinbusinesscyclesacrosscountries.

Inparticular,countriesjoiningacurrencyunionmaylosetheirabilitytostabilizecyclical

fluctuationsthroughindependentcounter-cyclicalmonetarypolicy.Ingeneral,empirical

researchfoundthatpairsofcountrieswithrelativelystrongeconomiclinkages,notonlyin

termsoftradeintensity,butalsointermsoffinancialandinstitutionalintegration,tend

180

Mathematics2023,11,2625

tohavehighlycorrelatedbusinesscycles.Forexample,Refs.[49–51]findthatthecloser

thetradelinkagesare,thehigherthecorrelationincountries’businesscyclesareaswell.

Similarly,Ref.[52]showsthatmorefinanciallyintegratedcountriesdisplaymorecorrelated

businesscycles.

WeincorporateinourmodeltheWorldTradeVolumeIndexthatismonthlycomputed

by the Netherlands Bureau for Economic Policy Analysis. This index, defined as the

arithmeticaverageofworldexportsandimportsofgoods,constitutesanindicatorofglobal

economicactivity. ItcoverstheUnitedStates,Japan,EU,andfourgroupsofemerging

countries: Asiancountries(excludingJapan),EasternEuropeandCIScountries,Latin

America,andAfricaandtheMiddleEast.

Here,wehavetoemphasizetheabilityofthetemporalfusionstransformersmethod-

ologytocapturecross-countrybusinesscycleco-movements,evenifthedriversofthis

synchronizationarenotexplicitlyintroducedinthelistofexplanatoryvariables.

3.ForecastingEconomicGrowthUsingDeepLearningandRegressionModels:

LiteratureReview

TheGreatRecession(2007–2009)andtheCOVID-19pandemicincreasedtheuncer-

taintysurroundingtheeconomiccycle. Thisindeterminationoccursinacontextofthe

financializationoftheglobaleconomyinrecentdecades,understoodasabroadsetof

changesintherelationshipbetweenthefinancialsectorandtherealsector,whichgave

greaterweightthanbeforetofinancialmotivesandactors, consequentlyaffectingthe

differentrelationshipsbetweenmacroeconomicand/orfinancialvariables.

Theinfluenceofmacroeconomicand/orfinancialvariablesonthebusinesscyclewas

extensivelydetailedintheprevioussection.Inthisone,wecollectthedifferenttechnical

contributionstotheforecastingofthebusinesscycle,measuredbyGDPinrealterms,from

advancedregressionmodels,especiallyintimeseriesanalysis,fortheuseofAItechniques.

3.1.TheUseofRegressionModelsforBusinessCycleForecasting

Thereisawidevarietyofregressionmodelsusedinmacroeconomicresearchinor-

dertoforecasteconomicactivity. TheyrangefromtheearlyARIMA([53–55]),orVAR

models([56,57])tothosemorecomplexonesthatanalyzethecyclefromanexplicitnon-

linearperspective.VARmodelsareparticularlyusefulforforecastingpurposebutsuffer

fromamajordrawback,astheyrequiretheestimationofmanypotentiallynon-significant

parameters.Thisover-parametrizationproblem,resultinginmulticollinearityandlossof

degreesoffreedom,leadstoinefficientestimatesandlargeout-of-sampleforecasterrors.

Tofacethisproblem,therearetwomainapproaches.Thefirstoneconsistinidentifying

non-significantlagsthroughstatisticaltestsandestimatingtherestrictedversionofthe

modelthatincorporatestheidentifiedrestrictionsontheparametersofthemodel. The

secondapproachusesquasi-VARmodels,whichspecifyanunequalnumberoflagsforthe

differentequations.

Alternatively,someauthors([58,59])proposeaBayesianVARorBVARmodel.Instead

ofeliminatingthelongestlags,theBayesianmethodimposesrestrictionsonthecoefficients

ofthemodel,assumingthatthesecoefficientsaremorelikelytoapproachzerothanthe

coefficientsoftheshortestlags. WithintheVARfamily,inordertocapturethesystemic

dimensionwhileretainingtheadvantageofestimatingasingleequation,structuralvec-

torautoregressive(SVAR)modelsemerged([60,61]). Finally,itisworthmentioningthe

time-varyingparameterVARmodels,whichsuccessfullymodelregime-switchingtime

series([62–64]).

Withinbusinesscyclemodelingfromanexplicitnonlinearperspective,therangeis

verybroad.Theyinclude,forexample,smoothtransitionregression(STR)models,which

areageneralclassofreduced-form,state-dependent,nonlineartimeseriesmodelsinwhich

thetransitionbetweenstatesis,generally,generatedendogenously,andwheresmooth

transitionautoregression(STAR)modelsareaparticularcase.See[65–67].

181

Mathematics2023,11,2625

Ref.[68]showsthattheSTRmodelsincludeparticularcases,inadditiontotheSTAR,

theexponentialautoregressive(EAR),thethresholdautoregressive(TAR),andtheSETAR

models. TARandSETARmodelsarethosewhich,maintainingtheideathatthelevel

andtimestructureinaneconomicphenomenondependonthecyclicalphaseinwhich

itisfound, providearelativelysimplewayofintroducingnon-linearelementsinthe

econometricanalysisoftimeseries.See[69–71].

Finally,withinthenonlinearmodelingofthebusinesscycle,wedistinguishthose

modelswherethestateofthecyclecanberepresentedbyabinarystatevariablewhose

evolutionisexplicitlycharacterizedbyaMarkovchain.Thisstatevariableconditionsthe

parametersofalinearmodelthatcompletestherepresentationoftheobserveddynamics.

WerefertoMarkov-switchingautoregression(MS-AR)models,see[57,72–79],andfurther

generalizetheMS-ARmodeltoaMS-VARtimeseriesmodel.

Ref.[80]useasmallsetofvariables(realGDP,theinflationrate,andtheshort-term

interestrate)toanalyzeatheoretical(timeseries)andtheoretical(structural)regression

models, as well as linear and nonlinear, to test whether the decline in U.S. real GDP

duringtheGreatRecessionhadthepotentialtobepredicted. Theirresultssuggestthat

structural(theoretical)models,especiallythenonlinearmodel,performwellonaverage

atallforecasthorizonsinexpost,out-of-sampleforecasts,althoughatcertainforecast

horizons,certainnonlinearatheoreticalmodelsperformbetter.Thenonlineartheoretical

modelalsodominatesintheexante,out-of-sampleforecastsoftheGreatRecession.

3.2.ForecastingRealGDPUsingArtificialIntelligenceModels

ForecastingrealGDPgrowth,suchaswithothermacroeconomicdata,isafarfrom

straightforwardprocess. Startingfromthecausalrelationshipbetweendependentand

independentvariables,traditionaleconomicmodelsusepredeterminedrelevantvariables

tomakepredictions,adoptingtop-downandtheory-drivenapproaches([81]).Thisprocess,

inrelationtothedataandmethodsused,isfoundedoneconomicintuitionandforecasters’

judgment. Ifanyoftheforecasters’assumptionsarenotmet,themodelswillproduce

inaccuratepredictions.

TheeffectofanexplanatoryvariableonrealGDPdependsonhowitisinterrelated

withotherexplanatoryones,which,inaddition,canvaryovertime.Thisfeaturecannot

bemodeledusingtheconventionalregressionframework,openingthedoortotheuse

ofAItechniques.AIisthedevelopmentofcomputer-basedalgorithmsthatcanperform

taskssimilartohumanintelligence,beingabletomodifytheiractionstomaximizetheir

chancesofsuccess.Suchalgorithmsareincreasinglycapableofsolvingextremelycomplex

problems,andcanassistindecision-making,includingtheclassificationandevaluationof

largeamountsofdata.

Unlikemanytraditionaleconomicforecastingmodels,AImachinelearningmodels

focusonpureprediction([82]). Beingmoreflexiblethantraditionaleconomicforecast-

ingmodels,theyproducepredictionswithoutpredeterminedassumptionsorjudgments.

Therefore,thankstothedevelopmentofnewalgorithmsandtheincreaseincomputing

power,machinelearningmodelswereactivelyappliedinvariousfields,fromforecasting

transportation,trafficorelectricityflows([14,83,84]),toforecastinghousingprices([85])

orfinancialmarketvolatility([14,86]). Inmostofthefieldsanalyzed,machinelearning

methodsperformbetterthantraditionaleconometricmodels,includingcaseswithlow-

frequencydata.Lookingattheirapplicationtoeconomics,suchastheinflationforecasting

studiesof[87,88],theyproducerobustpredictions.

Ref.[89]dividesAIlearningmethodsintofourmajorgroups:unsupervised,super-

vised,semi-supervised,andreinforcementlearning.

AlmostalltheAImodelsappliedforbusinesscycleforecastingfallwithinthesuper-

visedlearningmodels,althoughelementsofreinforcementlearningcanalsobeincorpo-

rated.ForrealGDPforecasting,differentAImodelsareused:K-nearestneighbor([90–92]);

decisiontrees,boostedtrees,gradientboostingand/orrandomforest([91,93–98]);artificial

neuralnetworksandtheirdeeplearningextensions([99–101]);ordinaryandalternative

182

Mathematics2023,11,2625

supportvectormachines([91,101–103]);andBoltzmannmachines([101]). Thesepapers

findthatalltheselearningalgorithmscanoutperformtraditionalstatisticalmodels,thus

offeringarelevantadditiontothefieldofeconomicforecasting.

Itisimportanttoremarkthatmostmachinelearningtechniques,suchasrandom

forestorgradientboostingalgorithms,arenotidealfortimeseriesforecastingsincethey

ignorethetimeorderofthefeatures.Theyassumethatthevalueofeachfeatureatacertain

timestepisindependentofthevalueofthesamefeatureattheprevioustimestep.Thisis

violatedintimeseriesdata,whereserialcorrelationsareessential.

Becauseofthis, recurrentneuralnetworks(RNNs), suchasgatedrecurrentunits

(GRUs)andlongshort-termmemorynetworks(LSTMs),areextensivelyusedtosolve

timeseriesforecastingproblemssincetheyarecapableofcapturingthedependencies

betweentimesteps.TheproblemwiththeseDNNsisthattheycannotcorrectlycapture

long-rangedependencies. Thisissueissolvedinthetransformerarchitecture,initially

presentedin[104].

ThispaperisacontributiontotherealGDPforecastingliteraturebasedontheap-

plicationofAI.ItproposestheapplicationofTFTs,recentlydevelopedby[14],whichare

encompassedwithinDNNs.TFTsprovideconsiderableadvantagesthatwillbedetailedin

thenextsection.

4.MethodologyandDatabase

Wewillapplyanewdeeplearningmodel, thetemporalfusiontransformers, for

forecastingjointlytherealGDPonaquarterlybasisfor25OECDcountriesatdifferent

timehorizons.WewilldetailthemainfeaturesofTFTs,explainingboththeattributesthat

makethemverysuitableforforecastingmacroeconomicvariablesandthedifferentblocks

oftheirarchitecture.Wewillthenexplainindetailthemethodologywedesignedforthe

jointforecastingoftheGDPsofasubstantialnumberofcountries.

4.1.TemporalFusionTransformersforForecastingRealGDP

TFT([14])isthestate-of-the-artmodelforinterpretable,multi-horizontimeseriesfore-

casting.Thisattention-basedarchitectureisspecificallydesignedfortimeseriesprediction

andprovidesseveraladvantagesoverotherdeeplearningmodels(Figure1).

Figure1.TheTFTadvantages.Source:[14].

First,TFTssupportdifferenttypesofvariablesasinputs: timeseriesthatareonly

knownuptothepresent(thisisthetypeofdatathatmostmodelsworkwith);timeseries

withknownvaluesinthefuture;andstaticortime-invariantvariables.Allthesevariables

183

Mathematics2023,11,2625

canbecategoricalorcontinuous.Duetoitsabilitytoprocessstaticvariables,TFTspermit

trainingonmultipletimeseries,fromdifferentdistributions.Thisisextremelyimportant

becauseitenabledustotrainthemodelwithdatafromdifferentcountries,significantly

increasingthesizeofthedataset,somethingessentialformachinelearningmodels.

Mostmodelsarenotabletoworkwithknownfuturevaluesandthisisessentialfor

certaintimeseriesproblems. Forexample,fromtheperspectiveofacentralbank,the

model’sabilitytoworkwithknownfuturevaluesofagivenexplanatoryvariablewill

allowforananalysisoftheimpactofmonetarypolicy(interestratesand/orquantitative

easing)onagivenmacroeconomicvariableunderstudy,beitinflationand/orrealGDP.

Secondly,TFTsallowmulti-horizonquantilepredictionthroughmulti-stepforecasts

bycalculatingpredictionintervalsusingthequantilelossfunction. Theusercandefine

theseforecastingintervals.

Finally,onemainpropertyofTFTsistheirinterpretability.Mostdeeplearningarchi-

tecturesare“blackbox”modelsandtheirpredictionscannotbeexplained.Generally,AI

explanatorymethodsobtaininterpretabilitymeasuresinadifferentiatedprocessfromthe

estimationone.Commonposthocmachinelearningexplanatorytechniques,suchasSHAP

orLIME,donottakeintoaccountthetemporalorderoftheinputs,ignoringdependen-

ciesbetweentimestepsthatareessentialintimeseries. TFTsaddressthisweaknessby

incorporatingvariableselectionnetworks(VSN)thatprovidevariableselectionweights,

whichquantifytheimportanceofeachfeatureinthepredictionofeachobservationin

thedataset. Then,selectionweightsarecollectedforeachvariableacrosstheentiretest

settocomputeanystatisticthatcharacterizeseachsamplingdistribution.Inadditionto

quantifyingtheimportanceofeachinputvariableinprediction,TFTspermitustovisualize

persistenttemporalpatterns,differentregimes,andsignificantevents.Forthispurpose,

TFTsemployaself-attentionmechanismthatestimatestheattentionweightsthatmeasure

theimportanceofeachperiod.

Having already explained the capabilities that make the TFT ideal for economic

forecasting,wewillnowbrieflyexplainitsarchitecturebeforedetailingthemethodology

wedesignedforthejointforecastingofrealGDPforaconsiderablenumberofcountries.

SeeFigure2.

Figure2.TFTarchitecture.Source:[14].

184

Mathematics2023,11,2625

TFThasacomplexarchitecture,whichgivesitenormousflexibilityandcomputing

potential,themainblocksbeing:

1-Gatingmechanisms:GatingmechanismsgiveTFTstheabilitytoskipunusedparts

ofthearchitecture.Thisisespeciallyimportantinsmallornoisydatasets,whereasimpler

modelcanenhanceperformance(astheproblemsolvedinthispaper).Thisgatedresidual

network(GRN)isoneofthemainblocksofTFTs.TheGRNtakesinthemaininputanda

contextvectoranddecideswhetheradditionaldenselayersareusefulortheselayerscan

beskippedthroughtheresidualconnection.SeeFigure3.

Figure3.GRNScheme.Source:[14].

2-Variableselectionnetworks(VSN):Inmostpredictionproblems,wehavevariables

thatdonotincreasethepredictionabilityofthemodel.TFTintroducedvariableselection

networks:thispartofthearchitectureremovesirrelevantinputsthatdecreasethealgorithm

performanceandprovidesinformationaboutthemostrelevantvariablesjustbyanalyzing

theweightsassignedtoeachone.

3-Staticcovariateencoders:TFTisabletouseinformationfromstaticdatathanksto

separateGRNencodersthatproducedifferentcontextvectorsthatareconnectedtoseveral

partsofthearchitecture.Thesekindsofencodersareespeciallyimportantforourproblem

sincetheyallowthemodeltotrainwithdatafromdifferentcountries.

4-LSTMEncoder-Decoder:Thissequence-to-sequencelayerisusedforlocalprocess-

ing;itcapturesshort-termtimedependencies.Knownfutureinputsaredirectlyconnected

tothedecoder.

5-Interpretablemulti-headself-attention: TFThasaself-attentionmechanismthat

makesthemodelcapableoflearninglong-termrelationships: itintegratesinformation

fromanytimestep.Thistransformerarchitecturepresentssomechangesincomparison

tostandardtransformers([104]);thesemodificationsallowforconductinginterpretability

studiesbytheanalysisofattentionweights.

6-Denselayers:Severaldenselayersarepartofthemodel;theselayerslearnthrough

differentnon-lineartransformations.Thefinaldenselayergeneratespredictionintervalsin

additiontopointforecasts.

7-Lossfunction:TFTistrainedbyminimizingthequantilelossofallquantileoutputs.

Weusethefollowingquantiles: {0.02,0.1,0.25,0.5,0.75,0.9,and0.98}. Thefollowing

equationrepresentsthelossfunction:

L(Ω,W)=∑ yt ∈Ω . ∑ q∈Q . ∑τ τ m = a 1 x QL(yt,yˆ M (q τ , m t− ax τ,τ),q) (1)

QL(yt,yˆ,q)=q(y−yˆ) + +(1−q)(yˆ−y) + . (2)

185

Mathematics2023,11,2625

4.2.Methodology

Inthissection,weprovideabriefexplanationofthedatausedinthetraining,valida-

tion,andtestdatasets,thehyperparameterconfiguration,andthemodelspecificationsfor

eachforecasthorizon.

Thetargetvalue(y)ofourneuralnetworkistheGDPlogarithmicgrowthrate,ex-

pressedas:

y=log

GDP(t+s)

, s=1, 2, 3or4 (3)

GDP(t)

wheresdenotesthenumberofquarters.Forexample,inthecaseoftheannualgrowthrate

forecast,itwouldbe:

y=log

GDP(t+4)

. (4)

GDP(t)

This means that we will train our network with four different target values and

differenthyperparameterssettingsdependingontheforecasthorizon.Wewillmeasurethe

performanceofthemodelsusingtwodifferentmetrics,theRMSEandtheMAE.Foreach

date,thedatasetiscomposedofthedatafrom25OECDselectedcountries.Thus,wewill

simultaneouslytrainandforecastforallofthem.

Themaindisadvantageofmachinelearningmodelsformacroeconomicforecastingis

thelackofavailabledata.WeusedthePythonlibraryPyTorchForecastingtoimplement

theTFT;thispackagedoesnothavestochasticgradientdescentavailable.Becauseofthis,

weneedtorefitthemodelforeachforecasttoincorporatethedatafromthelatestavailable

observation.ThisiscriticaltoforecasttheGDPsincetheeconomicparadigmcanchange

suddenly.

AsshowninFigure4,thefirstobservationthatbelongstothetestdatasetisthefirst

quarterof2009andthelastoneisthethirdquarterof2021.PyTorchForecastingusesthe

lastavailablequarterasthevalidationdataset;therefore,thevalidationandtestdatasets

willcontainoneobservationpercountryineachforecast.

Figure4.Quarterlypredictionmethodology.

Whenwemakepredictionsgreaterthanonequarter(s=2,3,or4quarters),thetest

datasetcontainstheGDPlogarithmicgrowthratethatcorrespondstothosesperiods.The

forecastthatwewillusetocheckthemodelperformanceisthelastone,inordertoavoid

overlappingdata.WecanseeinFigure5howwemaypredictQ42009whenthelastdata

availableareQ42008.Eventhoughourtestdatasetcontainsfourannualgrowthrates,we

onlyusethelastonesinceitisthefirstpredictionthatdoesnotcontainanyinformation

fromthetestdataset.

186

Mathematics2023,11,2625

Figure5.Annualpredictionmethodology.

Thehyperparametersusedtoforecastatdifferenttimehorizonsarethesame,with

theonlyexceptionbeingthenumberofepochs.Themainhyperparametersareshownin

Table1.

Table1.Mainhyperparameters.

ForecastHorizon

MainHyperparameters

1Q 2Q 3Q 4Q

Epochs 13 17 19 20

Learningrate 0.03

Dropout 0.1

Numberofheads 1

Statesize 16

Batchsize 64

Quantiles 0.02,0.1,0.25,0.5,0.75,0.9,0.98

Normalized GroupNormalizer

TheGroupNormalizerscalesbygroups(inthisapplication,countries).Itmeansthat

foreachgroup,ascalerisfittedandapplied.

InAppendixB,weaddedthecodeforannualpredictionsandhowwecomputethe

RMSEandtheMAEforthewholedataset.

4.3.SampleDataandVariables

Thedatabaseusedinthispapercomesfromdifferentcombinedsourcescorresponding

totheperiod1990–2021for25OECDcountries(SeeTable2). (i)TheOrganizationfor

EconomicCo-operationandDevelopment(OECD)forGDPinvolumeindex,andmain

economicindicators;(ii)TheBankforInternationalSettlements(BIS)fortheTotalDebtNon

FinancialPrivateSectorsoverGDP;(iii)FederalReserveEconomicData(FRED),Federal

ReserveBankofSt.LouisforCreditSpreads;(iv)NetherlandsBureauforEconomicPolicy

Analysis(CPB)forWorldTradedata;and(v)BloombergforCRBRawIndustrialsSpot

Index.Table3showsdetailedinformationaboutthevariables,thereasonforuse,andthe

sources.

Table2.Selectedcountries.

Australia Italy UnitedKingdom

Austria Japan UnitedStates

Belgium Korea SouthAfrica

Canada Mexico

Denmark Netherlands

Finland NewZealand

France Norway

Germany Portugal

Greece Spain

Iceland Sweden

Ireland Switzerland

187

Mathematics2023,11,2625

Table3.Variablesdescription.

Variable Definition ReasonofUse Source

Dependentvariable

GDPinvolumeindex,hundredths,

Dependentvariableforthecountry’s

GDPlogarithmicgrowthrateit 2015=100,ofeverycountryiin

economicgrowth.

OECD

yeart.

Independentvariables

Idiosyncraticvariables

Theslopeoftheyieldcurvewasshown

empiricallytobeasignificantpredictor

ofinflationandrealeconomicactivity.

Quiteafewacademicstudiessuggested

thattheslopeoftheyieldcurveseems

Itistheratiooflong-terminterest

tobeextremelypromisingasa

Yieldcurve(YCit) ratesonsovereigndebtto

predictorofrecessions.See[4–9].We

OECD

short-terminterestrates.

hypothesizethatitsimpacton

economicgrowthwilldependonhow

itinteractsnon-linearlywiththeglobal

creditspreadcycleandofficial

interestrates.

Itcapturestheprogressionofrisk

appetiteandthedebtaccumulation

process.Duringaneconomicexpansion

investors’riskappetitetendsto

increase;thelongertheexpansion,

withoutanymajorsetback,thehigher

theriskappetite,indebtedness,and

economicgrowth—exactlytheopposite

Ratioofthetotaldebtof duringperiodsofdeleveragingand

non-financialprivatesectorsat privatebalancesheet

marketvalueofonecountryover recessions([15,16,43,44,48,105–107]).

Debtnon-financialprivate

itsnominalGDP.Itisdeveloped, Ref.[108]foundanincreaseinthe BIS

sectors/GDP(privatedebt/GDP)it

calculatedandupdatedbytheBank householddebttoGDPratiopredicts

forInternationalSettlements(BIS). lowerGDPgrowthandhigher

Thisindexisregularlyupdated. unemploymentinthemediumrunfor

anunbalancedpanelof30countries

from1960to2012.Ref.[17]foundfor

almostallofthe43OECDcountries

analyzedthattheprivatedebt-to-GDP

ratioishighlypersistent.Theseresults

suggestlong-livedeffectsofshocksto

theprivatedebt-to-GDPratio,which

requireappropriatepolicyactions.

Thecompositeleadingindicator(CLI)

TheOECDCompositeLeading

isdesignedtoprovideearlysignalsof

Indicator(CLI)isanaggregatetime

turningpointsinbusinesscycles

seriesdisplayingareasonably

showingfluctuationintheeconomic

consistentleadingrelationshipwith

activityarounditslongtermpotential

OECDcompositeleading thereferenceseriesforthebusiness

level.Differentresearchfoundthatthe OECD

indicator(CLIit) cycleofacountry(GDP).ACLI

compositeleadingindicators(CLI)are

readingabove(below)100isalways

usefulforforecastinggrossdemand

anindicationthatanticipateslevels

product(GDP),bothinsampleandin

ofGDPabove(below)

anout-of-samplereal-time

long-termtrend.

exercise([4,32–34,38]).

Commonvariables

188

Mathematics2023,11,2625

Table3.Cont.

Variable Definition ReasonofUse Source

Muchresearchindicatestheusefulness

ofcreditcurveinformationtopredict

economicactivity([25–29,31]).Most

unconventionalmonetarypolicies,such

asassetpurchaseprogramsand

forwardguidance,aimtolower

long-termrates,significantlyaffecting

theinformationcontentoftheyield

FRED,

TheratiooftheMoody’sU.S.BAA curve.However,eveninsuch

Federal

corporatebondyieldstothatof circumstances,thebehaviourofthe

GlobalCreditspreadcycle(GCSCt)

AAAistakenasaproxyforthe corporatebondcreditspreadcurve

Reserve

Bankof

globalcreditspreadcycle. variesoverthebusinesscycle,

St.Louis

potentiallycontainingmore

informationaboutthefutureeconomy.

Morerecently,research([30])found

creditspreadcurveinformationin

higherdeciles(implyinglowcredit

quality)isstatisticallysignificantand

economicallyimportantforpredicting

thebusinesscycle.

Itisameasureofthepricemovements

of13sensitivebasiccommodities

whosemarketsarepresumedtobe

CRBRINDIndex(CRBRINDt) CRBRawIndustrialsSpotIndex amongthefirsttobeinfluencedby Bloomberg

changesineconomicconditions.As

such,itservesasoneearlyindicationof

impendingchangesinbusinessactivity.

Themonthlyworldtradevolume

indexiscomputedbytheCPB

(NetherlandsBureauforEconomic

PolicyAnalysis)andisdefinedas Itisanindicatorofglobaleconomic

arithmeticaverageofworldexports activity.Although,afterthefinancial

andworldimportsofgoods.The crisisin2008,thegrowthrateinworld

seriescoversUnitedStates,Japan tradeisunusuallylowrelativeto

andEUandfourgroupsof growthinworldGDP([109]),ahigher

WorldTradevolumeIndex(WTVIt) emergingcountries:OPEC,Asian externaldemandincreasesthe CPB

newlyindustrialisedcountries probabilityand/orintensityof

(Taiwan,HongKong,Singapore exporting,andtherefore,ofeconomic

andSouthKorea),transition growth,especiallyinperiodswhere

countries(centralandeastern domesticdemandisunder

Europeancountriesincluding pressure([46–48]).

Turkeyandex-SovietUnion’s

countries)andother

emergingeconomies

5.ResultsandDiscussion

TheTFTmodelisestimatedforthe25OECDcountrieslistedinTable2,focusingthe

analysisoftheresultsof10representativecountriesthatwereselectedtakingintoaccount

theirheterogeneityintermsofsize,growthpattern(demand-ledorexport-ledgrowth),

andmonetarysovereignty.

Inthissection,wepresentanddiscussthemostimportantresults.First,inSection5.1

wewilldiscusstheresultsobtainedovertheentiretestperiodforallforecasthorizons

anddifferentiatingthemacrossthe10representativecountries. Second,inSection5.2,

wewillpresenttheresultsacrossdifferentsub-periodsdefinedtoobservedifferencesin

performance,dependingonthestageofthebusinesscycle.Finally,wewillprovidesome

concreteexamplesofTFTforecastsandtheirinterpretability.

189

Mathematics2023,11,2625

5.1.PerformanceovertheEntirePeriod

Table4showshowTFToutperformsthestandardARIMAovertheentiretestperiod

fortheselectedcountriesintwometrics:meanabsoluteerror(MAE)androotmeansquare

error(RMSE).PercentagesreflecttheerrorexcessofARIMArelativetoTFT.Forexample,

foranannualforecast,ARIMARMSEis188.27%higherthanthatofTFT.Improvements

occurforallforecasttimehorizons.

Table4.ImprovementoftheMAEandRMSEofTFTrelativetoARIMA.

Metric t+1 t+2 t+3 t+4

MAE 8.38% 33.89%*** 47.98%*** 48.53%***

RMSEa 12.44% 88.80%*** 151.85%*** 157.07%***

aRMSEistheaverageoftheRMSEscalculatedatcountrylevel.Note:***significantcoefficientat1%.

Toevaluatethestatisticalsignificanceoftheresults,weperformaone-tailedhypothesis

testsontheTFTerrormetrics.Wecomputethe99thpercentileofthebootstrapdistribution

oftheTFTerrormetricsandcomparethiscriticalvalueagainsttheerrormetricsofthe

benchmarkmodel. Forthetwometricsandacrossallforecasthorizons’,exceptforone

quarter,ARIMAerrormeasuresarehigherthanthe99thpercentileoftheTFTerrormetric

distribution,confirmingthatTFTerrormetricsarestatisticallylowerthantheARIMAones,

atthe1%significancelevel(seeAppendixA).

Table5showstheincreasesinthetwoconsiderederrormetrics(MAEandRMSE),for

theARIMAmodelwithrespecttotheTFTinthe10selectedcountriesforthe1-quarterand

1-yearforecasts.ItshowsthattheTFTforecastsareusuallymoreaccuratethanARIMA,

beingthattheseimprovementsgreaterindemand-drivengrowthcountries.

Table5.ImprovementoftheMAEandRMSEofTFTrelativetoARIMAbycountry.

CAN GER DNK SPA FRA GBR ITA JPN POR USA

t+1 3.0% −8.0% 11.0% 23.3% 20.8% 25.0% −5.8% 5.0% 1.1% −2.1%

MAE

t+4 17.0% 4.2% 12.0% 113.8% 78.3% 103.5% 41.6% 1.8% 49.1% 36.8%

t+1 9.1% −19.1% 16.9% 21.1% 20.6% 45.4% −0.7% −1.1% 1.4% 2.4%

RMSE

t+4 63.3% 12.3% 7.6% 327.2% 205.2% 416.5% 92.0% 2.7% 127.1% 128.2%

OneofTFT’smostinterestingfeaturesisitsinterpretability.Figure6showstheencoder

variablesimportanceforonequarter(LHS)andannual(RHS)forecasts.

Figure6.Encodervariablesimportanceforonequarter(lefthandside)andannualpredictions(right

handside).

Asexpected, themostimportantpredictoristhenearestlagofrealGDPgrowth,

whichreflectstheautoregressivebehaviorofthetimeseries.Likewise,theOECDLeading

IndicatorIndexprovidesearlysignalsofturningpointsinbusinesscycles([4,32–34,109]).

TheCRBRawIndustrialSpotIndex’srelevanceconfirmsitservesasanearlyindicator

ofimpendingchangesinglobalbusinessactivity([41]). ThechangeintheWorldTrade

VolumeIndexisanindicatoroftheglobalexternaldemand,anditsimportancedepicts

howitaffectscountries’businessactivity.

190

Mathematics2023,11,2625

Itisremarkablethepredictivecapacityofthevariablethatcapturestheindebtedness

ofthenon-financialprivatesectorsasapercentageofGDP,whichplayedacatalyticrolein

theGreatRecessiononcethevalueofcollateralbegantodeteriorateinaccordancewith

HymanMinsky’sfinancialinstabilityhypothesis([15,16]).Recentstudiesprovideevidence

onthehighpersistenceoftheratioofprivatedebttoGDPfordifferentOECDcountries

andthekeyimportanceofmacroprudentialpolicyinthisarea([17]).

Relatedtothisvariable,ourproxyofglobalcreditspreadcycle(USACreditSpread)is

economicallyimportantforpredictingthebusinesscycle([25–31]).Incontrast,thelimited

forecastingcapacityoftheyieldcurveinTFTsuggeststhattheslopeofthesovereigndebt

interestratecurvediminisheditspredictivepower,comparedtopreviouswork([4–9]),in

anticipatingtheevolutionofthebusinesscycle.Thislossofforecastingaccuracyoccursin

acontextwherequantitativeeasingpoliciesgainedimportance.Moreresearchisneededto

understandtheeffectsofquantitativeeasingontheyieldcurve’spredictivepower.

5.2.PerformanceoverExpansiveandRecessivePeriods

AcomparisonofTFTversusARIMAwasperformedinbothrecessionandexpansion

sub-periodsinordertogivegreaterrobustnesstotheresultsobtainedatagloballevel.

Table6showshowTFTclearlyoutperformsthestandardARIMAduringtheCOVID-

19pandemicandbehavesalmostequallyintherestofsub-periods. Thedifferencein

performancebetweenbothmodelsincreasesinlong-termforecastsduetotheTFTability

tocapturenonlinearities.

Table6.ImprovementoftheMAEandRMSEaofTFTrelativetoARIMAbyperiod.

Period Metric t+1 t+2 t+3 t+4

MAE 13.82% 10.04% −3.54% −5.85%

2008–2011 RMSEa 10.96% 5.31% −3.52% −4.14%

MAE 0.18% −2.42% 8.01% 26.59%

2012–2015 RMSEa −2.76% −0.99% 4.35% 21.72%

MAE −4.85% 6.56% −10.54% 0.67%

2016–2019 RMSEa −6.20% 4.83% −6.85% 0.01%

MAE 9.43% 56.12% 116.82% 115.92%

2020–2021(Q3) RMSEa 12.47% 94.64% 190.81% 204.09%

aRMSEistheaverageoftheRMSEscalculatedatcountrylevel.

Table7exhibitstheincreasesinthetwoconsiderederrormetrics(MAEandRMSE),for

theARIMAmodelwithrespecttotheTFT,inthe10selectedcountriesfor1-yearforecasts

overthedifferentsub-periods.Ingeneral,TFTforecastsaremoreaccuratethanthoseofthe

ARIMA,beingthattheseimprovementsaregreaterinperiodsofeconomicslowdownor

recession,inparticular,indemand-drivengrowthcountries.

Table7.ImprovementoftheMAEandRMSEofTFTrelativetoARIMAbyperiodandcountryin

annualforecast.

Period Metric CAN DEU DNK ESP FRA GBR ITA JPN POR USA

MAE −13.4% −14.2% 10.0% 9.0% −20.8% −31.0% −1.7% −2.1% 19.9% −7.4%

2008–2011 RMSE −0.7% −13.0% 5.3% −0.2% −10.2% −18.5% 1.0% −2.2% 5.3% −5.9%

MAE 15.8% −10.2% 27.4% 49.4% 34.3% −27.8% 100.2% 3.2% 81.0% −17.7%

2012–2015 RMSE 6.4% −5.8% 21.6% 32.9% 29.5% −26.6% 70.2% −2.3% 74.1% 7.4%

MAE −15.8% 80.5% 6.5% −11.7% 40.0% −24.0% −21.3% −17.2% −29.0% 40.2%

2016–2019 RMSE −11.0% 77.6% −2.4% −21.0% 38.3% −23.3% −18.7% −22.5% −23.0% 41.8%

MAE 61.6% 19.1% 11.6% 201.3% 140.6% 237.5% 68.6% 18.4% 79.1% 111.8%

2020–2021(Q3)

RMSE 94.9% 41.6% 12.3% 363.3% 219.7% 476.6% 105.7% 16.2% 149.7% 190.8%

191

Mathematics2023,11,2625

5.3.ForecastExamples

InordertoprovideabetterunderstandingoftheTFT,inthissection,wepresent

concrete examples of its predictions and their interpretability. We show the quantile

forecastforSpainandtheUnitedStatesfortwoyears,2011and2017.Thefirstyeardisplays

howthemodelworksinaperiodofturbulence,whilethesecondpresentsitsperformance

inaperiodofstablegrowth.

Figure7representsthequantileforecastforSpain(LHS)andtheUSA(RHS)forthe

year2011. Inadditiontothepointforecasts(orangeline),theconfidenceintervalsfor

differentsignificancelevels(2%,10%,25%,50%,75%,90%,and98%)areplotted. The

primaryy-axisrepresentstheaccumulatedlogarithmicgrowthrate,whilethesecondary

y-axisprovidesinformationofwhichofthepreviousperiodshasmoreimportanceineach

prediction.Thisaspectisobtainedbyanalyzingtheattentionweights.Asexpected,the

GreatRecessionhasagreatimportance.

Figure7.2011quantileforecastforSpain(lefthandside)andtheUSA(righthandside).

Figure 8 shows the encoder variables importance for the 2011 forecast. Variable

time_idx,whichrepresentsthetemporalsequence,isthemostimportantone,followed

bytheWorldTradeVolumeIndex, theautoregressivecomponent, theOECDLeading

Indicator,andtheCRBRawIndustrialSpotIndex. Otherwise,theprivatedebttoGDP

ratioandourproxyofglobalcreditspreadcycle(USACreditSpread)arenotasrelevant,

asmostofprivatedeleveragingprocessalreadyoccurred.Finally,theyieldcurvespread

predictivepowerisalmostinsignificant.

Figure8.Encodervariablesimportancefortheyear2011forecast.

Figure9displaysthequantileforecastingresultsforSpain(LHS)andtheUSA(RHS)

in2017,includingthepredictedvaluescomparedtotheobservedones,theprediction

intervals,andtherelativeimportanceofeachlagintheforecast(greyline).

192

Mathematics2023,11,2625

Figure9.2017quantileforecastforSpain(lefthandside)andUSA(righthandside).

Figure10depictstheencodervariablesimportanceforthe2017forecast.Thevariable

thatcapturesthetemporalsequence(time_idx)isrevealedasthemostimportantone,

followedbytheautoregressivecomponentandtheOECDleadingindicator.

Figure10.Encodervariablesimportanceforthe2017forecast.

6.ConcludingRemarks

The main contribution of this paper is that it is the first to apply a new artificial

intelligencearchitecture,TFTs,recentlydevelopedby[14],tothejointforecastingofGDP

growthforalargenumberofOECDcountriesatdifferenttimehorizons.Itsrelevancelies

inthefactthatthisAIarchitectureoffersimportantcomparativeadvantagesoverregression

modelsandotherdeeplearningmethodsinacontextwherethetimeseriescharacteristics

ofbusinesscycleindicatorsareaffectedbylong-runnon-linearities.Mainly,itenablesthe

trainingofthemodelonmultipletimeseriesfromdifferentdistributions;itallowsfor

visualizingpersistenttemporalpatternsandidentifyingsignificanteventsanddifferent

regimes,providingquantileregressionsforforecastsandinterpretableresultssincethe

impactofeachexplanatoryvariableisquantified.

Futureresearchaimstoreinforceandimprovetheresultsobtained,incorporating

additionallycountriesandmoreexplanatoryvariables.Furthermore,itwillbenecessaryto

comparetheirresultswithmodelsthataremuchricherthanbaselineARIMAmodels,both

regressionmodels(dynamicfactormodels[110])anddeeplearningmodels,especiallystate-

of-the-artmethodssuchasthesampleconvolutionandinteractionnetwork(SCINet)[111],

Informer[112],DeepAR[84],orfrequencyimprovedlegendrememorymodel(FiLM)[113].

The results of the joint GDP forecasting of 25 OECD countries at different time

horizons—one,two,three,andfourquarters—usingmacroeconomicandfinancialvariables

outperformthoseobtainedwiththebenchmark(ARIMA)intermsofboththeMAEand

theRMSE,especiallyinperiodsofturbulence,suchastheCOVID-19shock.Theobtained

resultsshowthatTFTforecastsimprovementsaregreaterinthedemand-drivengrowth

countriesthaninexport-ledgrowthones.

193

Mathematics2023,11,2625

TheuseofTFTstopredictrealGDPyieldsveryinterestingresultsregardingthe

importanceoftheexplanatoryvariables.Therelativeimportanceofvariablesmightvary

somewhat,dependingonthephaseoftheeconomiccycleortheforecasttimehorizon.

ItisremarkablethepredictivecapacityoftheautoregressivecomponentandtheOECD

compositeleadingindicator,inadditiontotheCRBRawIndustrialSpotIndex,aswellas

thevariablethatcapturestheindebtednessofthenon-financialprivatesectors,whichis

relatedtoourproxyofglobalcreditspreadcycle(USACreditSpread),andtheworldtrade

indicator.Ontheoppositeside,itisworthhighlightingthelowpredictivepowerofthe

slopeoftheyieldcurve.

FutureresearchshouldexploittheonemainabilityofTFTs,whichisthepossibilityof

incorporatingtheeffectsofknownfutureinputsinthepredictions.Itallowspolicymakers

toperformtheimpactassessmentofchangesininstrumentaleconomicvariables,suchas

interestrates,taxes,etc.Giventhatoneofthefindingsinthispaperaretheimportanceof

privatedebtinforecastingrealGDP,thisframeworkcouldbeusedtosimulatetheeffects

ofcredittighteningmeasures.

Finally,itwouldbeveryinterestingtoexploitoneofthemostoutstandingfeaturesof

TFTs,thepossibilityofidentifyingdifferenteconomicregimes.Severalstudies([114–116])

suggestthehypothesisthat,inthelastdecades,theonlysourceofgrowthinthewestern

countriesisbubblegeneration(financialorrealestate).ThisnewAIarchitecturewouldbe

usefultoidentifytheblow-upperiodsandthesubsequentburstingones.

Inshort,TFTsarerevealedasanewAItoolavailabletoeconomistsandpolicymakers,

withenormouspotentialinthepredictionofeconomiccycles.

AuthorContributions:Allauthorshavecontributedequally.Allauthorshavereadandagreedto

thepublishedversionofthemanuscript.

Funding:Thisresearchreceivednoexternalfunding.

DataAvailabilityStatement:Dataavailableonrequest.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

AppendixA.OneSidedTestsfortheOutperformingofTFTGDPForecastwith

RespecttheBenchmarkARIMA

WeformallytesttheimprovementoftheMAEandRMSEmetricsofTFTrelative

toARIMAusingthebootstrapone-sidedtest. Thenullhypothesisisthatthedifference

betweenthemetricsofbothestimationproceduresisnotsignificantagainstthealternative

hypothesisofthemetric,fortheTFTislowerthanthatfortheARIMA.Wecomputethe

99%criticalvalueofthedistributionoftheTFTmetric(MAEorRMSE)usingbootstrap

resampling.Then,wecalculatethepercentagedifferenceoftheARIMAmetric(MAEor

RMSE,respectively)relativetothisbootstrapcriticalvalue.AsshowninTableA1,forboth

metrics,allthetest-statisticsforperiodsgreaterthanonequarterarepositive.Therefore,

wecanconcludethatTFToutperformsARIMAatthe99%significancelevelformost

predictionhorizons.

TableA1. PercentagedifferenceoftheARIMAperformancemetric(MAEandRMSE)ofARIMA

relativetothe99%criticalvalueofthebootstrapdistributionfortheTFTmetric.

Metric t+1 t+2 t+3 t+4

MAE −18.59% 8.21% 25.02% 26.22%

RMSEa −20.05% 60.46% 118.43% 120.20%

aRMSEistheaverageoftheRMSEcalculatedatcountrylevel.

194

Mathematics2023,11,2625

AppendixB.CodeforAnnualForecast

195

Mathematics2023,11,2625

196

Mathematics2023,11,2625

197

Mathematics2023,11,2625

198

Mathematics2023,11,2625

References

1. Stockhammer,E.Financialisationandtheslowdownofaccumulation.Camb.J.Econ.2004,28,719–741.[CrossRef]

2. Christodoulou-Volos,C.;Siokis,F.M.Long-rangedependenceinstockmarketreturns.Appl.Financ.Econ.2006,16,1331–1338.

[CrossRef]

3. Murialdo,P.;Ponta,L.;Carbone,A.Long-rangedependenceinfinancialmarkets:Amovingaverageclusterentropyapproach.

Entropy2020,22,634.[CrossRef][PubMed]

4. Estrella,A.;Mishkin,F.S.;Predicting,U.S.recessions:Financialvariablesasleadingindicators.Rev.Econ.Stat.1998,80,45–61.

[CrossRef]

5. Chauvet,M.;Potter,S.Forecastingrecessionsusingtheyieldcurve.J.Forecast.2005,24,77–103.[CrossRef]

6. Estrella,A.Whydoestheyieldcurvepredictoutputandinflation?Econ.J.2005,11,722–744.[CrossRef]

7. Kauppi,H.;Saikkonen,P.PredictingUSrecessionswithdynamicbinaryresponsemodels.Rev.Econ.Stat.2008,90,777–791.

[CrossRef]

8. Katayama,M.ImprovingRecessionProbabilityForecastsintheUSEconomy;WorkingPaper;LouisianaStateUniversity: Baton

Rouge,LA,USA,2009.

9. Hamilton,J.D.Callingrecessionsinrealtime.Int.J.Forecast.2011,27,1006–1026.[CrossRef]

10. VanDijk,D.;Franses,P.H.;Paap,R.Anonlinearlongmemorymodel,withanapplicationtoUSunemployment.J.Econom.2002,

110,135–165.[CrossRef]

11. Cuestas,J.C.;Garratt,D.IsrealGDPpercapitaastationaryprocess?Smoothtransitions,nonlineartrendsandunitroottesting.

Empir.Econ.2011,41,555–563.[CrossRef]

12. Choudhry,T.;Papadimitriou,F.I.;Shabi,S.Stockmarketvolatilityandbusinesscycle: Evidencefromlinearandnonlinear

causalitytests.J.Bank.Financ.2016,66,89–101.[CrossRef]

13. Cerra,M.V.;Fatás,A.;Saxena,M.S.C.HysteresisandBusinessCycles;InternationalMonetaryFund:Washington,DC,USA,2020.

14. Lim,B.;Arık,S.Ö.;Loeff,N.;Pfister,T.TemporalFusionTransformersforInterpretableMulti-HorizonTimeSeriesForecasting.

Int.J.Forecast.2021,37,1748–1764.[CrossRef]

15. Minsky,H.P.StabilizinganUnstableEconomy;YaleUniversityPress:NewHaven,CT,USA,1986.

16. Minsky, H.P.ThefinancialInstabilityHypothesis; WorkingPaper74; TheJeromeLevyEconomicsInstituteofBardCollege:

Annandale-On-Hudson,NY,USA,1992.

17. Caporale,G.M.;Gil-Alana,L.A.;Malmierca,M.Persistenceintheprivatedebt-t-GDPratio:Evidencefrom43OECDcountries.

Appl.Econ.2021,53,5018–5027.[CrossRef]

18. Stock,J.H.;Watson,M.W.Forecastingoutputandinflation:Theroleofassetprices.J.Econ.Lit.2003,41,788–829.[CrossRef]

19. Harvey,C.Therealtermstructureandconsumptiongrowth.J.Financ.Econ.1988,22,305–333.[CrossRef]

20. Laurent,R.D.Aninterestrate-basedindicatorofmonetarypolicy.Econ.Perspect.1988,12,3–14.

21. Estrella,A.;Hardouvelis,G.Thetermstructureasapredictorofrealeconomicactivity.J.Financ.1991,46,555–576.[CrossRef]

22. Estrella,A.;Mishkin,F.S.ThetermstructureofinterestratesanditsroleinmonetarypolicyinEuropeandtheUnitedStates:

ImplicationsfortheEuropeanCentralBank.Eur.Econ.Rev.1997,41,1375–1401.[CrossRef]

23. Bernard,H.;Gerlach,S.Doesthetermstructurepredictrecessions? Theinternationalevidence. Int. J.Financ. Econ. 1998,

3,195–215.[CrossRef]

24. Taylor,J.B.Discretionversuspolicyrulesinpractice.J.Monet.Econ.1993,39,195–214.[CrossRef]

25. Gilchrist,S.;Yankov,V.;Zakrajšek,E.Creditmarketshocksandeconomicfluctuations:Evidencefromcorporatebondandstock

markets.J.Monet.Econ.2009,56,471–493.[CrossRef]

26. Gilchrist,S.;Zakrajšek,E.Creditspreadsandbusinesscyclefluctuations.Am.Econ.Rev.2012,102,1692–1720.[CrossRef]

199

Mathematics2023,11,2625

27. Faust, J.; Gilchrist, S.; Wright, J.H.; Zakrajšek, E.Creditspreadsaspredictorsofreal-timeeconomicactivity: ABayesian

model-averagingapproach.Rev.Econ.Stat.2013,95,1501–1519.[CrossRef]

28. Bleaney,M.;Mizen,P.;Veleanu,V.BondspreadsandeconomicactivityineightEuropeaneconomies.Econ.J.2016,126,2257–2291.

[CrossRef]

29. Okimoto,T.;Takaoka,S.ThetermstructureofcreditspreadsandbusinesscycleinJapan.J.Jpn.Int.2017,45,27–36.[CrossRef]

30. Okimoto,T.;Takaoka,S.ThecreditspreadcurvedistributionandeconomicfluctuationsinJapan.J.Int.MoneyFinanc.2022,

122,102582.[CrossRef]

31. Gilchrist,S.;Mojon,B.CreditriskintheEuroarea.Econ.J.2018,128,118–158.[CrossRef]

32. Hamilton,J.D.;Pérez-Quirós,G.DotheLeadingIndicatorsLead?J.Bus.1996,69,27–49.[CrossRef]

33. Banerjee,T.;Marcellino,M.ArethereanyreliableleadingindicatorsforUSinflationandGDPgrowth? Int.J.Forecast. 2006,

22,137–151.[CrossRef]

34. Kulendran,N.;Wong,K.F.DeterminantsversusCompositeLeadingIndicatorsinPredictingTurningPointsinGrowthCycle.J.

TravelRes.2011,50,417–430.[CrossRef]

35. Tkacova,A.;Gavurova,B.;Behun,M.TheCompositeLeadingIndicatorforGermanBusinessCycle.J.Compet.2017,9,114–133.

[CrossRef]

36. OECD.CompositeLeadingIndicator(CLI).2023.Availableonline:https://data.oecd.org/leadind/composite-leading-indicator-

cli.htm(accessedon2May2023).

37. Hanson,M.S.The“pricepuzzle”reconsidered.J.Monet.Econ.2004,51,1385–1413.[CrossRef]

38. Beckmann,J.;Belke,A.;Czudaj,R.Doesgloballiquiditydrivecommodityprices?J.Bank.Financ.2014,48,224–234.[CrossRef]

39. Belke,A.;Bordon,I.;Hendricks,T.W.Monetarypolicy,globalliquidityandcommoditypricedynamics.N.Am.J.Econ.Financ.

2014,28,1–16.[CrossRef]

40. Yardeni,E.PredictingtheMarkets;YRIPress:Brookville,NY,USA,2018.

41. Ge,Y.;Tang,K.CommoditypricesandGDPgrowth.Int.Rev.FinancialAnal.2020,71,101512.[CrossRef]

42. Mian,A.R.;Sufi,A.Financeandbusinesscycles:Thecredit-drivenhouseholddemandchannel.J.Econ.Perspect.2018,32,31–58.

[CrossRef]

43. Minsky,H.P.CanItHappenAgain?M.E.Sharpe:NewYork,NY,USA,1984.

44. Minsky,H.P.TheFinancialInstabilityProcess: ARestatement;PostKeynesianEconomicTheory;Arestis,P.,Shouras,T.,Eds.;

WheatsheafBooks:Sussex,UK,1985.

45. Singh,T.DoesInternationalTradeCauseEconomicGrowth?ASurvey.WorldEcon.2010,33,1517–1564.[CrossRef]

46. Esteves,P.S.;Rua,A.Istherearolefordomesticdemandpressureonexportperformance?Empir.Econ.2015,49,1173–1189.

[CrossRef]

47. Bobeica,E.;Esteves,P.S.;Rua,A.;Staehr,K.Exportsanddomesticdemandpressure:Adynamicpaneldatamodelfortheeuro

areacountries.Rev.WorldEcon.2016,152,107–125.[CrossRef]

48. Laborda,J.;Salas,V.;Suárez,C.Manufacturingfirms’exportactivity:Businessandfinancialcyclesoverlaps!Int.Econ.2020,

162,1–14.[CrossRef]

49. Frankel,J.A.;Rose,A.K.Theendogeneityoftheoptimumcurrencyareacriteria.Econ.J.1998,108,1009–1025.[CrossRef]

50. Clark,T.E.;VanWincoop,E.Bordersandbusinesscycle.J.Int.Econ.2001,55,59–85.[CrossRef]

51. DeSoyres,F.;Gaillard,A.GlobaltradeandGDPcomovement.J.Econ.Dyn.Control2022,138,104353.[CrossRef]

52. Imbs,J.Trade,finance,specializationandsynchronization.Rev.Econ.Stat.2004,86,723–734.[CrossRef]

53. Box,G.;Jenkins,G.M.TimeSeriesAnalysis;ForecastingandControl;Holden-Day:SanFrancisco,CA,USA,1970.

54. Kirchgässner,G.;Wolters,J.;Hassler,U.Univariatestationaryprocesses.InIntroductiontoModernTimeSeriesAnalysis;Springer:

Berlin/Heidelberg,Germany,2013;pp.27–93.[CrossRef]

55. Chatfield,C.TheAnalysisofTimeSeries:AnIntroduction;CRCPress:BocaRaton,FL,USA,2016.

56. Sims,C.A.Macroeconomicsandreality.Econometrica1980,48,1–48.[CrossRef]

57. Hamilton,J.D.Anewapproachtotheeconomicanalysisofnonstationarytimeseriesandthebusinesscycle.Econometrica1989,

57,357–384.[CrossRef]

58. Litterman,R.B.Forecastingwithbayesianvectorautoregressions-Fiveyearsofexperience. J.Bus. Econ. Stat. 1986,4,25–38.

[CrossRef]

59. Spencer,D.E.Developingabayesianvectorautoregressionforecastingmodel.Int.J.Forecast.1993,9,407–421.[CrossRef]

60. Bernanke,B.;Blinder,A.TheFederalfundsrateandthechannelsofmonetarytransmission.Am.Econ.Rev.1992,82,901–921.

61. Sims,C.A.Interpretingthemacroeconomictimeseriesfacts:Theeffectsofmonetarypolicy.Eur.Econ.Rev.1992,36,975–1000.

[CrossRef]

62. D'Agostino,A.;Gambetti,L.;Giannone,D.Macroeconomicforecastingandstructuralchange.J.Appl.Econ.2013,28,82–101.

[CrossRef]

63. Korobilis,D.VARforecastingusingbayesianvariableselection.J.Appl.Econ.2013,28,204–230.[CrossRef]

64. Koop,G.;Korobilis,D.Largetime-varyingparameterVARs.J.Econom.2013,177,185–198.[CrossRef]

65. Terasvirta,T.;Anderson,H.M.Characterizingnonlinearitiesinbusinesscyclesusingsmoothtransitionautoregressivemodels.J.

Appl.Econ.1992,7,S119–S136.[CrossRef]

200

Mathematics2023,11,2625

66. Granger,C.W.;Teräsvirta,T.;Anderson,H.M.Modelingnonlinearityoverthebusinesscycle.InBusinessCycles,Indicatorsand

Forecasting;UniversityofChicagoPress:Chicago,IL,USA,1993;pp.311–326.

67. Granger,C.W.;Terasvirta,T.ModellingNon-LinearEconomicRelationships;OUPCatalogue:Oxford,UK,1993.

68. Escribano,A.;Jorda,O.ImprovedTestingandSpecificationofSmoothTransitionRegressionModels;NonlinearTimeSeriesAnalysisof

EconomicandFinancialData;Springer:Boston,MA,USA,1999;pp.289–319.

69. Tsay,R.S.Testingandmodellingthresholdautoregressiveprocesses.J.Am.Stat.Assoc.1989,84,231–240.[CrossRef]

70. Tiao,G.C.;Tsay,R.S.Someadvancesinnon-linearandadaptivemodellingintimeseries.J.Forecast.1994,13,109–131.[CrossRef]

71. Chen,R.;Langnau,A.TurningPointsDetectionofBusinessCycles: AModelComparison. 2010. Availableonline: https:

//ssrn.com/abstract=1680828(accessedon1May2023).[CrossRef]

72. Hamilton,J.D.SpecificationtestinginMarkov-switchingtime-seriesmodels.J.Econom.1996,70,127–157.[CrossRef]

73. Filardo,A.J.Business-cyclephasesandtheirtransitionaldynamics.J.Bus.Econ.Stat.1994,12,299–308.[CrossRef]

74. McCulloch,R.E.;Tsay,R.S.StatisticalanalysisofeconomictimeseriesviaMarkovswitchingmodels. J.TimeSer. Anal. 1994,

15,523–539.[CrossRef]

75. Filardo,A.J.;Gordon,S.F.Businesscycledurations.J.Econom.1998,85,99–123.[CrossRef]

76. Kim,C.J.;Nelson,C.R.StateSpaceModelswithRegimeSwitching:ClassicalandGibbs-SamplingApproacheswithApplications;MIT

Press:Cambridge,MA,USA,1999.

77. Camacho,M.;Perez-Quiros,G.;Poncela,P.ExtractingNonlinearSignalsfromSeveralEconomicIndicators;BankofSpainWorking

Paper1202;BankofSpain:Madrid,Spain,2012.

78. Camacho,M.;Perez-Quiros,G.;Poncela,P.Markov-SwitchingDynamicFactorModelsinRealTime;BankofSpainWorkingPaper

1205;BankofSpain:Madrid,Spain,2012.

79. Krolzig,H.M.Markov-SwitchingVectorAutoregressions:Modelling,StatisticalInference,andApplicationtoBusinessCycleAnalysis;

SpringerScience&BusinessMedia:Berlin,Germany,2013;Volume454.

80. Balcilar,M.;Gupta,R.;Majumdar,A.;Miller,S.M.WastherecentdownturninUSrealGDPpredictable? Appl. Econ. 2015,

47,2985–3007.[CrossRef]

81. Mullainathan,S.;Spiess,J.Machinelearning:Anappliedeconometricapproach.J.Econ.Perspect.2017,31,87–106.[CrossRef]

82. Varian,H.R.Bigdata:Newtricksforeconometrics.J.Econ.Perspect.2014,28,3–28.[CrossRef]

83. Yu,H.F.;Rao,N.;Dhillon,I.S.Temporalregularizedmatrixfactorizationforhigh-dimensionaltimeseriesprediction.InProceed-

ingsoftheAdvancesinNeuralInformationProcessingSystemsNeurIPSProceedings,Barcelona,Spain,5–10December2016.

84. Salinas,D.;Flunkert,V.;Gasthaus,J.;Januschowski,T.DeepAR:Probabilisticforecastingwithautoregressiverecurrentnetworks.

Int.J.Forecast.2020,36,1181–1191.[CrossRef]

85. Plakandaras,V.;Gupta,R.;Gogas,P.;Papadimitriou,T.ForecastingtheUSrealhousepriceindex.Econ.Model.2015,45,259–267.

[CrossRef]

86. Heber,G.;Lunde,A.;Shephard,N.;Sheppard,K.Oxford-ManInstitute’sRealizedLibrary;Version0.1;UniversityOfOxford:

Oxford,UK,2009.

87. Medeiros,M.C.;Vasconcelos,G.F.R.;Veiga,Á.;Zilberman,E.Forecastinginflationinadata-richenvironment:Thebenefitsof

machinelearningmethods.J.Bus.Econ.Stat.2019,39,98–119.[CrossRef]

88. Inoue,A.;Kilian,L.Howusefulisbagginginforecastingeconomictimeseries?ACasestudyofUSconsumerpriceinflation.J.

Am.Stat.Assoc.2008,103,511–522.[CrossRef]

89. Rahmani,A.M.;Yousefpoor,E.;Yousefpoor,M.S.;Mehmood,Z.;Haider,A.;Hosseinzadeh,M.;AliNaqvi,R.MachineLearning

(ML)inmedicine:Review,applications,andchallenges.Mathematics2021,9,2970.[CrossRef]

90. Jönsson,K.MachineLearningandNowcastsofSwedishGDP.J.Bus.CycleRes.2020,16,123–134.[CrossRef]

91. Cicceri,G.;Inserra,G.;Limosani,M.Amachinelearningapproachtoforecasteconomicrecessions—AnItaliancasestudy.

Mathematics2020,8,241.[CrossRef]

92. Maccarrone,G.;Morelli,G.;Spadaccini,S.GDPforecasting:Machinelearning,linearorautoregression?Front.Artif.Intell.2021,

4,757864.[CrossRef][PubMed]

93. Biau,O.;D’Elia,A.EuroAreaGDPForecastUsingLargeSurveyDataset—ARandomForestApproach;EuroindicatorsWorkingPaper

2011/002;EuropeanCommission:Brussels,Belgium,2011.

94. Tiffin,M.A.SeeingintheDark:AMachine-LearningApproachtoNowcastinginLebanon;InternationalMonetaryFund:Washington,

DC,USA,2016.

95. Behrens,C.;Pierdzioch,C.;Risse,M.Atestofthejointefficiencyofmacroeconomicforecastsusingmultivariaterandomforests.

J.Forecast.2018,37,560–572.[CrossRef]

96. Prüser,J.Forecastingwithmanypredictorsusingbayesianadditiveregressiontrees.J.Forecast.2019,38,621–631.[CrossRef]

97. Foltas,A.;Pierdzioch,C.OntheefficiencyofGermangrowthforecasts:Anempiricalanalysisusingquantilerandomforestsand

densityforecasts.Appl.Econ.Lett.2021,29,1644–1653.[CrossRef]

98. Yoon,J.ForecastingofrealGDPgrowthusingmachinelearningmodels:Gradientboostingandrandomforestapproach.Comput.

Econ.2021,57,247–265.[CrossRef]

99. Chai,S.H.;Lim,J.S.Forecastingbusinesscyclewithchaotictimeseriesbasedonneuralnetworkwithweightedfuzzymembership

functions.ChaosSolitonsFractals2016,90,118–126.[CrossRef]

201

Mathematics2023,11,2625

100. Jung,J.K.;Patnam,M.;Ter-Martirosyan,A.AnAlgorithmicCrystalBall:Forecasts-BasedonMachineLearning;InternationalMonetary

Fund:Washington,DC,USA,2018.

101. Alaminos,D.;Salas,M.B.;Fernández-Gámez,M.A.QuantumcomputinganddeeplearningmethodsforGDPgrowthforecasting.

Comput.Econ.2022,59,803–829.[CrossRef]

102. Emsia,E.;Coskuner,C.Economicgrowthpredictionusingoptimizedsupportvectormachines.Comput.Econ.2016,48,453–462.

[CrossRef]

103. Kouziokas,G.N.AnewW-SVMkernelcombiningPSO-neuralnetworktransformedvectorandbayesianoptimizedSVMinGDP

forecasting.Eng.Appl.Artif.Intell.2020,92,103650.[CrossRef]

104. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Polosukhin,I.Attentionisallyouneed.Advancesin

NeuralInformationProcessingSystemsNeurIPSProceedings.InProceedingsofthe31stConferenceonNeuralInformation

ProcessingSystems,LongBeach,CA,USA,4–9December2017.

105. Koo, R. Balance Sheet Recession: Japan’s Struggle with Uncharted Economics and Its Global Implications; John Wiley & Sons:

Singapore,2003.

106. Koo,K.TheHolyGrailofMacroeconomics:LessonsfromJapan’sGreatRecession;JohnWiley&Sons:Singapore,2009.

107. Laborda,J.;Salas,V.;Suárez,C.FinancialconstraintsonR&DprojectsandMinskymoments:Containingthecreditcycle.J.Evol.

Econ.2021,31,1089–1111.[CrossRef]

108. Mian,A.;Straub,L.;Sufi,A.Indebteddemand.Q.J.Econ.2021,136,2243–2307.[CrossRef]

109. Armelius,H.;Belfrage,C.J.;Stenbacka,H.Themysteryofthemissingworldtradegrowthaftertheglobalfinancialcrisis.Sver.

RiksbankEcon.Rev.2014,3,7–22.

110. Barhoumi,K.;Darné,O.;Ferrara,L.Dynamicfactormodels:Areviewoftheliterature.OECDJ.J.Bus.CycleMeas.Anal.2013,2.

[CrossRef]

111. Liu,M.;Zeng,A.;Chen,M.;Xu,Z.;Lai,Q.;Ma,L.;Xu,Q.Scinet:Timeseriesmodelingandforecastingwithsampleconvolution

andinteraction.Adv.NeuralInf.Process.Syst.2022,35,5816–5828.

112. Zhou,H.;Zhang,S.;Peng,J.;Zhang,S.;Li,J.;Xiong,H.;Zhang,W.Informer:Beyondefficienttransformerforlongsequence

time-seriesforecasting.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Virtually,2–9February2021;Volume35,

pp.11106–11115.

113. Zhou,T.;Ma,Z.;Wen,Q.;Sun,L.;Yao,T.;Yin,W.;Jin,R.Film:FrequencyimprovedLegendrememorymodelforlong-termtime

seriesforecasting.Adv.NeuralInf.Process.Syst.2022,35,12677–12690.

114. Gordon,R.J.IsUSEconomicGrowthOver?FalteringInnovationConfrontstheSixHeadwinds;NationalBureauofEconomicResearch:

Cambridge,MA,USA,2012;p.w18315.

115. Summers,L.H.USeconomicprospects:Secularstagnation,hysteresis,andthezerolowerbound.Bus.Econ.2014,49,65–73.

[CrossRef]

116. Summers,L.H.Demandsidesecularstagnation.Am.Econ.Rev.2015,105,60–65.[CrossRef]

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

202

mathematics

Article

NSNet: An N-Shaped Convolutional Neural Network with

Multi-Scale Information for Image Denoising

YifenLi1andYuanyangChen2,*

1 SchoolofEconomicsandManagement,ChangshaUniversity,Changsha410022,China

2 SchoolofAutomation,CentralSouthUniversity,Changsha410083,China

* Correspondence:204612129@csu.edu.cn

Abstract:Deeplearningmodelswithconvolutionaloperatorshavereceivedwidespreadattention

fortheirgoodimagedenoisingperformance.However,sincetheconvolutionaloperationprefers

toextractlocalfeatures,theextractedfeaturesmaylosesomeglobalinformation,suchastexture,

structure,andcolorcharacteristics,whentheobjectintheimageislarge.Toaddressthisissue,this

paperproposesanN-shapedconvolutionalneuralnetworkwiththeabilitytoextractmulti-scale

featurestocapturemoreusefulinformationandalleviatetheproblemofglobalinformationloss.The

proposednetworkhastwomainparts:amulti-scaleinputlayerandamulti-scalefeatureextraction

layer.Theformerusesatwo-dimensionalHaarwavelettocreateanimagepyramid,whichcontains

thecorruptedimage’shigh-andlow-frequencycomponentsatdifferentscales. Thelatterusesa

U-shapedconvolutionalnetworktoextractfeaturesatdifferentscalesfromthisimagepyramid.The

methodsetsthemean-squarederrorasthelossfunctionandusestheresiduallearningstrategyto

learntheimagenoisedirectly.Comparedwithsomeexistingimagedenoisingmethods,theproposed

methodshowsgoodperformanceingrayandcolorimagedenoising,especiallyintexturesand

contours.

Keywords:imagedenoising;wavelettransform;Unet;imagepyramid;multi-scalefeatures

MSC:68U10

Citation:Li,Y.;Chen,Y.NSNet:An

N-ShapedConvolutionalNeural 1.Introduction

NetworkwithMulti-Scale Imagedenoisingisoneofthebasictasksofcomputervisionandisofwideinterest

InformationforImageDenoising. toacademiaandindustry,asitcaneffectivelyimproveimagequality. Thepurposeof

Mathematics2023,11,2772. https:// imagedenoisingistoremovenoisefromacorruptedimageandrestoreitsoriginalcontent

doi.org/10.3390/math11122772 asmuchaspossible.Inmanycomputervisiontasks,imagedenoisingisoftenusedasa

AcademicEditor:JakubNalepa preprocessingmethodtoimprovethepracticalperformanceofadvancedcomputervision

tasks[1].Overthepastfewdecades,manyoutstandingimagedenoisingmethods,asshown

Received:4June2023 inFigure1,havebeenproposed,includingfiltering-based[2,3],sparse-representation-

Revised:15June2023

based[4–8],external-prior-based[9–12],low-rank-representation-based[13,14],anddeep-

Accepted:18June2023

learning-basedmethods[15–18].

Published:19June2023

Filtering-basedmethodswerethefirsttechniquestobeappliedtoimagedenoising

andrelyontheself-similarityofimages.Well-knownapproachesincludeGaussianfiltering,

meanfiltering,andmedianfiltering. Thesethreemethodsassumethatthepixelsinan

Copyright: ©2023bytheauthors. imagedonotexistinisolationandhaveconnectionstootherpixels. However,Buades

Licensee MDPI, Basel, Switzerland. etal.[2]foundthatsimilarpixelsarenotlimitedtolocalareas,andmakingfulluseofthe

Thisarticleisanopenaccessarticle redundantinformationinanimagecanimprovetheimagedenoisingperformance.Hence,

distributed under the terms and theyproposed anonlocalmeanfilteringmethod(NLM)basedonexistingsmoothing

conditionsoftheCreativeCommons filteringmethods.AlthoughNLMcanachievegooddenoisingperformance,itneedsto

Attribution(CCBY)license(https:// findasufficientnumberofsimilarblockswhencomputingeachpixel,whichgivesithigh

creativecommons.org/licenses/by/

4.0/).

Mathematics2023,11,2772.https://doi.org/10.3390/math11122772 https://www.mdpi.com/journal/mathematics

203

Mathematics2023,11,2772

computationalcomplexity. Tosolvethisproblem,Kostadinetal.[3]proposedablock-

matchingand3Dfiltering(BM3D)method,whichhasagooddenoisingperformanceand

fastcomputationalspeed.

Figure1.Classificationofimagedenoisingmethods.

Sparse-representation-basedmethodsarebasedonimagesparsityandachieveimage

denoising by training an over-complete dictionary. A more representative case is the

K-singularvaluedecomposition(KSVD)methodusingsparserepresentation[4].Inspired

byKSVD,Mairaletal.[5]combinedimageself-similaritywithsparsecodingtodecompose

similarpatchesusingsimilarsparsepatterns,thusformingaLearnedSimultaneousSparse

Coding(LSSC)method.Althoughsparserepresentationmodelshaveshowngoodresults

inimagedenoising,thesparserepresentationoftraditionalmodelsmaynotbeaccurate

enoughduetothedegradationoftheobservedimages.Tofurtherimprovetheperformance

ofimagedenoisingbasedonsparserepresentation,Dongetal.[6]proposedanonlocally

centralizedsparserepresentation(NCSR),whichtransformedthedenoisingprobleminto

aproblemofsuppressingsparsecodingnoise.Inaddition,becausethesparsecodingof

imagesusingasingletransformcanlimitperformance,Wenetal.[7]proposedastructured

over-complete sparsifying transform model with block cosparsity (OCTOBOS). These

methods[4–7]haveexhibitedgoodresultsindenoisingadditiveGaussianwhitenoise

(AWGN);however,itisdifficulttoobtaingoodperformanceinrealimagedenoising.To

achievebetterdenoisingofrealimages,Xuetal.[8]proposedatrilateralweightedsparse

codingscheme(TWSC).

External-prior-basedmethodsrealizeimagedenoisingbyusingthestatisticalproper-

tiesofnaturalimages.Arepresentativemethodisthedenoisingmethodbasedonexpected

patchloglikelihood(EPLL)proposedbyZoranandWeiss[9]. Thismethodappliesthe

Gaussianmixturemodeltolearnpriorknowledgefromalargenumberofnaturalimage

blocksandappliesittothedenoisingofothernaturalimages.SimilartoEPLL,Xuetal.[10]

proposedapatchgroupprior-baseddenoisingmethod(PGPD)tolearntheself-similar

featuresofnaturalimagesfromgroupsofsimilarpatchesusingtheGaussianmixturedistri-

bution.InspiredbyEPLL,Chenetal.[11]proposedanexternalpatchprior-guidedinternal

clusteringapproachbycombininganimageexternalpriorandaninternalself-similarity

prior,whichisnamedPCLR.Toimprovethetexturerestorationcapabilityoftheimage

denoisingmethod,Zouetal.[12]proposedagradienthistogrampreservationmethod

(GHP)basedontextureenhancement.GHPimprovestexturerecoverybypreservingthe

gradientdistributionofthecorruptedimage.

Low-rankrepresentation-basedmethodsexploitthelow-rankpropertiesofnatural

imagesandachievedenoisingbyextractingtheirlow-rankcomponents.Atypicalcaseis

theWeightedNuclearNormMinimization(WNNM)proposedbyGuetal.[13].Low-rank

matrixfactorizationisalsoamethodusedtoextractlow-rankcomponentsfromadataset

andisoftenappliedincaseswheretheimagesizeislargeanditsrankismuchsmaller

thanthelengthandwidthofthedataset.Themostwell-knownmethodisthelow-rank

matrixfactorizationbasedonvariationalBayesian(VBMFL),whichwasproposedbyZhao

204

Mathematics2023,11,2772

etal.[14].ThismethodimprovestherobustnessofthemodeltooutliersbyusingaLaplace

distributiontoestablishanoisemodel.

Deep-learning-baseddenoisingmethodsarecurrentlythemostpopular.Theyusually

learnthedirectmappingfromthecorruptedimagetothecleanimageorthenoise.Since

deep-learning-baseddenoisingmethodsdonotrelyonimagepriori(e.g.,self-similarity,

sparsity,gradient,statisticalproperties,andlow-rankproperties),theydonothaveto

spendmuchtimefindingandprocessingsimilarblocksintheimages. Thus,theynot

onlyachieveagooddenoisingperformancebutalsohaveafastinferencespeed.Schmidt

etal.[15]proposedamethodbasedonacascadeofshrinkagefields(CSF)toimprove

thedenoisingperformancewhileconsideringcomputationalefficiency. Chenetal.[16]

extendedconventionalnonlinearreaction–diffusionmodelswithseveralparametrized

linearfiltersaswellasseveralparametrizedinfluencefunctionsandproposedatrainable

nonlinearreaction–diffusionmethod(TNRD).AlthoughCSFandTNRDshowgooddenois-

ingperformance,theycanonlyprovidethebestdenoisingresultsatknownnoiselevels.

Tosolvetheproblemofblindimagedenoising,Zhangetal.[17]proposedadeeplearning

methodusingadenoisingconvolutionalneuralnetwork(DnCNN),whichwasthefirst

applicationofresiduallearningtogeneralimagedenoising. Theapplicationofresidual

learningtoimagedenoisinghasgreatlyimprovedthedenoisingperformanceofnetworks

andinspiredmanyoutstandingdenoisingmethodsbasedondeeplearning[17–22]. In

addition,Zhangetal.[18]furtherimprovedtheDnCNNandproposedafastandflexible

denoisingconvolutionalneuralnetwork(FFDNet),whichachievesagoodtrade-offbe-

tweentheinferencespeedanddenoisingperformancebydownsamplingandmanually

inputtinganoiseestimationmap.Binhetal.[23]combinedDnCNNwithResNetandpro-

posedaconvolutionaldenoisingneuralnetworkcalledFlashLightCNN.Acomplex-valued

deepconvolutionalneuralnetworkcalledCDNetwasproposedbyQuanetal.[24],andit

effectivelyimprovedthedenoisingperformanceofthenetwork.Guanetal.[25]proposed

animagedenoisingmethodforremotesensingimagescalledMRFENet.Itdemonstrated

gooddenoisingperformanceandpreservedtheedgedetailsoftheimages.Zhangetal.[26]

utilizeddilatedconvolutionstocapturemorecontextualinformationandthenproposeda

hybriddenoisingneuralnetworkcalledHDCNNtoenhancethedenoisingperformance

ofCNNnetworksincomplexapplicationscenarios. Tianetal.[27]combineddynamic

convolution,wavelettransform,anddiscriminativelearningtoproposeaconvolutional

neuralnetworkbasedonthewavelettransformcalledMulti-stageImageDenoisingCNN

withtheWaveletTransform(MWDCNN).Toreducetheparametersizeandtrainingburden

ofdeepdenoisingnetworks,Tangetal.[28]employedacascadedresidualnetworkand

proposedalightweight,multi-scale,efficientconvolutionalneuralnetwork.

Theresultsofmostdenoisingmethodsareobtaineddirectlyfromthefusionofhigh-

levelfeatures,whilelow-levelfeaturescontainingtextureandcontourinformationare

ignored, resulting in the loss of some important information. Furthermore, since the

convolutionaloperationpreferstoextractlocalfeatures, itisdifficulttoextractglobal

informationsuchastexturesandcontourswhentheobjectsintheimagearerelatively

large.Tosolvetheseproblems,anN-shapedconvolutionalneuralnetwork,namedNSNet,

usingmulti-scalefeaturesisproposedinthispaper.Inthismodel,a2DHaarwaveletis

usedtoconstructanimagepyramidthatcontainshigh-andlow-frequencycomponents

ofthecorruptedimageatdifferentscales.Themulti-scalefeaturesareextractedfromthe

imagepyramidbyaU-shapedconvolutionalnetwork[29],andthelow-andhigh-level

featuresarefusedbyskipconnectionsintheU-shapednetwork.The2DHaarwaveletis

widelyusedinimagedenoising,andmanyscholarshaveachievedexcellentdenoising

performancewithit[30–33].ToverifythedenoisingperformanceofNSNet,thedenoising

ofgrayandcolorimageswascarriedoutatdifferentnoiselevelsandcomparedwith

existingdenoisingmethods.Thecontributionsofthisworkaresummarizedasfollows:

(1) AnN-shapedconvolutionalneuralnetworkforextractingmulti-scaleinformation

isproposed. Thenetworkexploitsmulti-scaleinformationtocompensateforthe

205

Mathematics2023,11,2772

drawbacksofconvolutionaloperationsinextractingglobalfeatures,whicheffectively

improvesthenetwork’sabilitytorecovertexturesandcontours.

(2) Aschemeforconstructingimagepyramidsusinga2DHaarwaveletisproposed.The

imagepyramidisobtainedbyusingamulti-scale2DHaarwavelet,andeachlayer

ofthepyramidcontainsonelow-frequencycomponentandthreehigh-frequency

components.Inimagedenoising,thehigh-frequencycomponentscanbeusedasan

estimateofthenoiseleveltofacilitatedenoising.

(3) NSNetshowsgooddenoisingperformanceforAWGNatanoiselevelrangeof(0,55)

andgoodrecoveryoftexturesandcontours.Itprovidesasolutionforapplications

thatneednotonlydenoisingbutalsotextureandcontourrecovery.

Therestofthispaperisorganizedasfollows. Section2presentsthetechniquesin-

volvedintheproposedmodel.Section3describestheproposedNSNetandtheconstruction

oftheimagepyramidindetail.Section4presentstheresultsofexperiments,andSection5

concludesthepaper.

2.TheoreticalAspects

2.1.The2DHaarWavelet

Theprocessofdecomposinganimageusingthe2DHaarwaveletisshowninFigure2.

The b"lock√s with√fiv$e-pointed stars in the figure are th"e finit√e imp√uls$e response filter.

hϕ = 1/ 2,1/ 2 denotesalow-passfilter,andhψ = −1/ 2,1/ 2 denotesahigh-

passfilter.Thedownarrow(↓)indicatesdownsampling,whichmeansaddingtwoadjacent

pixelsinthecolumnorrowdirection.

(cid:561)

Figure2.The2DHaarwavelettransform.

Theimageisfirstprocessedwiththetwofiltersseparatelyandiscompressedinthe

columndirectiontoobtainalow-frequencycomponentLandahigh-frequencycomponent

H. Thetwocomponentsarethenprocessedwithlow-andhigh-passfiltersinturnand

compressedintherowdirectiontoobtainthelow-frequencycomponent LL,thehigh-

frequencycomponentLHintheverticaldirection,thehigh-frequencycomponentHLin

thehorizontaldirection,andthehigh-frequencycomponentHHinthediagonaldirection.

Accordingtotheprincipleof2DHaarwavelets,assumingthatthecorruptedimageis

X∈Rm×n,theformulasforthecomponentsoftheimagecanbesimplifiedas

A =X(2i,2j), B =X(2i+1,2j) (1)

ij ij

C =X(2i,2j+1), D =X(2i+1,2j+1) (2)

ij ij

(cid:11) (cid:12) (cid:11) (cid:12)

LL = 1 A +B +C +D , HL = 1 B +D −A −C (3)

ij 2 ij ij ij ij ij 2 ij ij ij ij

(cid:11) (cid:12) (cid:11) (cid:12)

LH = 1 C +D −A −B , HH = 1 A +D −B −C (4)

ij 2 ij ij ij ij ij 2 ij ij ij ij

206

Mathematics2023,11,2772

where{i|0≤i≤m/2}and{j|0≤j≤n}.Thetwo-scale2DHaarwaveletappliedtothe

image “Monarch” is shown in Figure 3. Through the 2D Haar wavelet, the image is

decomposedintothreehigh-frequencycomponents(LH,HL,HH)andalow-frequency

component(LL).

Figure3.Two-scale2DHaarwaveletprocessingresultsontheimage“Monarch”.

2.2.U-ShapedConvolutionalNetwork

TheU-shapedconvolutionalnetworkwasfirstproposedbyRonnebergeretal.[29].

Thenetworkhasbeenwidelyusedinvariousfieldsforitspowerfulencodinganddecoding

capabilities[34,35]. TheU-shapedconvolutionalnetworkincludesfourdownsampling

operatorsandfourupsamplingoperatorsandusesskipconnectionsatthesamestage,

whichnotonlygivesthenetworktheabilitytoextractmulti-scalefeaturesbutalsoensures

thattheoutputintegratesmorelow-levelfeatures[21]. ThestructureoftheU-shaped

convolutionalnetworkwithbatchnormalization(BN)isshowninFigure4.

Figure4.NetworkstructureoftheU-shapednetworkwithBN.

Whentheneuralnetworkbecomesverydeep,aninternalcovariateoffsetmayoccur,

whichcanleadtotwoproblems:(1)itaffectsthelearningefficiencyandmakesthelearning

processunstable,and(2)itmakestheinputdataofthelaterlayerstoolargeorsmall,thus

fallingintothesaturationareaoftheactivationfunctionandcausingthelearningprocessto

stopprematurely.Tosolvetheproblemoftheinternalcovariateoffset,ageneralapproachis

toaddBN,asproposedbyIoffeandSzegedy[36],totheU-shapedconvolutionalnetwork.

TheBNlayerisusuallyplacedbetweentheconvolutionaloperationandtheRectified

LinearUnit(ReLU),andtheparametersoftheBNlayerareadjustedbytraining.Suppos-

ingthatthereisamini-batchB = {X1···m }ofsizem,andtheparameterstobelearned

areγandβ,theBNprocesscanbeexpressedas

%

γ= Var[x], β=E[x], (5)

207

Mathematics2023,11,2772

μ B = m 1 i ∑ = m 1 x i , δ B 2 = m 1 i ∑ = m 1 (x i −μ B )2, (6)

xˆ = %x i −μ B , y =γxˆ +β, (7)

i i i

δ2+ε

B

whereεisaconstantaddedtothemini-batchvariancefornumericalstability.

2.3.ResidualLearning

Whenthenetworkbecomesverydeep,someconvolutionallayersmayappearto

haveidentitymapping,resultingindegradationproblemsandvanishingandexploding

gradients. Tosolvethisproblem, Heetal.[37]proposedaresidualnetworkwiththe

residual block shown in Figure 5. It connects the input and output directly through

ashortcutconnection, allowing F(x)tolearnsmallchanges. Thisnotonlyallowsthe

convolutionallayertomaintainidentitymappingbutalsoavoidsvanishingandexploding

∗

gradients.Therelationshipbetweentheinputxandoutputx oftheresidualblockis

x

∗=F(x)+x.

(8)

Figure5.Basicstructureofaresidualblock.

Inimagedenoising,whenthenoiselevelislow,themappingfromthenoisyimage

tothecleanimageisclosetoanidentitymapping,whichisnotconducivetothetraining

ofthenetwork.Tosolvethisproblem,Zhangetal.[17]firstappliedresiduallearningto

imagedenoising.AssumingthattheinputimageisInputandtheoutputimageisOutput,

theirrelationshipis

F(x)=Output−Input. (9)

Itcanbeseenfrom(9)thatresiduallearningforimagedenoisingusesnoiseasthe

trainingtarget,whichisavaluabletechniqueforimprovingthedenoisingperformanceof

themodel.

3.TheProposedNSNetModel

Inthissection,theproposedNSNetmodelisintroducedindetail;itsarchitecture

isshowninFigure6. Itmainlyconsistsofamulti-scaleinputlayerandamulti-scale

featureextractionlayer.Themulti-scaleinputlayerusesa2DHaarwavelettocreatean

imagepyramid,whichdecomposesthecorruptedimageintohigh-andlow-frequency

componentsatdifferentscales.Themulti-scalefeatureextractionlayerusesaU-shaped

convolutional network to extract features at different scales from the image pyramid.

Additionally,NSNetsetsthemean-squarederrorasthelossfunctionandusestheresidual

learningstrategytolearnthenoisedirectly.

208

Mathematics2023,11,2772

Figure6.ArchitectureofNSNet.

The2DHaarwaveletcandecomposetheimageintofoursub-images,eachwithasize

halfthatoftheoriginalimage.Byusinga2DHaarwavelettodecomposetheimage,we

canobtain

LL1,(LH1,HL1,HH1 )=dwt(y), (10)

wheredwt(·)representsthe2DHaarwavelet,yisthecorruptedimage,LL1isthelow-

frequencycomponent,andLH1,HL1,andHH1arethehigh-frequencycomponents.Then,

the2DHaarwaveletisappliedonceagaintothelow-frequencycomponentLL1toobtain

LL2,(LH2,HL2,HH2 )=dwt(LL1 ), (11)

Finally,toobtaintheimagepyramidshowninFigure7,thesameoperationisrepeated

twice,resultingin

LL3,(LH3,HL3,HH3 )=dwt(LL2 ), (12)

LL4,(LH4,HL4,HH4 )=dwt(LL3 ). (13)

Figure7.Imagepyramidconstructedbya2DHaarwavelet.

Theimagepyramidcontainsimagesatfivedifferentscales,eachofwhichcorresponds

toadifferentstageoftheU-shapedconvolutionalnetwork.Inadditiontotheoriginalscale,

eachscalecontainsalow-frequencycomponentLLandthreehigh-frequencycomponents

LH, HL,and HH. AsshowninFigure7,thelow-frequencycomponentisclosetothe

corruptedinputimage,whilethehigh-frequencycomponentscontainalotofnoiseand

sometextures,whichcanbeconsideredanestimateofthenoiselevel.

The image degradation model is established as y = x+v, where y denotes the

corruptedimage,xdenotesthecleanimage,andvdenotesthenoise.Theproposedmodel

inputsthecorruptedimageyintothenetworktopredictthenoisev≈ F(y)andfinally

209

Mathematics2023,11,2772

obtainsthecleanimagex=y−vthroughsimplesubtraction.Themean-squarederroris

usedasthelossfunction:

L(θ)= 1 ∑ N ||F(y;θ)−(y −x)||2, (14)

2N i=1 i i i F

whereθrepresentstheparametersetofthemodel,Nisthetotalnumberofimages,and

x andy representtheithcleanimageandnoisyimage,respectively.

i i

Forconvenience,theproposedmodeltrainedataknownnoiselevelisnamedNSNet-

S,andthemodeltrainedatanunknownnoiselevelisnamedNSNet-B.Thepseudo-code

oftheproposedmethodisshowninAlgorithm1.

Algorithm1ThealgorithmofNSNet

Input:AlltrainingimagesDfromtheobserveddataset,denoisingmode(BorS),noiselevel

noiseL,rangeofnoiselevelnoiseR,maximumepochMepoch.

Output:Thetrainednetworkf.

1: Initialingmodelparametersθandlearningrateη;

2: Samplingmpatches(x1,···,xm )fromD;

3: forepoch=1toMepochdo

4: ifepoch>30then

5: η←η/10;

6: endif

7: Setgˆ=0;

8: fori=1tomdo

9: ifmode==“B”then

10: SettingnoiseLasanintegerattherangenoiseRrandomly;

11: endif

12: AddingGaussiannoisewiththenoiselevelofnoiseLtoxi:

yi =xi +noisei;

13: Performingmulti-scalewavelettransformonyitoobtainy1

i

,y2

i

,y3

i

,y4

i

:

y1

i

={LL1,LH1,HL1,HH1 }=dwt(yi ),y2

i

={LL2,LH2,HL2,HH2 }=dwt(LL1 ),

y3

i

={LL3,LH3,HL3,HH3 }=dwt(LL2 ),y4

i

={LL4,LH4,HL4,HH4 }=dwt(LL3 );

14: Predictingnoiseusingthenetwor(cid:11)kfwithparamet(cid:12)erθ:

outi ← f yi,y1

i

,y2

i

,y3

i

,y4

i

;θ ;

15: CalculatingthelossaccordingtoEquation(14);

16: Computingthegradient: gˆ←gˆ+

m

1∇ θL(θ);

17: endfor

18: Updatingθ: θ←θ−η×gˆ;

19: endfor

4.ExperimentalResults

Grayimagedenoisingandcolorimagedenoisingwerecarriedouttocomparethe

denoisingperformanceoftheproposedNSNetwiththoseofexistingmodels,including

NLM[2],BM3D[3],KSVD[4],NCSR[6],OCTOBOS[7],TWSC[8],GHP[9],EPLL[10],

PGPD[11],PCLR[12],WNNM[13],CSF[15],TNRD[16],andFFDNet[18]. Moreover,

twodifferenttypesofDnCNNs[17]werealsoselectedasthecomparedmodels. They

areDnCNN-SandDnCNN-B,whicharetrainedatknownandunknownnoiselevels,

respectively.

4.1.EvaluationMetrics

Theresultsofalldenoisingmethodswereanalyzedquantitativelyintermsofthepeak

signal-to-noiseratio(PSNR)andstructuralsimilarity(SSIM).

210

Mathematics2023,11,2772

(1) Supposing that the recovered image is I ∈ Rm×n and the corrupted image is

K∈Rm×n,thePSNRiscalculatedas

MSE= 1 m ∑ −1n ∑ −1 [I(i,j)−K(i,j)]2, (15)

mn i=0 j=0

(cid:24) (cid:31)

MAX2

PSNR=10·log I , (16)

10 MSE

where MSEisthemean-squarederror,and MAXI denotesthemaximumvalueofthe

pixelsintheimage. Ingeneral,MAXI =255ifeachpixelisrepresentedin8-bitbinary

formor1ifitisrepresentedin1-bitbinary.

(2)TheSSIMiscalculatedas

SSIM(I,K)= (cid:11)

(2μ

I

μ

K

+c(cid:12)1(cid:11) )(σ

IK

+c2 )

(cid:12) (17)

μ2

I

+μ2

K

+c1 σ

I

2+σ

K

2+c2

whereμ Iandμ KdenotethemeansofIandK,respectively,andσ Iandσ Kdenotetheirstan-

darddeviations,whileσ IKdenotesthecovarianceofIandK,andc1andc2areconstants.

4.2.ExperimentalSetting

Fortheablationexperiment,NSNet,NSNetwithoutBN,Unet,andUnetwithoutBNwere

compared.Allcomparedmethodsweretrainedusing400imagesofsize180×180pixels,as

mentionedin[17].ThetestsetswereSet12,whichiswidelyusedintheevaluationofdenoising

methods,andBSD68[38].Intrainingthemodel,thesizeofthepatchwassetto48×48,and

128×618patcheswerecroppedfromthe400images.Fourdenoisingmethodsweretrained

atnoiselevelsof15,25,35,45,and50. Foranoiselevelofα,thenoisewasgeneratedbya

Gaussiandistributionwithameanofzeroandavarianceofα.

Forthedenoisingofgrayimages,the400imageswerestillusedasthetrainingset,and

128×2934patchesofsize48×48werecroppedfromthem.Sincemostimagedenoising

methodscanonlyobtainthebestdenoisingperformanceataknownnoiselevel,toachieve

afaircomparison,theproposedmethodwastrainedatanunknownnoiselevelandatnoise

levelsof15,25,and50.ThetestsetswereSet12andBSD68,neitherofwhichparticipated

inmodeltraining.

Forcolorimagedenoising,432imageswereselectedfromthecolorimagedataset

CBSD500[39]astrainingsamples,andtheremaining68images(CBSD68)wereusedas

thetestset.ThetestsetalsoincludedKodak24[40]andMcMaster[41].Inthisexperiment,

96×3900patcheswerecroppedfromthe432imagestotrainthecolorimagedenoising

model. Theothersettingswerelargelyconsistentwiththesettingsusedforgrayimage

denoising.ThespecificsettingsofNSNetareshowninTable1.

Table1.SpecificsettingsofNSNetusedinallexperiments.

Experiment Model NoiseLevel PatchSize NumberofPatches

Ablationexperiment NSNet-S 15,25,35,45, 48×48 128×618

50

Grayimagedenoising NSNet-S 15,25,50 48×48 128×2934

Grayimagedenoising NSNet-B (0,55) 48×48 128×2934

Colorimagedenoising NSNet-B (0,55) 48×48 96×3900

WhentrainingNSNet-S,eachcleanimageinputtothemodelwascorruptedbythe

samelevelofnoise. WhentrainingNSNet-B,eachcleanimageinputtothemodelwas

corruptedbynoiseataleveldrawnrandomlyfromtherange(0,55).TheAdamoptimizer

wasusedtotunethemodelwithaninitiallearningrateof0.001.Themaximumtraining

epoch was 50. After 30 epochs, the learning rate was adjusted to 0.0001. The size of

211

Mathematics2023,11,2772

eachmini-batchwassetto128. ThedenoisingnetworkwastrainedinPyTorch,andall

experimentswerecarriedoutinthepycharmenvironmentrunningonaPCwithanAMD

Ryzen95900HXwithRadeonGraphics3.30GHzCPUandanNVIDIAGeForceRTX

3070LaptopGPU.

4.3.AblationExperiment

Thissectiondescribestheablationexperimentthatwascarriedouttodemonstrate

theeffectivenessofthemaincomponentsoftheproposedmodel.Theexperimenttested

thedenoisingperformanceofNSNet,Unet,NSNetwithoutBN,andUnetwithoutBNat

noiselevelsof15,25,35,45,and50.ThedenoisingresultsontheSet12datasetandthegray

versionofBSD68areshowninTable2,inwhichvalueswith#and*representthebestand

second-bestdenoisingperformance,respectively.

Table2.AveragePSNR/SSIMoffourdenoisingmethodsintheablationexperiment.

Nosie Method

Model Level

NSNet Unet NSNet(-BN) Unet(-BN)

σ=15 32.90#/0.9040# 32.75/0.9017 32.76*/0.9025* 31.81/0.8835

σ=25 30.50#/0.8643# 30.48*/0.8640* 30.33/0.8610 30.28/0.8602

Set12 σ=35 28.95#/0.8319# 28.89*/0.8300* 28.65/0.8243 28.77/0.8270

σ=45 27.81#/0.8041# 27.80*/0.8029* 27.66/0.7993 26.52/0.7945

σ=50 27.32#/0.7910# 27.32*/0.7901* 26.93/0.7737 26.90/0.7724

σ=15 31.79#/0.8927# 31.71*/0.8912* 31.70/0.8916* 31.04/0.8748

σ=25 29.31#/0.8322# 29.29*/0.8321* 29.20/0.8294 29.18/0.8288

BSD68 σ=35 27.82#/0.7849# 27.76*/0.7810* 27.65/0.7779 27.71/0.7788

σ=45 26.78#/0.7446# 26.77*/0.7442* 26.70/0.7413 26.63/0.7364

σ=50 26.35#/0.7267# 26.34*/0.7260* 26.10/0.7101 26.11/0.7106

Note:NSNet(-BN)meansNSNetwithoutBN,andUnet(-BN)meansUnetwithoutBN.#Thebestdenoising

performance.*Thesecond-bestdenoisingperformance.

ThedenoisingperformanceofNSNetisbetterthanthatofUnetatallnoiselevels,

whichshowsthatmulti-scaleinputcanimprovethedenoisingperformance.Theresultsfor

NSNetandNSNetwithoutBNshowthatthedenoisingperformanceofNSNetisgreatly

improvedafteraddingtheBNlayer. Asmentionedin[29],theBNlayercanimprove

thedenoisingperformanceoftheneuralnetwork.Atallnoiselevels,NSNetwithoutBN

achievesbetterdenoisingthanUnetwithoutBN,anditsdenoisingperformanceiscloseto

thatofUnetatlownoiselevels,whichindicatesthatthemulti-scaleinputgreatlyimproved

thedenoisingperformanceofthemodelatlownoiselevels. Withincreasesinthenoise

level, thestructureofthecompressedimageisincreasinglycorrupted; thus, itcannot

provideaccurateinformationforthenetwork.Inthiscase,theperformanceofNSNetis

similartothatofUnet.Forexample,thedenoisingperformanceofNSNetissimilartothat

ofUnetatanoiselevelof50.

4.4.GrayImageDenoising

Inthisexperiment,AWGNwasaddedtoSet12andthegrayversionofBSD68,andthe

noiselevelsweresetto15,25,and50.ThedenoisingresultsofallmethodsonSet12are

showninTables3–5.Duetoinsufficientparameters,CSFcannotbetestedatanoiselevel

of50.

Table3showsthedenoisingresultsofallmethodsatanoiselevelof15.NSNet-Shasa

betterdenoisingperformancethanothermethodsandobtainedthefirst-rankeddenoising

performanceontenimages. NSNet-Srankedaveryclosesecondintermsofdenoising

theimage“House”.Inthiscase,thedenoisingperformanceofNSNet-Sis1.86dBhigher

thanthatoftheworstmethod,NLM,onaverage,and0.1dBhigherthanthatofDnCNN-S,

onaverage,intermsofPSNR.Theaverageresultsofallmethodsshowthatthereislittle

difference in the denoising performanceof most methods at a noise levelof 15. Ata

212

Mathematics2023,11,2772

lownoiselevel,theself-similarity,sparsity,andlow-rankpropertiesoftheimagearestill

relativelycomplete,andthetraditionaldenoisingmethods(e.g.,BM3D,NCSR,TWSC,

PCLR,WNNM)alsoachieveagooddenoisingperformance.

Table3.PSNRsofallmethodsonSet12atanoiselevelof15.

Model C.man House Pappers Starfish Monar. Airpl. Parrot Lena Barbara Boat Man Couple Average

NLM 30.05 33.23 31.59 30.30 30.47 29.42 30.07 33.16 31.33 31.25 31.27 30.97 31.09

BM3D 31.92 34.95 32.70 31.15 31.86 31.08 31.38 34.27 33.11 32.14 31.93 32.11 32.38

KSVD 31.46 34.24 32.20 30.70 31.41 30.75 30.95 33.71 32.42 31.76 31.53 31.47 31.89

NCSR 32.01 35.04 32.66 31.50 32.25 31.19 31.37 34.12 33.06 32.08 31.98 32.00 32.44

OCTOBOS 31.91 34.32 32.49 31.04 31.72 30.98 31.29 33.91 32.59 31.87 31.74 31.77 32.14

TWSC 32.01 35.11# 32.83 31.64 32.47 31.14 31.52 34.39 33.64# 32.24 32.09 32.15 32.60

EPLL 31.82 34.14 32.58 31.08 32.03 31.16 31.40 33.87 31.34 31.91 31.97 31.91 32.10

GHP 31.48 34.07 32.40 31.09 31.63 30.77 31.16 33.54 32.01 31.72 31.62 31.54 31.92

PCLR 32.23 35.07 33.00 31.75 32.63 31.45 31.62 34.27 33.12 32.25 32.16 32.14 32.64

PGPD 31.83 34.79 32.61 31.25 32.15 31.19 31.32 34.04 32.74 32.03 31.99 32.07 32.33

WNNM 32.18 35.15 32.97 31.83 32.72 31.40 31.61 34.38 33.61* 32.28 32.12 32.18 32.70

CSF 31.95 34.40 32.83 31.56 32.34 31.34 31.36 34.07 31.93 32.01 32.09 31.99 32.32

TNRD 32.19 34.55 33.03 31.76 32.57 31.47 31.63 34.25 32.14 32.15 32.24 32.11 32.51

DnCNN-

32.59* 34.99 33.24* 32.13* 33.25* 31.67* 31.88* 34.58 32.61 32.42* 32.43* 32.43* 32.85*

S

DnCNN-

32.14 34.96 33.09 31.92 33.08 31.54 31.64 34.52 32.03 32.36 32.37 32.38 32.67

B

FFDnet 32.37 35.05 33.01 31.95 32.92 31.55 31.79 34.60* 32.48 32.36 32.37 32.43* 32.74

NSNet- 32.67# 35.09* 33.33# 32.29# 33.32# 31.79# 31.97# 34.69# 32.80 32.50# 32.48# 32.52# 32.95#

S

NSNet-

32.02 34.63 32.74 32.08 32.87 31.31 31.60 34.42 30.59 32.29 32.18 32.20 32.41

B

Note:#Thebestdenoisingperformance.*Thesecond-bestdenoisingperformance.

Table4.PSNRsofallmethodsonSet12atanoiselevelof25.

Model C.man House Pappers Starfish Monar. Airpl. Parrot Lena Barbara Boat Man Couple Average

NLM 29.97 30.38 29.02 27.82 28.07 27.33 27.98 30.38 28.59 28.74 28.80 28.32 28.61

BM3D 29.45 32.86 30.16 28.56 29.25 28.43 28.93 32.08 30.72 29.91 29.62 29.72 29.98

KSVD 28.90 32.10 29.65 28.19 28.81 28.16 28.46 31.36 29.58 29.32 29.11 28.88 29.38

NCSR 29.43 32.89 30.05 28.77 29.43 28.45 28.86 31.92 30.62 29.77 29.58 29.49 29.94

OCTOBOS 29.25 32.08 29.78 28.24 28.78 28.28 28.67 31.56 29.88 29.51 29.26 29.23 29.54

TWSC 29.54 33.05 30.32 28.98 29.71 28.55 29.08 32.22 31.26# 29.99 29.71 29.79 30.18

EPLL 29.24 32.04 30.07 28.43 29.30 28.56 28.91 31.62 28.55 29.69 29.63 29.48 29.63

GHP 29.28 32.50 30.04 28.66 29.02 28.28 28.87 31.69 30.29 29.71 29.49 29.37 29.77

PCLR 29.67 32.98 30.46 28.87 29.75 28.77 29.13 32.17 30.65 30.00 29.77 29.73 30.16

PGPD 29.26 32.79 30.07 28.49 29.29 28.54 28.80 31.93 30.28 29.82 29.66 29.68 29.88

WNNM 29.64 33.23 30.40 29.03 29.85 28.70 29.13 32.25 31.24* 30.03 29.77 29.82 30.26

CSF 29.47 32.40 30.28 28.80 29.62 28.72 28.89 31.80 29.03 29.77 29.72 29.53 29.84

TNRD 29.71 32.54 30.55 29.02 29.86 28.89 29.18 32.01 29.41 29.92 29.88 29.71 30.06

DnCNN- 30.21# 33.10 30.82* 29.36 30.41* 29.08* 29.44* 32.41 30.01 30.20 30.08 30.08 30.43*

S

DnCNN-

30.03 33.04 30.73 29.24 30.37 29.06 29.35 32.40 29.67 30.19 30.06 30.05 30.35

B

FFDnet 30.05 33.26* 30.72 29.28 30.29 29.01 29.42 32.57* 29.98 30.23* 30.07* 30.15* 30.42

NSNet- 30.12* 33.30# 31.05# 29.90# 30.48# 29.24# 29.45# 32.64# 30.39 30.27# 30.14# 30.22# 30.60#

S

NSNet-

30.05 33.05 30.62 29.62* 30.33 28.97 29.39 32.57* 27.54 30.23* 29.99 30.05 30.20

B

Note:#Thebestdenoisingperformance.*Thesecond-bestdenoisingperformance.

213

Mathematics2023,11,2772

Table5.PSNRsofallmethodsonSet12atanoiselevelof50.

Model C.man House Pappers Starfish Monar. Airpl. Parrot Lena Barbara Boat Man Couple Average

NLM 24.26 25.69 24.79 23.88 24.16 23.60 24.35 25.97 24.31 24.80 25.06 24.41 24.61

BM3D 26.13 29.69 26.68 25.04 25.82 25.10 25.90 29.05 27.23 26.78 26.81 26.46 26.73

KSVD 25.68 27.97 26.09 24.53 25.30 24.61 25.38 27.86 25.47 25.95 26.10 25.30 25.85

NCSR 26.15 29.62 26.53 25.09 25.77 24.93 25.71 28.90 26.99 26.67 26.67 26.19 26.60

OCTOBOS 25.62 28.59 26.15 24.57 25.04 24.86 25.39 28.37 26.17 26.30 26.27 25.82 26.10

TWSC 26.46 30.17 26.88 25.41 26.27 25.38 26.11 29.08 27.54* 26.88 26.82 26.48 26.96

EPLL 26.03 28.77 26.63 25.04 25.78 25.24 25.84 28.42 24.82 26.65 26.72 26.24 26.35

GHP 25.91 28.51 26.38 24.39 25.53 24.76 25.71 27.43 25.44 25.99 25.92 25.46 25.95

PCLR 26.56 29.77 27.03 25.32 26.24 25.50 26.15 29.11 27.11 26.99 26.94 26.55 26.94

PGPD 26.40 29.73 26.69 25.10 25.89 25.34 25.84 29.00 26.84 26.82 26.84 26.47 26.75

WNNM 26.42 30.33 26.91 25.43 26.32 25.42 26.09 29.25 27.79# 26.97 26.94 26.64 27.04

CSF - - - - - - - - - - - - -

TNRD 26.61 29.49 27.08 25.42 26.32 25.59 26.16 28.94 25.70 26.94 26.99 26.50 26.81

DnCNN-

27.26 29.96 27.35 25.64 26.83 25.83 26.42 29.34 26.15 27.19 27.19 26.86 27.17

S

DnCNN-

27.26 29.91 27.35 25.60 26.84 25.82 26.48 29.34 26.32 27.18 27.17 26.87 27.18

B

FFDnet 27.24 30.36* 27.41 25.68 26.92 25.79 26.57# 29.63 26.41 27.30* 27.26* 27.04* 27.30*

NSNet- 27.38# 30.43# 27.54# 26.24* 26.93* 25.96# 26.50 29.74# 27.04 27.38# 27.31# 27.14# 27.47#

S

NSNet- 27.35* 30.24 27.47* 26.17# 26.94# 25.89* 26.54* 29.70* 25.46 27.30* 27.19 27.01 27.27

B

Note:#Thebestdenoisingperformance.*Thesecond-bestdenoisingperformance.

Table4showsthedenoisingresultsobtainedbyallmethodsatanoiselevelof25.With

increasesinthenoiselevel,thebestandsecond-bestdenoisingperformancewasobtained

withthedeep-learning-basedmethods,whichshowsthesuperiorityofdeeplearningin

imagedenoising. Asthenoiselevelincreases,theself-similarityandotherfeaturesof

theimageareincreasinglycorrupted,whichleadstothefactthatthetraditionalimage-

prior-baseddenoisingmethodsarenolongeradvantageous. Thedeep-learning-based

denoisingmethodslearnthepotentialnoisedirectlyfromthecorruptedimageandrely

lessonthepriorknowledgeoftheimage.Thisallowsthemtoachieveagooddenoising

performance,evenathighnoiselevels. Inthiscase,NSNet-Sisrankedfirstintermsof

denoisingperformanceontenimagesandsecondononeimage.NSNet-Bisrankedsecond

intermsofdenoisingperformanceonthreeimages.ThedenoisingperformanceofNSNet-S

is1.99dBhigherthanthatoftheworstmethod,NLM,and0.17dBhigherthanthatof

thesecond-bestmethod,DnCNN-S,intermsofPSNR.Comparedwiththetraditional

denoisingmethodsBM3D,NCSR,TWSC,andWNNM,NSNet-BisclosetoWNNMand

outperformsBM3D,NCSR,andTWSCatanoiselevelof25.

Table5showsthedenoisingresultsobtainedbyallmethodsatanoiselevelof50.In

thiscase,NSNet-Sisrankedfirstintermsofdenoisingperformanceoneightimagesand

secondontwoimages.NSNet-Bisrankedfirstintermsofdenoisingperformanceontwo

imagesandsecondonsiximages. Comparedwithothermethods,NSNet-Bprovidesa

betterdenoisingperformanceatahighnoiselevel.Thereasonforthismaybethatanimage

withhighnoisewillcauseagreaterdeviationthanonewithlownoise,andthenetwork

willpaymoreattentiontotherestorationofimageswithhighnoisewhentrainingNSNet-B.

Inthiscase,NSNet-Sis2.86dBhigherthantheworstmethod,NLM,and0.17dBhigher

thanthesecond-bestmethod,FFDNet.NSNet-Balsohasanoutstandingperformance;its

denoisingperformancesurpassesthatofDnCNN-BandWNNManddiffersfromthatof

FFDNetbyonly0.03dB.

Intheabovethreeexperiments,NSNetshowsagooddenoisingperformanceinmost

cases,althoughthatofNSNetontheimage“Barbara”isnotasgoodasthatoftraditional

methods(e.g.,TWSC,WNNM).“Barbara”hassimilarrichtextures,andthemethodbased

onimageself-similaritycaneffectivelyusethemtoachievebetterdenoising.Bothtexture

andnoisearehigh-frequencyinformation;therefore,imagedenoisingmethodsthatuse

residuallearningtendtotreattextureasnoise,whichmakesthedenoisingperformance

214

Mathematics2023,11,2772

oftheproposedmodelpoor. Inaddition,thesameexperimentswereconductedonthe

datasetBSD68tobetterdemonstratethedenoisingperformanceofNSNet.Theaverage

PSNRsandSSIMsofallmethodsonSet12andBSD68areshowninTable6. Compared

withothermethods,theaveragedenoisingperformanceofNSNet-Sonthetwodatasetsis

thebest,andNSNet-Bhasabetterdenoisingperformanceatahighnoiselevel.

Table6.AveragePSNRs/SSIMsofallmethodsondatasetsSet12andBSD68.

Set12 BSD68

Model

σ=15 σ=25 σ=50 σ=15 σ=25 σ=50

NLM 31.09/0.8594 28.62/0.7711 24.61/0.5695 29.82/0.8322 27.56/0.7296 24.01/0.5212

BM3D 32.38/0.8957 29.98/0.8510 26.73/0.7681 31.08/0.8722 28.57/0.8017 25.62/0.6869

KSVD 31.89/0.8847 29.38/0.8308 25.85/0.7260 30.86/0.8677 28.29/0.7889 25.18/0.6548

NCSR 32.44/0.8958 29.94/0.8501 26.60/0.7673 31.19/0.8770 28.61/0.8045 25.59/0.6864

OCTOBOS 32.14/0.8889 29.54/0.8378 26.10/0.7433 31.08/0.8744 28.46/0.7989 25.33/0.6705

TWSC 32.60/0.8989 30.18/0.8549 26.96/0.7731 31.28/0.8782 28.76/0.8077 25.77/0.6903

EPLL 32.10/0.8936 29.63/0.8444 26.35/0.7475 31.19/0.8825 28.68/0.8123 25.68/0.6877

GHP 31.92/0.8693 29.77/0.8415 25.95/0.7562 30.83/0.8513 28.49/0.8039 24.94/0.6809

PCLR 32.64/0.8979 30.16/0.8542 26.94/0.7763 31.38/0.8799 28.84/0.8106 25.88/0.6970

PGPD 32.33/0.8900 29.88/0.8447 26.75/0.7602 31.14/0.8705 28.64/0.8019 25.76/0.6877

WNNM 32.70/0.8982 30.26/0.8557 27.04/0.7775 31.32/0.8766 28.80/0.8029 24.43/0.6838

CSF 32.32/0.8923 29.84/0.8450 -/- 31.24/0.8746 28.73/0.8055 -/-

TNRD 32.51/0.8967 30.06/0.8520 26.81/0.7666 31.42/0.8825 28.91/0.8155 25.96/0.7024

DnCNN-S 32.85*/0.9025* 30.43*/0.8616 27.17/0.7828 31.74*/0.8907* 29.23*/0.8279 26.24/0.7189

DnCNN-B 32.67/0.9000 30.35/0.8599 27.18/0.7816 31.62/0.8868 29.16/0.8244 26.23/0.7164

FFDnet 32.74/0.9024 30.42/0.8631* 27.30*/0.7900* 31.64/0.8902 29.19/0.8828 26.29/0.7239

NSNet-S 32.95#/0.9054# 30.59#/0.8662# 27.47#/0.7956# 31.81#/0.8936# 29.33#/0.8339# 26.42#/0.7316#

NSNet-B 32.41/0.8943 30.20/0.8595 27.27/0.7895 31.46/0.8870 29.18/0.8304* 26.32*/0.7242*

Note:#Thebestdenoisingperformance.*Thesecond-bestdenoisingperformance.

Figures8and9showthedenoisingperformanceofallcomparedmethodsongray

imagesatnoiselevelsof25and50,respectively. Inordertofacilitatethecomparisonof

thedenoisingperformance,theresultsweretransformedintopseudo-colorimages.The

redboxinFigure8showstherestorationeffectofallcomparedmethodsonthe“grass”.It

canbeseenthatNSNet’srecoveryofthe“grass”isclosertothecleanimagethantheother

comparedmethodsandresultsinsharperandcleareredgesandtextures.Theredboxin

Figure9furtherdemonstratestheadvantagesofNSNetinedgeandtexturerestoration.As

showninFigure9,comparedtoothermethods,NSNetcannotonlymaketheedgesand

texturessharperbutalsorestoremoreimagedetails.

4.5.ColorImageDenoising

Theprevioussectioncomparedthedenoisingperformanceofthemethodsongray

images,whereBM3D,DnCNN,andFFDNethadthebetterdenoisingperformanceand

computationalspeed.Intheexperimentdescribedinthissubsection,thesemethodswere

selectedforafurthercomparativetestofthedenoisingabilityoftheproposedmodelwith

colorimages. ThedatasetsusedherearethecolorversionsofCBSD68,Kodak24,and

McMaster.

215

Mathematics2023,11,2772

(cid:561)

(cid:561)

Figure8.Resultsofsomedenoisingmethodsatanoiselevelof25.

216

Mathematics2023,11,2772

(cid:561)

(cid:561)

(cid:561)

Figure9.Resultsofsomedenoisingmethodsatanoiselevelof50.

Thedenoisingperformanceoffourmethods(BM3D,DnCNN,FFDNet,andNSNet)at

noiselevelsof35,45,and55isshowninTable7.TheproposedNSNetisthebestmodelin

thedenoisingexperimentswithCBSD68andKodak24,withMcMasterrankedsecond.

217

Mathematics2023,11,2772

Table7.AveragePSNRs/SSIMsofallmethodsoncolorimages.

Noise Method

Dataset Level

BM3D DnCNN FFDNet NSNet

σ=35 28.88/0.8160 29.60*/0.8422* 29.59/0.8408 29.69#/0.8481#

CBSD68 σ=45 27.84/0.7793 28.43/0.8060* 28.44*/0.8048 28.58#/0.8150#

σ=55 26.97/0.7468 27.50/0.7736 27.56*/0.7738* 27.70#/0.7854#

σ=35 29.89/0.8208 30.45/0.8387 30.56*/0.8405* 30.67#/0.8478#

Kodak24 σ=45 28.91/0.7906 29.31/0.8057 29.44*/0.8083* 29.59#/0.8187#

σ=55 28.06/0.7629 28.38/0.7753 28.57*/0.7811* 28.72#/0.7929#

σ=35 29.93/0.8237 30.15/0.8392 30.83#/0.8550# 30.60*/0.8527*

McMaster σ=45 29.00/0.7988 29.08/0.8116 29.68#/0.8275* 29.55*/0.8281#

σ=55 28.13/0.7712 28.17/0.7832 28.76#/0.8032* 28.73*/0.8049#

Note:#Thebestdenoisingperformance.*Thesecond-bestdenoisingperformance.

InthedenoisingexperimentwiththedatasetCBSD68,NSNetperformed0.81dBbetter

thanBM3D,0.09dBbetterthanDnCNN,and0.1dBbetterthanFFDNetatanoiselevelof

35.Itwas0.74dBbetterthanBM3D,0.15dBbetterthanDnCNN,and0.14dBbetterthan

FFDNetatanoiselevelof45,and0.73dBbetterthanBM3D,0.2dBbetterthanDnCNN,

and0.14dBbetterthanFFDNetatanoiselevelof55. Inthedenoisingexperimentwith

thedatasetKodak24,NSNetwas0.78dBbetterthanBM3D,0.22dBbetterthanDnCNN,

and0.11dBbetterthanFFDNetatanoiselevelof35. Itwas0.68dBbetterthanBM3D,

0.28dBbetterthanDnCNN,and0.15dBbetterthanFFDNetatanoiselevelof45,and

0.66dBbetterthanBM3D,0.34dBbetterthanDnCNN,and0.15dBbetterthanFFDNetat

anoiselevelof55.InthedenoisingexperimentusingtheMcMasterdataset,althoughthe

denoisingperformanceofNSNetwasnotasgoodasthatofFFDNet,thecomparisonofall

methodsintermsofSSIMshowsthatNSNetisabletorecoverthestructureofthecolor

imagebetter.

Figure10showsthedenoisingresultsoffourmethods(BM3D,DnCNN,FFDNet,

andNSNet)ononeimageofthepublicdatasetCBSD68atanoiselevelof45. Tobetter

demonstratethedenoisingperformanceoftheproposedmethod,tworepresentativeparts

arehighlighted. TheseshowthatNSNetrepairsthetexturebetterthanothermethods.

Figure11showsthedenoisingresultsoffourmethodsatanoiselevelof40.NSNethasa

moresignificantrepaireffecton“stone”intheimage,anditsrecoveryoftexturesisbetter

thanthoseofothermethods.

(cid:561)

Figure10.ComparisonofdenoisingresultsononecolorimageofthepublicdatasetCBSD68[39]ata

noiselevelof45.

218

Mathematics2023,11,2772

(cid:561)

Figure11.ComparisonofdenoisingresultsononecolorimageofthepublicdatasetCBSD68[39]ata

noiselevelof40.

5.Conclusions

Inthisstudy,anN-shapedconvolutionalnetworkthatcanextractmulti-scaleinforma-

tionisproposed.NSNetisabletoextractmulti-scaleinformationfromcorruptedimages

andusesittocompensateforthedrawbacksofconvolutionaloperationsinextractingglobal

features,thusenhancingNSNet’sabilitytocaptureglobalinformationandreconstruct

texturesandcontours.Ablationexperimentsdemonstratethatextractingmulti-scaleinfor-

mationisbeneficialtoimprovingthedenoisingperformanceofthemodelatnoiselevelsin

therangeof(0,50).GrayandcolorimagedenoisingexperimentsdemonstratethatNSNet

outperformsmanyexistingimagedenoisingmethodsatnoiselevelsof15,25,and50,es-

peciallyathighnoiselevels.Inaddition,NSNethasagoodblinddenoisingperformance,

whereitsperformanceathighnoiselevelsisclosetothatatknownnoiselevels.

AuthorContributions:Conceptualization,writing—reviewandediting,visualization,supervision,

andfundingacquisition,Y.L.Methodology,software,validation,investigation,andwriting—original

draftpreparation,Y.C.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.

Funding:ThisresearchwasfundedbytheChangshaMunicipalNaturalScienceFoundationunder

Grantkq2208432.

DataAvailabilityStatement:Notapplicable.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

References

1. Chatterjee,P.;Milanfar,P.Isdenoisingdead?IEEETrans.ImageProcess.2009,19,895–911.[CrossRef][PubMed]

2. Buades,A.;Coll,B.;Morel,J.-M.Anon-localalgorithmforimagedenoising.InProceedingsofthe2005IEEEComputerSociety

ConferenceonComputerVisionandPatternRecognition,SanDiego,CA,USA,20–25June2005;Volume2,pp.60–65.

3. Dabov,K.;Foi,A.;Katkovnik,V.;Egiazarian,K.Imagedenoisingbysparse3-Dtransform-domaincollaborativefiltering.IEEE

Trans.ImageProcess.2007,16,2080–2095.[CrossRef][PubMed]

4. Elad,M.;Aharon,M.Imagedenoisingviasparseandredundantrepresentationsoverlearneddictionaries.IEEETrans.Image

Process.2006,15,3736–3745.[CrossRef][PubMed]

5. Mairal,J.;Bach,F.;Ponce,J.;Sapiro,G.;Zisserman,A.Non-localsparsemodelsforimagerestoration.InProceedingsofthe2009

IEEE12thInternationalConferenceonComputerVision,Kyoto,Japan,29September–2October2009;pp.2272–2279.

219

Mathematics2023,11,2772

6. Dong,W.;Zhang,L.;Shi,G.;Li,X.Nonlocallycentralizedsparserepresentationforimagerestoration.IEEETrans.ImageProcess.

2013,22,1620–1630.[CrossRef][PubMed]

7. Wen,B.;Ravishankar,S.;Bresler,Y.Structuredovercompletesparsifyingtransformlearningwithconvergenceguaranteesand

applications.Int.J.Comput.Vis.2015,114,137–167.[CrossRef]

8. Xu,J.;Zhang,L.;Zhang,D.Atrilateralweightedsparsecodingschemeforreal-worldimagedenoising.InProceedingsofthe

EuropeanConferenceonComputerVision,Munich,Germany,8–14September2018;pp.20–36.

9. Zoran,D.;Weiss,Y.Fromlearningmodelsofnaturalimagepatchestowholeimagerestoration. InProceedingsofthe2011

InternationalConferenceonComputerVision,Barcelona,Spain,6–13November2011;pp.479–486.

10. Xu,J.;Zhang,L.;Zuo,W.;Zhang,D.;Feng,X.Patchgroupbasednonlocalself-similaritypriorlearningforimagedenoising.In

Proceedingsofthe2015IEEEInternationalConferenceonComputerVision(ICCV),Santiago,Chile,7–13December2015;pp.

244–252.

11. Chen,F.;Zhang,L.;Yu,H.Externalpatchpriorguidedinternalclusteringforimagedenoising.InProceedingsofthe2015IEEE

InternationalConferenceonComputerVision(ICCV),Santiago,Chile,7–13December2015;pp.603–611.

12. Zuo,W.;Zhang,L.;Song,C.;Zhang,D.Textureenhancedimagedenoisingviagradienthistogrampreservation.InProceedings

ofthe2013IEEEConferenceonComputerVisionandPatternRecognition,Portland,OR,USA,23–28June2013;pp.1203–1210.

13. Gu,S.;Zhang,L.;Zuo,W.;Feng,X.Weightednuclearnormminimizationwithapplicationtoimagedenoising.InProceedingsof

the2014IEEEConferenceonComputerVisionandPatternRecognition,Columbus,OH,USA,23–28June2014;pp.2862–2869.

14. Zhao,Q.;Meng,D.;Xu,Z.;Zuo,W.;Yan,Y.L1-normlow-rankmatrixfactorizationbyvariationalbayesianmethod.IEEETrans.

NeuralNetw.Learn.Syst.2015,26,825–839.[CrossRef][PubMed]

15. Schmidt,U.;Roth,S.Shrinkagefieldsforeffectiveimagerestoration.InProceedingsofthe2014IEEEConferenceonComputer

VisionandPatternRecognition,Columbus,OH,USA,23–28June2014;pp.2774–2781.

16. Chen,Y.;Yu,W.;Pock,T.Onlearningoptimizedreactiondiffusionprocessesforeffectiveimagerestoration.InProceedingsofthe

2015IEEEConferenceonComputerVisionandPatternRecognition(CVPR),Boston,MA,USA,7–12June2015;pp.5261–5269.

17. Zhang,K.;Zuo,W.;Chen,Y.;Meng,D.;Zhang,L.Beyondagaussiandenoiser:Residuallearningofdeepcnnforimagedenoising.

IEEETrans.ImageProcess.2017,26,3142–3155.[CrossRef][PubMed]

18. Zhang,K.;Zuo,W.;Zhang,L.Ffdnet:Towardafastandflexiblesolutionforcnn-basedimagedenoising. IEEETrans. Image

Process.2018,27,4608–4622.[CrossRef][PubMed]

19. Guo,S.;Yan,Z.;Zhang,K.;Zuo,W.;Zhang,L.Towardconvolutionalblinddenoisingofrealphotographs.InProceedingsofthe

2019IEEE/CVFConferenceonComputerVisionandPatternRecognition,LongBeach,CA,USA,15–20June2019;pp.1712–1722.

20. Ma,R.;Zhang,B.;Hu,H.Gaussianpyramidofconditionalgenerativeadversarialnetworkforreal-worldnoisyimagedenoising.

NeuralProcess.Lett.2020,51,2669–2684.[CrossRef]

21. Anwar,S.;Barnes,N.Realimagedenoisingwithfeatureattention.InProceedingsofthe2019IEEE/CVFInternationalConference

onComputerVision(ICCV),Seoul,RepublicofKorea,27October–2November2019;pp.3155–3164.

22. Li,D.;Chen,H.;Jin,G.;Jin,Y.;Chen,E.Amultiscaledilatedresidualnetworkforimagedenoising.Multim.ToolsAppl.2020,79,

34443–34458.[CrossRef]

23. Binh,P.H.T.;Cruz,C.;Egiazarian,K.FlashlightCNNimagedenoising.InProceedingsoftheIEEEEuropeanSignalProcessing

Conference,Amsterdam,TheNetherlands,18–21January2021;pp.670–674.

24. Quan,Y.;Chen,Y.;Shao,Y.;Teng,H.;Xu,Y.;Ji,H.Imagedenoisingusingcomplex-valueddeepCNN.PatternRecognit.2021,111,

107–113.[CrossRef]

25. Guan,X.;Hu,W.;Fu,H.Remotesensingimagedenoisingalgorithmwithmulti-receptivefieldfeaturefusionandenhancement.

ActaPhotonicaSin.2022,51,365–377.

26. Zheng,M.;Zhi,K.;Zeng,J.;Tian,C.;You,L.AhybridCNNforimagedenoising.J.Artif.Intell.Technol.2022,2,93–99.[CrossRef]

27. Tian,C.;Zheng,M.;Zuo,W.;Zhang,B.;Zhang,Y.;Zhang,D.Multi-stageimagedenoisingwiththewavelettransform.Pattern

Recognit.2023,134,109050.[CrossRef]

28. Tang,Y.;Wang,X.;Zhu,J.;Gao,Y.;Jiang,A.LMENet:Alightweightmultiscaleefficientconvolutionalneuralnetworkforimage

denoising.InProceedingsoftheIEEERegion10Conference2022,HongKong,China,1–4November2022;pp.1–6.

29. Ronneberger,O.;Fischer,P.;Brox,T.U-net:Convolutionalnetworksforbiomedicalimagesegmentation.InProceedingsofthe

InternationalConferenceonMedicalImageComputingandComputer-assistedIntervention2015,Munich,Germany,5–9October

2015;pp.234–241.

30. Gungor,M.A.;Gencol,K.Developingacompressionprocedurebasedonthewaveletdenoisingandjpeg2000compression.Optik

2020,218,164933.[CrossRef]

31. Liu,P.;Zhang,H.;Zhang,K.;Lin,L.;Zuo,W.Multi-levelwavelet-CNNforimagerestoration. InProceedingsofthe2018

IEEE/CVFConferenceonComputerVisionandPatternRecognitionWorkshops,SaltLakeCity,UT,USA,18–22June2018;pp.

773–782.

32. Gungor,M.A.AcomparativestudyonwaveletdenoisingforhighnoisyctimagesofCOVID-19disease.Optik2021,235,166652.

[CrossRef][PubMed]

33. Qian,Y.;Huang,Z.;Fang,H.;Zuo,Z.Wglfnets:Wavelet-basedglobal-localfilteringnetworksforimagedenoisingwithstructure

preservation.Optik2022,261,169089.[CrossRef]

220

Mathematics2023,11,2772

34. Fu,H.;Cheng,J.;Xu,Y.;Wong,D.W.K.;Liu,J.;Cao,X.Jointopticdiscandcupsegmentationbasedonmulti-labeldeepnetwork

andpolartransformation.IEEETrans.Med.Imaging2018,37,1597–1605.[CrossRef][PubMed]

35. Liu,Y.;Cheng,M.-M.;Hu,X.;Wang,K.;Bai,X.Richerconvolutionalfeaturesforedgedetection.InProceedingsofthe2017

ConferenceonComputerVisionandPatternRecognition,Honolulu,HI,USA,21–26July2017;pp.5872–5881.

36. Ioffe,S.;Szegedy,C.Batchnormalization:Acceleratingdeepnetworktrainingbyreducinginternalcovariateshift.InProceedings

ofthe32ndInternationalConferenceonInternationalConferenceonMachineLearning,Lille,France,6–11July2015;pp.448–456.

37. He,K.;Zhang,X.;Ren,S.;Sun,J.Deepresiduallearningforimagerecognition.InProceedingsofthe2016IEEEConferenceon

ComputerVisionandPatternRecognition(CVPR),LasVegas,NV,USA,27–30June2016;pp.770–778.

38. Roth,S.;Black,M.J.Fieldsofexperts:Aframeworkforlearningimagepriors.InProceedingsofthe2005IEEEComputerSociety

ConferenceonComputerVisionandPatternRecognition,SanDiego,CA,USA,20–25June2005;Volume2,pp.860–867.

39. Martin,D.;Fowlkes,C.;Tal,D.;Malik,J.Adatabaseofhumansegmentednaturalimagesanditsapplicationtoevaluating

segmentationalgorithmsandmeasuringecologicalstatistics.InProceedingsoftheEighthIEEEInternationalConferenceon

ComputerVision,Vancouver,BC,Canada,7–14July2001;Volume2,pp.416–4232.

40. Franzen,R.KodakLosslessTrueColorImageSuite.1999.Availableonline:http://r0k.us/graphics/kodak(accessedon1January

2022).

41. Zhang,L.;Wu,X.;Buades,A.;Li,X.Colordemosaickingbylocaldirectionalinterpolationandnonlocaladaptivethresholding.J.

Electron.Imaging2011,20,23016.

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

221

mathematics

Article

An Analysis of Climate Change Based on Machine Learning and

an Endoreversible Model

SebastiánVázquez-Ramírez1,MiguelTorres-Ruiz1,*,RolandoQuintero1,KwokTaiChui2

andCarlosGuzmánSánchez-Mejorada1

1 InstitutoPolitécnicoNacional,CIC,UPALM-Zacatenco,MexicoCity07320,Mexico;

svazquezr1102@alumno.ipn.mx(S.V.-R.);rquintero@ipn.mx(R.Q.);cmejora@ipn.mx(C.G.S.-M.)

2 DepartmentofElectronicEngineeringandComputerScience,SchoolofScienceandTechnology,

HongKongMetropolitanUniversity,HongKong,China;jktchui@hkmu.edu.hk

* Correspondence:mtorresru@ipn.mx;Tel.:+52-(55)-5729-6000(ext.56590)

Abstract:SeveralSunmodelssuggestaradioactivebalance,wheretheconcentrationofgreenhouse

gasesandthealbedoeffectarerelatedtotheEarth’ssurfacetemperature.Thereisaconsiderable

incrementingreenhousegasesduetoanthropogenicactivities.Climatechangecorrelateswiththis

alterationintheatmosphereandanincreaseinsurfacetemperature.Efficientforecastingofclimate

changeanditsimpactscouldbehelpfultorespondtothethreatofc.c. anddevelopsustainably.

Manystudieshavepredictedtemperaturechangesinthecomingyears.Theglobalcommunityhasto

createamodelthatcanrealizegoodpredictionstoensurethebestwaytodealwiththiswarming.

Thus,weproposeafinite-timethermodynamic(FTT)approachinthecurrentwork.FTTcansolve

problemssuchasthefaintyoungSunparadox.Inaddition,weusedifferentmachinelearningmodels

toevaluateourmethodandcomparetheexperimentalpredictionandresults.

Keywords: clustering; machinelearning; greenhousegas; finite-timethermodynamics; climate

change

MSC:68U01

Citation:Vázquez-Ramírez,S.;

Torres-Ruiz,M.;Quintero,R.;Chui,

K.T.;GuzmánSánchez-Mejorada,C. 1.Introduction

AnAnalysisofClimateChangeBased

Theissueofclimatechangestandsasoneofthemostsignificantobstaclesthathuman-

onMachineLearningandan

itymustconfront.Thus,extensivescientificevidencedemonstratesthatthealteringclimate

EndoreversibleModel.Mathematics

hassignificantlyimpactedsocietiesthroughouthistoryandinthepresent,posingsevere

2023,11,3060. https://doi.org/

effectsforthefuture.Modernadvancementsinquantitativeempiricalstudieshaveshed

10.3390/math11143060

lightonthecrucialinterconnectionswithintheinterconnectedclimate–humansystem[1].

AcademicEditor:WeiFang Variousstatisticalstudieshaveexploredthecause-and-effectrelationshipbetweenpartic-

Received:15June2023 ularclimateconditionsandtheirinfluenceonsocialinteraction,agriculture,economics,

Revised:8July2023 migratoryflows,andhealth[2].

Accepted:9July2023 Theemergenceofscientificeffortsindifferentfieldshascreatedaconsensusconcern-

Published:11July2023 ingthesustainabledevelopmentofinitiativesandstrategiestomitigateclimatechange.

Themostsevereconsequencesofclimatechangedirectlyaffectthehealthofcitizensdueto

humanactivitiescausingtheproliferationofgreenhousegasesintheatmosphere,which

inducestheincreaseintemperaturesandalterationofthehydrologiccycle[3].Theanalysis

Copyright: ©2023bytheauthors. oftheclimatechangesituationisverytimely,becausesecondaryeffectsareassociated

Licensee MDPI, Basel, Switzerland. withthenegativeimpactonagriculture,thegeographicdistributionofinfectiousdiseases,

Thisarticleisanopenaccessarticle

large-scalemigrations,cleanwateraccess,andothers[4].

distributed under the terms and

Machinelearningtechniqueshaverecentlysuccessfullyemployedstatisticaldown-

conditionsoftheCreativeCommons

scalingmethodsforglobalclimatemodels.AccordingtoNouranietal.[5],adiverserange

Attribution(CCBY)license(https://

ofmachinelearningmodelshavebeendevelopedandusedingroundwatermodeling

creativecommons.org/licenses/by/

andotherpredictiontaskswithinthefieldofenvironmentalengineering[6]. Prediction

4.0/).

Mathematics2023,11,3060.https://doi.org/10.3390/math11143060 https://www.mdpi.com/journal/mathematics

223

Mathematics2023,11,3060

modelsfocusedonmachinelearningtoanalyzeclimatevariablessuchasprecipitationand

temperaturehavebeenproposedinotherstudiestoimproveaccuracy[7]. Thesupport

vectorregressionmodel,theadaptiveneurofuzzyinferencesystem,andthefeedforward

neuralnetwork(FFNN)arethemostfrequentlyemployedmachinelearningmodelsto

analyzeclimatechangeandparticulargroundwaterlevels[8,9]. Otherapproachesare

basedonGaussianmodels,whicharesuitablemethodsforglobalclimatemodeling[10].

Recently,therehasbeenagrowingemergenceofdeeplearningmodelsthathave

garneredsignificantattentionacrossvariousengineeringdisciplinesduetotheirability

toextractfeaturesfromdata.Amongthesemodels,thelongshort-termmemory(LSTM)

neuralnetworkstandsoutasapowerfuldeeplearningmodelcapableofcapturingsequen-

tialcharacteristicsfromtimeseriesdata.LSTMhasalreadybeensuccessfullyappliedin

groundwater-levelmodeling,asdemonstratedbyNouranietal.[11]. Accordingtothe

literaturereview,decisiontrees,randomforests,andartificialneuralnetworksarethemost

commonlyappliedmachinealgorithmstoanalyzeclimatechangeriskassessment.They

haveenabledtheidentification,classification,anddetectionoftargetsandenvironmental

andstructuralfeatures,particularlyfloodandlandslideriskevents[12].

In the same context, analyzing changes in hydrological systems directly impacts

globalclimatechange,inwhichclassicmachinelearningalgorithmscouldbelimitedto

quantifyingeventsrelatedtotheclimatevariabilityinthosehydrologicalsystems.However,

theGaussianprocessregressionmethodhasbeendemonstratedtoimprovetheanalysis

concerningnonlinearclimatevariables[13].

Ontheotherhand,theliteraturereportsacrucialsynergybetweenthephysics-based

modelsandmachine-learningtechniquestodevelophybridapproachestoclimatechange

analysis[14].Thus,Chukwujinduetal.[15]revealedacrucialrelationshipbetweenphysics

andartificialintelligencetounderstandbettertheclimatechangecausedbysolarradiation.

Accordingtothedevelopmentandintegrationofmultidisciplinaryfields,thelast

yearshaveinvolvedapplyingphysicstheoriestoanalyzevariousEarthphenomena.Now,

physicistsandcomputerscientistshavedemonstratedenormousinterestinstudyingthe

aforementionedsecondaryeffectsofclimatechange.Inthissense,Jusupetal.[16]consid-

ered“socialphysics”anessentialtooltoquantifysocialandenvironmentalphenomena.

Moreover,thisapproachisorientedtowardanalyzingdifferentissuesinwhichthisdis-

ciplinecanexplicitlyexplaineachphenomenon. Forinstance,inaddressingtheclimate

changetopic,theuseofnetworkareatodescribethecomplexproblemofEarth’sclimate

systemevidenceshowphysicsmethodsaresuitabletoworkinamultidisciplinaryway

withotherfieldstofacethisissuequantitatively.

Addressingtherisksassociatedwithclimatechange,Steffenetal.[17]recognizedthe

relationshipbetweenthesocialcommunityandclimate.Therefore,thisstrategyextends

beyondsolelyunderstandingthephysicalaspects,andrequiresmobilizinghumanaction.

Scientistsarestrivingtomeetthischallengebyintegratingclimatescience,socialsciences,

computerscience,andhumanities,resultinginanewfieldcalledearthsystemscience,

whichaimstofosteraholisticunderstandingoftheEarth’scomplexdynamics.

Ontheotherhand,globalwarmingisavisibleconsequenceoftheheightenedin-

tensityandfrequencyofextremeweatherandclimateevents,whichencompassarange

ofphenomena,includingheatwaves,droughts,wildfires,floods,andhurricanes.These

extremeeventsposeasubstantialrisktohumanlivesandlivelihoods,evidentthrough

consequencessuchasfreshandcleanwaterscarcityanddiminishedfoodproduction.Such

extremeeventsarecharacterizedbytheclimaticvariablesurpassingacriticalthreshold.It

isworthnotingthatsomeextremeeventsmayarisefromnaturalclimatevariabilityand

arenotdirectlylinkedtohuman-inducedforces[18].

Thereisahighdegreeofconfidencethattheanthropogenicriseingreenhousegas

concentrationsandotherhuman-inducedfactorsisresponsibleformorethan50%ofthe

reportedglobalaveragesurfacetemperatureaccumulationbetween1951and2010[16].

Thus,consideringthetheoreticalfoundationspresentedin[16,19],weproposeafinite-

timethermodynamicapproachtomodelandpredictEarth’sglobalwarming,comparing

224

Mathematics2023,11,3060

theresultsofthemodelwiththeimplementationofmachinelearningtechniquestoassess

thepredictions.

Finite-timethermodynamics(FTT)hasbeendevelopedbyplacingrealisticlimitson

irreversibleprocessesthroughvariousproperties,suchaspower,efficiency,anddissipa-

tion.FTTcanbeconsideredanextensionofclassicalequilibriumthermodynamics(CET),

inwhichthermodynamicmodelsmoresimilartotherealworldaresoughtcomparedto

thosegivenbyCET.So,thesemodelsconsidertheirreversibilitiesofthesystem[20,21].

Theapproachincorporatestheconstraintsoffinite-timeoperation;constraintsonsystem

variables;andgenericmodelsforthesourcesofirreversibility,andthustheproduction

ofentropysuchasfiniterate,heattransfer,friction,andheatleakage,amongothers[22].

Moreover,anextremeoroptimumofathermodynamicallysignificantvariableiscalculated,

suchasminimizingentropyproduction,maximizingenergyoravailability,andmaximiz-

ingpowerandefficiency[22]. ThepioneeringworkoftheFTTcorrespondstoCurzon

andAhlborn[20,22],inwhichthefundamentallimitsofapowerplantusedamachine

endoreversiblemodel. ThisismadeupofanendoreversibleCarnotcycle,wheretheirre-

versibleprocessesinvolvetheexchangeofheatbetweenthethermalreservoirsandthe

activesubstance.

Thethermalengineiscomposedoftwotemperaturestores,T1andT2,whereT1 >T2,

twoirreversiblecomponentsthatarethetwothermalresistances,whichproducethermal

flowstowardsthereversibleCarnotenginewithintermediatetemperaturesT1wandT2w,

withT1w >T2w,placedbetweentheintermediatestores.Themodelconsidersalinearheat

transferbetweentwoirreversiblecomponents(thermalconductancesαandβ)conductances

(seeFigure1).

Figure1.SchemeofaendoreversiblemodelproposedbyDeVos[23].

Summingup,Figure1showsaschematicrepresentationoftheendoreversibleCurzon–

Ahlbornengine.ItisbuiltbytworeservoirsoftemperaturesT1andT2,respectively:αand

β,whichdenotethermalconductanceconstants,andareversibleCarnotenginerepresented

byT1ωandT1ω,wherePisthepoweroutputofthecycle.

225

Mathematics2023,11,3060

Aproblemsolvedbyfinite-timethermodynamicsefficientlyistheso-calledweak

youngSunparadoxproposedbySaganandMullen[24].Thisstudypresentsadrawback

forunderstandingtheearlystagesofplanetEarth,sincetheSun’sluminosityabout4.5Gyr

agowasbetween70–80%ofitsvaluetooperate[24–26]. So, itrepresentsaterrestrial

temperaturebelowthewaterfreezingpoint.Theplanet’ssurfacetemperatureiscontrolled

bythesolarradiationitacquiresanditsinterchangewiththegasesintheatmosphere.We

considerablackbodyradiativeequilibriumbetweentheyoungSunandtheEarthobtained

inasurfacetemperatureT=255K,lowenoughtokeepmostoftheplanet’ssurfacefrozen

downto1–2Gyr[24].However,severalstudies,togetherwithsedimentaryrecords,suggest

theexistenceofanaveragesurfacetemperaturecapableofhavingliquidwaterforalmost

theentirehistoryoftheplanet[24].So,toresolvesuchaparadox,thefirstassumptionis

takenthatsolarradiationhasincreasedintheSun’slifetimeduetotheincreaseindensity

ofthesolarnucleus[24].TheluminosityoftheyoungSunhasbeenestimatedtobe30%

lessthantheactualvaluereceivedfromtheSun,accordingtowhatwassaidbyGough[24],

whereIscisthepresentluminosityoftheSunandt0 ≈4.56Gyr,whichisthepresentage

oftheSun. Equation(1)showstheevolutionoftheSun’sluminosity,andthisequation

affectstheamountofaveragesolarradiationq¯s = Isc (1−ρ)/4receivedbytheplanet.

TheequationoftheluminosityofGoughisexpressedinthefollowingway:

! (cid:22) (cid:23)(cid:27)

I(t)= 1+0.4 1− t

−1

Isc (1)

t0

Basedonthefoundation,theproblemofthermodynamicequilibriumbetweenthesolar

system’splanetsdependsontheinfluxofsolarincidentIsc,theEarth’salbedoρ,andthe

effectofgreenhouseγ. Thus,theissueofthethermalequilibriumamongsolarsystem

planetsandacorrecttemperatureestimationissolvedbasedontheatmosphere’sphysical

characteristics. Curzon and Ahlborn [22] introduced the finite-time thermodynamics

concept.TheyachievedthisusingaCarnotcyclemodel,incorporatinglimitedheattransfer

between the heat reservoir and the working substance, all within a maximum-power

operatingregime.Followingitsinitialintroduction,finite-timethermodynamicsunderwent

furtherdevelopmenttoencompassvariousoperatingregimes,including—butnotlimited

to—efficiencypower,ecologicalfunction,andmore. UsingtheFTT-basedapproachin

creatingmodelsforpowerconvertersresultsinmoreaccuraterepresentationsoftheir

operational levels in real-world scenarios. In [20], an atmospheric convection model,

knownastheGordon–Zarmi(GZ)model,wasintroducedtoestimatethetemperatureof

theEarth’slowestatmosphericlayerandestablishanupperlimitforaveragewindpower.

TheGZmodelincorporatesaconvectioncell,anendoreversibleCarnotcycle,andtwo

externalthermalreservoirs,suchasair,surroundingtheactivesubstance.

Thestudypresentedin[27]examinedtheendoreversiblemodelandrecognizedthat

thereisadissipationofwindenergy.Theauthorsproposedtoderiveanupperlimitfor

theefficiencyofconvertingsolarenergyintowindenergy,whichisapproximately8.3%,

assumingtheatmospheric“heatengine”isfullypoweredbyacompletepowerengine.

Ontheotherhand,VanderWelimprovedanewefficiencyofthesolarenergyupper

boundwmax ≈ 10.23%withanotherendoreversiblemodelbasedonconvectiveHadley

cells[24,28].ThepeculiarityoftheGZmodelsisthattheyofferapotentialresolutionto

theparadoxknownasthe“youngandweakSun”,whichwasinitiallyintroducedbyCarl

SaganandGeorgeMullenin1972[25,26].TheGZandGoughmodelsexaminetheevolution

ofthesolarconstant,enablingtheinvestigationofpotentialfuturescenariosforEarth’s

temperature.Thesemodelsemployvariousobjectivefunctions,includingmaximumpower,

efficientpower,andecologicalfunction,toanalyzeandassessthesescenarios.

Hence,thepresentresearchstudyaimstoinvestigatetheplanet’ssurfacetemperatures

resultingfromtheescalatinglevelsofgreenhousegases.Theapproachinvolvesanalyzing

thethermodynamicbehavioroftheatmospherewithinafinite-timeregime.Wedecided

toemploythismethodology,consideringthegoodresultsinpredictingclimatechangein

226

Mathematics2023,11,3060

severalgeologicerasinthepast. So,itispossibletomodifyandsettheendoreversible

machinemodeltoforecasttemperaturesderivedfromclimatechangeinthecomingyears.

Theremainingpaperisorganizedasfollows:Thesubsequentsectionconsistsofcom-

prehensivestate-of-the-artclimatechangemodelsbasedondifferentapproaches.Section3

describesthepreliminaryfoundationsconcerningfinite-timethermodynamics;Section4

outlinesthemethodsrelatedtotheproposedendoreversiblemodel;andSection5describes

theproposedmodelanditspeculiarities.Section6showstheexperimentalresults,andthe

discussionoftheoutcomesandfindingsareincludedinSection7,andthelastsection

involvestheconclusionandfutureworks.

2.RelatedWork

Globalwarmingcausedbyhumanactivitiesrepresentsoneofthemostsignificant

challengesofthepresenttime.Theclassicalapproachesconcerningclimatechangehave

studiedcomplexsystemssuchasdifferentialequationsanddevelopmentsinchaostheory.

Nevertheless,thelargeamountofdataavailableallowsustouseartificialintelligence

techniques,whicharemorestraightforwardthanthoseusedbytheareasofcomplexity

science,resultinginthepredictionoffuturescenariosduetoclimatechange.

AccordingtoHoughton[29],globalwarmingisaclimatesystemwhereseveralvari-

ablesareresponsibleforraisingglobalaveragetemperatures. Mostoftheseeffectsare

relatedtotheradiativebalanceoftheplanetaryatmosphere:watervaporfeedback,cloud

radiationfeedback,andoceancirculationfeedback.Inconsequence,allofthemrefertothe

albedoandgreenhouseeffects.Therefore,toforecastglobalwarming,asetofcharacteristics

thataffecttheglobalemissionofgreenhousegasesmustbetaken.Thesegaseshavehada

notableincreaseduetoanthropogenicbehaviorandactivity.Developmentprojectionsof

globalaveragetemperaturechangesforthepresentcenturyareintherangeof0.15–0.6°C

perdecade.Understandingthisproblemallowsustoconsiderhumans’andecosystems’

impactsandadaptivecapacity[29].

Oneofthemajorconsequencesofglobalwarmingisthemeltingoficebodiesonthe

Earth.TheArcticSeaisoneoftheleadingindicatorsoftheincreaseinaveragetemperature.

Thestudyoftheiceconcentrationandtheriseinsealevelhasvariousapproaches,oneof

whichthatiswidelyusedisdeeplearningtechniquestopredicthowtheiceconcentration

changeswiththeincreaseinaveragetemperature[30]. InthesamewaythattheArctic

layersandtheirmeltingshowtheeffectofclimatechange,alloceansexperiencethesame

significantwarmingandarisingsealevel,soitisnecessarytogeneratediagnosticand

prognosticpredictionmodelstoelucidatetheseincreasesandtheirrisks,sincetheyare

associatedwithotheradverseeventssuchasthepropagationofcycles,lackofrain,andthe

growthandspreadofdiseases.Accordingtodiverseauthors,thecombinationofmachine

learninganddeeplearningtechniquescangiveusentirelyaccuratepredictionsforthe

future[31–34].

InthestudycarriedoutbySidhuetal.[35],theuseofmachinelearningisanalyzedto

understandtheimpactofclimatechangeondifferenttypesofcrops,takingintoaccount

climate–yieldrelationships.Theauthorscomparedtheusuallinearregressiontechniquefor

estimatinghistoricaldatatoapproximateyieldagainstclimatechangeandusingboosted

regressiontrees. Theconclusionssuggestedthatinterpretingresultsbasedonasingle

modelcangeneratebiasesintheinformationobtained.

Ontheotherhand, duetothehigheconomicandsocialimpactsassociatedwith

climatechange,itisessentialtounderstandthecausesandidentifythepatternsofthe

obtaineddatatomakecorrectpredictions.AccordingtoZhengetal.[36],theconstructionof

areliablemodelbasedonexperimentaldataandtherelationshipbetweentemperatureand

theconcentrationofgasesintheatmospheresuchascarbondioxide(CO2 ),nitrousoxide

(N2O)andmethane(CH4 ),isthefirstchallengetoaddresstheclimatechangeproblem.

Zheng’sstudyusedvariouslearningtechniques,suchaslinearregression,supportvector

machines,andrandomforeststobuildanaccuratemodelthatwouldidentifychangesinthe

227

Mathematics2023,11,3060

atmosphere’sincreasingtemperature,dominatedmainlybytheincreaseinthetemperature

ofCO2duetoitshigherconcentrationwithingreenhousegases.

Differentauthorsarguethattheconstructionofareliablemodelcombinedwiththe

temperaturedatasetandmachinelearningpredictiontoolswillhelpustohaveabetter

understandingofthephenomenon,andthusbeabletomakeagoodforecastthatallows

ustofacetherisksofclimatechange.ThethermalequilibriummodelwasstudiedbyDe

VosandFlater[28],whoanalyzedsolarradiationasanenergyconverterusedtoexamine

theaveragetemperatureofaplanet. Itiscarriedoutbytheradiationfromtheplanet’s

surfaceandtheirradiancereachingEarth. Thisanalysistakesintoaccountthephysical

characteristicsoftheatmosphere,suchasfriendlinessandthealbedoeffect[22,27,28].Thus,

thetotalfluxQappearsasshowninEquation(2).

(cid:22) (cid:23)

Q=4πR2σ (1−ρ)f T4−(1−γ)T4 (2)

4 s p

Itisthefirstthermodynamicmodelthatallowsforadynamicstudyofthedifferent

layersoftheatmosphere,withthelowestlayercorrespondingtothetemperatureonthe

planetarysurface. Thisdevelopmentcananalyzevariousscenarioswheregreenhouse

gasesandalbedoconcentrationsaremodified.Thefeasibilityofthemodelwastestedin

thestudyofgeologicaleras,andseveralauthorscarriedoutthesolutionofthefaintyoung

Sunparadox[24,25]. Thestudyofthesolarconvertersundertheregimeoffinite-time

thermodynamicswasanalyzedinthiswork,changingtheparameterstocurrenttime,

consideringtheincreaseinCO2maingreenhousegas[36];itsrelationshipwithalbedowas

developedtoo.Inaddition,adissipationofenergyinthesystemhasrealisticresultsatthe

currenttime.

Accordingtothestateoftheart,thereareseveralproposalsrelatedtoanalyzingglobal

climatechangebasedonpredictionmodelsdevelopedwithdeeplearningapproaches,us-

ingspecificallyconvolutionalandrecurrentneuralnetworks.In[37],amethodtoefficiently

predictweatherforecastingwasproposedbydesigningamodelbasedonaconvolutional

neuralnetwork(CNN).Thus,Miloshevichetal.[38]proposedamethodologytocreate

forecastingartifactstrainedwithdataof8000-yearmodels,consideringaninfrastructure

definedbyasetofvariousCNNs,whichwasprimarilyfocusedondescribingextreme

heatwavedatasets.

Ontheotherhand,theCNNarchitecturehasbeenwidelyemployedtoassesspre-

dictionsbetweenthehourlysoiltemperatureandthesubsurfacedepth. Thus,ref.[39]

describedaone-dimensionalCNNpredictionmodeltodemonstratethattheairtempera-

tureandsurfacethermalradiationdirectlyimpactthesoiltemperaturepredictionmodel,

affectingglobalwarming.

Diversestudieshaverevealedthatclimatechangerushestheincreasingglobaltemper-

ature,causingariseintheinternationalsealevel.Consequently,Hassan[40]implemented

asetofdifferentmultivariablepredictionmodelsbasedontheprincipaldeeplearning

techniques:recurrentneuralnetworks(RNN),longshort-termmemorynetworks(LSTM),

gatedrecurrentunitnetworks(GRU),andWaveNetasaparticularcaseofCNN.Themod-

elsused29yearsofdatawithmultiplevariablessuchaschangesintheoceanheatcontent,

levelofcarbondioxide,massvariationintheGreenlandandAntarcticaregions,andglobal

temperatureanomalies.

AccordingtoGhimireetal.[41],theuseofaconvolutionalneuralnetworkwitha

multilayerperceptron(MLP)generatesefficientforecastsofglobalsolarradiation(GSR).

Theoutcomesoftheirmodelachievedarelativeerroroflessthan10%,generatingamodel

withveryhighperformancecomparedtoclimatemodels,especiallyinmodelsdeveloped

withconvectivecells,suchasGordonandZarmi-typemodels. Therefore,usingCNN

enrichesthepredictionsoftheclimatemodels,inducingbetterforecaststhatdetectextreme

weathereventscausedbyclimatechange.

In consequence, the impact of climate change is reflected in the manifestation of

extremeweathereventssuchasdroughts, floods, andheatwaves. So, improvingthe

228

Mathematics2023,11,3060

methodsforpredictingglobalwarminganditseffectsallowsforadaptingasasociety

to the planet’s dynamic environment. An issue to analyze with climate change is its

correlationwiththehydroclimaticsystemsoftheEarth.Larsonetal.[42]proposedadeep

convolutionalresidualregressiveneuralnetworktodetermineriverbasins’responseto

thewatercycle’sflows. Theanalysisrevealedthatthisarchitectureandthecatchment

flowdataexhibitedsatisfactorypredictionperformanceforvariouslocationsatdifferent

timescales.

Naturaldisastersarerelatedtoclimatechange;someexamplesoftheseeventsinclude

flashfloods, droughts, andhurricanes. Thus, thePacificOceanweatherphenomenon

knownasElNiño-SouthernOscillation(ENSO)iscausedbycyclicalchangesinseasurface

temperature(SST)andtemperaturesintheatmospherenearthetropics.TheENSOimpact

generatestemperaturevariations,makingthemslightlywarmerorcolderuptoextreme

temperatures,inducingnaturaldisasters.AsclaimedbyJonnalagaddaandHashemi[43],

theuseoftheadaptivegraphconvolutionalrecurrentneuralnetwork(AGCRNN)cancap-

turethetemporalrelationshipsoffeatureswiththeOceanicNiñoIndex(ONI),increasing

thepredictiontimefromthreemonthstoeighteenmonths,surpassingthecurrentdynamic

andstatisticalmodels.

Inrecentyears,ithasbeenobservedthattheautomateddetectionofextremeweather

eventshasincreased.Therefore,itisrequiredtoimprovethepredictionperformanceto

dealwiththeseweatheranomalies.Currentresearchhasshownthatnewconvolutional

neuralnetworkarchitecturesenhancemeteorologicaleventdetection. AccordingtoLa-

combeetal.[44],theuseofweightedlossfunctionscounteractingtheclassimbalancein

thedatatogetherwithacorrectarchitecturecouldshowasignificantimprovementofthe

predictionupto39.2%concerningeventsasnaturalcyclones.Duetothehighimpactsof

extremeweatherevents,anenergytransitionthatdoesnotdependontheburningoffossil

fuels,themaingeneratorofgreenhousegases,isurgent.Photovoltaicpowerproductionis

agoodpowergenerationoption.However,thistypeofenergyproductionissensitiveto

weather,andcangeneratevariationsdependingonweatherconditions.Tomakerealistic

energyproductionforecasts,Ramakrishnanetal.[45]suggestedacombinedCNNand

LSTMmodel,obtainingabetterpercentageofphotovoltaicyieldprediction,considering

slowclimatefluctuationsandsubstantialclimaticvariations.

Ontheotherhand,amongthemostsignificantconsequencesofclimatechangeis

relatedtothesolarenergygenerationofpowersystems.Recently,theaccuracyofintrahour

solarforecastinghasbeenacrucialtopictobeanalyzedinthefieldduetotwocritical

aspects:(1)theaccuracyofpredictionmodelsconsideringthedynamiccoverageofclouds,

and(2)theshortforecasthorizonforaminimaltimewindow[46].Thus,differentproposals

andmethodstofacetheseaspectshavebeenproposed. CaldasandAlonso-Suárez[47]

designed a hybrid model to predict solar irradiance, merging sky (cloud status) data

providedbyimagesandirradiancemeasures. Theoutcomesrevealedthatthemodelis

efficientinpreservingsolarenergyresources. Inthissense,Pedroetal.[48]presenteda

studytocomparemachinelearningalgorithmssuchask-nearestneighborsandgradient

boostingintaskstoclassifydatabasedonintrahourforecastingandirradiance,taking

informationfromskyimages. Moreover,solarenergyisthemostfavorablerenewable

sourceofelectricity,employingasystembasedonaphotovoltaicpowersupply. In[49],

anartificialneuralmodelwasdesignedtopredictsolarirradiancevalueswithoutusingthe

detectionofclouds.

3.Preliminary

3.1.Finite-TimeThermodynamics

TheendoreversibleCarnotmachineisnotinthermodynamicequilibriumwiththe

reservoirsandtheactivesubstance.Thereisaseparationbetweentheinternallyreversible

processes and the irreversibilities at the system boundaries, where internal processes

withfastrelaxationtimescanbeconsideredreversibleandtheentropychangeforthe

thermodynamicuniverseΔSu ofthemachineispositive,theentropybeingofournull

229

Mathematics2023,11,3060

workingsubstanceΔSw =0.Thisdefinitionisknownastheendoreversibilityhypothesis;

whenthemodelproposedbyCurzonandAhlborn[22]evolvesinfinitetime,themodel’s

powerisnonzero,unlikethatgivenbyCET[50].

3.2.CurzonandAhlbornEngine

TheenginehasthermalconductancesthatcomplywithFourier’slawforheatconduc-

tion(Q˙ =−λ∇T).Inthepresentwork,wewillusethefollowingnotationtorefertothe

heatflowsQ=Q˙,suchthat:

Q1 =α(T1 −T1w ) (3)

Q2 =β(T2w −T2 ) (4)

AformofsolutiontotheCurzonandAhlborn[22]engineandthemachineschematic

wasproposedin[27].Fromtheconservationofenergy,wehavetheheatflowQ1fromthe

upperreservoir,towardsthereversiblemachinewithpowerPtotheoutputflowQ2[51].

Bytheentropicconservationofthesystem,ΣS=0.Therefore,theproductionofentropy

mustbezero,whereasforthereversibleinternalmachine,weassumethatitsentropy

changesarezero(endoreversibilityhypothesis)[23,28,51,52].

σ= Q1 − Q2 =0 (5)

T1w T2w

FromEquation(5)withthesecondlawofthermodynamics,wehavethefollowing

relationshipforthermalconductorsT1wandT2w.

T1w = α+ α β T1 + α+ β β1− 1 η T2 (6)

α β

T2w = α+β (1−η)T1 + α+β T2 (7)

SubstitutingT1winEquation(6)andT2winEquation(7)withourflowQ1andQ2,we

obtainEquations(8)and(9).

Q1 =γ T1 − 1 T − 2 − η T1 η (8)

(cid:22) (cid:23)

Q2 =T2 β γ ( ( T 1 1 − (1 η − )T η 1 ) + − β T T 2 2 ) (9)

withtheexpression:

αβ

γ=

α+β

Thus,fromthedefinitionofefficiency,wecanobtainanexpressionforthepower

givenby:

P=γ η(T1 − 1 T − 2 η −T1 η) (10)

ResultinginefficiencyatmaximumpowerfortheCurzon–Ahlbornmachineknown

infinite-timethermodynamicsasη cathatsatisfies0<η ca <η c.

η CA =1− T T 2 1 (11)

IntheendoreversibleCurzon–Ahlbornmodel,thedissipationwillbegivenbyformu-

lasthathavebeenderivedthatshowtheefficiencyofanengineundermaximumpower

conditions[20,21].

Φ

rb

=Q2 −T

T

2

1

Q1 (12)

230

Mathematics2023,11,3060

4.MaterialsandMethods

4.1.GordonandZarmi(GZ)Model

TheatmosphericconvectionmodelproposedbyGZconsistsofacellasanendore-

versibleCarnotcyclebetweentwothermalreservoirsofextremetemperatures:thetem-

peratureT1istheworkingfluid(atmosphere)temperatureatthelowestaltitudeinthe

system,relatedtothetemperatureofEarth’ssurface;thetemperatureinthehighestpart

oftheworkingfluidisthecoldreservoirintheGZmodel,andthetemperatureisrelated

tothecosmicbackgroundradiationT2 =3K(seeFigure2)[20].Theinputenergyissolar

radiation,theactivesubstanceistheatmosphere,andtheworkperformedbythefluidof

thethermalmachineisthemeanpowerofthewinds.TheGZconvectioncellconsistsof

severalcomponents,includingtwoisothermalbrancheswheretheatmosphereabsorbs

heatatloweraltitudes.Additionally,twointermediateadiabaticbranchesareassumedto

beinstantaneous,andtheremainingbranchreleasesheatathigheraltitudesintotheuni-

verse[53].TheGZmaximizestheworkpercycleW,subjecttothermodynamicrestrictions

andtheaveragesolarradiationfluxqs[20,53].

q¯s = Isc (1−ρ) (13)

4

TheGZmodelworkswithaSun–Earth–windsystemasanendoreversibleengine,

inwhichtheinputheatisthesolarradiation,theactivesubstanceistheatmosphere,andthe

laborproducedbythiscycleisthemeanpowerofthewinds.Thecoldstoreforthismachine

isouterspace,withthetemperatureofthecosmicbackgroundradiationof3K[20].

Figure2. SimplifiedschemaproposedbytheGZdiagramofacyclicheatenginedrivenbysolar

energy,theheatinputisthesolarradiationperareaqs,andtheworkingfluidistheatmosphere.

Incontrast,theworkoutputisthemaximumwindenergy. Themodelcanobtainmaximumand

minimumtemperaturesoftheatmospherewithoutconsideringanyothereffectontheEarthapart

fromtheonealreadydescribedintheconvectivecell[20].

Figure2showsaschematicviewofthesimplifiedsystem,includingitsisothermaland

adiabaticbranches.Inaddition,thisdiagramisasimplifiedversionofathermalengine

drivenbysolarenergy.Thedescriptionofthisfigureisdenotedasfollows:

231

Mathematics2023,11,3060

1. The atmosphere absorbs solar radiation at low altitudes through two isothermal

branches. Atthesametime,heatispushedoutathighaltitudesthroughanother

branch,inwhichtheatmosphererejectstheexcessheat.

2. Therearetwointermediateadiabatscharacterizedbyascendinganddescendingair

currents,whichoccurinstantaneously.

Thetemperaturesassociatedwiththefour-cyclebranchesareasfollows:

1. T1representsthetemperatureoftheworkingfluidintheisothermalbranchsituated

atthelowestaltitude.Here,theworkingfluidabsorbssolarradiationduringevery

halfcycle.

2. Inthesecondhalfofthecycle,heatisreleasedfromtheworkingfluidattemperature

T2(atthehighestaltitudeofthecell)throughblackbodyradiation,whichisdirectedto-

wardsthecoldreservoirattemperatureTex(representingthe3Kbackgroundradiation

oftheuniverse)[20,54].

Theobjectiveofthismodelistomaximizetheworkpercycle,equivalenttomaximizing

theaveragepoweroutput,accordingtocertainthermodynamicrestrictions.Fromthefirst

lawofthermodynamicsforthismodel,wehavethefollowing:

(cid:26)

ΔU=−W+

t=tc

qs (t)−σ[T4(t)−Tex4(t)]dt=0 (14)

t=0

whereΔUisthechangeininternalenergyoftheactivesubstance,σistheStefan–Boltzman

constant(5.67×10 −8

m

W

2K4

), tc isthecycletime,and T isthetemperatureoftheactive

substance.Theentropychangeissubjecttotheendoreversibilityrestriction.

(cid:26) (cid:22) (cid:23)

ΔS= t= t= 0 tc qs (t)−σ[T T 4 ( ( t t ) )−T e 4 x (t)] dt=0 (15)

ThevariablesT,Textarefunctionsassociatedwiththetime.

(cid:15)

T(t)= T T 1 2 0 tc ≤ /2 t ≤ ≤ t tc ≤ /2 tc (16)

Tex (t)=3k 0≤t≤tc (17)

Thevariableqsisafunctionoftime,IscistheaveragesolarconstantovertheEarth’s

surface(1372.7W/m2),theaveragealbedoρ=0.35,andtheaveragevaluesareasfollows:

(cid:15)

qs (t)= 0 Isc (1−ρ)/ t 2 c/2 0 ≤ ≤ t t ≤ ≤ t t c c/2 (18)

T¯ =(T1 +T2 )/2 (19)

T¯n=(Tn+Tn)/2 (20)

1 2

Themeanpowerofthewindsisobtainedby:

P= W

t0

=q¯s +σT

e

4

x

−σT¯4 (21)

ThemodelusedbyGZconsidersthefollowingapproximationq¯s >>σT

e

4

x

;wehave

thefollowingEquation:

P=q¯s −σT¯4 (22)

Fromtheendoreversibilitycondition,thevariablesT,Texandthemeanvalueswe

obtainedare:

ΔS = q¯s − σ (T3+T3) (23)

int T1 2 1 2

232

Mathematics2023,11,3060

To maximize P subject to the endoreversibility condition, the Lagrangian is de-

fined in terms of the Lagrange multiplier λ and the thermodynamic constraint given

byL=P−λΔS,sothat:

L=T4(t)+λ[qs (t)/T(t)−σT3(t)] (24)

ForfindingtheextremeofL,thatis,solving ∂ ∂ T L( ( t t ) ) =0,wehavethefollowingsystem

ofequations:

T

1

5(t)+3σλT

1

4/4−λqs (t)/4=0 (25)

T5(t)+3σλT4/4=0 (26)

2 2

GZfoundthefollowingtemperaturevaluesforthelowestandhighestlayersofthe

Earth’satmosphereT1 =277K,T2 =192KandPmax =17.1

m

W

2

. Thesevaluesarenotfar

fromtheliteraturePmax =7

m

W

2

,T1 =290K(onthesurface)andT2 =195K(between75and

90km).GordonandZarmi[20]statedthattheirmeanpowerofwindsshouldbetakenas

anupperlimit.

4.2.NonendoreversibilityParameterinG-Z

Inrecentstudies,thenonendoreversibilityparameterRhasbeenusedtoinvestigate

thethermalmachinesofTTF.ThisparameterwasintroducedfromtheClausiusinequality,

consideringaclearancemeasureintheendoreversibleregime[55].

ΔSw1 +ΔSw2 ≤0 (27)

ΔSw1changesinthehotisothermandΔSw2inthecoldcompressionisotherm,inthe

endoreversiblecase.Thus,thisinequalitybecomesequalityinthefollowingequation.

ΔSw1 +RΔSw2 =0, (28)

whereRisgivenby:

R= (cid:5) Δ Δ S Sw w1 2 (cid:5) (29)

w w h h e e r r e e R R = = 1 (cid:5) Δ Δ is S S w w th 1 2 (cid:5) e ; e t n h d e o p r a e r v a e m rs e i t b e l r e o li f m n i o t n [5 -e 1 n ]. d T o h re e v p e r r e s v ib io il u it s y G is Z in co t n h v e e i c n t t i e o r n v c a e l l 0 lp ≤ ro R ces ≤ si 1 s ,

enrichedusingtheparameterR. Thus,tomaximizePsubjecttotheendorreversibility

conditionplustheparameterR,theLagrangeanL=P−λΔStooccupyisgivenasfollows:

& (cid:25)

L= σ (T4+T4)+λ q¯s − Rσ(T 1 3+T 2 3) (30)

2 1 2 T1 2

Solving∂ ∂ T L( ( t t ) ) =0tofindtheextremaoftheLagrangian;solvingthesystemnumerically,itis

foundthatforanonendoreversibilityparameterR=0.953[55]forρ=0.35,Isc =1372.7W/m2.

GZfoundthefollowingtemperaturevaluesforthelowestandhighestlayersoftheEarth’s

atmosphereT1 =280.562K,T2 =194.293K.

5.TheProposedModel

5.1.GreenhouseFactor

Theplanet’ssurfacetemperaturecomputationismodifiedbyaddingthegreenhouse

parameter γ. Therefore, it is necessary to add the greenhouse effect to the equations

proposedbythethermodynamicsoffinitetimes,toobtainthetemperaturesofthelower

233

Mathematics2023,11,3060

andupperlayersofouractivesubstance(inthiscase,theair). Thus,theequationsfor

entropyandinternalenergyarealsochanged.

(cid:26)

ΔU=−w+

t=tc

qs (t)−σ(1−γ)[T4(t)−Tex4(t)]dt=0 (31)

t=0

Equation(15)isexpressedintermsofthenonendoreversibilityparameterandthe

greenhousefactor,givingasaresultthefollowingexpression:

(cid:26) (cid:22) (cid:23)

ΔS= t= t= 0 tc qs (t)−R(1−γ T ) ( σ t) [T4(t)−T e 4 x (t)] dt=0 (32)

FromtheG-Zsection,theaveragepowerofthewindsP= w

t

c,inwhichq¯s >>σT

e

4

x

,

thepowerexpressionoutputforthecaseofthegreenhouseeffectisoftheform:

σ

P=q¯s −

2

(1−γ)[T

1

4+T

2

4] (33)

Equations(31)and(32)showusagreenhousefactoractingonthetwolayersofthe

atmospherewithtemperaturesT1andT2.TomaximizePsubjecttotheendoreversibility

condition, we defined the Lagrangian in terms of the Lagrange multiplier λ and the

thermodynamicconstraintgivenbyL=P−λΔS,sothat:

(cid:15) ’

L=q¯s − σ

2

(1−γ)[T

1

4+T

2

4]−λ

T

q¯s

1

− σ

2

(1−γ)[T

1

3+T

2

3] (34)

whereλisaLagrangemultiplier. BysolvingtheEuler–Lagrangeequations ∂ ∂ T L( ( t t ) ) = 0,

asystemofequationsisobtained,whichallowsustocalculatetheextremesofthepower.

For ∂ ∂ T L 1 ( ( t t ) ) =0:

T 1 5−3 4 RλT 1 4− 2σ(1 q¯s −γ) =0 (35)

Forthecase ∂ ∂ T L 2 ( ( t t ) ) =0:

T2 = 3

4

R λ (36)

Finally,for ∂L ∂λ (t) =0wehave:

q¯s − σ (1−γ)[T3+T3]=0 (37)

T1 2 1 2

Eliminatingλandgivingthevalueofqs ≈229W/m2[50],wehavetwoequations

whosenumericalsolutionprovidesthehighestandlowestlayersurfacetemperatures.

ThelowoftheEarth’satmosphereisunderaregimeofmaximumpowerintermsofthe

nonendoreversibilityparameterR,thealbedoρ,thegreenhouseeffectγ,andthecurrent

solarconstantIsc.

T 1 5−T2T 1 4− 3Rσ( 2 1 qs −γ)T2 =0 (38)

T 1 4+T 2 3T1 − Rσ( 2 1 q¯ − s γ) =0 (39)

234

Mathematics2023,11,3060

5.2.GreenhouseFactorintheLowestLayeroftheAtmosphereAverageSurfaceTemperature

ThepowerfortheG-ZmodelisgivenbyP= w

t

c,whereforTex =3Kq¯s >>σT

e

4

x

,the

outputpowerexpressionwiththegreenhouseeffectinthelowerpartisthefollowing:

P=q¯s − σ

2

R[(1−γ)T

1

4+T

2

4] (40)

ItisnecessarytomaximizePsubjecttotheendoreversibilityconditionandthegreen-

houseeffectatthebottom.Then,theLagrangianisdefinedintermsoftheLagrangemultiplier

λandtheconstraintonthermodynamicsshowingthefollowingLagrangianexpression:

(cid:15) ’

L=q¯s − σ

2

[(1−γ)T

1

4+T

2

4]−λ

T

q¯s

1

− σ

2

[(1−γ)T

1

3+T

2

3] (41)

SolvingtheEuler–Lagrangeequations ∂ ∂ T L( ( t t ) ) =0,weobtainthefollowingequations:

For ∂ ∂ T L 1 ( ( t t ) ) =0:

T 1 5−3 4 RλT 1 4− 2σ(1 q¯s −γ) =0 (42)

For ∂ ∂ T L 2 ( ( t t ) ) =0:

T2 = 3

4

R λ (43)

For ∂L ∂λ (t) =0,wehave:

q¯s − σ [(1−γ)T3+T3]=0 (44)

T1 2 1 2

RemovingtheλparametersfromEquations(42)–(44),weobtain:

T 1 5−T2T 1 4− 3Rσ( 2 1 q¯s −γ)T2 =0 (45)

T 1 4+ (1− 1 γ)T 2 3T1 − Rσ( 2¯ 1 q − s γ) =0 (46)

TheFTTmodelsaredevelopedasenginesthatusetheconversionofsolarenergy

intowindenergy;thehypothesisisthatatmosphericworkasa“heatengine”provides

reasonablevaluesfortheaveragepowerofwindsandextremetemperaturesinspecific

layersoftheatmosphere.Tocomputetheefficiencyoftheenergyconverter,itisnecessary

totaketheaveragepoweroutputassociatedwiththeyearlyaveragesolarradiationfluxqs

expressedperunitareaoftheEarth’ssurface(seeEquation(47)).Therefore,solarenergy

efficiencyorperformanceisdefinedasw=P/qs.

w= (1−γ)(R R − [(1 1) − + γ R ) 4 + (1 R − 3( η 1 ) − 3[1 η) − 3] R(1−η)] (47)

Thus,fortheendoreversiblecaseR=1:

w= (1− η γ ( ) 1 + − ( η 1 ) − 3 η)3 (48)

Equation(48)showsusthatevenforanendoreversiblecase,theefficiencyofsolar

energydependsonthegreenhouseeffect. Foraregimeatmaximumpowerforγ = 0,

7.67%ofthesolarenergyqscanbeconvertedintoenergy,regardlessoftheplanetandthe

solarsystem.

Nevertheless,itdoesnotrepresentarealisticmodeloftheatmosphereoftheplanets.

Themodelcanbeextendedbyconsideringotherthermodynamicregimes,suchasthe

235

Mathematics2023,11,3060

ecologicalandefficientpowerregimes.Otherconditions,suchasphysicalandgeometric

issuesabouttheplanet,improveourthermalengine,whichimpliesmoreaccuratepredic-

tions.AccordingtothemodeldevelopedbyDeVosandFlatter[27],theyobtainedavalue

ω=9.64%whereasaHadley-typeconsidersaconvectioncellanddividestheplanetinto

twohemispheres,thusgeneratingdifferentheatexchangeswhereradiationisreceivedor

emittedfromtheirsurfaceareas.

ThemodelsproposedbyDeVosaswellasGordonandZarmi[20,27]cancompute

thetemperaturesoftheatmosphereofsomepastorfutureperiodsoftheEarth,aswas

carriedoutinthestudybyAnguloandBarranco-Jiménez[24],wherethetemperaturesof

earlyagewerecalculatedwithenoughaccuracy.Inthepresentwork,weworkedsimilarly,

butforafuturetimeoftheatmosphere(predictionevent),weconsideredtheatmosphere’s

physicalcharacteristics,suchasthealbedogreenhouseeffect. ThemodelcreatedbyDe

Vosshowsanexcellentrelationshipbetweenthetheoreticalandexperimentaldata.Our

proposedworkapproximatedthealbedodependentonthegreenhouseeffectwitha=0.072,

b=0.4955,andc=0.1527.

ρ=aγ2+bγ+c (49)

TheGZ-typemodelswiththegreenhousefactorandthealbedoconditionabove,

andtheatmosphererepresentedbyEquations(45)and(46),allowustoobtaintemperatures

of the highest and lowest layers of the atmosphere. It is necessary to determine the

atmosphericcharacteristicsoftheGZ-typemodels.Accordingtothesolutionofthefaint

youngSunparadoxpresentedin[24],thefinite-timethermodynamicsmodelsefficiently

resolvetheparadox,calculatingtheplanet’saveragesurfacetemperaturefromdifferent

geologicalstages.UsingscenarioswheretheluminosityoftheSunistakenintoaccount

throughtheGoughEquation(1),itisnecessarytomodifythisequationtoactualluminosity,

asrepresentedinEquation(50).

! (cid:22) (cid:23)(cid:27)

I(t)= 1+0.4

1−t+t0 −1

Isc (50)

t0

Usingthealbedoρ(Equation(49)),theaveragesolarradiationflux,andgreenhouse

coefficientγ,wemodifiedtheschemeproposedbyAnguloandBarrancotodetermine

theeffectsofclimatechangeduetotheincreaseingreenhousegas,takingtherelationship

proposedinourwork. Thatrelationshipbetweenthealbedoandgreenhouseeffectis

representedinEquation(49),includingthepresent-dayvaluesforaverageluminosity,

itsvariationperyear(Equation50),andthechangesdirectlyproportionaltothefluxqs

expressedinEquation(13). Nevertheless,itisnecessarytoconsiderthedissipationin

themaximumpowerregimetoobtainrealisticresults. Thismodificationallowsresults

tobeobtainedtopredicttheeffectsofclimatechangeinfutureyears.Thus,theaverage

temperatureofthesurface(Ts)atpresentwillbebasedontheexistingrelationshipinthe

dissipation(Equation(12))ofthesysteminmaximum-powerconditionsintheGZ-type

modelwithEquations(45)and(46).

(cid:22) (cid:23)

Ts =T1 +T2 β γ ( ( T 1 1 − (1 η − CA η ) C T A 1 ) + − β T T 2 2 ) −T2 γ(T T 1 1 ( − 1 T − 2 η − CA T ) 1 η CA ) (51)

Simplifying:

(cid:22) (cid:23) (cid:22) (cid:23)

Ts =T1 +T2 ( T 1 1 − (1 η − CA η C )T A 1 )− + T T 2 2 − T T2 1 (T1− (1 T − 2− η C T A 1 ) η CA ) (52)

6.ExperimentalResults

Itisnecessarytodeterminepossibleandfuturescenariosforthegrowthofgreenhouse

gases. Mostoftheconcentrationofgasesintheatmospherehaspresentedasignificant

increasesincethe1970sduetoindustrialactivities. AccordingtotheMaunaLoalabo-

ratoryinHawaii[53,56],thedatashowamassiveriseinCO2bytheempiricalformula

236

Mathematics2023,11,3060

concentrationfortheinterval1975≤t≤2100[53].So,theexpressionobtainedbyWubbles

concerningthetracegastrendsandtheirpotentialroleinclimatechangeisvalidforthis

methodology[53].

[CO2 ]=330e0.0056(t−1975) (53)

AccordingtoEquation(49),thealbedoandthegreenhouseeffectarerelated.Forthe

Earth,thevalueofthegreenhouseeffectcanbedefinedasγ = (Es −F)/Es,whereEs

isthesurfaceemissionandFistheoutgoingradiation[24]. Moreover,itisnoticedthat

the increase in greenhouse gases rises over time, according to Wubbles and different

experimentalmeasurements.Withallthesecharacteristics,thenaturalaveragetemperature

(Ts)anditspossibleevolutioninthecomingyearscanbedeterminedwithreasonable

accuracy.TotesttheGZmodel,adissipationφ ,developedinthiswork,isconsidered,

rb

solvingnumericallywith R = 1anddifferentvaluesofγarerelatedtotheyear. Itis

adatacompilationbyBerkeleyEarth. ThestudyshowsthetemperatureoftheEarth’s

surface,andtheexperimentallymeasuredtemperaturesT werecomparedagainstour

obs

theoreticallycalculatedtemperaturesTstouseaforecastingtechniquelatertodetermine

thefutureoftemperatures.

Ontheotherhand,thecomparisonwasmadeusingmachinelearningtechniques

suchaslinearregression,Ridgeregression,andartificialneuralnetworks. Concerning

theimplementation,weusedtheScikit-learnframeworkforregressionmethodsandthe

TensorFlowpackagewithKerasfordesigningtheartificialneuralnetwork.Theparameters

fortheartificialintelligence-basedapproachweredescribedaccordingtotheformalism

ofScikit-learnandTensorFlowKeras.Thus,thesetupparametersandconfigurationwere

establishedasfollows:

• Linearregression:train_size = X_train, X_test, y_train, y_test =

train_test_split(X, y, train_size = 0.8)

• Ridgeregression:train_size = X_train, X_test, y_train, y_test =

train_test_split(X, y, train_size = 0.8)

• NeuralnetworkoptimizerwasimplementedbyapplyingAdam’salgorithm.There-

gressionlosswasdefinedbyMeanSquaredError. Moreover,fourlayerswereestab-

lishedwiththeactivationfunctions:linear, linear, relu, linear.

DataPreprocessing

Toanalyzethecomplexityofclimatechange,theterrestrialandoceanictemperatures

oftheplanetweremeasured. Theuseddataareacompilationofadatasetprovidedby

BerkeleyLaboratory.OtherwidelyuseddatasetsareMLOSTNOAALand-OceanSurface

TemperatureandGISTEMfromNASA[57–59].ThedatacompilationbyBerkeleyrecords

landaveragetemperaturesintheformatyyyy/mm/dd. So,asplitwasmadebyyear,

month,andday,takingthetemperatureofeachmonth,andthemeantemperatureperyear

wascomputed.Itwasobservedthatthereisacorrelationwithavalueof0.89betweenthe

variablesoftheyearandthelandaveragetemperaturefromtheyear1975to2015[57–59].

Figure3showstheclimatologyoftheaverageannualterrestrialtemperaturebetween1951

and1980fromtheBerkeleyEarthDatawithaglobalmeanof9.17Celsius. Inourwork,

themeanexperimentaltemperatureofeachyearwascomparedwiththeobtaineddata

fromourtheoreticalmodel.

Theresultsofthedataandthesurfacetemperatures Ts obtainedfromthemodel

expressedinEquation(52)thatwasdevelopedinthisworkareshowninTable1.Allthe

resultsregardingdataarepresentedindegreesCelsius.

237

Mathematics2023,11,3060

Table1.AveragetemperaturesobservedandcomputedbytheGZ-typemodel.

Year T obs Ts

1975 8.74 8.41

1976 8.34 8.44

1977 8.85 8.48

1978 8.69 8.51

1979 8.73 8.55

1980 8.98 8.58

1981 9.16 8.62

1982 8.63 8.65

1983 9.02 8.69

1984 8.65 8.73

1985 8.65 8.77

1986 8.83 8.80

1987 8.99 8.84

1988 9.20 8.88

1989 8.922 8.92

1990 9.23 8.96

1991 9.17 9.00

1992 8.83 9.04

1993 8.86 9.08

1994 9.03 9.12

1995 9.34 9.16

1996 9.03 9.21

1997 9.20 9.24

1998 9.52 9.29

1999 9.28 9.33

2000 9.20 9.37

2001 9.41 9.38

2002 9.57 9.46

2003 9.52 9.50

2004 9.32 9.48

2005 9.70 9.59

2006 9.53 9.64

2007 9.73 9.73

2008 9.43 9.74

2009 9.50 9.78

2010 9.703 9.82

2011 9.51 9.87

2012 9.507 9.92

2013 9.606 9.97

2014 9.570 10.02

2015 9.831 10.07

Thetemperatureincreaseduetogreenhousegasgrowthhasbeenanalyzedsince1975.

ItwasfixedthisyearbecauseofthesignificantincreaseintheconcentrationofCO2,as

shownbytheexperimentaldevelopmentofWubblesinEquation(53),whenseeingthe

correlationsoftheobservationalvariablesofthetemperatureoftheBerkeleydatabase.

Wecannoticeahighcorrelationbetweentheyearandtheland’saveragetemperature,

andthecorrelationisequalto0.89. Therefore,alinearregressionmodelissufficientin

thiscasetomakeafuturepredictionofthetemperature.Inthefollowingplot(Figure4,

averagetemperaturesobservedandcalculatedbytheGZ-typemodel),wecanobservea

relationshipbetweentheaveragetemperatureperyearmeasuredagainstthetemperature

ofthemodifiedGZmodel.

238

Mathematics2023,11,3060

Figure3.Climatologyofannualmeanlandtemperature.NCAR,ClimateDataGuide[59].

Figure4.AveragetemperaturesobservedandcomputedbytheGZ-typemodelcomparedwiththe

averagemeasuredyearlytemperature.

Thus,(Figure5,averagetemperaturesobservedsince1975withlinearregression)

showshowalinearregressionadjustsperfectlytopredicttheevolutionofthetemperature

fromtheyear1975.Itispossibletoinferhowthetemperaturechangewillbetowardsthe

year2100thankstothistypeofmodeling.

Ontheotherhand,Table2presentsthefuturepredictionofthetemperaturesusing

linearregression(LR),ridgeregression(RR),andanartificialneuralnetwork(ANN).Thus,

theANNhasfivelayers:aninputlayerwithalinearactivationfunction;threelayerswith

arectifiedlinearactivationfunction,orReluorReLUforshort;andanoutputlayerwitha

linearactivationfunction.Alltechniqueswereappliedtotheobservedtemperatures(T )

obs

andthemodels’temperaturesusedinthepresentwork.Inthesameway,thethirdcolumn

shows the temperatures computed (Ts) from our model of Gordon and Zarmi (GZM)

withoutapplyingalinearregression,wherethephysicalcharacteristicsoftheatmosphere

239

Mathematics2023,11,3060

aretakenintoaccountandwhattheoreticaltemperaturewouldbereached.Inaddition,

Table2depictstheentirepredictionmadeupto2100,startingin2016.

Table2.AveragetemperaturesobservedandcomputedbytheGZtypemodel.

Year T obswithLR TswithLR T obswithRR T obswith TswithGZM

NN

2016 9.839 10.049 9.845 10.089 10.121

2017 9.842 10.094 9.860 10.094 10.176

2018 9.845 10.135 9.869 10.099 10.228

2019 9.860 10.178 9.884 10.105 10.281

2020 9.885 10.219 9.907 10.110 10.334

2021 9.913 10.251 9.937 10.115 10.387

2022 9.941 10.292 9.967 10.120 10.440

2023 9.969 10.333 9.996 10.125 10.495

2024 9.997 10.374 10.026 10.130 10.550

2025 10.025 10.426 10.056 10.135 10.606

2026 10.053 10.456 10.086 10.140 10.663

2027 10.081 10.497 10.116 10.144 10.720

2028 10.109 10.538 10.146 10.149 10.777

2029 10.137 10.579 10.175 10.154 10.836

2030 10.165 10.620 10.205 10.159 10.895

2031 10.193 10.661 10.235 10.164 10.954

2032 10.221 10.702 10.265 10.169 11.014

2033 10.249 10.743 10.295 10.174 11.018

2034 10.277 10.784 10.325 10.179 11.138

2035 10.305 10.825 10.354 10.184 11.200

2036 10.333 10.866 10.384 10.189 11.263

2037 10.361 10.907 10.414 10.194 11.327

2038 10.389 10.948 10.444 10.199 11.392

2039 10.417 10.989 10.474 10.204 11.456

2040 10.445 11.030 10.504 10.209 11.524

2041 10.473 11.071 10.533 10.213 11.591

2042 10.501 11.112 10.563 10.218 11.659

2043 10.529 11.153 10.593 10.223 11.728

2044 10.557 11.194 10.623 10.233 11.798

2045 10.585 11.235 10.653 10.238 11.868

2046 10.613 11.276 10.683 10.243 11.939

2047 10.641 11.317 10.713 10.246 12.012

2048 10.669 11.358 10.742 10.248 12.085

2049 10.697 11.399 10.772 10.253 12.159

2050 10.725 11.440 10.802 10.258 12.234

2051 10.753 11.481 10.832 10.263 12.311

2052 10.781 11.522 10.862 10.268 12.388

2053 10.809 11.563 10.892 10.272 12.465

2054 10.837 11.604 10.921 10.277 12.545

2055 10.865 11.645 10.951 10.282 12.625

2056 10.893 11.686 10.981 10.287 12.707

2057 10.921 11.727 11.011 10.292 12.789

2058 10.949 11.768 11.041 10.297 12.872

2059 10.977 11.809 11.071 10.302 12.957

2060 11.005 11.850 11.100 10.307 13.043

2061 11.033 11.891 11.130 10.312 13.129

2062 11.061 11.932 11.160 10.317 13.218

2063 11.089 11.973 11.190 10.322 13.308

2064 11.117 12.014 11.220 10.327 13.398

2065 11.145 12.055 11.250 10.332 13.490

2066 11.173 12.096 11.279 10.336 13.584

2067 11.201 12.137 11.309 10.341 13.659

2068 11.229 12.178 11.339 10.346 13.775

2069 11.257 12.219 11.369 10.351 13.872

240

Mathematics2023,11,3060

Table2.Cont.

Year T obswithLR TswithLR T obswithRR T obswith TswithGZM

NN

2070 11.285 12.260 11.399 10.356 13.972

2071 11.313 12.301 11.429 10.361 14.072

2072 11.341 12.342 11.458 10.366 14.174

2073 11.369 12.383 11.488 10.371 14.277

2074 11.397 12.424 11.518 10.376 14.383

2075 11.425 12.465 11.548 10.381 14.490

2076 11.453 12.506 11.578 10.386 14.599

2077 11.481 12.547 11.608 10.390 14.709

2078 11.509 12.588 11.637 10.396 14.820

2079 11.537 12.629 11.667 10.401 14.935

2080 11.565 12.670 11.697 10.405 15.050

2081 11.593 12.711 11.727 10.410 15.168

2082 11.621 12.752 11.757 10.415 15.287

2083 11.649 12.793 11.787 10.420 15.408

2084 11.677 12.834 11.816 10.425 15.533

2085 11.705 12.875 11.846 10.430 15.658

2086 11.733 12.916 11.876 10.435 15.786

2087 11.761 12.957 11.906 10.440 15.916

2088 11.789 12.998 11.936 10.445 16.048

2089 11.817 13.039 11.966 10.450 16.183

2090 11.845 13.080 11.995 10.455 16.320

2091 11.873 13.121 12.025 10.460 16.460

2092 11.901 13.162 12.055 10.465 16.601

2093 11.929 13.203 12.085 10.469 16.746

2094 11.957 13.244 12.115 10.474 16.894

2095 11.985 13.285 12.145 10.479 17.043

2096 12.013 13.326 12.174 10.484 17.196

2097 12.041 13.367 12.204 10.489 17.352

2098 12.069 13.408 12.234 10.494 17.511

2099 12.097 13.449 12.264 10.499 17.673

2100 12.125 13.490 12.294 10.504 17.838

Figure5.Averagetemperaturesobservedsince1975withlinearregressionadjustedtopredictthe

riseofmeantemperature.

Moreover,Figure6showstheevolutionofthesurfacetemperature(Ts),according

tothepredictionsmadebythemodelproposedinourworkwiththeinitialsGZMand

241

Mathematics2023,11,3060

thetemperaturepredictionfromtheexperimentaldata(T

obs

). Thus, TS andT

obs

were

forecastedusingmachinelearningtechniques.

Figure6.Comparisonoftheevolutionoftemperaturefromtheyear2020to2100throughtheoretical

andexperimentalmodels.

Fromacorrelationanalysisbetweenthetemperaturevariablesunderdifferentmachine

learningtechniques,suchaslinearregression(LR),ridgeregression(RR),artificialneural

network(ANN),andtheproposedendoreversiblemodel(GZM),itcanbeobservedthat

theGZMmodelismoresuitablewithalinearrelationship(seeFigure7).

Figure7.Comparisonofthecorrelationbetweenyearvariablesandobservedtemperatureswiththe

theoreticalmodel.

242

Mathematics2023,11,3060

7.Discussion

Accordingtoseveralauthors,thechangesintheconcentrationofgasesintheatmo-

sphere,mainlygreenhousegases,inadditiontotheirdirectedrelationshipwiththealbedo

effect,arerelatedtoclimatechange[24,29,60,61].

Climatemodeldevelopmentandtheimplicationsinamodel’spredictionreliability

canbedifficult,becausetheclimateisacomplexsystemwithmanyvariablesandfactors.

Themodelsarefullycoupledwhenstudyingacompleteinteractionamongtheglobal

radiationbudget,differentlayersoftheatmosphere,physicalandchemicalatmospheric

processes,andtheirimplicationsinthebiosphere.Themodelsareconsideredpartiallycou-

pledanddevelopedinasystemofSun–atmosphere–ocean.Differentialequationsrepresent

thegoverningequationsthatdescribeatmosphericandoceancirculation,geophysicalfluid

dynamics,continuityequations,theinputofsolarradiation,andphysicalthermodynamic

processes[29,61–65].Therefore,globalclimatemodelscanhavemanydegreesoffreedom.

Nevertheless,thesemodelsareverycomplexandexpensivetosolvethroughanalytical

andcomputationalmethods.Thus,thenonlinearityleadstomultiplesolutionsthatmust

becarefullyanalyzedtofindphysicallyacceptableresultsandpredictions. Amethod

usedtoworkwiththesechaoticsystemsistheuseofapproximationsorattractors,the

useanddevelopmentofsimplifiedclimatemodels,orthelinearizationofglobalclimate

models[29,65–67].

Inthiswork,weusedaclimatemodelbasedontheGordon–Zarmiapproach,where

thesystemisrepresentedlikeaheatenginethatdescribesanEarth–atmosphere–Sunsystem,

providing reasonable values of extreme temperatures in the layers of the atmosphere.

ThemodelsolvedtheparadoxoftheyoungandweakSun,proposingaseriesofscenarios

withthedifferentgreenhouseeffectandalbedovalues,takingintoaccounttheluminosity

oftheSunandtheevolutionofthesevaluesovertime.Thesevariablesareresponsiblefor

generatingglobalwarming,andtheobtainedpredictioniscorrelatedwiththeestimated

warmingvaluesfromexperimentaldata.

AccordingtoHoughtonetal.[29],itisessentialtonotethatsincetheclimateisachaotic

system,itspredictionsbecomeverycomplicated,sousingclimatemodelsandpredictions

madefromexperimentaldatathroughnumericaltechniquesormachinelearninghelpto

providerobustnesstofuturepredictions.

Inthisanalysisofclimatechange,anendoreversiblemodelingoftheGordonand

Zarmitypewascarriedout.Unlikeotherfinite-timethermodynamicstudiesforstudying

theatmosphere,adjustmentsweremadetogivethemodelrealisticresultsifapplied.Asfor

theclimaticanalysisofgeologicaleras,asobservedinotherworks,itisnoticedthatthe

resultsdonotcorrespondtowhatisreportedbyobservationsofthecurrenttemperature.

AccordingtoLevarioetal.[21],foracorrectthermodynamicoptimizationofpowerplants,

itisnecessarytoconsiderthesystem’svariations.Therefore,themodelingwasperformed

consideringthosevariations,thechangeinluminosityperyear,theincreaseingreenhouse

gas,anditsrelationshipwiththeterrestrialalbedo,thusadaptingittoourmodelofwindsat

maximumpower.Inthisway,thefamilyfromEquation(45)toEquation(53)complements

thesystemtocalculateclimatechangeduetoatmosphericconditionsandtheincreasein

greenhousegasesbyanthropogenicconditions.

FromTable1,anincreaseintheaveragetemperatureoftheEarth’ssurfacecanbeseen

from1975to2015,bothintheobservational(experimental)modelandthetheoreticalmodel

developedinourwork.Theriseintemperatureinbothcasesisrelatedtotheincreasein

greenhousegasesintheatmosphere.

InFigure2,wecanappreciatethedifferencesbetweenthepointsobtainedexperimen-

tally(observationandmeasuresinthelaboratory)andthemodelingproposedinourwork.

SupposeweobserveFigure3andcorrelationanalysis;inthatcase,theexperimentalpoints

inblueshowahighlineartendency,solinearorridgeregressionisanexcellenttechnique

forcorrectlypredictingtemperatureincreases.

Ontheotherhand,thepointsofourpreviouslymentionedmodelingoftheGZM

wouldseemtoshowthesamelineartrend,soinTable2,twocomparisonsweremade,

243

Mathematics2023,11,3060

takingintoaccountalinearregressionwithTsLRandananalysisobtaineddirectlyfrom

ourmodelingwithTsGZM.Asaresult,weobtainedadifferencebetweentheanalysis

withLRandGZM.Thisisexplainedconsideringthatthetemperatureobservationsonly

recordedpointsinourvector. Incontrast, themodelingrecordsthesepoints, andthe

physicalinformationoftheatmosphereissaved,aswellasthethermodynamicvariablesof

thesystem,whichgivesusresultsofthemeantemperatureincreasewithmorevaluethan

thoseobtainedbyananalysisofexperimentalpoints.

Moreover, Figure 4 shows a plot of the predictions made from the experimental

data T andthemodelingoftheGZMsystem. Itisimportanttonotethatinfuture

obs

scenarioswithforecastingbyGZM,theaveragetemperatureishigherthanthatobtained

by the data of the evolution of the observed temperatures T from various machine

obs

learningtechniques. Nevertheless,therateoftemperatureincreaseisintherangeper

decade,accordingto[29]. Theplotshowsthatthetemperatureevolutioninthecaseof

theconstructionofanANN,LR,andRRgrowsinawidespreadgradualwaycompared

withourproposedmodel.TheGZMmodelsavestheatmosphere’sphysicalcharacteristics,

suchasentropicrelationships,radiationconditions,andirradiance. Ithelpstopresent

morerealisticbehaviorinthedata,unliketheotherforecasting,whichonlyshowsusa

regressionofthelineartypewithoutconsideringtheevolutionofthephysicalparameters

causedbythealterationsintheEarth’satmosphere.

Themostsignificantchallengefordevelopingasunmodelisestablishingacritical

finite-timethermodynamicscondition.Developingobjectivefunctionsthatcharacterizethe

“optimal”modesofoperationisnotatrivialtask.However,therearenoestablishedcriteria

tosettheobjectivefunctions,sotheobjectiveofthemodelingitselfistheonethataffects

theconstructionofthe“heatengine”,inadditiontoaffectingitsbehaviorintheenergy

converteranditsperformance[68].

Solar energy converters under the branch of FTT have been developed to create

modelswithbettercoupledexperimentalandtheoreticalresults.Theseenergyconverters

arefocusedonentropyminimizationandoutputpowermaximization, amongothers.

AccordingtoDeVos[28],theCurzonandAhlbornengineisvalidwhentheheattransferis

linearorNewtonian,soanotherchallengerelatedtothesemodelingtypesistoworkthe

heattransferlinearly.

8.ConclusionsandFutureWork

Inthisarticle,weproposedanewfinite-timethermodynamicsapproachtopredict

changesinsurfacetemperatureinthelowestlayeroftheatmospherethatcorrespondsto

theaveragetemperature.Theproposedapproachconsiderstheevolutioninalbedoand

greenhousegases,thechangeinluminosityperyear,andthesystem’sdissipationinthe

regimeofmaximum-powerconditions. Ourmodelachievespredictionsintherangeof

futureprojections,obtainingbetterresultsthanthemachinelearningtechniquesusedin

theexperiments.Anotherareaforimprovementisthatitperformsasimpleclimatemodel,

avoidingthecomplexityofmodelingtheclimateasachaoticsystem.Thecurrentmodeling

isamodificationofpreviousmodelsoftheGZtypethat,inadditiontoobtainingrealistic

valuesoftheextremetemperaturesofthesystem,alsoallowsustocarryouttheevolution

oftemperaturesaccordingtothemodificationsofthephysicalprocessesoftheplanetina

rateofchangeoftime.

Thus,anincreaseintemperatureislinkedtophysicalconditionssuchasirradiance

andradiation.Moreover,acomparisonwithdifferentmachinelearningtechniquesshowed

ariseintemperatureinallthesemethods. Itiscrucialtonoticethatmachinelearning

algorithmsdonotpreserveatmosphericinformationintheperiodstudied. Therefore,

theforecastingcouldpresentabiasinthepredictionbecausethesearetrainedonlywith

experimentaldatawithoutconsideringthevariablesthatgenerateclimatechange.Thecom-

parisongivesrobustnesstothemodelwhencomparingtheexperimentaldatawiththe

theoreticalones. Asmentionedpreviously, duetothehighdegreesoffreedomofthe

climatemodel,interdisciplinaryworksarenecessarytofacenewchallengesinclimate

244

Mathematics2023,11,3060

warming.Allthetechniquesandourmodelingdemonstratedanincreaseintemperature.

Wecanconcludethesuccessofourmodelbycomparingitwithourexperimentaldata.

Inaddition,accordingtoHoughton[29],theprojectionsofglobalaveragetemperature

changesareintherangeof0.15°C–0.6°Cperdecade,whichisinthethresholdofthe

obtainedvalues.

Inthepresentwork,theendoreversibleenginesofFTTdealwiththeproblemofthe

radiativethermalbalancebetweenplanets,generatingaSun–Earth–windsystemthrough

an atmospheric heat engine that allows for the optimization of the extreme values of

themodeltofindthemaximumoutputpowerandentropyminimization,amongothers.

Thus,thesevaluesallowustoworkunderdifferentthermalregimesoftheFTT,namely

themaximumpowerregime(MPR),maximumecologicalregime(MER),andmaximum

efficiencypower(MEPR).ThismodelwascreatedundertheMERregime. According

toseveralauthors,tofullymodel,itisnecessarytogeneralizevariouscasesandverify

experimentaldataduetoclimatevariabilityasasubjectofstudy.Therefore,anextension

ofourresearchworkwouldbetoanalyzetheotherthermodynamicregimes.Wehaveto

proposeseveralcasesofincreasesingreenhousegasesandthealbedoeffect,comparethem

withtheexperimentaldata,andcomplementthemwithdeeplearningtechniques. All

theoreticalpredictionswillalwaysbecomparedagainstexperimentaldatatofaceclimate

changeinthebestway.

Ontheotherhand,itisnecessarytoconductstudiesconcerningtheatmosphereand

considerawindenginethemostcommoncontrolinobtainingthemaximumpowerasit

works,collectingdatafromtheseexperimentsandgeneratingmachinelearningmodels

tocharacterizethephenomenon. Inthispaper,studyingotherregimeswillallowusto

analyzethewholespectrumofourmodeling(windengine)andthusobserveallcasesof

globalwarming.

AuthorContributions:Conceptualization,S.V.-R.andM.T.-R.;methodology,R.Q.;software,C.G.S.-M.

andK.T.C.;validation,S.V.-R.andM.T.-R.;formalanalysis,R.Q.andS.V.-R.;investigation,M.T.-R.;

resources,K.T.C.;datacuration,C.G.S.-M.;writing—originaldraftpreparation,S.V.-R.;writing—

reviewandediting, M.T.-R.; visualization, K.T.C.; supervision, M.T.-R.; projectadministration,

C.G.S.-M.;fundingacquisition,K.T.C.Allauthorshavereadandagreedtothepublishedversionof

themanuscript.

Funding:ThisworkwaspartiallysponsoredbytheInstitutoPolitécnicoNacionalandtheConsejo

NacionaldeCienciayTecnologíaundergrants20230655,20231372,andSECTEI-2023,respectively.

InstitutionalReviewBoardStatement:Notapplicable.

InformedConsentStatement:Notapplicable.

DataAvailabilityStatement:Notapplicable.

Acknowledgments:Wearethankfultothereviewersfortheirtimeandtheirinvaluableandcon-

structivefeedbackthathelpedimprovethequalityofthepaper.

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

References

1. Kirilenko,A.P.;Sedjo,R.A.Climatechangeimpactsonforestry. Proc.Natl.Acad.Sci.USA2007,104,19697–19702.[CrossRef]

[PubMed]

2. Carleton,T.A.;Hsiang,S.M.Socialandeconomicimpactsofclimate. Science2016,353,aad9837.[CrossRef][PubMed]

3. Wheeler,T.;VonBraun,J.Climatechangeimpactsonglobalfoodsecurity. Science2013,341,508–513.[CrossRef][PubMed]

4. Louis,M.E.S.;Hess,J.J. Climatechange:Impactsonandimplicationsforglobalhealth. Am. J.Prev. Med. 2008,35,527–538.

[CrossRef][PubMed]

5. Nourani,V.;Tapeh,A.H.G.;Khodkar,K.;Huang,J.J.Assessinglong-termclimatechangeimpactonspatiotemporalchangesof

groundwaterlevelusingautoregressive-basedandensemblemachinelearningmodels. J.Environ.Manag.2023,336,117653.

[CrossRef]

6. Yeganeh-Bakhtiary,A.;EyvazOghli,H.;Shabakhty,N.;Kamranzad,B.;Abolfathi,S.Machinelearningasadownscalingapproach

forpredictionofwindcharacteristicsunderfutureclimatechangescenarios. Complexity2022,2022,8451812.

245

Mathematics2023,11,3060

7. Rajaee,T.;Ebrahimi,H.;Nourani,V.Areviewoftheartificialintelligencemethodsingroundwaterlevelmodeling. J.Hydrol.

2019,572,336–351.[CrossRef]

8. Sattari,M.T.;Mirabbasi,R.;Sushab,R.S.;Abraham,J. PredictionofgroundwaterlevelinArdebilplainusingsupportvector

regressionandM5treemodel. Groundwater2018,56,636–646.[CrossRef]

9. Zare,M.;Koch,M. GroundwaterlevelfluctuationssimulationandpredictionbyANFIS-andhybridWavelet-ANFIS/Fuzzy

C-Means(FCM)clusteringmodels:ApplicationtotheMiandarbandplain. J.Hydro-Environ.Res.2018,18,63–76.[CrossRef]

10. Donnelly,J.;Abolfathi,S.;Pearson,J.;Chatrabgoun,O.;Daneshkhah,A.Gaussianprocessemulationofspatio-temporaloutputs

ofa2Dinlandfloodmodel. WaterRes.2022,225,119100.[CrossRef]

11. Nourani,V.;Khodkar,K.;Paknezhad,N.J.;Laux,P. Deeplearning-baseduncertaintyquantificationofgroundwaterlevel

predictions. Stoch.Environ.Res.RiskAssess.2022,36,3081–3107.[CrossRef]

12. Zennaro,F.;Furlan,E.;Simeoni,C.;Torresan,S.;Aslan,S.;Critto,A.;Marcomini,A.Exploringmachinelearningpotentialfor

climatechangeriskassessment. Earth-Sci.Rev.2021,220,103752.[CrossRef]

13. Kalu,I.;Ndehedehe,C.E.;Okwuashi,O.;Eyoh,A.E.;Ferreira,V.G.Identifyingimpactsofglobalclimateteleconnectionpatterns

onlandwaterstorageusingmachinelearning. J.Hydrol.Reg.Stud.2023,46,101346.[CrossRef]

14. Nwokolo,S.C.;Obiwulu,A.U.;Ogbulezie,J.C. Machinelearningandanalyticalmodelhybridizationtoassesstheimpactof

climatechangeonsolarPVenergyproduction. Phys.Chem.EarthPartsA/B/C2023,130,103389.[CrossRef]

15. Nwokolo,S.C.;Ogbulezie,J.C.;Obiwulu,A.U.Impactsofclimatechangeandmeteo-solarparametersonphotosynthetically

activeradiationpredictionusinghybridmachinelearningwithPhysics-basedmodels. Adv. SpaceRes. 2022,70,3614–3637.

[CrossRef]

16. Jusup,M.;Holme,P.;Kanazawa,K.;Takayasu,M.;Romic´,I.;Wang,Z.;Gecˇek,S.;Lipic´,T.;Podobnik,B.;Wang,L.;etal. Social

physics. Phys.Rep.2022,948,1–148.[CrossRef]

17. Steffen,W.;Richardson,K.;Rockström,J.;Schellnhuber,H.J.;Dube,O.P.;Dutreuil,S.;Lenton,T.M.;Lubchenco,J.Theemergence

andevolutionofEarthSystemScience. Nat.Rev.EarthEnviron.2020,1,54–63.[CrossRef]

18. Seneviratne,S.; Nicholls,N.; Easterling,D.; Goodess,C.; Kanae,S.; Kossin,J.; Luo,Y.; Marengo,J.; McInnes,K.; Rahimi,

M.; et al. Changesin Climate Extremes andTheir Impacts onthe Natural PhysicalEnvironment. 2012. Available on-

line:https://library.harvard.edu/sites/default/files/static/collections/ipcc/docs/AR5_WG2_n_SREX_chapters_and_review/

ii_SREX/c_Final_draft_SREX/SREX-Chap3_FINAL.pdf(accessedon12March2023).

19. Wang,Z.;Jusup,M.;Guo,H.;Shi,L.;Gecˇek,S.;Anand,M.;Perc,M.;Bauch,C.T.;Kurths,J.;Boccaletti,S.;etal. Communicating

sentimentandoutlookreversesinactionagainstcollectiverisks. Proc.Natl.Acad.Sci.USA2020,117,17650–17655.[CrossRef]

20. Gordon,J.M.;Zarmi,Y.Windenergyasasolar-drivenheatengine:Athermodynamicapproach. Am.J.Phys.1989,57,995–998.

[CrossRef]

21. Levario-Medina,S.;Valencia-Ortega,G.;Arias-Hernandez,L.OptimizacionTermodinámicadeAlgunasPlantasGeneradorasde

EnergiaMediantelak-PotenciaEficiente.2021.Availableonline:https://www.esfm.ipn.mx/assets/files/esfm/docs/RNAFM/

articulos-2020/XXVRNAFM013.pdf(accessedon23April2023).

22. Curzon,F.L.;Ahlborn,B.EfficiencyofaCarnotengineatmaximumpoweroutput. Am.J.Phys.1975,43,22–24.[CrossRef]

23. Arias-Hernandez,L.A.;Angulo-Brown,F. Ageneralpropertyofendoreversiblethermalengines. J.Appl. Phys. 1997,81,

2973–2979.[CrossRef]

24. Angulo-Brown,F.;Rosales,M.A.;Barranco-Jimenez,M.A.ThefaintyoungSunparadox:Asimplifiedthermodynamicapproach.

Adv.Astron.2012,2012,478957.[CrossRef]

25. Sagan,C.;Mullen,G.EarthandMars:Evolutionofatmospheresandsurfacetemperatures. Science1972,177,52–56.[CrossRef]

26. Kasting,J.F.;Grinspoon,D.H.ThefaintyoungSunproblem. InTheSuninTime;UniversityofArizonaPress:Tucson,AZ,USA,

1991;pp.447–462.

27. DeVos,A.;Flater,G.Themaximumefficiencyoftheconversionofsolarenergyintowindenergy. Am.J.Phys.1991,59,751–754.

[CrossRef]

28. DeVos,A.;VanderWel,P.TheefficiencyoftheconversionofsolarenergyintowindenergybymeansofHadleycells. Theor.

Appl.Climatol.1993,46,193–202.[CrossRef]

29. Houghton,J.Globalwarmingreportsonprogress. Physics2005,68,1340–1403.

30. Wang,R.;Li,L.;Gentine,P.;Zhang,Y.;Chen,J.;Chen,X.;Chen,L.;Ning,L.;Yuan,L.;Lü,G.Recentincreaseintheobservation-

derivedlandevapotranspirationduetoglobalwarming. Environ.Res.Lett.2022,17,024020.[CrossRef]

31. Chi,J.;Kim,H.c. Predictionofarcticseaiceconcentrationusingafullydatadrivendeepneuralnetwork. RemoteSens.2017,

9,1305.[CrossRef]

32. Asthana,T.;Krim,H.;Sun,X.;Roheda,S.;Xie,L.Atlantichurricaneactivityprediction:Amachinelearningapproach.Atmosphere

2021,12,455.[CrossRef]

33. Nieves,V.;Radin,C.;Camps-Valls,G.Predictingregionalcoastalsealevelchangeswithmachinelearning.Sci.Rep.2021,11,7650.

[CrossRef]

34. Khasnis,A.A.;Nettleman,M.D.Globalwarmingandinfectiousdisease. Arch.Med.Res.2005,36,689–696.[CrossRef][PubMed]

35. Sidhu,B.S.;Mehrabi,Z.;Ramankutty,N.;Kandlikar,M.Howcanmachinelearninghelpinunderstandingtheimpactofclimate

changeoncropyields? Environ.Res.Lett.2023,18,024008.[CrossRef]

36. Zheng,H.Analysisofglobalwarmingusingmachinelearning. Comput.WaterEnergyEnviron.Eng.2018,7,127.[CrossRef]

246

Mathematics2023,11,3060

37. Cheremisin,G.;Egorov,D.;Kravchenko,O.;Dev,A. Deepconvolutionalneuralnetworkforreconstructingthecloudphase

distributionfromlevel-1bMODISdata. Proc.AIPConf.Proc.2023,2819,030005.

38. Miloshevich,G.;Cozian,B.;Abry,P.;Borgnat,P.;Bouchet,F.Probabilisticforecastsofextremeheatwavesusingconvolutional

neuralnetworksinaregimeoflackofdata. Phys.Rev.Fluids2023,8,040501.[CrossRef]

39. Farhangmehr,V.;Cobo,J.H.;Mohammadian,A.;Payeur,P.;Shirkhani,H.;Imanian,H.AConvolutionalNeuralNetworkModel

forSoilTemperaturePredictionunderOrdinaryandHotWeatherConditions:ComparisonwithaMultilayerPerceptronModel.

Sustainability2023,15,7897.[CrossRef]

40. Hassan,K.M.A.PredictingFutureGlobalSeaLevelRiseFromClimateChangeVariablesUsingDeepLearnin. Int.J.Comput.

Digit.Syst.2023.[CrossRef]

41. Ghimire,S.;Nguyen-Huy,T.;Prasad,R.;Deo,R.C.;Casillas-Perez,D.;Salcedo-Sanz,S.;Bhandari,B.Hybridconvolutionalneural

network-multilayerperceptronmodelforsolarradiationprediction. Cogn.Comput.2023,15,645–671.[CrossRef]

42. Larson,A.;Hendawi,A.;Boving,T.;Pradhanang,S.M.;Akanda,A.S.DiscerningWatershedResponsetoHydroclimaticExtremes

withaDeepConvolutionalResidualRegressiveNeuralNetwork. Hydrology2023,10,116.[CrossRef]

43. Jonnalagadda,J.;Hashemi,M.LongLeadENSOForecastUsinganAdaptiveGraphConvolutionalRecurrentNeuralNetwork.

Eng.Proc.2023,39,5.

44. Lacombe,R.;Grossman,H.;Hendren,L.;Lüdeke,D. Improvingextremeweathereventsdetectionwithlight-weightneural

networks. arXiv 2023,arXiv:2304.00176.

45. Raman,R.;Mewada,B.;Meenakshi,R.;Jayaseelan,G.;Sharmila,K.S.;Taqui,S.N.;Al-Ammar,E.A.;Wabaidur,S.M.;Iqbal,A.

ForecastingthePVPowerUtilizingaCombinedConvolutionalNeuralNetworkandLongShort-TermMemoryModel. Electr.

PowerComponentsSyst.2023,1–17.[CrossRef]

46. Lin,F.;Zhang,Y.;Wang,J.Recentadvancesinintra-hoursolarforecasting:Areviewofground-basedskyimagemethods. Int.J.

Forecast.2023,39,244–265.[CrossRef]

47. Caldas,M.;Alonso-Suárez,R.Veryshort-termsolarirradianceforecastusingall-skyimagingandreal-timeirradiancemeasure-

ments. Renew.Energy2019,143,1643–1658.[CrossRef]

48. Pedro,H.T.;Coimbra,C.F.;David,M.;Lauret,P.Assessmentofmachinelearningtechniquesfordeterministicandprobabilistic

intra-hoursolarforecasts. Renew.Energy2018,123,191–203.[CrossRef]

49. Kamadinata,J.O.;Ken,T.L.;Suwa,T.Skyimage-basedsolarirradiancepredictionmethodologiesusingartificialneuralnetworks.

Renew.Energy2019,134,837–845.[CrossRef]

50. Barranco-Jimenez,M.A.;Chimal-Eguia,J.C.;Angulo-Brown,F.TheGordonandZarmimodelforconvectiveatmosphericcells

undertheecologicalcriterionappliedtotheplanetsofthesolarsystem. Rev.Mex.Fis.2006,52,205–212.

51. Ocampo-Garcia,A.OptimizacionTermodinamicayTermoeconomicadeModelosExtendidosdeMaquinasEndorreversibles.

Ph.D.Thesis,InstitutoPolitecnicoNacional,MexicoCity,Mexico,2020.

52. Angulo-Brown,F.;Arias-Hernandez,L.A.;Santillan,M.Onsomeconnectionsbetweenfirstorderirreversiblethermodynamics

andfinite-timethermodynamics. Rev.Mex.Fis.2002,48,182–192.

53. NormaSanchez,F.;Angulo-Brown,M.B.J.PosiblesfuturosescenariosdelatemperaturasuperficialdelaTierraconlaevolucion

delaconstantesolar. InProceedingsoftheXXIICongresoNacionaldeTermodinamica,SociedadMexicanadeTermodinamica

A.C.,MexicoCity,Mexico,10–12September2007.

54. Barranco-Jimenez,M.A.;Angulo-Brown,F. Asimplemodelontheinfluenceofthegreenhouseeffectontheefficiencyof

solar-to-windenergyconversion. IlNuovoCimentoC2003,26,535–552.

55. Barranco-Jimenez,M.A.;Angulo-Brown,F.Anonendoreversiblemodelforwindenergyasasolar-drivenheatengine. J.Appl.

Phys.1996,80,4872–4876.[CrossRef]

56. NationalOceanicandAtmosphericAdministration. TrendsinAtmosphericCarbonDioxide. 2023. Availableonline: https:

//gml.noaa.gov/ccgg/trends/(accessedon3July2023).

57. BerkeleyEarth. GlobalWarmingDataOverview. 2023. Availableonline: https://berkeleyearth.org/data/(accessedon3

July2023).

58. NationalCenterforAtmosfericResearch. GlobalSurfaceTemperatures: BEST:BerkeleyEarthSurfaceTemperatures. 2023.

Availableonline: https://climatedataguide.ucar.edu/climate-data/global-surface-temperatures-best-berkeley-earth-surface-

temperatures(accessedon3June2023).

59. NationalAeronauticsandSpaceAdministration. GISSSurfaceTemperatureAnalysis(GISTEMPv4).2023.Availableonline:

https://data.giss.nasa.gov/gistemp/(accessedon3June2023).

60. Pierrehumbert,R.T.Infraredradiationandplanetarytemperature. Phys.Today2011,64,33–38.[CrossRef]

61. Curry,J.A.;Webster,P.J.ThermodynamicsofAtmospheresandOceans;Elsevier:Amsterdam,TheNetherlands,1998.

62. vonParis,P.;Rauer,H.;Grenfell,J.L.;Patzer,B.;Hedelt,P.;Stracke,B.;Trautmann,T.;Schreier,F.WarmingtheearlyEarth—CO2

reconsidered. Planet.SpaceSci.2008,56,1244–1259.[CrossRef]

63. Krasnopolsky,V.M.;Fox-Rabinovitz,M.S.Complexhybridmodelscombiningdeterministicandmachinelearningcomponents

fornumericalclimatemodelingandweatherprediction. NeuralNetw.2006,19,122–134.[CrossRef][PubMed]

64. Schmidt,G.A.;Sherwood,S.Apracticalphilosophyofcomplexclimatemodelling. Eur.J.Philos.Sci.2015,5,149–169.[CrossRef]

65. Knutti,R.;Rugenstein,M.A.Feedbacks,climatesensitivityandthelimitsoflinearmodels. Philos.Trans.R.Soc.AMath.Phys.

Eng.Sci.2015,373,20150146.[CrossRef][PubMed]

247

Mathematics2023,11,3060

66. Visconti,G.FundamentalsofPhysicsandChemistryoftheAtmosphere;Springer:Berlin/Heidelberg,Germany,2001.

67. North,G.R.;Cahalan,R.F.;Coakley,J.A.,Jr. Energybalanceclimatemodels. Rev.Geophys.1981,19,91–121.[CrossRef]

68. LevarioMedina,S.EstudiodeAlgunasFuncionesCompromisoySusEfectosenlaOptimizaciónTermodinámicaenlosModelos

deConvertidoresdeEnergía.Ph.D.Thesis,EscuelaSuperiordeFísicayMatemáticas,InstitutoPolitécnicoNacional,MexicoCity,

Mexico,2021.

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

248

mathematics

Article

ACMKC: A Compact Associative Classification Model Using

K-Modes Clustering with Rule Representations by Coverage

JamolbekMattiev1,*,MonteDavityan2andBrankoKavsek3,4

1 ComputerScienceDepartment,UrgenchStateUniversity,KhamidAlimdjan14,

Urgench220100,Uzbekistan

2 ComputerScienceDepartment,CaliforniaStateUniversityofFullerton,2555NutwoodAvenue,

Fullerton,CA92831,USA;monte@csu.fullerton.edu

3 DepartmentofInformationSciencesandTechnologies,UniversityofPrimorska,Glagoljaška8,

6000Koper,Slovenia;branko.kavsek@upr.si

4 AILaboratory,JožefStefanInstitute,JamovaCesta39,1000Ljubljana,Slovenia

* Correspondence:jamolbek.mattiev@famnit.upr.siormattiev.jamolbek@urdu.uz;Tel.:+998-99-5854223

Abstract: Thegenerationandanalysisofvastamountsofdatahavebecomeincreasinglyprevalent

indiverseapplications. Inthisstudy,weproposeanovelapproachtoaddressthechallengeof

ruleexplosioninassociationruleminingbyutilizingthecoverage-basedrepresentationsofclusters

determinedbyK-modes. WeutilizetheFP-Growthalgorithmtogenerateclassassociationrules

(CARs). Tofurtherenhancetheinterpretabilityandcompactnessoftheruleset,weemploythe

K-modesclusteringalgorithmwithadistancemetricthatbinarizestherules.Theoptimalnumber

ofclustersisdeterminedusingthesilhouettescore. Representativerulesarethenselectedbased

ontheircoveragewithineachcluster.Toevaluatetheeffectivenessofourapproach,weconducted

experimentalevaluationsonbothUCIandKaggledatasets.Theresultsdemonstrateasignificant

reductionintherulespace(71rulesonaverage,whichisthebestresultamongallstate-of-the-artrule-

learningalgorithms),aligningwithourgoalofproducingcompactclassifiers.Ourapproachoffers

apromisingsolutionformanagingrulecomplexityinassociationrulemining,therebyfacilitating

improvedruleinterpretationandanalysis,whilemaintainingasignificantlysimilarclassification

accuracy(ACMKC:80.0%onaverage)tootherrulelearnersonmostofthedatasets.

Citation:Mattiev,J.;Davityan,M.; Keywords:classassociationrules;clustering;representativerule;modelcoverage;classification

Kavsek,B.ACMKC:ACompact

AssociativeClassificationModel

MSC:90C90

UsingK-ModesClusteringwithRule

RepresentationsbyCoverage.

Mathematics2023,11,3978. https://

doi.org/10.3390/math11183978 1.Introduction

AcademicEditor:WeiFang Inthemoderneraofdata-drivenapplications,therehasbeenasignificantincreasein

thegatheringandretentionoflargeamountsofdata.Extractingassociationrulesfromthese

Received:10August2023

extensivedatasetsandreducingtheircomplexcombinationshasbecomeacrucialmethod

Revised:9September2023

foruncoveringvaluableinsights[1]. However,amajorhurdleliesinthesheernumber

Accepted:15September2023

Published:19September2023 ofrulesdiscoveredinreal-worlddatasets,whichrequiresthecrucialtaskofpruningand

clusteringrulestocreateclassifiersthatareconcise,precise,andeasytounderstand.

Associationrule(AR)mining[2]seekstocreateallrelevantrulesinadatabase,ad-

heringtouser-definedthresholdsforminimumsupportandconfidence. Ontheother

Copyright: ©2023bytheauthors. hand,classificationruleminingfocusesonextractingasubsetofrulestodevelopprecise

Licensee MDPI, Basel, Switzerland. andeffectivemodelsforpredictinglabelsofambiguousobjects. Combiningthesetwo

Thisarticleisanopenaccessarticle crucialdata-miningmethodsinAssociativeClassification(AC)allowsforthecreationofa

distributed under the terms and cohesiveframework[3,4].AssociationrulesutilizemanyoftheACtechniquespresented

conditionsoftheCreativeCommons byresearcherstocreateefficientandaccurateclassifiers[5–12].Althoughtheireffectiveness

Attribution(CCBY)license(https:// dependsonuser-definedfactorslikeminimumsupportandconfidence,researchinvestiga-

creativecommons.org/licenses/by/

tionshaveshownthatACmethodscanbemoreaccuratethanconventionalcategorization

4.0/).

Mathematics2023,11,3978.https://doi.org/10.3390/math11183978 https://www.mdpi.com/journal/mathematics

249

Mathematics2023,11,3978

systems.Unsupervisedlearningtechniqueslikeclustering[13–15]alsoplayasignificant

part.Partitionalclusteringorhierarchicalclusteringaretwocategoriesofclusteringtech-

niques.Inpartitionalclustering[16,17],objectsaredividedintodistinctclusterstoensure

thatobjectsinsideaclusteraremoresimilarthanthoseinotherclusters.Ontheotherhand,

nestedpartitionsmakeupahierarchyinhierarchicalclustering[18].Whilethetop–down

methodstartswithasingleclusterthatcontainsallitemsandthensplitsthemintosmaller

clusters,thebottom–upmethodjoinssmallerclusterstocreatebiggerones.

Ourresearchfocusesongeneratingstrongclassassociationrules(CARs)usingthe

“FP-Growth”algorithmforfrequentitemsets,satisfyingminimumsupportandconfidence

requirements.Additionally,weproposeanapproachtoassociativeclassificationutilizing

K-modesclusteringwithanoveldistancemetricbuiltondirectmeasurementslikerule

itemstoreducetherulespace.Ourmethodrepresentsrulesasbinaryvectorsofitemsets,

enablingefficientsimilaritycalculationandmakingitcompatiblewithclusteringtechniques

likeK-modes. WeexplorethebenefitsandmethodologyofK-modesclustering,which

revealshiddenpatternsinitemsetsandprovidescomputationalefficiencyforlargedatasets

comparedtootherclusteringapproaches. Moreover,weintroduceatwo-stepprocess

usingthesilhouettescoretodeterminetheoptimalnumberofclusters,ensuringabalance

betweencohesionandseparation. AfterclusteringtheCARs,weselectarepresentative

CARforeachclusterusingtwoapproachesbasedondatasetcoverageandrulessimilarity,

aimingtoenhancecoverageandclassificationaccuracy.

Inordertoassesstheeffectivenessofourproposedtechniques,wecarriedoutex-

perimentson13meticulouslychosendatasetssourcedfromtheUCIMachineLearning

DatabaseRepository[19]andKaggle.Acomparativeevaluationwasconducted,comparing

ourmethodsagainstsevenwell-knownassociativeandclassicalclassificationalgorithms.

ThesealgorithmsincludeDecisionTableandNaïveBayes(DTNB)[20],DecisionTable

(DT)[21],ClassificationBasedonPredictiveAssociationrules(CPAR)[22],Classification

basedonMultipleAssociationRules(CMAR)[18],C4.5[23],Classification-BasedAssocia-

tion(CBA)[3],andSimpleAssociativeClassifier(SA)[24].

ExperimentalresultsshowedthatACMKCachievedthebestresultwhencomparing

the average number of classification rules while maintaining the similar classification

accuracywithothermodels. TheACMKCmodelshowedgreatadvantagetoproduce

statisticallysmallerclassifiersonbiggerdatasets,whichwastheprimarygoalofthestudy.

The following sections of the paper are structured as follows: Section 2 includes

pastworksrelatedtoourresearch. Section3presentsacomprehensiveexplanationof

ourproposedmethodology.Section4focusesontheexperimentalevaluation.Section5

outlinestheconclusionandfutureplans.ThepaperconcludeswiththeAcknowledgement

andReferencessections.

2.RelatedWork

Ourproposedapproachintroducesinnovationintheselectionof“strong”classas-

sociationrules,theclusteringprocess,andthedeterminationofa“representative”class

associationruleforeachcluster.Otherrelevantstudiesalsoaddresstheconceptofclus-

teringCARs,buttheyemployvariousapproaches. Thissectiondiscussestheserelated

approachestoclusteringCARs,highlightingboththesimilaritiesanddifferencescompared

toourproposedapproach.

Tothebestofourknowledge,andduetothelackofinformationrelatingtothecombi-

nationofclassassociationrulesandclustering,ourapproachservesasacoalescenceofthese

twotocreateamethodofdeterminingrepresentativeclassassociationrulesforclusters.

Whiletherearemethodsthatemployassociativeclassificationandclusteringtoaccomplish

asimilarfeat,oursdiffersinthatitusesCARSinsteadofassociativeclassification.

Thetechniquesusedin[25]involveAssociationRuleClassificationandClustering

units. IntheAssociationRuleClassificationunit, theAprioriAlgorithmisappliedto

identifyregularitiesbetweenflowparameters;itisusedforthefinerclassificationandpre-

dictionofIPsandportsforfutureapplicationservicing.Thisapproachfocusesonderiving

250

Mathematics2023,11,3978

associationrulestoenhanceclassificationaccuracy.Ontheotherhand,intheClustering

unit,bothK-MeanandModel-basedclusteringalgorithmsarecomparedtodeterminethe

optimumperformance.Unsupervisedclusteringtechniquesgroupdatasetswithsimilar

characteristicstogether,aidingtheclassificationprocess. K-Meanpartitionsdataintok

groupstominimizetheEuclideandistanceofclustercenters. Model-BasedClustering

assumesadatamodelandutilizestheMclustpackagewithExpectation–Maximization

(EM)forparameterestimationandhierarchicalclustering.Thesetechniquesdifferfrom

K-modesandclassassociationrulesbyexploringdistinctapproachestodatarepresentation,

rulegeneration,andclusteringstrategiesforclassificationtasks.

AnewmethodresearchersproposeutilizesK-means(partitional)clusteringtocluster

association rules [26]. The primary objective of this research is to cluster discovered

associationrulestofacilitateuserselectionofthemostsuitablerules.Fourstepsmakeup

thealgorithm:(1)The“Apriori”algorithmisusedtoextractARsfromfrequentpatterns;

(2)Lift,Cosinus,Conviction,andInformationGainarecomputedforallrulesgeneratedin

step1;(3)UsingtheK-meansalgorithm,asetofassociationrulesisdividedintodisjoint

clusters;theyattempttoclustertherulesthatsharethefewestsimilarities.Euclideanand

degreeofsimilaritydistancesareused;(4)Finally,thegroupofrulesisrankedfrombestto

worstbasedonthecentroidofeachcluster.

TheCPARalgorithmisintroducedbyYinandHanasafusionofassociativeclassifica-

tionandtraditionalrule-basedclassificationmethods.CPARemploysagreedyalgorithm

anddrawsinspirationfromtheFirst-OrderInductiveLearner(FOIL)[27]techniqueto

directlygeneraterulesfromthetrainingdataset,deviatingfromthegenerationofavast

numberofcandidaterulesderivedfromfrequentitemsetsinotherassociativeclassification

approaches.CPARevaluateseachruleusingexpectedaccuracytoaddressoverfittingand

employsadistinctclassificationprocess.Firstly,itselectsallruleswhosebodiesmatchthe

testingexample;then,itextractsthebestkrulesforeachclassamongtheselectedrules.

Finally,CPARcomparestheaverageexpectedaccuracyofthebestkrulesperclassfrom

step2andpredictstheclasslabelassociatedwiththehighestexpectedaccuracy.

CMAR,anassociativeclassificationmethod,employsmultipleassociationrulesfor

classification.ItextendstheefficientFP-Growthalgorithm[28]tominelargedatasetsand

introducesanoveldatastructurecalledaCR-tree.TheCR-treeaimstostoreandretrieve

alargenumberofrulescompactlyandefficientlybyutilizingaprefixtreestructurethat

exploresrulesharing,resultinginsignificantcompactness.Additionally,theCR-treeacts

asanindexstructureforrules,enablingefficientruleretrieval.Intheruleselectionphase,

CMARidentifieshighlyconfidentandrelatedrulesbyconsideringdatasetcoverageand

analyzingtheircorrelation.ForeachruleR,allexamplescoveredbyRareidentified,and

ifRcorrectlyclassifiesanexample,itisselectedforinclusioninthefinalclassifier. The

covercountofexamplescoveredbyRisincrementedby1,withacovercountthresholdC

initiallyapplied.IfthecovercountofanexampleexceedsC,thatexampleisremoved.This

iterativeprocesscontinuesuntilboththetrainingdatasetandrulesetareempty.

Liu,Hsu,andMadevelopedtheheuristictechniqueknownasCBA[3]in1998. Its

structure is similar to associative classification algorithms and includes steps for rule

developmentandselection. CBAusesaniterativeprocessforrulecreationcomparable

totheApriorialgorithm[2]. CBAdetectsfrequentrule-itemsandcreatesstrongclass

associationrulesfromthesefrequentitemsetsbyrepeatedlyexaminingthedata.Apruning

techniquebasedonapessimisticerrorrateisusedintherule-generationphase.Rulesare

extracteddependingondatasetcoverageduringtherule-selectionstep.Arulequalifies

asaprospectiveclassifiercandidateifitaccuratelyclassifiesatleastoneexample.Finally,

basedontheassessmentoftotalerror,rulesareaddedtothefinalclassifier.

Inreference[29],aclassifiernamedJ&Bwasdevelopedthroughathoroughexplo-

rationofthecompleteexamplespace,resultinginastraightforwardandaccurateclas-

sifier. Ourselectionofstrongclassassociationruleswasbasedontheircontributionto

enhancingthecoverageofthelearningset. J&Bincorporatesastoppingcriterioninthe

rule-selectionprocess,whichreliesonthecoverageofthetrainingdataset.Intherepresen-

251

Mathematics2023,11,3978

tativeCAR-selectionprocessofthisstudy,weemployedtheJ&Bapproachwithoutusinga

stoppingcondition. Thereisnoneedtouseastoppingcriterioninthismethodbecause

thesizeoftheclassifier,whichisdecidedbythenumberofclusters,isdeterminedusinga

separatestrategy.

Conditionalmarket-basketdifference(CMBP)andconditionalmarket-basketlog-

likelihood(CMBL)approachesaretwofurtherstrategiessuggestedin[30].Thismethod

groupsassociationrulesusinganewnormalizeddistancemetric.Agglomerativeclustering

isusedtogrouptherulesbasedondistance. Inaddition,therulesareclusteredusing

self-organizingmapsandmulti-dimensionallyscaledinavectorspace.Thisapproachis

relativelysimilartoours,butinsteadofusing“indirect”measurementsbasedonCAR

supportandcoverage,wesuggestanewnormalizeddistancemetricbasedon“direct”and

“combined”distancesbetweenclassassociationrules.

AnotherrelatedstrategyisminingclusterswithARs[31].TheFP-Growthalgorithm

generatestherulesinthiscase.However,auniquedistancemetric(basedonK-modes)is

afterwardappliedtoidentifysimilaritiesbetweenrules.Providedisthelistofproducts

purchasedbyeachclient,andrulesareclusteredusingatop–downhierarchicalclustering

algorithmtoidentifyclustersinapopulationofcustomers.Afterclusteringtherules,we

introduceaspecificdistancemetrictoassesstheeffectivenessoftheclusteringprocess.

3.Methodology

Ourapproach(Compact,AccurateandDescriptiveAssociativeClassifier)isdivided

into3mainactionsoutlinedintheprecedingsection.Thefollowingsubsectionsgointo

furtherdepthabouteachofthesesteps.

3.1.ClassAssociationRuleGeneration

Inthissubsection,weaddressthemethodoffindingthestrongCARsfromfrequent

itemsets. TheprocessofcreatingARstypicallyconsistsoftwoprimarystages: first,all

frequentitemsetsfromthetrainingdatasetarefoundusingtheleastsupport;then,weuse

thesefrequentitemsetsalongwithminimumconfidencetocreatestrongassociationrules.

TheidenticalprocessusedforARcreationisalsofollowedinthediscoveryofCARs.The

maindistinctionisthatintherule-generationphase,therule’sresultinCARgeneration

comprisesjusttheclasslabel,whereastherule’sresultinARgenerationmightcontain

anyfrequentitemset.Inthefirststep,the“FP-Growth”algorithmisemployedtodiscover

frequentitemsets.The“FP-Growth”algorithmusesa“growth”techniquetodecreasethe

numberofitemsetcandidatesateachlevel,thereforespeedingupthesearchprocess.To

createthe2-frequentitemsetandbeyond,itstartsbydeterminingthe1-frequentitemset.

Sincetheycannotaddtofrequentitemsets, anyinfrequentitemsetsfoundduringthe

procedurearediscarded.Bycompletingthistrimmingstepbeforecalculatingthesupport

at each level, the temporal complexity of the algorithm is decreased. After obtaining

everyfrequentitemsetfromthetrainingdatasets,creatingstrongclassassociationrules

(CARs)thatmeettheminimalsupportandminimumconfidencerequirementsisasimple

process.Thefrequentitemsetsfoundinthefirststageserveasthebasisfortheserules.The

confidenceofarulecanbecalculatedusingthefollowingformula:

confidence(A→B)= su s p u p p o p r o t_ r c t_ o c u o n u t n (A t(A ∪ ) B) (1)

In Equation (1), the support count of an itemset is used, where A represents the

premise(itemsetontheleft-handsideoftherule),Brepresentstheconsequence(class

labelontheright-handsideoftherule), support_count(A∪B) representsthenumber

oftransactionsthatcontainbothitemsetsAandB,andsupport_count(A)representsthe

numberoftransactionsthatcontainitemsetA.Onthebasisofthepriorequation, the

followingprocedurescanbeusedtobuildstrongclassassociationrulesthatsatisfythe

minimumconfidencethreshold:

252

Mathematics2023,11,3978

• GenerateallnonemptysubsetsSforeachfrequentitemsetLandaclasslabelC.

• ForeachnonemptysubsetSof L, outputthestrongrule Rintheformof“S→C”

if s s u u p p p p o o r r t t _ _ c c o o u u n n t t ( ( R S) ) ≤ min_conf, wheremin_conf representstheminimumconfidence

threshold.

3.2.Clustering

Clusteringalgorithmsputcomparableexamplestogetherintoclusters,wherethe

examplesineachclusterdifferfromtheexamplesinotherclustersandsharecommonalities

witheachother.Amongthedifferentclusteringtechniques,K-modesisanoteworthyone.

Becauseofitsuniquebenefitsinsomesituations,suchasefficientlymanagingdatasets

withdiscretequalitiesorcategoricalvariables,likethesuggesteddistancematrixweuseto

describeassociationrules,theK-modestechniqueisused.

3.2.1.DistanceMetric

Wesuggestanewdistancemetricinthispartthatisbasedondirectmeasurements

forruleitems. Ourmainobjectiveistodecreasetherulespacebyusingdirectdistance

measurementsforclustering.

Theencodingofrulesasabinaryvectorofitemsetsisoneofourwork’scontributions.

Withthisstructure,calculatingsimilaritiesacrossrulesisquickandeasy,andourbinary

governeddatasetisaperfectfitforclusteringmethodslikeK-modes.

The antecedent, or left side of the rule, is taken into consideration when we are

calculatingthedistancebetweentherulesthathavethesameclassvalue.

LetR={r1,r2,...,rn }bearuleset,andeachruleisdenotedasfollows:r={a1,a2,...,a

k

}

→ {c},where{a1,a2,...,a

k

}arevaluesoftheattributeandcisaclassvalue. Wefirst

transfertheruleitemsa intoabinaryvector. Theexistingattribute’svalueisreplaced

i

with1andtheremainingattribute’svalues(whichwerenotpresentinarule)arereplaced

with0.

Example: LetusassumethatattributeWindyhastwovalues: “T”and“F”,and

attributeTemperaturehasthreevalues: “Hot”, “Mild”and“Cool”. Anantecedentof

theexampleruleisasfollows:Windy=TandTemp=Cool;asubsettedexampleofthe

representedruleisshownbelow.

Rule Windy=T Windy=F Temp=Hot Temp=Mild Temp=Cool

{Windy=T,

1 0 0 0 1

Temp=Cool}

Aftertransferringtherulesintobinaryvectors,weuseasimplemethodofcomputing

thedistancebetweentworulesasfollows:

Giventworules(rule1,rule2):

rule1={y1,y2,...,y

k

}→{c}

rule2={z1,z2,...,z

k

}→{c}

where{y1, y2, ..., y

k

andz1, z2, ..., z

k

}⊆0,1,andc∈C. Wecomputethesimilarity

betweenrule1andrule2asfollows:

k

distance(rule1,rule2)= ∑|y −z| (2)

i i

i=1

3.2.2.K-Modes

InK-modes,theclusteringprocessinvolvesiterativelyassigningexamplestoclus-

ters,consideringthemodes(themostfrequentvalues)ofthecategoricalattributes.This

approachseekstoidentifygroupsofexamplesthatsharesimilarmodesacrossallcategor-

253

Mathematics2023,11,3978

icalvariables,ensuringthattheresultingclustersareinternallycohesive.Byemploying

K-modes,wecanachieveseveralbenefits. Firstly,itallowsustocapturetheinherent

structurewithintheitemsetscontainedintherules,revealingpatternsandassociations

thatmightbehiddeninnumerical-basedclusteringmethods.Secondly,K-modesoffers

computationalefficiencyandscalabilityforlargedatasetswithcategoricalvariables. It

canhandlehigh-dimensionaldataandhandlealargenumberofcategorieswithineachat-

tribute,makingitsuitableforreal-worldapplicationswithdiverseandcomplexcategorical

data.TheK-modesalgorithmisdescribedinAlgorithm1.

Algorithm1TheK-modesalgorithmforpartitioning,whereeachcluster’scenterisrepre-

sentedbythemedianvalueoftheobjectsinthecluster.

Input:k:thenumberofclusters,D:adatasetcontainingnrules

Output:Asetofkclusters

1: ArbitrarilychoosekrulesfromDastheinitialclustercenters;

2: repeat

3: (Re)assigneachruletotheclustertowhichtheruleisthemostsimilarbasedonthemedian

valueoftherulesinthecluster;

4: Updatetheclustermedians,i.e.,calculatethemedianvalueoftherulesforeachcluster;

5: until nochange.

WeruntheK-modesmethodtwice.SinceAlgorithm1takesthenumberofclustersin

advance,weinitiallyrunthealgorithmtodeterminetheoptimalnumberofclusters.Then,

thealgorithmisrunagainwiththedeterminedoptimalclusters.Whendeterminingthe

optimalnumberofclustersinK-modes,thesilhouettescorecanbeutilizedasametric.The

silhouettescoreassistsinidentifyingthe“natural”numberofclustersbyevaluatingthe

cohesionandseparationofexampleswithintheclusters.

Tocalculatethesilhouettescore,eachexampleisassignedtoacluster,andthefollow-

ingvaluesarecomputed:

• Theaveragedissimilarity(distance)betweenanexampleiandallotherexamples

withinthesamecluster. Thisvaluemeasureshowwellanexamplefitswithinits

assignedclusterwithlowervaluesindicatingbettercohesion.

• Theaveragedissimilarity(distance)betweenanexampleiandallexamplesinthenear-

estneighboringcluster.Thisvaluecapturestheseparationordissimilaritybetweenan

exampleandotherclusterswithhighervaluesindicatinggreaterdissimilarity.

Bycomputingthesilhouettescoresforallexamplesacrossarangeofclusternumbers,

theoptimalnumberofclusterscanbeidentified.The“natural”numberofclusterscorre-

spondstothepointwherethesilhouettescoreishighest,indicatingtheconfigurationwith

thebestbalanceofcohesionandseparation. Thealgorithmthatidentifiesthe“natural”

numberofclustersispresentedinAlgorithm2.

Algorithm2Computingtheoptimalnumberofclusters.

Input:D:adatasetcontainingnrules;max_clusters:themaximumnumberofclusterstosearchfor

Output:Optimalnumberofclusters

1:

Opt_number_of_cluster=1;

2:

Best_score=1;

3:

for(k=2;k≤max_clusters;k++)do

4: RunK-modeswithdatasetDandnumberofclustersask;

5: Calculatesilhouette_score;

6:

ifsilhouette_score>=Best_scorethen

7:

Best_score=silhouette_score;

8:

Opt_number_of_cluster=k;

9: endif

10: endfor

11: returnOpt_number_of_clusters

254

Mathematics2023,11,3978

3.3.ExtractingtheRepresentativeCAR

Afterlocatingeachcluster,thelaststepistoseparatetherepresentativeCARsfrom

each cluster to create a descriptive, compact, and useful associative classifier. In this

work,weextractedrepresentativerulesbasedondatasetcoveragewhileconsideringthe

rulessimilarity.

Thedecisionwasmadetoutilizethisapproachinordertoraisetheclassification

accuracyandoverallcoverage.Itisnotnecessarytoconsidertheouter-classoverlapping

problem—whichindicatesthatsomesamplesfromdifferentclasseshavesimilarcharac-

teristics—becauseweareclusteringsimilarruleswiththesameclassvalue.However,we

shouldavoidtheinter-classoverlappingproblem,whichariseswhenmultiplerulesfrom

thesameclasscoverthesamesamples.BychoosingtherepresentativeCARsaccording

todatabasecoverage,weworkaroundthisissue. Whenthecoverageoftherulesisthe

same,wetakeintoaccounthowsimilartherulesaretoeachother. Thismeansthatwe

selecttheCARthatisclosesttotheclustercenter(ithasthelowestaveragedistancetoall

otherrules).ThestepsaredescribedinAlgorithm3.

Algorithm3ARepresentativeCARbasedonDatasetCoverageandMinimumDistance.

Input: A set of class association rules in CARs array, a training dataset D and

covered_traindataarray

Output:Threerepresentativeclassassociationrules

1: CARs=sort(CARs,coverage,minimum_distance);

2: Representative_CARs.add(CARs[1]):

3:

for(i=2;i≤CARs.length;i++)do

4:

for(j=1;j≤D.length;j++)do

5:

ifcovered_traindata[j]=falsethen

6: ifCARs[i]coversD[j]then

7:

covered_traindata[j]=true;

8: incrementcontributionofCARs[i]by1;

9: endif

10: endif

11: endfor

12: ifcontributionofCARs[i]>0then

13: Representative_CARs.add(CARs[i]);

14: break;

15: endif

16: ifRepresentative_CARs.length=3then

17: returnRepresentative_CARs;

18: endif

19: endfor

Firstly,classassociationruleswithintheclusteraresorted(line1)bycoverageand

minimum_distanceindescendingorderbythefollowingcriteria:GiventworulesR1andR2,

R1issaidtohaveahigherrankthanR2,whichisdenotedasR1 >R2,

• Ifandonlyif,coverage(R1 )>coverage(R2 );or

• Ifcoverage(R1 )=coverage(R2 )but,minimum

d

istance(R1 )>minimum

d

istance(R2 );

• Iftheentiresetofparametersoftherulesisequal,wemaychooseanyofoneofthem.

Aftersortingtherulesbasedoncoverageandminimumdistance,weextractedthe

topthreerulesforeachcluster. Weselectedthreerulesasoptimalaccordingtoexperi-

ments. Eachpotentialruleischecked(Lines3–19);ifitcoversatleastonenewexample

(Lines12–15),thenweaddittotherepresentativeCARsarrayandremovealltheexamples

coveredbythatrule;otherwise,wecontinue.

255

Mathematics2023,11,3978

AssociativeClassificationModel

Afterextractingtherepresentativeclassassociationrules,weproduceourexplainable,

compactanddescriptivemodelwhichisrepresentedinAlgorithm4.

Algorithm4CompactandExplainableAssociativeClassificationModel.

Input:AdistancematrixdandnumberofclustersS

Output:Clusterheights(AHCCLH),ClusterofCARs(AHCCLC)

1: Initialization:minimumsupportandminimumconfidencethresholdsaresettogenerate

theCARs;

2: Generate:ThefrequentitemsetsaregeneratedfromthedatasetbyusingtheFP-Growth

algorithmandusedtoproducestrongclassassociationrules,whicharesortedbased

onconfidenceandsupport.Carsarethengrouppedaccordingtoclasslabel;

3: Cluster:ForeachgroupofCARs,theK-modesclusteringalgorithmisutilizedtocluster

them. Forthispurpose,thenewlydevelopeddistancemetric(Section3.2.1)isused

tofindthesimilaritybetweenCARs,andtheoptimalnumberofclustersisidentified

basedonthesilhouettescore(Algorithm2);

4: Extractrepresentativerules:Threerepresentativerulesareextractedforeachcluster

accordingtoAlgorithm3:

5: Producingfinalmodel:Foreachclassvalue,alltherulesextractedfromeachclusterare

collectedtoproducethefinalcompactandexplainableassociativeclassificationmodel.

4.Results

Experimentalassessmentsupportedtheaccomplishmentofthescientificgoals.Thir-

teenreal-worlddatasetsfromKaggleandtheUCIMachineLearningDatabaseRepository

wereusedtotestourmodels. Bycomparingourclassifier’sclassificationaccuracyand

rulecounttothoseofeightwell-knownrule-basedclassificationalgorithms(DTNB,DT,

C4.5,CPAR,CMAR,CBA,andSA),wewereabletoassessitsperformance. Apaired

t-testwasusedtodeterminethestatisticalsignificanceofeachdifference(witha95%level

ofsignificance).

Associativeclassifierswererunwithdefaultparametersatminimumsupport=1%

andminimumconfidence=50%.WeutilizedtheirWEKAworkbenchimplementationwith

defaultparametersfortheotherclassificationmodels.Thedescriptionofthedatasetsis

showninTable1.

Anevaluationmethodologythatuses10-foldcross-validationwasusedtoachieve

allexperimentaloutcomes. Table2displaystheexperimentalfindingsforclassification

accuracy(meanvaluesthroughoutthe10-foldcross-validationwithstandarddeviations).

Table2showsthattheACMKCmodelachievedthebestaccuraciesonthe“Abalone”,

“Adult”,“Connect4”and“Diabetes”datasetsamongallclassificationmodelsandobtained

comparableaccuraciesonotherdatasets.Ourproposedmodelattainedthethirdhighest

resultonaverageaccuracywith80.0%,whichwasslightlylowerthantheresultsoftheC4.5

(82.7%)andCMAR(82.4%)models.Rule-basedmodelsDTNB,DT,andC4.5obtainedbetter

accuraciesonthe“Car.Evn”and“Nursery”datasetsthanassociativeclassificationsCPAR,

CMAR,CBA,SA,andACMKC.Themainreasonisthatthosedatasetsareimbalanced,

whichcausesaproblemintherule-generationpartofACmodels(ACmodelswerenotable

toproduceenoughclassassociationrulesforeachclassvaluewithimbalanceddatasets).

Interestingly,CPARandCMARachievedover99%accuracyonthe“Mushroom”dataset,

whichwas15–25%higherthanotherrulelearners.

256

Mathematics2023,11,3978

Table1.Datasetsdescription.

Analyzed

Dataset

Attributes Classes Records Rules

Car.Evn 7 4 1728 10,000

Tic-Tac-Toe 10 2 958 10,000

Nursery 9 5 12,960 20,000

Mushroom 23 2 8124 20,000

Abalone 9 3 4177 10,000

Adult 15 2 45,221 20,000

Laptop 11 3 1303 10,000

Chess 37 2 3196 10,000

Connect4 43 3 67,557 10,000

Airplane 17 2 103,904 20,000

AirlineReviews 8 2 129,455 20,000

Diabetes 13 2 70,692 10,000

Recruitment 7 2 215 1000

Table2.Evaluationofclassificationmodelsonaccuracy.

Dataset DTNB DT C4.5 CPAR CMAR CBA SA ACMKC

Car.Evn 95.4±0.8 91.3±1.7 92.1±1.7 78.1±2.5 86.7±2.1 91.2±3.9 86.2±2.1 83.0±3.0

Tic-Tac-Toe 69.9±2.7 74.4±4.4 85.2±2.7 70.5±1.6 95.3±1.8 73.1±0.8 91.7±1.5 74.4±3.7

Nursery 94.0±1.5 93.6±1.2 95.4±1.4 78.9±1.2 91.7±2.2 92.1±2.4 91.6±1.2 85.6±1.3

Mushroom 75.0±7.2 53.4±8.3 78.7±8.4 99.1±0.0 99.4±0.0 75.6±10.9 73.1±6.0 83.0±0.9

Abalone 62.1±1.3 61.8±1.5 62.3±1.2 60.2±1.1 58.3±1.7 61.1±1.0 61.0±0.9 66.9±5.3

Adult 73.0±4.1 82.0±2.3 82.4±4.7 77.4±2.9 80.2±2.4 81.8±3.4 80.8±2.6 82.8±4.5

Laptop 75.7±2.6 72.9±2.9 75.3±2.3 70.9±2.7 72.8±1.0 75.4±2.0 72.0±1.4 71.5±3.3

Chess 93.7±3.0 97.3±3.1 98.9±3.6 93.7±3.2 93.8±2.9 95.4±2.9 92.2±3.8 95.7±2.7

Connect4 78.8±5.9 76.7±7.7 80.0±6.8 68.6±4.4 68.8±4.7 80.9±8.1 78.7±6.0 82.4±4.4

Airplane 89.6±0.9 93.2±0.3 95.7±0.2 88.2±1.3 91.7±2.2 75.7±6.9 77.4±8.1 83.2±0.8

AirlineReviews 94.0±1.0 94.0±1.9 93.8±1.4 96.0±0.9 94.2±1.2 74.2±1.8 76.2±2.6 92.1±2.1

Diabetes 72.9±0.6 73.1±0.5 72.9±0.4 69.9±1.7 70.9±0.6 71.7±2.4 70.0±1.7 74.2±1.5

Recruitment 65.1±5.2 67.5±5.9 63.0±6.4 63.8±3.4 67.2±2.8 64.4±2.5 61.6±4.1 65.3±5.5

Average(%): 79.9±2.8 79.3±3.2 82.7±3.2 78.8±2.1 82.4±2.0 77.8±3.8 77.9±3.2 80.0±3.0

Table3displaysstatisticallysignificanttesting(wins/lossescounts)onaccuracybe-

tween ACMKC and other classification methods. The following represent the results

displayedbelow:W:ourapproachwassignificantlybetterthanthealgorithmsbeingcom-

pared;L:theselectedrule-learningalgorithmsignificantlyoutperformedouralgorithm;N:

nosignificantdifferencehasbeendetectedinthecomparison.

ItcanbeseenfromTable3thatourproposedmodeloutperformedSA(8/3/2)and

CPAR(7/3/3)methodsbasedonwin/lossescounts.AlthoughACMKCstatisticallylost

totheC4.5modelon6datasetsoutof13, itachievedcomparableresultswithDTNB,

DTandCMARalgorithmsandhadaslightlybetterresultthanCBA(5/3/5)intermsof

win/lossescounts.

Inourgoaltodevelopanassociationrule-basedmodelthatsignificantlyreducesthe

requirednumberofrules,wefindourmodelusesfarlessrulesthatmanyothercommon

rule-basedandassociativeclassificationmodels,whichisshowninTable4.Onaverage,for

thedatasetswetested,ourmodelproduced71ruleswiththeothertwoclosestalgorithms

beingCPARat90rulesandCBAat95rules.Ourmethodbeatstheothercomparedmethods

forsevenoutofthirteendatasetsandperformsinthetoptwofortheleastamountofrules

257

Mathematics2023,11,3978

fortenofthethirteentesteddatasets.Theothermodelsincomparisonproducedfarmore

rulesonaverage.

Table 3. Comparisonofclassificationmodelsonaccuracybasedonstatisticallysignificantwins/

lossescounts.

DTNB DT C4.5 CPAR CMAR CBA SA

W 5 3 3 7 4 5 8

L 4 3 6 3 5 3 3

N 4 7 4 3 4 5 2

Table4.Evaluationofclassificationmodelsbasedonnumberofrules.

Dataset DTNB DT C4.5 CPAR CMAR CBA SA ACMKC

Car.Evn 144 432 123 40 567 72 160 21

Tic-Tac-Toe 258 121 88 11 166 23 60 48

Nursery 1240 804 301 60 1935 141 175 132

Mushroom 50 50 26 19 100 15 70 12

Abalone 165 60 49 17 834 132 155 36

Adult 737 1571 279 120 3411 126 130 101

Laptop 101 101 72 41 783 39 75 45

Chess 507 101 31 14 282 14 120 12

Connect4 3826 952 3973 657 6877 349 600 267

Airplane 3201 4444 772 41 391 104 660 120

AirlineReviews 186 890 259 117 3218 121 140 99

Diabetes 160 244 221 37 3572 95 160 24

Recruitment 20 8 13 10 106 15 14 12

Average: 773 1060 477 90 1710 95 184 71

Themainadvantageofourmodelisproducingnoticeablysmallerclassifiersonbigger

datasetscomparingtootherrule-basedandassociativeclassificationmodels(illustratedin

Figure1).

Whenthesizeofthedatasetincreases,thenumberofrulesintheDTNB,DT,C4.5

andCMARmodelsalsorises.However,ACMKCisnotsensitivetothedatasetsize,which

canbeprovenonselecteddatasetsinFigure1. Figure1illustratesthehugeadvantage

ofourproposedmodelcomparedtootherclassificationmodelsintermsofclassifiersize.

Table5providesdetailedinformationonthestatisticallysignificantwin/losscountsofour

methodswhencomparedtootherclassificationmodelsforthenumberofrules.

Table5showsthatACMKCstatisticallyoutperformedallthemodelsonthenumber

ofrulesaccordingtothewin/lossescounts.AlthoughACMKCachievedslightlyworse

resultsthantheC4.5andCMARalgorithmsonaccuracy,itproducedstatisticallysmaller

classifiersthanthosemodelsinalldatasets. Ourproposedmodelachievedstatistically

betterresultsthanDTNBoneverydatasetandDTon12datasetsoutof13intermsof

classifiersize.OurmodelhadastatisticallyworseresultthanCBAonthreedatasetsand

CPARonfourdatasets,andtherewerenostatisticaldifferencesbetweenthosemethodson

threedatasetsoutof13.

AsdisplayedinFigure2,ourmethodprovidescompetitiveaccuraciesagainstthe

otherclassificationmodelswhileutilizingsignificantlylessrules.OnlytheCPARalgorithm

providesasimilarresultwhentradingaccuracyandnumberofrules;yet,onaverage,our

methodutilizesfarlessrules.

258

Mathematics2023,11,3978

Figure1.Comparisonofclassificationmodelsonbiggerdatasetsbasedonclassifiersize.

Table 5. Comparison of classification models on rules based on statistically significant wins/

lossescounts.

DTNB DT C4.5 CPAR CMAR CBA SA

W 13 12 12 6 13 7 12

L 0 1 0 4 0 3 0

N 0 0 1 3 0 3 1

Figure2.Comparisonofclassificationmodelsintermsofaverageaccuracyandnumberofrules.

It is of note that not only does our method perform comparably and sometimes

betterinregardtoaccuracy,italsohasbetterprecision,recallandF-measurescoreswhen

259

Mathematics2023,11,3978

comparingourmethodtootherclassassociationrulealgorithmsusedinclassificationtasks

(showninFigure3).Asmentionedabove,itdoesthiswhileproducingsignificantlyfewer

rulesthanothermethods,whichwasthemaingoalofthisresearch.

Figure3.Comparisonofclassificationmodelson“precision”,“recall”and“F-measure”.

5.Conclusions

Byexhaustivelysearchingthewholeexamplespaceutilizingconstraintsandclustering,

thefundamentalgoalofthisresearchistoproduceacompactandmeaningfulyetaccurate

classifier.Accordingtoexperimentalfindings,ACMKCgreatlydecreasedthenumberof

classificationruleswhileretainingclassificationaccuracy,whichwasthemajorobjectiveof

thisstudy.Morespecifically,theACMKCmethodoutperformedallothermodelsinterms

ofaveragenumberofruleswith71rules,whichwastentimesbetterthantheresultsof

theDTNB,DT,andCMARalgorithms.Theproposedmodel’soverallaccuracywasonpar

withthatofallothermodels,anditwasthethirdhighestbetweenallclassificationmodels.

Theadvantageoftheproposedmodeloverpreviousrule-basedandassociativeclas-

sificationmodelswasdemonstratedexperimentallybythefactthatitproducedsmaller

classifiersonlargerdatasets.

Infuturework,weplantooptimizeourmodelACMKCtoimproveitstimecomplexity,

whichisamajordrawbackofourmethod. Wealsowouldliketoinvestigatewaysof

includingnumericattributesintotheassociativeclassificationmodels,asusingclustering

onclassassociationruleswithnumericattributesmayrevealnewinterestingperspectives

onthesubject.

AuthorContributions:Conceptualization,J.M.,M.D.andB.K.;methodology,J.M.andM.D.;software,

J.M.andM.D.;validation,J.M.andM.D.;formalanalysis,J.M.,M.D.andB.K.;writing—originaldraft

preparation,J.M.andM.D.;writing—reviewandediting,J.M.andB.K.Allauthorshavereadand

agreedtothepublishedversionofthemanuscript.

Funding:JamolbeMattievacknowledgesfundingbytheMinistryof“InnovativeDevelopment”of

theRepublicofUzbekistan,grant:UZ-N47.

DataAvailabilityStatement:Thedatasetusedinthispapercanbefoundathttps://www.kaggle.

com/datasets?tags=13302-Classificationandhttps://archive.ics.uci.edu/(accessedon27June2023).

Acknowledgments:TheSlovenianResearchAgencyARRSprovidedfinancingfortheprojectJ2-2504,

whichthefirstandthirdauthorsrecognize. TheyalsoexpresstheirgratitudetotheRepublicof

Slovenia(InvestmentfundingoftheRepublicofSloveniaandtheEuropeanUnionoftheEuropean

260

Mathematics2023,11,3978

RegionalDevelopmentFund)andtheEuropeanCommissionforsupportingtheInnoRenewCoE

projectthroughtheHorizon2020Widespread-Teamingprogram,respectively(GrantAgreement

#739574).TheMinistryof“InnovativeDevelopment”oftheRepublicofUzbekistan,whichprovided

moneyforthisstudy,isalsoacknowledgedandsincerelythankedbythefirstauthor.Thesecond

authorwaspartiallyfundedbytheNationalScienceFoundation(NSF)grantoftheCalifornianState

University(grantnumber#1826490).

ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

References

1. Lent,B.;Swami,A.;Widom,J. Clusteringassociationrules. InProceedingsofthe13thInternationalConferenceonData

Engineering,Birmingham,UK,7–11April1997;pp.220–231.[CrossRef]

2. Agrawal,R.;Srikant,R.Fastalgorithmsforminingassociationrules. InProceedingsofthe20thInternationalConferenceonVery

LargeDataBases,VLDB,Santiago,Chile,12–15September1994;Volume1215,pp.487–499.

3. Liu,B.;Hsu,W.;Ma,Y.IntegratingClassificationandAssociationRuleMining. InProceedingsoftheFourthInternationalCon-

ferenceonKnowledgeDiscoveryandDataMining,NewYork,NY,USA,27–31August1998;KDD’98;AAAIPress:Washington,

DC,USA,1998;pp.80–86.

4. Mattiev,J.;Kavšek,B.CMAC:ClusteringClassAssociationRulestoFormaCompactandMeaningfulAssociativeClassifier. In

MachineLearning,Optimization,andDataScience,Proceedingsofthe6thInternationalConference,LOD2020,Siena,Italy,19–23July

2020;Springer:Berlin/Heidelberg,Germany,2020;pp.372–384.[CrossRef]

5. Hu,L.Y.;Hu,Y.H.;Tsai,C.F.;Wang,J.S.;Huang,M.W. Buildinganassociativeclassifierwithmultipleminimumsupports.

SpringerPlus2016,5,528.[CrossRef][PubMed]

6. Deng,H.;Runger,G.;Tuv,E.;Bannister,W.CBC:AnAssociativeClassifierwithaSmallNumberofRules.Decis.SupportSyst.

2014,59,163–170.[CrossRef]

7. Rajab,K. NewAssociativeClassificationMethodBasedonRulePruningforClassificationofDatasets. IEEEAccess2019,7,

157783–157795.[CrossRef]

8. Mattiev,J.;Kavšek,B.Coverage-BasedClassificationUsingAssociationRuleMining. Appl.Sci.2020,10,7013.[CrossRef]

9. Thabtah,F.;Cowling,P.;Peng,Y. MCAR:Multi-classClassificationbasedonAssociationRule. InProceedingsofthe3rd

ACS/IEEEInternationalConferenceonComputerSystemsandApplications,Cairo,Egypt,6January2005;Volume2005,p.33.

[CrossRef]

10. Thabtah,F.;Cowling,P.;Peng,Y.MMAC:Anewmulti-class,multi-labelassociativeclassificationapproach. InProceedingsof

theFourthIEEEInternationalConferenceonDataMining(ICDM’04),Brighton,UK,1–4November2004;pp.217–224.[CrossRef]

11. Mattiev,J.;Kavsek,B.Distancebasedclusteringofclassassociationrulestobuildacompact,accurateanddescriptiveclassifier.

Comput.Sci.Inf.Syst.2021,18,791–811.[CrossRef]

12. Chen,G.;Liu,H.;Yu,L.;Wei,Q.;Xing,Z.Anewapproachtoclassificationbasedonassociationrulemining. Decis.SupportSyst.

2006,42,674–689.[CrossRef]

13. Kaufman,L.;Rousseeuw,P.FindingGroupsinData:AnIntroductiontoClusterAnalysis;JohnWiley&Sons:Hoboken,NJ,USA,

1990.[CrossRef]

14. Zaït,M.;Messatfa,H.Acomparativestudyofclusteringmethods. FutureGener.Comput.Syst.1997,13,149–159.[CrossRef]

15. Arabie,P.;Hubert,L.J. AnOverviewofCombinatorialDataAnalysis. InClusteringandClassification;Arabie,P.,Hubert,L.J.,

Soete,G.D.,Eds.;WorldScientificPublishing:Hackensack,NJ,USA,1996;pp.5–63.

16. Ng,T.R.;Han,J.EfficientandEffectiveClusteringMethodsforSpatialDataMining. InProceedingsofthe20thConferenceon

VeryLargeDataBases(VLDB),Santiago,Chile,12–15September1994;pp.144–155.

17. Zhang,T.;Ramakrishnan,R.;Livny,M.BIRCH:AnEfficientDataClusteringMethodforVeryLargeDatabases. InProceedings

ofthe1996ACMSIGMODInternationalConferenceonManagementofData,NewYork,NY,USA,22–27June20131996;

SIGMOD’96;pp.103–114.[CrossRef]

18. Theodoridis,S.;Koutroumbas,K.Chapter13.ClusteringAlgorithmsII:HierarchicalAlgorithms;AcademicPress:SanDiego,CA,

USA,2009;pp.653–700.[CrossRef]

19. Dua,D.;Graff,C.UCIMachineLearningRepository;UniversityofCalifornia:Irvine,CA,USA,2019.

20. Hall,M.;Frank,E. CombiningNaiveBayesandDecisionTables. InProceedingsoftheTwenty-FirstInternationalFlorida

ArtificialIntelligenceResearchSocietyConference,CoconutGrove,FL,USA,15–17May2008;AAAIPress:Washington,DC,

USA,2008

21. Kohavi,R.ThePowerofDecisionTables. InEuropeanConferenceonMachineLearning;Springer:Berlin/Heidelberg,Germany,

1995;pp.174–189.

22. Yin,X.;Han,J. CPAR:ClassificationBasedonPredictiveAssociationRules. InProceedingsofthe2003SIAMInternational

ConferenceonDataMining.SocietyforIndustrialandAppliedMathematics,SanFrancisco,CA,USA,1–3May2003;Volume3.

[CrossRef]

23. Salzberg,S.L.C4.5:ProgramsforMachineLearningbyJ.RossQuinlan;Springer:Berlin/Heidelberg,Germany,1994;Volume16,

pp.235–240.[CrossRef]

261

Mathematics2023,11,3978

24. Mattiev,J.;Kavšek,B.SimpleandAccurateClassificationMethodBasedonClassAssociationRulesPerformsWellonWell-Known

Datasets. InMachineLearning,Optimization,andDataScience,Proceedingsofthe5thInternationalConference,LOD2019,Siena,Italy,

10–13September2019;Springer:Berlin/Heidelberg,Germany,2019;pp.192–204.[CrossRef]

25. Chaudhary,U.;Papapanagiotou,I.;Devetsikiotis,M. Flowclassificationusingclusteringandassociationrulemining. In

Proceedingsofthe201015thIEEEInternationalWorkshoponComputerAidedModeling,AnalysisandDesignofCommunication

LinksandNetworks(CAMAD),Miami,FL,USA,3–4December2010.[CrossRef]

26. Dahbi,A.;Mohammed,M.;Balouki,Y.;Gadi,T.ClassificationofassociationrulesbasedonK-meansalgorithm. InProceedings

ofthe20164thIEEEInternationalColloquiumonInformationScienceandTechnology(CiSt),Tangier,Morocco,24–26October

2016;pp.300–305.[CrossRef]

27. Quinlan,J.R.;Cameron-Jones,R.M.FOIL:Amidtermrepor. InMachineLearning:ECML-93,ProceedingsoftheEuropeanConference

onMachineLearningVienna,Austria,5–7April1993;Springer:Berlin/Heidelberg,Germany,1993;Volume667,pp.3–20.[CrossRef]

28. Han,J.;Pei,J.;Yin,Y.MiningFrequentPatternswithoutCandidateGeneration;AssociationforComputingMachinery:NewYork,

NY,USA,2000;pp.1–12.

29. Mattiev,J.;Kavšek,B.Acompactandunderstandableassociativeclassifierbasedonoverallcoverage. ProcediaComput.Sci.2020,

170,1161–1167.[CrossRef]

30. Gupta,K.G.;Strehl,A.;Ghosh,J.Distancebasedclusteringofassociationrules. InProceedingsoftheArtificialNeuralNetworks

inEngineeringConference,St.Louis,MI,USA,7–10November1999;pp.759–764.

31. Kosters,W.A.;Marchiori,E.;Oerlemans,A.A.J. MiningClusterswithAssociationRules. InProceedingsoftheAdvancesin

IntelligentDataAnalysis,Amsterdam,TheNetherlands,9–11August1999;Hand,D.J.,Kok,J.N.,Berthold,M.R.,Eds.;Springer:

Berlin/Heidelberg,Germany,1999;pp.39–50.

Disclaimer/Publisher’sNote: Thestatements,opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual

author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto

peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

262

MDPI

St.Alban-Anlage66

4052Basel

Switzerland

www.mdpi.com

MathematicsEditorialOffice

E-mail:mathematics@mdpi.com

www.mdpi.com/journal/mathematics

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are

solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s).

MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjurytopeopleorpropertyresultingfrom

anyideas,methods,instructionsorproductsreferredtointhecontent.

Academic Open

Access Publishing

mdpi.com ISBN 978-3-0365-9818-5



## Tables

### Table from Page 17

|    |                            | None   | None   |                   |    |
|:---|:---------------------------|:-------|:-------|:------------------|:---|
|    | (cid:68)(cid:349)(cid:374) |        |        | (cid:68)(cid:258) |    |

### Table from Page 63

|    |    |    |    |    |    |    |    |    |    |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|    |    |    |    |    |    |    |    |    |    |
|    |    |    |    |    |    |    |    |    |    |

### Table from Page 63

| None   | None   | None   |    |    | None   | None   | None   | None   |    |    | None   |
|:-------|:-------|:-------|:---|:---|:-------|:-------|:-------|:-------|:---|:---|:-------|
|        |        |        |    |    |        |        |        |        |    |    |        |
|        |        |        |    |    |        |        |        |        |    |    |        |

### Table from Page 63

| None   | None   | None   | None   |    | None   | None   | None   | None   | None   | None   | None   |
|:-------|:-------|:-------|:-------|:---|:-------|:-------|:-------|:-------|:-------|:-------|:-------|
|        |        |        |        |    |        |        |        |        |        |        |        |
|        |        |        |        |    |        |        |        |        |        |        |        |

### Table from Page 63

|    | None   |    |    |    | None   | None   | None   |    |    |    |
|:---|:-------|:---|:---|:---|:-------|:-------|:-------|:---|:---|:---|
|    |        |    |    |    |        |        |        |    |    |    |

### Table from Page 64

|    |    |    |    |    |    |    |    |    |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|    |    |    |    |    |    |    |    |    |
|    |    |    |    |    |    |    |    |    |
|    |    |    |    |    |    |    |    |    |
|    |    |    |    |    |    |    |    |    |

### Table from Page 64

| None   |    |
|:-------|:---|
|        |    |
|        |    |
|        |    |

### Table from Page 64

| None   | None   | None   | None   |    | None   |
|:-------|:-------|:-------|:-------|:---|:-------|
|        |        |        |        |    |        |
|        |        |        |        |    |        |
|        |        |        |        |    |        |
|        |        |        |        |    |        |
|        |        |        |        |    |        |
|        |        |        |        |    |        |

### Table from Page 65

|    | None   |    |    |
|:---|:-------|:---|:---|
|    |        |    |    |
|    |        |    |    |
|    |        |    |    |

### Table from Page 65

|    |
|:---|
|    |
|    |

### Table from Page 65

|    | None   | None   | None   |
|:---|:-------|:-------|:-------|
|    |        |        |        |
|    |        |        |        |
|    |        |        |        |

### Table from Page 66

|    |    | None   | None   |    |    |    | None   | None   |    |    |    |    | None   |    |    | None   |    |    |
|:---|:---|:-------|:-------|:---|:---|:---|:-------|:-------|:---|:---|:---|:---|:-------|:---|:---|:-------|:---|:---|
|    |    |        |        |    |    |    |        |        |    |    |    |    |        |    |    |        |    |    |
|    |    |        |        |    |    |    |        |        |    |    |    |    |        |    |    |        |    |    |

### Table from Page 66

| None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   |    |
|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:---|
|        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |    |
|        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |    |

### Table from Page 67

| None   | None   |    | (cid:38)(cid:87)   | None   | None   | None   | (cid:90)   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   | None   |
|:-------|:-------|:---|:-------------------|:-------|:-------|:-------|:-----------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |
|        |        |    |                    |        |        |        |            |        |        |        |        |        |        |        |        |        |        |        |

### Table from Page 67

|    |    | None   | None   |    |    | None   | None   |    |    |    |    |    | None   | None   | None   | None   |    |    |
|:---|:---|:-------|:-------|:---|:---|:-------|:-------|:---|:---|:---|:---|:---|:-------|:-------|:-------|:-------|:---|:---|
|    |    |        |        |    |    |        |        |    |    |    |    |    |        |        |        |        |    |    |
|    |    |        |        |    |    |        |        |    |    |    |    |    |        |        |        |        |    |    |

### Table from Page 68

|    |    |
|:---|:---|
|    |    |
|    |    |

### Table from Page 68

| None   | None   | None   | None   |    |
|:-------|:-------|:-------|:-------|:---|
|        |        |        |        |    |
|        |        |        |        |    |
|        |        |        |        |    |

### Table from Page 68

| None   | None   |    |    |    |
|:-------|:-------|:---|:---|:---|
|        |        |    |    |    |
|        |        |    |    |    |
|        |        |    |    |    |

### Table from Page 68

|    |    |
|:---|:---|
|    |    |
|    |    |

### Table from Page 69

| None   |    |    | None   |    |    | None   |    |    | None   | None   | None   | None   |    |    |
|:-------|:---|:---|:-------|:---|:---|:-------|:---|:---|:-------|:-------|:-------|:-------|:---|:---|
|        |    |    |        |    |    |        |    |    |        |        |        |        |    |    |
|        |    |    |        |    |    |        |    |    |        |        |        |        |    |    |
|        |    |    |        |    |    |        |    |    |        |        |        |        |    |    |
|        |    |    |        |    |    |        |    |    |        |        |        |        |    |    |

### Table from Page 69

| None   | None   | None   | None   |    |
|:-------|:-------|:-------|:-------|:---|
|        |        |        |        |    |
|        |        |        |        |    |
|        |        |        |        |    |
|        |        |        |        |    |
|        |        |        |        |    |

### Table from Page 69

| None   | None   | None   |    | None   |
|:-------|:-------|:-------|:---|:-------|
|        |        |        |    |        |
|        |        |        |    |        |
|        |        |        |    |        |
|        |        |        |    |        |

### Table from Page 69

| None   |    | None   | None   | None   | None   |
|:-------|:---|:-------|:-------|:-------|:-------|
|        |    |        |        |        |        |
|        |    |        |        |        |        |
|        |    |        |        |        |        |
|        |    |        |        |        |        |
|        |    |        |        |        |        |

