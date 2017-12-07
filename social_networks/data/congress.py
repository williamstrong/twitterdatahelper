from social_networks.data import __congress__
from social_networks.database_controller import *
import pickle
import json


def congress_users():

    with open(__congress__, 'rb') as f:
        congress_users = pickle.load(f)

    tmp = []

    for user in congress_users:
        tmp.append({'twitter_name':user.screen_name, 'name':user.name})

    return tmp


def add_name():
    # Current congress data
    r = ReadFromDatabase('data', 'congress_map_trimmed')
    data = r.read_raw_data()

    c = congress_users()



    count = 0

    tmp_stuff = []
    for i in data:
        for j in c:
            if i['user'] == j['twitter_name']:
                i['name'] = j['name']
                count += 1
                tmp_stuff.append(i)

    Database('data').remove_collection('congress_map_trimmed_with_name')
    w = WriteToDatabase('data', 'congress_map_trimmed_with_name')
    w.collection.insert_many(tmp_stuff)
    # print(data[0])

def add_party():
    r = ReadFromDatabase('data', 'congress_map_trimmed_with_name')
    data = r.read_raw_data()

    with open('congress_members.json', 'r') as f:
        info = f.read()

    info = json.loads(info)


    results = [res for res in data]
    data.close()
    for i in results:
        i['name'] = i['name'].replace("Sen. ", '')
        i['name'] = i['name'].replace('Dr. ', '')
        i['name'] = i['name'].replace('Rep. ', '')
        i['name'] = i['name'].replace('Rep.', '')
        i['name'] = i['name'].replace('Rep ', '')
        i['name'] = i['name'].replace('U.S. Rep ', '')
        i['name'] = i['name'].replace('U.S. ', '')
        i['name'] = i['name'].replace('US Rep ', '')
        i['name'] = i['name'].replace('Senator ', '')
        i['name'] = i['name'].replace(', MD', '')
        i['name'] = i['name'].replace('Dr. ', '')
        i['name'] = i['name'].replace('Governor ', '')
        i['name'] = i['name'].replace('Congressman ', '')

        if i['name'] == 'CathyMcMorrisRodgers':
            i['name'] = 'Cathy McMorris Rodgers'

        if i['name'] == "Glenn 'GT' Thompson":
            i['name'] = 'Glenn Thompson'

        if i['name'] == "johnculberson":
            i['name'] = 'John Culberson'

        r.collection.save(i)

    matched = []
    count = 0
    new_col = []
    for i in info:
        # print(i)
        # data.rewind()
        for j in results:
            # a = i['name']
            # b = j['name']
            # print(a)
            # print(b)
            if i['name'] == j['name']:
                # Add to matched
                matched.append(i['name'])
                count += 1

                # Add new data
                j['party'] = i['party']
                j['district'] = i['district']
                j['state'] = i['state']
                j['years'] = i['years']
                r.collection.save(j)
                new_col.append(j)



    Database('data').remove_collection('current_congress_with_data')
    WriteToDatabase('data', 'current_congress_with_data').collection.insert_many(new_col)

    data.close()


if __name__ == "__main__":
    # congress_users()
    # congress_data()

    add_name()
    add_party()

    a = ReadFromDatabase('data', 'current_congress_with_data').read_raw_data()
    for i in a:
        print(i)
    # data = r.read_raw_data()
    # for i in data:
    #     print(i)



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