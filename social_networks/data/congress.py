from social_networks.data import __congress__


def congress_users():
    import pickle

    with open(__congress__, 'rb') as f:
        congress_users = pickle.load(f)

    tmp = []

    for user in congress_users:
        tmp.append(user.screen_name)

    return tmp

if __name__ == "__main__":
    for i in congress_users():
        print(i)

"""
JoeLieberman
BachusAL06
RepRonPaul
Robert_Aderholt
JudgeTedPoe
SenBobCorker
VoteMarsha
RepAdamSmith
RepMikeQuigley
BillCassidy
BilbrayCA50
DrPhilRoe
RepMcClintock
Jim_Moran
RepJimMatheson
GabbyGiffords
SenSherrodBrown
DeanHeller
eltongallegly24
RepJoeBaca
USRepMikeDoyle
WI2Tweets
RepGoodlatte
repdonyoung
RepMaxineWaters
JackKingston
RandyNeugebauer
RepMikeRogersAL
RepBrianHiggins
DrPhilGingrey
repgregwalden
FrankPallone
jahimes
SenSanders
SenJeffMerkley
HarryEMitchell
PatrickMcHenry
RepWalterJones
johnthune
RepGusBilirakis
congbillposey
RepTrentFranks
RepHankJohnson
PeteSessions
RepKenMarchant
TomRooney
aaronschock
GreggHarper
ConnieMackIV
CynthiaLummis
RepGregoryMeeks
RepBillShuster
DarrellIssa
WhipHoyer
JimOberstar
JudyBiggert
SenMarkey
USRepSullivan
cbrangel
RoyBlunt
SenatorBurr
SteveAustria
RepPerlmutter
RepSchrader
VernBuchanan
TheLugarCenter
AnderCrenshaw
RepMaryFallin
RepCliffStearns
SenArlenSpecter
PeterRoskam
RepSteveIsrael
RepJoeBarton
RepKevinBrady
MikeHMichaud
LeonardBoswell
SenatorCollins
ArturDavis
RepLynnJenkins
MaryBonoUSA
RepMikeCoffman
SenJohnMcCain
repbenraylujan
DanaRohrabacher
RepBarrett
DavidVitter
CongressmanGT
SpeakerRyan
zachwamp
mlfudge
PaulBrounMD
JeffFortenberry
RepSires
SenatorMenendez
JerryMoran
LEETERRYNE
RepPeteKing
MicheleBachmann
RestoreAccount
OrrinHatch
Jim_Jordan
lisamurkowski
JudgeCarter
cathymcmorris
jasoninthehouse
RepErikPaulsen
SenatorReid
russfeingold
bobinglis
RepMikeHonda
SenChrisDodd
virginiafoxx
clairecmc
davereichert
JeffFlake
GovPenceIN
repblumenauer
BarbaraBoxer
GlennNye
LamarSmithTX21
michaelcburgess
JohnEnsign
petehoekstra
RepShimkus
kevinomccarthy
boblatta
jaredpolis
RobWittman
CandiceMiller
Randy_Forbes
CongJoeWilson
Dennis_Kucinich
JohnKerry
chelliepingree
johnculberson
tomperriello
RosLehtinen
keithellison
RepTimRyan
JohnCornyn
PeteOlson
RogerWicker
ChuckGrassley
neilabercrombie
JimDeMint
ThadMcCotter
MarkUdall
SpeakerBoehner
MarkWarner
askgeorge
RepTomPrice
TeamCantor
JohnBoozman"""