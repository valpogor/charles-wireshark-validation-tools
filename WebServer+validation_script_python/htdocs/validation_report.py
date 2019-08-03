import os
import sys
from datetime import datetime
import glob
import re
import time
import codecs
from operator import itemgetter, attrgetter, methodcaller
# import sysinfo
# import getpass
# a = getpass.getuser()
# # SYS
# path = 'C:/Users/' + a + '/Desktop/test/'
path = ("/Applications/MAMP/htdocs/uploadsLIVE/")
pathR = ("/Applications/MAMP/htdocs/reportsLIVE/")
s = datetime.now().strftime("%Y%m%d-%H%M")
sys.stdout = open(pathR + "report-" + s + ".html", 'w')
# Open any file with chls extension

for f in glob.glob(os.path.join(path, '*.chls')):
    f = codecs.open(f, 'r', 'latin1').read()
    # f = open(f, 'r').read()
#
ADID = r'_YO_.{24}'
f_id = r' <Error>.{0,150}/2</Error>'
f_idF = r'xxxt.[$].{9}'
if " <Error>." in f:
    flag = re.search(f_id, f).group()[-38:-10]
if ' <Impression' in f:
    # SI = r' <Impression id="FWi_.{0,115}/1</Impression>'
    SI = r' <Impression.{0,130}/1</Impression>'
    DI = r' <Error>.{0,150}</Error>'
    FQ = r' <Tracking event="firstQuartile.{0,120}Tracking>'
    MP = r' <Tracking event="midpoint.{0,120}Tracking>'
    TQ = r' <Tracking event="thirdQuartile">.{0,120}Tracking>'
    C =  r' <Tracking event="complete.{0,120}Tracking>'
    AE = r' <Tracking event="close">.{0,120}Tracking>'
else:
    SI = r'<Impression.{0,130}/1</Impression>'
    DI = r'<Error>.{0,150}</Error>'
    FQ = r'<Tracking event="firstQuartile.{0,120}Tracking>'
    MP = r'<Tracking event="midpoint.{0,120}Tracking>'
    TQ = r'<Tracking event="thirdQuartile">.{0,120}Tracking>'
    C = r'<Tracking event="complete.{0,120}Tracking>'
    AE = r'<Tracking event="close">.{0,120}Tracking>'

patDATE = r'(.{3},\s+\d+\s.{3}.{5}\s\d+:\d+)'
patSiteS = r'(gmott_.{15,29})'
FillerP = r'(Ad id="filler_YO_)(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s.{0,44}'
FillerPn = r'(Ad id="filler_YO_)(.*).(></Linear>)'

TrirdPart = r' <Impression>https://s.{220,330}</Impression>'
x = "&#9989"
y = "&#10060"
# x = "x"
# y = "y"
SIf= r'GET /sl.{60,65}/1'
DIf= r'GET /sl.{60,65}/1'
FQf= r'GET /sl.{60,65}/4'
MPf= r'GET /sl.{60,65}/5'
TQf= r'GET /sl.{60,65}/6'
Cpf= r'GET /sl.{60,65}/3'
Apf= r'GET /sl.{60,65}/2'

Adl = []
Sl = []
Dl = []
Fl = []
Ml = []
Tl = []
Cl = []
Al = []
Sf = []
Df = []
Ff = []
Mf = []
Tf = []
Cf = []
Af = []
Sr = []
Dr = []
Fr = []
Mr = []
Tr = []
Cr = []
Ar = []
Filler = []
Fduration = []
TP = []

pDate = []
pSites = []
flag1 = []
FiredC=[]
flagr= []
for match in re.compile(ADID).finditer(f): Adl.append(match.group()[4:13])
for match in re.finditer ( patDATE, f ): pDate.append ( match.group () )
for match in re.finditer ( patSiteS, f ): pSites.append ( match.group () )
for match in re.finditer ( FillerP, f ): Fduration.append ( match.group ()[-7:-1] )
if len(Fduration)==0:
    for match in re.finditer(FillerPn, f): Fduration.append(match.group()[-28:-22])
if 'filler_YO'in f:
    Filler.append ( Adl[-1] )
    del Adl[-1]
for match in re.compile(TrirdPart).finditer(f):Dl.append(match.group()[-51:-43])
for match in re.compile(SI).finditer(f):Sl.append(match.group()[-51:-43])
# if len(Sl)==0:
#     for match in re.finditer(SIn, f): Sl.append(match.group()[-51:-43])
for match in re.compile ( DI ).finditer ( f ):Dl.append(match.group()[-46:-38])
for match in re.compile ( FQ ).finditer ( f ):Fl.append ( match.group ()[-49:-41] )
for match in re.compile ( MP ).finditer ( f ):Ml.append ( match.group ()[-49:-41] )
for match in re.compile ( TQ ).finditer ( f ):Tl.append ( match.group ()[-49:-41] )
for match in re.compile ( C ).finditer ( f ):Cl.append ( match.group ()[-49:-41] )
if len(Cl)-len(Adl)==1:
    del Cl[-1]
for match in re.compile ( AE ).finditer ( f ):Al.append ( match.group ()[-50:-42] )
for match in re.compile ( FQ ).finditer ( f ):flag1.append ( match.group ()[-49:-41] )
for match in re.compile (f_idF).finditer ( f ):(FiredC).append ( match.group ()[-9:-1])
for match in re.compile (SIf).finditer ( f ):Sf.append ( match.group ()[-38:-30])
for match in re.compile (DIf).finditer ( f ):Df.append ( match.group ()[-38:-30])
for match in re.compile (FQf).finditer ( f ):Ff.append ( match.group ()[-38:-30])
for match in re.compile (MPf).finditer ( f ):Mf.append ( match.group ()[-38:-30])
for match in re.compile (TQf).finditer ( f ):Tf.append ( match.group ()[-38:-30])
for match in re.compile (Cpf).finditer ( f ):Cf.append ( match.group ()[-38:-30])
for match in re.compile (Apf).finditer ( f ):Af.append ( match.group ()[-38:-30])

for i in range(len(flag1)):
    if len(FiredC)<len(flag1):
        FiredC.append(".")
    if set(FiredC[i]) & set(flag1[i]):
        flagr.append ( x )
    else:
        flagr.append(y)


for i in range(len(Sl)):
    if len(Sl)>len(flag1):
        Sld = []
        Sld.append ( Sl[0] )
        del Sl[0]
        j=Sld[0]
        if j in Sf:
            Sf.remove(j)
    if len(Sf)<len(Sl):
        Sf.append(".")
for i in range ( len ( Sl ) ):
    if set(Sf[i]) & set(Sl[i]):
        Sr.append (x)
    else:
        Sr.append(y)
# for i in range(len(Dl)):
    # if len(Df)<len(Dl):
    #     Df.append(".")
    # if set(Df[i]) & set(Dl[i]):
    #     Dr.append (x)
    # else:
    #     Dr.append(y)
if len(Dr)<len(Sr):
    q = len ( Sr ) - len ( Dr )
    Dr.append(x)
j= len(Dr)-len(Fr)
    # else:
    #     Dr.append ( y )
# for i in range(len(Dl)):
#     if set ( Df[i] ) & set ( Dl[i] ):
#         print "yes"

# print j

    # if len(Df)<len(Sr):
    #     Df.append(x)
    # if Sld>0:
    #     Dr.append ( x )
        # Dr.remove ( len ( q ) )
    # if set(Df[i]) & set(Ff[i]):
    #     Dr.append (x )
    # else:
    #     Dr.append(y)
        # if len(Dr)>len(Sr):
        #     j=len(Dr)-len(Sr)
        #     Dr.remove(len(j))


for i in range(len(Fl)):
    if len(Ff)<len(Fl):
        Ff.append(".")
    if set(Ff[i]) & set(Fl[i]):
        Fr.append ( x )
    else:
        Fr.append(y)
for i in range(len(Ml)):
    if len(Mf)<len(Ml):
        Mf.append(".")
    if set(Mf[i]) & set(Ml[i]):
        Mr.append ( x )
    else:
        Mr.append(y)
for i in range(len(Tl)):
    if len(Tf)<len(Tl):
        Tf.append(".")
    if set(Tf[i]) & set(Tl[i]):
        Tr.append ( x )
    else:
        Tr.append(y)
for i in range(len(Cl)):
    if len(Cf)<len(Cl):
        Cf.append(".")
    if set(Cf[i]) & set(Cl[i]):
        Cr.append ( x )
    else:
        Cr.append(y)
for i in range(len(Al)):
    if len(Af)<len(Al):
        Af.append(".")
    if set(Af[i]) & set(Al[i]):
        Ar.append ( x )
    else:
        Ar.append(y)
# print Sl
# print len(Sl)
# print Sf
# print Sr
# print len(flag1)
# # Profile
if "prof=372496:dfw_ios_mobile" in f:
    pProf = '372496:dfw_ios_mobile'
elif "prof=372496:dfw_ios_tablet" in f:
    pProf = "372496:dfw_ios_tablet"
elif "prof=372496:dfw_android_tablet" in f:
    pProf = "372496:dfw_android_tablet"
elif "prof=372496:dfw_android_mobile" in f:
    pProf = "372496:dfw_android"
elif "prof=372496:dfw_desktop" in f:
    pProf = "372496:dfw_desktop"
else:
    pProf = 'Not found'



# # # # # print html
print "<html>"
print "<head>"
print "<title>" + "DIRECTV Adworks Automation Report for LIVE TV" + "</title>"
print "</head>"
print "<body>"
print "<style>"
print "tr:hover {background-color: 82baff;}"
print "td {border: 1px solid #ddd;padding: 5px;}"
print "th {border: 1px solid #ddd;padding-top: 7px;padding-bottom: 7px;text-align: center;background-82baff: white;color: black;}"
print "</style>"
print "<img src=http://events.adage.com/digital2012/images/attlogo.png HEIGHT=100 WIDTH=380 ALIGN=left >"
print "<h1 id=Report ALIGN=left> AUTOMATION REPORT LIVE TV </h1>"
print "<br>"
print "<table id=Report>"
print "<tr>"
print "<th align = center>&nbsp&nbsp&nbsp&nbsp DAY / TIME  : </th>"
print "<td>" + time.strftime ( "%d/%m/%Y" ) + "     " + time.strftime ( "%I:%M %p" ) + "</td>"
print "</tr>"
print "<tr>"
print "<table style=width:1050px border='1'>"
print "</tr>"
print "<br>"
print "<tr>"
print "<th align = left>" + "Date / Time DAI" + "</th><th>" + pDate[0] + "</th><tr>"
if "prof" in f:
    print "<th align = left>" + "Profile" + "</th><th>" + pProf + "</th><tr>"
else:
    print
if "gmott" in f:
    print "<th align = left>" + "Site Section" + "</th><th>" + pSites[0] + "</th><tr>"
else:
    print
if 'filler_YO'in f:
    print  "<th align = left>" + "Filler" + "</th><th>" + "ID:" + "&nbsp" + str(Filler[0]) +"&nbsp"+"&nbsp"+"&nbsp"+ "Duration:" + "&nbsp" + str(Fduration[0]) + "&nbsp"+"sec" + "</th><tr>"
if 'Innovid Ads<'in f:
    print  "<th align = left>" + "Third Party AD" + "</th><th>"  + "Innovid Ads" + "</th><tr>"

print "</tr>"
print "</table>"
print "</body>"
print "<br>"
print "<table id=Report>"
print "<tr>"
print "<table style=width:1050px border='1'>"
print "</tr>"
print "<tr>"
print "<th>"+'AD ID, total:'+str(len(Adl))+"</th>"
print "<th>Slot Impression</th>"
print "<th>Default Impression</th>"
print "<th>First Quartile</th>"
print "<th>Midpoint Quartile</th>"
print "<th>Third Quartile</th>"
print "<th>Complete</th>"
print "<th>Adslotend</th>"
print "</tr>"
print "<tr>"
#
index = 0
for index in range ( len ( Adl ) ):
    for si in range ( index, len ( Sr ) ):
        for di in range ( index, len ( Dr ) ):
            for fq in range ( index, len ( Fr ) ):
                for mq in range ( index, len ( Mr ) ):
                    for tq in range ( index, len ( Tr ) ):
                        for c in range ( index, len ( Cr ) ):
                            for ae in range ( index, len ( Ar ) ):
                                break
    print "<tr>"
    print  "<td>" + Adl[index] + "</td"
    print "</tr>"
    print  "<td align = center>" + Sr[index] + "</td>"
    if Df>0:
        print  "<td align = center>" + Sr[index] + "</td>"
    else:
        print  "<td align = center>" + Dr[index] + "</td>"
    print  "<td align = center>" + Fr[index] + "</td>"
    print  "<td align = center>" + Mr[index] + "</td>"
    print  "<td align = center>" + Tr[index] + "</td>"
    print  "<td align = center>" + Cr[index] + "</td>"
    if Af>0:
        print  "<td align = center>" + Sr[index] + "</td>"
    else:
        print  "<td align = center>" + Ar[index] + "</td>"
print "</table>"
print "</body>"
print "<br>"
# # validation Ad request parameters for DAI Live
maxdp= r'&maxd=....'
maxdr = []

for match in re.finditer ( maxdp, f ): maxdr.append ( match.group ()[-4:-1] )
if len(maxdr) == 0:
    maxdr.append("Not found")
mindp= r'&mind=....'
mindr = []
for match in re.finditer ( mindp, f ): mindr.append ( match.group ()[-4:-1] )
if len(mindr) == 0:
    mindr.append("Not found")

nwp= r'&nw=.*&mo'
nwr = []
for match in re.finditer ( nwp, f ): nwr.append ( match.group ()[-9:-3]  )
if len(nwr) == 0:
    nwr.append("Not found")

ssnwp= r'&ssnw=.*&vi'
ssnwr = []
for match in re.finditer ( ssnwp, f ): ssnwr.append ( match.group ()[-9:-3]  )
metrp= r'&metr=.*&p'
metrr = []
for match in re.finditer ( metrp, f ): metrr.append ( match.group ()[-7:-2]  )
asnwp= r'&asnw=.*&cs'
asnwr = []
for match in re.finditer ( asnwp, f ): asnwr.append ( match.group ()[-8:-3]  )
vdurp= r'&vdur=.*&ca'
vdurr = []
for match in re.finditer ( vdurp, f ): vdurr.append ( match.group ()[-7:-3]  )
if len(vdurr) == 0:
    vdurr.append("Not found")
vipp= r'&vip=.*&re'
vipr = []
for match in re.finditer ( vipp, f ): vipr.append ( match.group ()[-16:-3]  )
clientIpp= r', clientIp=.*, user'
clientIpr = []
for match in re.finditer ( clientIpp, f ): clientIpr.append ( match.group ()[-19:-6]  )
caidp= r'&caid=.*&as'
caidr = []
for match in re.finditer ( caidp, f ): caidr.append ( match.group ()[-14:-3]  )
pvrnp= r'&pvrn=.*&vp'
pvrnr = []
for match in re.finditer ( pvrnp, f ): pvrnr.append ( match.group ()[-14:-3]  )
vprnp= r'&vprn=.*&vc'
vprnr = []
for match in re.finditer ( vprnp, f ): vprnr.append ( match.group ()[-14:-3]  )
vcidp= r'&vcid=.*3D'
vcidr = []
for match in re.finditer ( vcidp, f ): vcidr.append ( match.group ()[-31:-6]  )
if len(vcidr) == 0:
    vcidr.append("Not found")

modep= r'&mode=.*&vd'
moder = []
for match in re.finditer ( modep, f ): moder.append ( match.group ()[-8:-3]  )
csidp= r'&csid=.*&ss'
csidr = []
for match in re.finditer ( csidp, f ): csidr.append ( match.group ()[-30:-3]  )
respp= r'&resp=.*&me'
respr = []
for match in re.finditer ( respp, f ): respr.append ( match.group ()[-9:-3]  )
if len(respr) == 0:
    respr.append("Not found")

ptgtp= r';ptgt=.*&slau='
ptgtr = []
for match in re.finditer ( ptgtp, f ): ptgtr.append ( match.group ()[-8:-6]  )
slaup= r'&slau=.*&sl'#&&slau=midroll&sl
slaur = []
for match in re.finditer ( slaup, f ): slaur.append ( match.group ()[-11:-3]  )
slidp= r'&slid=.*&cp'#&slid=midroll1&cp
slidr = []
for match in re.finditer ( slidp, f ): slidr.append ( match.group ()[-12:-3]  )
cpsqp= r'&cpsq=.*&maxd='
cpsqr = []
for match in re.finditer ( cpsqp, f ): cpsqr.append ( match.group ()[-8:-6]  )

hhidp= r'&hhid=.*3D'
hhidr = []
for match in re.finditer ( hhidp, f ): hhidr.append ( match.group ())
if len(hhidr) == 0:
    hhidr.append("Not found")


attnidp= r'&attnid=.*3D'
attnidpn= r'&attnid=.(.*).isLive'
attnidr = []
for match in re.finditer ( attnidp, f ): attnidr.append ( match.group () [-31:-6] )
if len(attnidr) == 0:
    for match in re.finditer(attnidpn, f): attnidr.append(match.group()[7:14])
    if len(attnidr) == 0:
        attnidr.append("=Not found")
comscore_impl_typep= r'&comscore_impl_type=.*&com'
comscore_impl_typer = []
for match in re.finditer ( comscore_impl_typep, f ): comscore_impl_typer.append ( match.group () [-28:-26] )

comscore_platformp= r'&comscore_platform=.*&com'
comscore_platformr = []
for match in re.finditer ( comscore_platformp, f ): comscore_platformr.append ( match.group () [-10:-2] )

comscore_devicep= r'&comscore_device=.*&nielsen'#&comscore_device=iPad6%2C11&n
comscore_devicer = []
for match in re.finditer ( comscore_devicep, f ): comscore_devicer.append ( match.group () [-50:-45] )

nielsen_dev_groupp= r'&nielsen_dev_group=.*&nie'#&nielsen_dev_group=devgrp%2CTAB&nie
nielsen_dev_groupr = []
for match in re.finditer ( nielsen_dev_groupp, f ): nielsen_dev_groupr.append ( match.group () [-17:-4] )

nielsen_platformp= r'&nielsen_platform=.*&_fw'#&nielsen_platform=plt%2CMBL&_fw
nielsen_platformr = []
for match in re.finditer ( nielsen_platformp, f ): nielsen_platformr.append ( match.group () [-14:-4] )
fw_nielsen_app_idp= r'&_fw_nielsen_app_id=.*;ptgt' #&_fw_nielsen_app_id=P7CFE36DB-A8D9-4801-95FE-51C29101342C;ptgt
fw_nielsen_app_idr = []
for match in re.finditer ( fw_nielsen_app_idp, f ): fw_nielsen_app_idr.append ( match.group () [-43:-5] )
#
if 'sltp' in f:
    sltp = x
else:
    sltp = y
if 'exvt' in f:
    exvt = x
else:
    exvt = y
if 'slcb' in f:
    slcb = x
else:
    slcb = y
if 'aeti' in f:
    aeti = x
else:
    aeti = y
if 'emcr' in f:
    emcr = x
else:
    emcr = y
if 'amcb' in f:
    amcb = x
else:
    amcb = y
if 'prof=372496:dfw_' in f:
    prof = x
else:
    prof = y
if 'nw=372496' in f:
    nw = x
else:
    nw = y
if 'mode=live' in f:
    mode = x
else:
    mode = y
if 'vdur=123' in f:
    vdur = x
else:
    vdur = y
if 'slid=midroll2, caid=a110250794' in f:
    caid = x
elif 'slid=midroll2, caid=a110110608' in f:
    caid = x
elif 'slid=midroll2, caid=a19762660' in f:
    caid = x
elif 'slid=midroll2, caid=a110304965' in f:
    caid = x
elif 'slid=midroll2, caid=a110111948' in f:
    caid = x
elif 'caid=a110104545' in f:
    caid = x
elif 'caid=a110061062' in f:
    caid = x
elif 'caid=a110232111' in f:
    caid = x
elif 'caid=a1' in f:
    caid = x
else:
    caid = y
if 'asnw=87146' in f:
    asnw = x
else:
    asnw = y
if 'csid=gmott_desktop_watch_live_' in f:
    csid = x
elif 'gmott_ios_mobile_watch_live' in f:
    csid = x
elif 'csid=gmott_android_watch_live_' in f:
    csid = x
elif 'csid=gmott_android_tablet_watch_live' in f:
    csid = x
elif 'csid=gmott_ios_tablet_watch_live' in f:
    csid = x
else:
    csid = y
if 'ssnw=372496' in f:
    ssnw = x
else:
    ssnw = y
if 'vip=' in f:
    vip = x
else:
    vip = y
if 'resp=vmap1' in f:
    resp = x
else:
    resp = y
if 'metr=1031' in f:
    metr = x
else:
    metr = y
if 'pvrn=' in f:
    pvrn = x
elif 'pvrn=827952954' in f:
    pvrn = x
elif 'pvrn=1820135090' in f:
    pvrn = x
elif 'pvrn=2079798332' in f:
    pvrn = x
elif 'pvrn=2059051399' in f:
    pvrn = x
elif 'pvrn=1206821216' in f:
    pvrn = x
elif 'pvrn=29927171' in f:
    pvrn = x
elif 'pvrn=1478569375' in f:
    pvrn = x
elif 'pvrn=395911817' in f:
    pvrn = x
else:
    pvrn = y
if 'vprn=' in f:
    vprn = x
elif 'vprn=827952954' in f:
    vprn = x
elif 'vprn=1820135090' in f:
    vprn = x
elif 'vprn=2079798332' in f:
    vprn = x
elif 'vprn=2059051399' in f:
    vprn = x
elif 'vprn=1206821216' in f:
    vprn = x
elif 'vprn=29927171' in f:
    vprn = x
elif 'vprn=1478569375' in f:
    vprn = x
elif 'vprn=395911817' in f:
    vprn = x
else:
    vprn = y
if 'vcid=zhd0v7Tz%2FGHHjmqrX0Deqg' in f:
    vcid = x
elif 'vcid=0EIDrf0ajacBgBY7IIX2Vw' in f:
    vcid = x
elif 'vcid=' in f:
    vcid = x
else:
    vcid = y
if 'comscore_impl_type=' in f:
    comscore_impl_type = x
else:
    comscore_impl_type = y
if 'comscore_platform=PC' in f:
    comscore_platform = x
elif 'comscore_platform=ios' in f:
    comscore_platform = x
elif 'comscore_platform=android' in f:
    comscore_platform = x
else:
    comscore_platform = y
if 'comscore_device=Windows+Server+2008+R2+%2F+7' in f:
    comscore_device = x
elif 'comscore_device=iPhone' in f:
    comscore_device = x
elif 'comscore_device=Android_' in f:
    comscore_device = x
elif 'comscore_device=iPad' in f:
    comscore_device = x
else:
    comscore_device = y
if 'nielsen_dev_group=devgrp%2' in f:
    nielsen_dev_group = x
else:
    nielsen_dev_group = y
if 'nielsen_platform=plt%2CDSK' in f:
    nielsen_platform = x
elif 'nielsen_platform=plt%2CMBL' in f:
    nielsen_platform = x
else:
    nielsen_platform = y
if 'fw_nielsen_app_id=P7CFE36DB-A8D9-4801-95FE-51C29101342C' in f:
    fw_nielsen_app_id = x
else:
    fw_nielsen_app_id = y
if 'ptgt=a' in f:
    ptgt = x
else:
    ptgt = y
if 'slau=midroll' in f:
    slau = x
else:
    slau = y
if 'slid=midroll1' in f:
    slid = x
elif 'slid=midroll2' in f:
    slid = x
else:
    slid = y
if 'cpsq=1' in f:
    cpsq = x
elif 'cpsq=2' in f:
    cpsq = x
else:
    cpsq = y

if maxdr[:1]==[0,9]:
    print "yes"
if 'maxd=' in f:
    maxd = x
elif 'maxd=150' in f:
    maxd = x
elif 'maxd=120' in f:
    maxd = x
elif 'maxd=300' in f:
    maxd = x
else:
    maxd = y
if 'mind=' in f:
    mind = x
elif 'mind=150' in f:
    mind = x
elif 'mind=120' in f:
    mind = x
elif 'mind=300' in f:
    mind = x
else:
    mind = y
if 'attnid=dfw001' in f:
    attnid = x
else:
    attnid = y
if 'hhid=zhd0v7Tz%2FGHHjmqrX0Deqg%3D%3D' in f:
    hhid = x
elif 'hhid=0EIDrf0ajacBgBY7IIX2Vw%3D%3D' in f:
    hhid = x
elif 'hhid=' in f:
    hhid = x
else:
    hhid = y
if 'clientIp=' in f:
    clientIp = x
else:
    clientIp = y
# table validation
if 'gmott' in f:
    print "<table>"
    print "<body>"
    print "<table id=Validation Ad request parameters>"
    print "<table style=width:1050px border='1'>"
    print "<th>Validation Ad request parameters</th>"
    print "</table>"
    print "</body>"
    print "<table>"
    print "<body>"
    print "<table id=Validation Ad request parameters>"
    print "<table style=width:1050px border='1'>"
    print    "<tr>""<td>" + sltp + "sltp""</td>""<td>" + maxd+"maxd=" + str(maxdr[-2])+"</td>""<td>" +vcid + "vcid" +str(vcidr[-1]) + "</td>""<td>" + resp + "resp" + str(respr[-1])+"</td>""<td>" +caid+"caid"+str(caidr[-3])+"</td>""<td>" + comscore_impl_type + "comscore_impl_type"+str(comscore_impl_typer[-1])+"</td>""</tr>"
    print    "<tr>""<td>" + slcb + "slcb"+"</td>""<td>" +mind+"mind=" + str(mindr[-2]) +"</td>""<td>" +hhid + "hhid" + str(hhidr[-1])+ "</td>""<td>" +nw+"nw="+ str(nwr[-1])+ "</td>""<td>" +clientIp+ "clientIp" +str(clientIpr[-1])+ "</td>""<td>" + comscore_platform + "comscore_platform"+str(comscore_platformr[-1])+"</td>""</tr>"
    print    "<tr>""<td>" + amcb + "amcb""</td>""<td>" + vdur+ "vdur"+str(vdurr[-1])+"</td>""<td>" + attnid + "attnid" + str(attnidr[-1])+"</td>""<td>" +asnw+ "asnw="+str(asnwr[-1])+"</td>""<td>" +vip+ "vip" + str(vipr[-1])+"</td>""<td>" + comscore_device + "comscore_device" + str(comscore_devicer[-1])+"</td>""</tr>"
    print    "<tr>""<td>" + aeti+ "aeti"+"</td>""<td>" + cpsq + "cpsq" +str(cpsqr[-2])+"</td>""<td>" + csid + "csid=gmott" +str(csidr[-1])+ "</td>""<td>" + metr+"metr"+ str(metrr[-1]) + "</td>""<td>" +ssnw+"ssnw=" + str(ssnwr[-1]) + "</td>""<td>" + nielsen_dev_group + "nielsen_dev_group" + str(nielsen_dev_groupr[-1])+"</td>""</tr>"
    print    "<tr>""<td>" + emcr + "emcr"+ "</td>""<td>"  +mode + "mode" + str(moder[-1])+ "</td>""<td>" + "</td>""<td>" + slid + "slid" + str(slidr[-3])+"</td>""<td>" + pvrn+"pvrn" + str(pvrnr[-3])+ "</td>""<td>" + nielsen_platform + "nielsen_platform" +str(nielsen_platformr[-1])+ "</td>""</tr>"
    print    "<tr>""<td>" + exvt + "exvt"+ "</td>""<td>" + ptgt + "ptgt" + str(ptgtr[-1])+"</td>""<td>" + "</td>""<td>" + slau + "slau" + str(slaur[-1])+"</td>""<td>" + vprn + "vprn"+str(vprnr[-3]) +"</td>""<td>" + fw_nielsen_app_id + "fw_nielsen_app_id"+str(fw_nielsen_app_idr[-1])+"</td>""</tr>"
    print "</table>"
    print "</body>"
    print "</html>"
    print "</table>"
    print "</body>"
    print "</html>"
else:
    print
