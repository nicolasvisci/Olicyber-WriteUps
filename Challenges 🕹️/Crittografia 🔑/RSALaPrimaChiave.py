#!/usr/bin/env python3
from Crypto.Util.number import *
import string
e = 65537
n = 11599469215086283756239000323368207328888145111801687279952858519692571454576743213591474246385542521855249880051364427742007447330667804421622274846205769
c = [5880792219702857038643631444000662274997090749990816412642858237750864568276888684497432046359989695313347389766998519842370345512391791676822845113398754, 4976972096947215995604250302120022863724895715346083646855543963329247781262451899029118643158061394120410879487993483866284176498327793885573656815959625, 11533478320221726260579640234629942318235499494819282592707750949879377838153010591699870387733922335237346601688052059159711330257768224077404011307065502, 6578746857498711761521471737262108194348271400824730284518810946761224187855742368157346489709474171892314244109091096808461225937239969612671436689947146, 40392424158100314627057049269725003226278847219814028431132604271016670430845243933350713012952527019147272452755597062194771694902059574620487790145357, 8940773031260128816353055588056553762174304755194627122656101231849888146723299412495411641543320104568844524323442721074997637332927564813921786500578783, 7984784320545875917590734780858897857038334597156022063135915636401931746575156743176244483654097981682154627492244229120815526214459900295599313544227624, 8726361200928671469895309795311953939907207829055317813772040351606093030953303162108723050724434523055468294271626869389754617053082826339689136742130108, 7417749460829589872125015470473215663301512126557338249364767880097167628946787955886428357239009748621520124971407149634165113201860416364735206568534983, 3651575660315522748881313702629899556759815262116313174060673358864308845882922515867398534174480581039825296726046595117354947118504958035020484969190072, 2729665080212688034318826371788198585511207665652009253419241042229354649630802873944313152045039368936476429416274601231358654208866077925266462770458656, 10263048253606984297123478724549603022911190452564582984819673374864047714844730108530907695117857268312227035665259970999887200163673802445141625430514814, 4161268575042878388338254485204921903115753995587094245885781803476005854570440855893195593742898394111531505690716615694198992116059614015397479107995130, 7417749460829589872125015470473215663301512126557338249364767880097167628946787955886428357239009748621520124971407149634165113201860416364735206568534983, 11533478320221726260579640234629942318235499494819282592707750949879377838153010591699870387733922335237346601688052059159711330257768224077404011307065502, 4976972096947215995604250302120022863724895715346083646855543963329247781262451899029118643158061394120410879487993483866284176498327793885573656815959625, 4681912725673019871443561451419395066053419376607563995366260416152571052501135318936871569982910442869454288025059773463637103183173901939380864464743507, 11533478320221726260579640234629942318235499494819282592707750949879377838153010591699870387733922335237346601688052059159711330257768224077404011307065502, 8940773031260128816353055588056553762174304755194627122656101231849888146723299412495411641543320104568844524323442721074997637332927564813921786500578783, 11423510528481254653722753030443951375438327975061847006552200116842671491412197269348216405017375323023103748474060309270443583040889846090306674187220123, 7417749460829589872125015470473215663301512126557338249364767880097167628946787955886428357239009748621520124971407149634165113201860416364735206568534983, 8726361200928671469895309795311953939907207829055317813772040351606093030953303162108723050724434523055468294271626869389754617053082826339689136742130108, 11423510528481254653722753030443951375438327975061847006552200116842671491412197269348216405017375323023103748474060309270443583040889846090306674187220123, 10263048253606984297123478724549603022911190452564582984819673374864047714844730108530907695117857268312227035665259970999887200163673802445141625430514814, 7417749460829589872125015470473215663301512126557338249364767880097167628946787955886428357239009748621520124971407149634165113201860416364735206568534983, 11423510528481254653722753030443951375438327975061847006552200116842671491412197269348216405017375323023103748474060309270443583040889846090306674187220123, 10263048253606984297123478724549603022911190452564582984819673374864047714844730108530907695117857268312227035665259970999887200163673802445141625430514814, 2763933001803204486404977590428655070374645166799194564837051268540673808019656414872574657154244285031674815061739570475906120714339949094699925206973605, 8726361200928671469895309795311953939907207829055317813772040351606093030953303162108723050724434523055468294271626869389754617053082826339689136742130108, 6815947336659824779195428243794677536273796347974540155087174021542202027112580398956449226750698039076818006188092726964024729540059945989096449057834588, 10263048253606984297123478724549603022911190452564582984819673374864047714844730108530907695117857268312227035665259970999887200163673802445141625430514814, 7417749460829589872125015470473215663301512126557338249364767880097167628946787955886428357239009748621520124971407149634165113201860416364735206568534983, 8333734799339493559678955789619922158298739024487455613439873912214855006300104663941336615744988157011795176947319756925896272388708377718259312920347105, 10263048253606984297123478724549603022911190452564582984819673374864047714844730108530907695117857268312227035665259970999887200163673802445141625430514814, 8940773031260128816353055588056553762174304755194627122656101231849888146723299412495411641543320104568844524323442721074997637332927564813921786500578783, 6284846751767392184771017395810689449703790083582134540966884439997965107203503721721565646758267656378167370179394322876635680275943164791150881151397508, 5156750795121096005286481831243300939236934700546846606275954309489260380956137146037448251518456858441169348352256134117553444268716688546022091198082045]
for i in c:
    for j in string.printable:
        cipher = pow(ord(j), e, n)
        if cipher == i:
            print(j, end="")
            break
print()
