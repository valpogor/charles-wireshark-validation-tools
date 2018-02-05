import os
import subprocess
import sys
from datetime import datetime
import glob
import re
import time
path = ("/Applications/MAMP/htdocs/server/files/logs/")
pathR = ("/Applications/MAMP/htdocs/server/files/report_live/")
x = "&#9989"
y = "&#10060"
# Open any file with chls extension
files = []
wire = []
wtxt = []
os.chdir(path)
files += [each for each in os.listdir(path) if each.endswith('.chls')]
wire += [each for each in os.listdir(path) if each.endswith('.pcapng')]
# convert Wireshark log to txt
for i in range(len(wire)):
    tsharkCall = ["tshark","-Tpdml","-V","-r", wire[i]]
    tsharkCall2 = ["tshark", "-Tek", "-V", "-r", wire[i]]
    tsharkOut = open(pathR + wire[i] + ".txt", 'w')
    tsharkOut2 = open(pathW + wire[i] + ".txt", 'w')
    tsharkProc = subprocess.call(tsharkCall, stdout=tsharkOut)
    tsharkProc2 = subprocess.call(tsharkCall2, stdout=tsharkOut2)
wtxt += [each for each in os.listdir(pathR) if each.endswith('.txt')]
for i in range(len(files)):
    f = open(files[i], 'r').read()
    sys.stdout = open(pathR + files[i] + ".html", 'w')
    if "4</Error>" in f:
        ER = '4e'
    ADID = r'_YO_.{24}'
    IDr = ur'/BeaconProxy/.{5,8}-'
    f_id = r' <Error>.{0,150}/2</Error>'
    f_idF = r'xxxt.[$].{9}'
    if " <Error>." in f:
        flag = re.search(f_id, f).group()[-38:-10]
    if "GET /sl" in f:
        if ' <Impression' in f:
            SI = r' <Impression.{0,130}/1</Impression>'
            DI = r' <Error>.{0,150}</Error>'
            FQ = r' <Tracking event="firstQuartile.{0,120}Tracking>'
            MP = r' <Tracking event="midpoint.{0,120}Tracking>'
            TQ = r' <Tracking event="thirdQuartile">.{0,120}Tracking>'
            C = r' <Tracking event="complete.{0,120}Tracking>'
            AE = r' <Tracking event="close">.{0,120}Tracking>'
        else:
            SI = r'<Impression.{0,130}/1</Impression>'
            DI = r'<Error>.{0,150}</Error>'
            FQ = r'<Tracking event="firstQuartile.{0,120}Tracking>'
            MP = r'<Tracking event="midpoint.{0,120}Tracking>'
            TQ = r'<Tracking event="thirdQuartile">.{0,120}Tracking>'
            C = r'<Tracking event="complete.{0,120}Tracking>'
            AE = r'<Tracking event="close">.{0,120}Tracking>'
    else:
        SI = r' <Impression>http://dai-.{0,130}/1</Impression>'
        DI = r'<Error>http://dai-.{0,150}</Error>'
        FQ = r' <Tracking event="firstQuartile">http://dai-.{0,120}Tracking>'
        MP = r' <Tracking event="midpoint">http://dai-.{0,120}Tracking>'
        TQ = r' <Tracking event="thirdQuartile">.{0,120}Tracking>'
        C = r' <Tracking event="complete">http://dai-.{0,120}Tracking>'
        AE = r' <Tracking event="close">http://dai-.{0,120}Tracking>'
    patDATE = r'(.{3},\s+\d+\s.{3}.{5}\s\d+:\d+)'
    patSiteS = r'(gmott_.{15,29})'
    Duration = r'<Duration>.{0,2}:.{0,2}:.{0,2}..{0,3}</Duration>'
    FillerP = r'(Ad id="filler_YO_)(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s.{0,44}'
    FillerPn = r'(Ad id="filler_YO_)(.*).(></Linear>)'
    if "B/sl" in f:
    	SIf = r'B/sl.{60,74}/1t'
        DIf = r'B/sl.{60,65}/1t'
        FQf = r'B/sl.{60,65}/4t'
        FQf1 = r'B/sl.{60,65}/6t'
        MPf = r'B/sl.{60,65}/5t'
        MPf1 = r'B/sl.{60,65}/7t'
        TQf = r'B/sl.{60,65}/6t'
        TQf1 = r'B/sl.{60,65}/8t'
        Cpf = r'B/sl.{60,65}/3t'
        Cpf1 = r'B/sl.{60,65}/5t'
        Apf = r'B/sl.{60,65}/2t'
    else:
    	SIf = r'GET /sl.{60,65}/1'
        DIf = r'GET /sl.{60,65}/1'
        FQf = r'GET /sl.{60,65}/4'
        FQf1 = r'GET /sl.{60,65}/6'
        MPf = r'GET /sl.{60,65}/5'
        MPf1 = r'GET /sl.{60,65}/7'
        TQf = r'GET /sl.{60,65}/6'
        TQf1 = r'GET /sl.{60,65}/8'
        Cpf = r'GET /sl.{60,65}/3'
        Cpf1 = r'GET /sl.{60,65}/5'
        Apf = r'GET /sl.{60,65}/2'
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
    ID = []
    Filler = []
    Fduration = []
    Aduration = []
    pDate = []
    pSites = []
    TP = []
    si1 = []
    if "Innovid Ads" in f:
        TP.append("Innovid Ads")
    if "googlesyndication" in f:
        TP.append('GoogleSyndication')
    for match in re.compile(ADID).finditer(f): Adl.append(match.group()[4:13])
    for match in re.compile(IDr).finditer(f): ID.append(match.group()[13:21])
    for match in re.finditer(patDATE, f): pDate.append(match.group())
    for match in re.finditer(patSiteS, f): pSites.append(match.group())
    for match in re.finditer(FillerP, f): Fduration.append(match.group()[-7:-3])
    for match in re.finditer(Duration, f): Aduration.append(match.group()[-19:-12])
    if len(Fduration) == 0:
        for match in re.finditer(FillerPn, f): Fduration.append(match.group()[-28:-22])
    if 'filler_YO' in f:
        Filler.append(Adl[-1])
        del Adl[-1]
        del Aduration[-1]
    ID.sort()
    ID = list(set(ID))
    ID.sort()
    if len(ID)-len(Adl)==1:
        si1.append(ID[-1])
        del ID[-1]
    if "B/sl" in f:
    	for match in re.compile(SI).finditer(f): Sl.append(match.group()[-51:-43])
        for match in re.compile(DI).finditer(f): Dl.append(match.group()[-46:-38])
        for match in re.compile(FQ).finditer(f): Fl.append(match.group()[-49:-41])
        for match in re.compile(MP).finditer(f): Ml.append(match.group()[-49:-41])
        for match in re.compile(TQ).finditer(f): Tl.append(match.group()[-49:-41])
        for match in re.compile(C).finditer(f): Cl.append(match.group()[-49:-41])
        if len(Cl) - len(Adl) == 1:
            del Cl[-1]
        for match in re.compile(AE).finditer(f): Al.append(match.group()[-50:-42])
        for match in re.compile(SIf).finditer(f): Sf.append(match.group()[-39:-31])
        for match in re.compile(DIf).finditer(f): Df.append(match.group()[-39:-31])
        for match in re.compile(FQf).finditer(f): Ff.append(match.group()[-39:-31])
        for match in re.compile(FQf1).finditer(f): Ff.append(match.group()[-39:-31])
        for match in re.compile(MPf).finditer(f): Mf.append(match.group()[-39:-31])
        for match in re.compile(MPf1).finditer(f): Mf.append(match.group()[-39:-31])
        for match in re.compile(TQf).finditer(f): Tf.append(match.group()[-39:-31])
        for match in re.compile(TQf1).finditer(f): Tf.append(match.group()[-39:-31])
        for match in re.compile(Cpf).finditer(f): Cf.append(match.group()[-39:-31])
        for match in re.compile(Cpf1).finditer(f): Cf.append(match.group()[-39:-31])
        for match in re.compile(Apf).finditer(f): Af.append(match.group()[-39:-31])
    else:
    	for match in re.compile(SI).finditer(f): Sl.append(match.group()[-51:-43])
        for match in re.compile(DI).finditer(f): Dl.append(match.group()[-46:-38])
        for match in re.compile(FQ).finditer(f): Fl.append(match.group()[-49:-41])
        for match in re.compile(MP).finditer(f): Ml.append(match.group()[-49:-41])
        for match in re.compile(TQ).finditer(f): Tl.append(match.group()[-49:-41])
        for match in re.compile(C).finditer(f): Cl.append(match.group()[-49:-41])
        if len(Cl) - len(Adl) == 1:
            del Cl[-1]
        for match in re.compile(AE).finditer(f): Al.append(match.group()[-50:-42])
        for match in re.compile(SIf).finditer(f): Sf.append(match.group()[-38:-30])
        for match in re.compile(DIf).finditer(f): Df.append(match.group()[-38:-30])
        for match in re.compile(FQf).finditer(f): Ff.append(match.group()[-38:-30])
        for match in re.compile(FQf1).finditer(f): Ff.append(match.group()[-38:-30])
        for match in re.compile(MPf).finditer(f): Mf.append(match.group()[-38:-30])
        for match in re.compile(MPf1).finditer(f): Mf.append(match.group()[-38:-30])
        for match in re.compile(TQf).finditer(f): Tf.append(match.group()[-38:-30])
        for match in re.compile(TQf1).finditer(f): Tf.append(match.group()[-38:-30])
        for match in re.compile(Cpf).finditer(f): Cf.append(match.group()[-38:-30])
        for match in re.compile(Cpf1).finditer(f): Cf.append(match.group()[-38:-30])
        for match in re.compile(Apf).finditer(f): Af.append(match.group()[-38:-30])
    Ff.sort()
    Ff = list(set(Ff))
    Ff.sort()
    Mf.sort()
    Mf = list(set(Mf))
    Mf.sort()
    Tf.sort()
    Tf = list(set(Tf))
    Tf.sort()
    Cf.sort()
    Cf = list(set(Cf))
    Cf.sort()
    Sf = [z if z in Sf else "none" for z in Sl]
    Af = [z if z in Af else "none" for z in Al]
    if len(Dl)<len(Al):
        Dl = [z if z in Dl else z for z in Al]
    Df = [z if z in Df else "none" for z in Al]
    Ff = [z if z in Ff else "none" for z in Fl]
    Mf = [z if z in Mf else "none" for z in Ml]
    Tf = [z if z in Tf else "none" for z in Tl]
    Cf = [z if z in Cf else "none" for z in Cl]
    if Sl[0]==Sf[0]:
        si = x
    else:
        si = y
    if Al[0]==Af[0]:
        ae = x
    else:
        ae = y
    for i in range(len(Al)):
        if Df[i] in Al:
            Dr.append(x)
        else:
            Dr.append(y)
    for i in range(len(Fl)):
        if Ff[i] in Fl:
            Fr.append(x)
        else:
            Fr.append(y)
    for i in range(len(Ml)):
        if Mf[i] in Ml:
            Mr.append(x)
        else:
            Mr.append(y)
    for i in range(len(Tl)):
        if Tf[i] in Tl:
            Tr.append(x)
        else:
            Tr.append(y)
    for i in range(len(Cl)):
        if Cf[i] in Cl:
            Cr.append(x)
        else:
            Cr.append(y)

# # Profile
    if "prof=372496:dfw_ios_mobile_mm" in f:
        pProf = '372496:dfw_ios_mobile_mm'
    elif "prof=372496:dfw_ios_tablet_mm" in f:
        pProf = "372496:dfw_ios_tablet_mm"
    elif "prof=372496:dfw_android_tablet_mm" in f:
        pProf = "372496:dfw_android_tablet_mm"
    elif "prof=372496:dfw_android_mobile_mm" in f:
        pProf = "372496:dfw_android_mm"
    elif "prof=372496:dfw_desktop_mm" in f:
        pProf = "372496:dfw_desktop_mm"
    elif "prof=372496:dfw_tvos_mm" in f:
        pProf = "372496:dfw_tvos_mm"
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
    print "<img src='/img/attlogo.png' HEIGHT=100 WIDTH=380 ALIGN=left>"
    print "<h1 id=Report ALIGN=left> AUTOMATION REPORT LIVE TV </h1>"
    print "<br>"
    print "<table id=Report>"
    print "<tr>"
    print "<th align = center>&nbsp&nbsp&nbsp&nbsp DAY / TIME  : </th>"
    print "<td>" + time.strftime("%d/%m/%Y") + "     " + time.strftime("%I:%M %p") + "</td>"
    print "</tr>"
    print "<tr>"
    print "<table style=width:1050px border='1'>"
    print "</tr>"
    print "<br>"
    print "<tr>"
    if "Safari" in f and "Chrome" not in f:
        device = "<img src='/img/safari.png' HEIGHT=40 WIDTH=40 ALIGN=right>"
    elif "Chrome" in f:
        device = "<img src='/img/chrome.png' HEIGHT=38 WIDTH=38 ALIGN=right>"
    elif "ios_mobile" in f:
        device = "<img src='/img/iphone.png' HEIGHT=40 WIDTH=80 ALIGN=right>"
    elif "ios_tablet" in f:
        device = "<img src='/img/ipad.png' HEIGHT=40 WIDTH=60 ALIGN=right>"
    elif "tvos" in f:
        device = "<img src='/img/tvos.png' HEIGHT=40 WIDTH=60 ALIGN=right>"
    elif "android_" in f:
        device = "<img src='/img/android.png' HEIGHT=40 WIDTH=80 ALIGN=right>"
    else:
        device =''
    if len(pDate[2])>0:
        print "<th align = left>" + "Date / Time DAI" + "</th><th>" + pDate[2] + "</th><tr>"
    elif pDate[1]>0:
        print "<th align = left>" + "Date / Time DAI" + "</th><th>" + pDate[1] + "</th><tr>"
    else:
        print "<th align = left>" + "Date / Time DAI" + "</th><th>" + time.strftime("%d/%m/%Y") + "     " + time.strftime("%I:%M %p") + "</th><tr>"

    if "prof" in f:
        print "<th align = left>" + "Profile" + "</th><th>" + pProf + device + "</th><tr>"
    else:
        print
    if "live_SEC" in f:
    	channel= "<img src='/img/sec.png' HEIGHT=30 WIDTH=90 ALIGN=right>"
    elif "live_ESPNU" in f:
        channel="<img src='/img/espnu.png' HEIGHT=30 WIDTH=40 ALIGN=right>"
    elif "live_ESPNews" in f:
        channel="<img src='/img/espnews.png' HEIGHT=20 WIDTH=130 ALIGN=right>"
    else:
        channel=""
    if "AdBreakResolutionManager" in f:
        if 'csid=gmott_desktop_watch_live_SEC' in f:
            csid = x
            csidn = 'gmott_desktop_watch_live_SEC'
        elif 'csid=gmott_desktop_watch_live_ESPNU' in f:
            csid = x
            csidn = 'gmott_desktop_watch_live_ESPNU'
        elif 'csid=gmott_desktop_watch_live_ESPNews' in f:
            csid = x
            csidn = 'gmott_desktop_watch_live_ESPNews'
        elif 'gmott_ios_mobile_watch_live_SEC' in f:
            csid = x
            csidn = 'gmott_ios_mobile_watch_live_SEC'
        elif 'gmott_ios_mobile_watch_live_ESPNU' in f:
            csid = x
            csidn = 'gmott_ios_mobile_watch_live_ESPNU'
        elif 'gmott_ios_mobile_watch_live_ESPNews' in f:
            csid = x
            csidn = 'gmott_ios_mobile_watch_live_ESPNews'
        elif 'csid=gmott_android_watch_live_SEC' in f:
            csid = x
            csidn = 'gmott_android_watch_live_SEC'
        elif 'csid=gmott_android_watch_live_ESPNU' in f:
            csid = x
            csidn = 'gmott_android_watch_live_ESPNU'
        elif 'csid=gmott_android_watch_live_ESPNews' in f:
            csid = x
            csidn = 'gmott_android_watch_live_ESPNews'
        elif 'csid=gmott_android_tablet_watch_live_SEC' in f:
            csid = x
            csidn = 'gmott_android_tablet_watch_live_SEC'
        elif 'csid=gmott_android_tablet_watch_live_ESPNU' in f:
            csid = x
            csidn = 'gmott_android_tablet_watch_live_ESPNU'
        elif 'csid=gmott_android_tablet_watch_live_ESPNews' in f:
            csid = x
            csidn = 'gmott_android_tablet_watch_live_ESPNews'
        elif 'csid=gmott_ios_tablet_watch_live-SEC' in f:
            csid = x
            csidn = 'gmott_ios_tablet_watch_live_SEC'
        elif 'csid=gmott_ios_tablet_watch_live_SEC' in f:
            csid = x
            csidn = 'gmott_ios_tablet_watch_live_SEC'
        elif 'csid=gmott_ios_tablet_watch_live_ESPNU' in f:
            csid = x
            csidn = 'gmott_ios_tablet_watch_live_ESPNU'
        elif 'csid=gmott_ios_tablet_watch_live_ESPNews' in f:
            csid = x
            csidn = 'gmott_ios_tablet_watch_live_ESPNews'
        elif 'gmott_tvos_watch_live_ESPNews' in f:
            csid = x
            csidn = 'gmott_tvos_watch_live_ESPNews'
        elif 'gmott_tvos_watch_live_ESPNU' in f:
            csid = x
            csidn = 'gmott_tvos_watch_live_ESPNU'
        elif 'gmott_tvos_watch_live_SEC' in f:
            csid = x
            csidn = 'gmott_tvos_watch_live_SEC'
        else:
            csid = y
            csidn = ''
        print "<th align = left>" + "Site Section" + "</th><th>" + csidn + channel + "</th><tr>"
    else:
        print
    if 'filler_YO' in f:
        print  "<th align=left>"+"Filler"+"</th><th>"+"ID:"+"&nbsp"+str(Filler[0])+"&nbsp"+"&nbsp"+"&nbsp"+"Duration:"+"&nbsp"+str(Fduration[0])+"&nbsp"+"sec"+"</th><tr>"
    # for i in range(len(TP)):
    if len(TP)>0:
            # TPr = TP[i]
        print  "<th align=left>" + "Third Party AD" + "</th><th>" + str(TP) + "</th><tr>"
        # print TP
    print  "<th align = left>" + "Slot Impression" +si+ "</th><th>" + "Ad Slot end"+ae + "</th><tr>"
    print  "<th align = left>" + "<a href=" + pathl + ">Log file</a>" + "</th><tr>"
    print "</tr>"
    print "</table>"
    print "</body>"
    print "<br>"
    print "<table id=Report>"
    print "<tr>"
    print "<table style=width:1050px border='1'>"
    print "</tr>"
    print "<tr>"
    print "<th>" + 'AD ID, total:' + str(len(Adl)) + "</th>"
    print "<th>Duration</th>"
    print "<th>Default Impression</th>"
    print "<th>First Quartile</th>"
    print "<th>Midpoint Quartile</th>"
    print "<th>Third Quartile</th>"
    print "<th>Complete</th>"
    print "</tr>"
    print "<tr>"
    #
    index = 0
    for index in range(len(ID)):
        for di in range(index, len(Dr)):
            for fq in range(index, len(Fr)):
                for mq in range(index, len(Mr)):
                    for tq in range(index, len(Tr)):
                        for c in range(index, len(Cr)):
                            # for fc in range(index, len(Cl)):
                            for cc in range(index, len(Aduration)):
                                break
        print "<tr>"
        print "<td>" + ID[index]+ "</td"
        print "</tr>"
        print  "<td align = center>" + Aduration[index] + "</td>"
        print  "<td align = center>" + Dr[index] + "</td>"
        print  "<td align = center>" + Fr[index] + "</td>"
        print  "<td align = center>" + Mr[index] + "</td>"
        print  "<td align = center>" + Tr[index] + "</td>"
        print  "<td align = center>" + Cr[index] + "</td>"
    print "</table>"
    print "</body>"
    print "<br>"
    # # validation Ad request parameters for DAI Live
    maxdp = r'&maxd=....'
    maxdr = []
    for match in re.finditer(maxdp, f): maxdr.append(match.group()[-4:-1])
    if len(maxdr) == 0:
        maxdr.append("Not found")
    mindp = r'&mind=....'
    mindr = []
    for match in re.finditer(mindp, f): mindr.append(match.group()[-4:-1])
    if len(mindr) == 0:
        mindr.append("Not found")
    nwp = r'&nw=.*&mo'
    nwr = []
    for match in re.finditer(nwp, f): nwr.append(match.group()[-9:-3])
    if len(nwr) == 0:
        nwr.append("Not found")
    ssnwp = r'&ssnw=.*&vi'
    ssnwr = []
    for match in re.finditer(ssnwp, f): ssnwr.append(match.group()[-9:-3])
    metrp = r'&metr=.*&p'
    metrr = []
    for match in re.finditer(metrp, f): metrr.append(match.group()[-7:-2])
    asnwp = r'&asnw=.*&cs'
    asnwr = []
    for match in re.finditer(asnwp, f): asnwr.append(match.group()[-8:-3])
    vdurp = r'&vdur=.*&ca'
    vdurr = []
    for match in re.finditer(vdurp, f): vdurr.append(match.group()[-7:-3])
    if len(vdurr) == 0:
        vdurr.append("Not found")
    vipp = r'&vip=.*&re'
    vipr = []
    for match in re.finditer(vipp, f): vipr.append(match.group()[-16:-3])
    clientIpp = r', clientIp=.*, user'
    clientIpr = []
    for match in re.finditer(clientIpp, f): clientIpr.append(match.group()[-19:-6])
    pvrnp = r'&pvrn=.*&vp'
    pvrnr = []
    for match in re.finditer(pvrnp, f): pvrnr.append(match.group()[5:15])
    vprnp = r'&vprn=.*&vc'
    vprnr = []
    for match in re.finditer(vprnp, f): vprnr.append(match.group()[5:15])
    vcidp = r' vcid=.*==;'
    vcidr = []
    for match in re.finditer(vcidp, f): vcidr.append(match.group()[5:32])
    if len(vcidr) == 0:
        vcidr.append("Not found")
    modep = r'&mode=.*&vd'
    moder = []
    for match in re.finditer(modep, f): moder.append(match.group()[-8:-3])
    csidp = r'&csid=.*&ss'
    csidr = []
    for match in re.finditer(csidp, f): csidr.append(match.group()[-30:-3])
    respp = r'&resp=.*&me'
    respr = []
    for match in re.finditer(respp, f): respr.append(match.group()[-9:-3])
    if len(respr) == 0:
        respr.append("Not found")
    ptgtp = r';ptgt=.*&slau='
    ptgtr = []
    for match in re.finditer(ptgtp, f): ptgtr.append(match.group()[-8:-6])
    slaup = r'&slau=.*&sl'  # &&slau=midroll&sl
    slaur = []
    for match in re.finditer(slaup, f): slaur.append(match.group()[-11:-3])
    slidp = r'&slid=.*&cp'  # &slid=midroll1&cp
    slidr = []
    for match in re.finditer(slidp, f): slidr.append(match.group()[-12:-3])
    cpsqp = r'&cpsq=.*&maxd='
    cpsqr = []
    for match in re.finditer(cpsqp, f): cpsqr.append(match.group()[-8:-6])
    hhidp = r' hhid=.*==,'
    hhidr = []
    for match in re.finditer(hhidp, f): hhidr.append(match.group()[5:32])
    if len(hhidr) == 0:
        hhidr.append("Not found")
    attnidp = r'&attnid=.*3D'
    attnidpn = r'&attnid=.(.*).isLive'
    attnidr = []
    for match in re.finditer(attnidp, f): attnidr.append(match.group()[7:14])
    if len(attnidr) == 0:
        for match in re.finditer(attnidpn, f): attnidr.append(match.group()[7:14])
        if len(attnidr) == 0:
            attnidr.append("=Not found")
    comscore_platformp = r'&comscore_platform=.*&com'
    comscore_platformr = []
    if 'comscore_platform=PC' in f:
        comscore_platformr.append('=PC')
    elif 'comscore_platform=ios' in f:
        comscore_platformr.append('=ios')
    elif 'comscore_platform=android' in f:
        comscore_platformr.append('=android')
    else:
        comscore_platformr.append('')
    comscore_devicep = r'&comscore_device=.*&nielsen'  # &comscore_device=iPad6%2C11&n
    comscore_devicer = []
    if 'comscore_device=OS+X' in f:
        comscore_devicer.append('=OS+X')
    elif 'comscore_device=iPhone' in f:
        comscore_devicer.append('=iPhone')
    elif 'comscore_device=iPad' in f:
        comscore_devicer.append('=iPad')
    elif 'comscore_device=Android' in f:
        comscore_devicer.append('=Android')
    elif 'comscore_device=AppleTV' in f:
        comscore_devicer.append('=AplleTV')
    else:
        comscore_devicer.append('')
    nielsen_dev_groupp = r'&nielsen_dev_group=.*&nie'  # &nielsen_dev_group=devgrp%2CTAB&nie
    nielsen_dev_groupr = []
    for match in re.finditer(nielsen_dev_groupp, f): nielsen_dev_groupr.append(match.group()[-7:-4])
    nielsen_platformp = r'&nielsen_platform=.*&_fw'  # &nielsen_platform=plt%2CMBL&_fw
    nielsen_platformr = []
    for match in re.finditer(nielsen_platformp, f): nielsen_platformr.append(match.group()[-7:-4])
    fw_nielsen_app_idp = r'&_fw_nielsen_app_id=.*;ptgt'  # &_fw_nielsen_app_id=P7CFE36DB-A8D9-4801-95FE-51C29101342C;ptgt
    fw_nielsen_app_idr = []
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
    if 'caid=a110250794' in f:
        caid = x
        caidr = 'caid=a110250794'
    elif 'caid=a110110608' in f:
        caid = x
        caidr = 'caid=a110110608'
    elif 'caid=a19762660' in f:
        caid = x
        caidr = 'caid=a19762660'
    elif 'caid=a110304965' in f:
        caid = x
        caidr = 'caid=a110304965'
    elif 'caid=a110111948' in f:
        caid = x
        caidr = 'caid=a110111948'
    elif 'caid=a110104545' in f:
        caid = x
        caidr = 'caid=a110104545'
    elif 'caid=a110061062' in f:
        caid = x
        caidr = 'caid=a110061062'
    elif 'caid=a110232111' in f:
        caid = x
        caidr = 'caid=a110232111'
    elif 'caid=a110290054' in f:
        caid = x
        caidr = 'caid=a110290054'
    elif 'caid=a1' in f:
        caid = x
        caidr = 'caid=a110'
    else:
        caid = y
        caidr = ''
    if 'asnw=87146' in f:
        asnw = x
    else:
        asnw = y
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
        respr = 'vmap1'
    else:
        resp = y
        respr = ''
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
    if 'comscore_impl_type=b' in f:
        comscore_impl_type = x
        comscore_impl_typer = 'comscore_impl_type=b'
    else:
        comscore_impl_type = y
        comscore_impl_typer = ''
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
    elif 'comscore_device=OS' in f:
        comscore_device = x
    elif 'comscore_device=AppleTV' in f:
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
        for match in re.finditer(fw_nielsen_app_idp, f): fw_nielsen_app_idr.append(match.group()[-43:-5])
    else:
        fw_nielsen_app_id = y
        for match in re.finditer(fw_nielsen_app_idp, f): fw_nielsen_app_idr.append(match.group()[-21:-5])
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
    if maxdr[:1] == [0, 9]:
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
    if 'AdBreakResolutionManager' in f:
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
        print    "<tr>""<td>" + sltp + "sltp""</td>""<td>" + maxd + "maxd=" + str(
            maxdr[-2]) + "</td>""<td>" + vcid + "vcid" + str(vcidr[-1]) + "</td>""<td>" + resp + "resp" + respr + "</td>""<td>" + caid + "caid" + caidr + "</td>""<td>" + comscore_impl_type + "comscore_impl_type"+comscore_impl_typer + "</td>""</tr>"
        print    "<tr>""<td>" + slcb + "slcb" + "</td>""<td>" + mind + "mind=" + str(
            mindr[-2]) + "</td>""<td>" + hhid + "hhid" + str(hhidr[-1]) + "</td>""<td>" + nw + "nw=" + str(
            nwr[-1]) + "</td>""<td>" + clientIp + "clientIp" + str(
            clientIpr[-1]) + "</td>""<td>" + comscore_platform + "comscore_platform" + str(
            comscore_platformr[-1]) + "</td>""</tr>"
        print    "<tr>""<td>" + amcb + "amcb""</td>""<td>" + vdur + "vdur" + str(
            vdurr[-1]) + "</td>""<td>" + attnid + "attnid" + str(attnidr[-1]) + "</td>""<td>" + asnw + "asnw=" + str(
            asnwr[-1]) + "</td>""<td>" + vip + "vip" + str(
            vipr[-1]) + "</td>""<td>" + comscore_device + "comscore_device" + str(comscore_devicer[-1]) + "</td>""</tr>"
        print    "<tr>""<td>" + aeti + "aeti" + "</td>""<td>" + cpsq + "cpsq" + str(
            cpsqr[-2]) + "</td>""<td>" + csid + "csid=" + csidn + "</td>""<td>" + metr + "metr" + str(
            metrr[-1]) + "</td>""<td>" + ssnw + "ssnw=" + str(
            ssnwr[-1]) + "</td>""<td>" + nielsen_dev_group + "nielsen_dev_group=devgrp," + str(
            nielsen_dev_groupr[-1]) + "</td>""</tr>"
        print    "<tr>""<td>" + emcr + "emcr" + "</td>""<td>" + mode + "mode" + str(
            moder[-1]) + "</td>""<td>" + "</td>""<td>" + slid + "slid" + str(
            slidr[-3]) + "</td>""<td>" + pvrn + "pvrn" + str(
            pvrnr[-3]) + "</td>""<td>" + nielsen_platform + "nielsen_platform=plt," + str(nielsen_platformr[-1]) + "</td>""</tr>"
        print    "<tr>""<td>" + exvt + "exvt" + "</td>""<td>" + ptgt + "ptgt" + str(
            ptgtr[-1]) + "</td>""<td>" + "</td>""<td>" + slau + "slau" + str(
            slaur[-1]) + "</td>""<td>" + vprn + "vprn" + str(
            vprnr[-3]) + "</td>""<td>" + fw_nielsen_app_id + "fw_nielsen_app_id" + str(
            fw_nielsen_app_idr[-1]) + "</td>""</tr>"
        print "</table>"
        print "</body>"
        print "</html>"
        print "</table>"
        print "</body>"
        print "</html>"
    else:
        print
	continue
 for i in range(len(wtxt)):
     f = open(pathR + wtxt[i], 'r').read()
     sys.stdout = open(pathR + wtxt[i] + ".html", 'w')
     Adl = []
     Sl = []
     Dl = []
     Dl2 = []
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
     Aduration = []
     pDate = []
     ID = []
     ADID = r'_YO_.{24}'
     patDATE = r'Date:.{20,23}'
     Duration = r'Duration.{0,30}'
     FillerP = r'(Ad id="filler_YO_)(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\s.{0,44}'
     FillerPn = r'(filler_YO_)(.*).&lt;/Duration'
     IDr = ur'/BeaconProxy/.{5,8}-'
     SI = r';Impression.{100,110}/1'
     DI = r';Error.{100,110}/2'
     DI2 = r';Error.{100,110}/4'
     FQ = r';Tracking event=&quot;firstQuartile.{100,112}/'
     MP = r';Tracking event=&quot;midpoint.{100,112}/'
     TQ = r';Tracking event=&quot;thirdQuartile.{100,112}/'
     C = r';Tracking event=&quot;complete.{100,112}/'
     AE = r';Tracking event=&quot;close.{100,112}'
     SIf = r'GET /sl.{60,65}/1'
     DIf = r'GET /sl.{60,65}/1'
     FQf = r'GET /sl.{60,65}/4'
     FQf2 = r'GET /sl.{60,65}/6'
     MPf = r'GET /sl.{60,65}/5'
     MPf2 = r'GET /sl.{60,65}/7'
     TQf = r'GET /sl.{60,65}/6'
     TQf2 = r'GET /sl.{60,65}/8'
     Cpf = r'GET /sl.{60,65}/3'
     Cpf2 = r'GET /sl.{60,65}/5'
     Apf = r'GET /sl.{60,65}/2'
     for match in re.compile(ADID).finditer(f): Adl.append(match.group()[4:13])
     for match in re.finditer(patDATE, f): pDate.append(match.group()[6:28])
     for match in re.finditer(FillerP, f): Fduration.append(match.group()[-7:-3])
     for match in re.compile(Duration).finditer(f): Aduration.append(match.group()[15:23])
     for match in re.compile(IDr).finditer(f): ID.append(match.group()[13:21])
     if len(Fduration) == 0:
         for match in re.finditer(FillerPn, f): Fduration.append(match.group()[-22:-17])
     if 'filler_YO' in f:
         Filler.append(Adl[-1])
         del Adl[-1]
         del Aduration[-1]
     for match in re.compile(SI).finditer(f): Sl.append(match.group()[-38:-30])
     for match in re.compile(DI).finditer(f): Dl.append(match.group()[-38:-30])
     for match in re.compile(DI2).finditer(f): Dl2.append(match.group()[-38:-30])
     for match in re.compile(FQ).finditer(f): Fl.append(match.group()[-37:-29])
     for match in re.compile(MP).finditer(f): Ml.append(match.group()[-37:-29])
     for match in re.compile(TQ).finditer(f): Tl.append(match.group()[-37:-29])
     for match in re.compile(C).finditer(f): Cl.append(match.group()[-37:-29])
     if len(Cl) - len(Adl) == 1:
         del Cl[-1]
     for match in re.compile(AE).finditer(f): Al.append(match.group()[-36:-28])
     for match in re.compile(SIf).finditer(f): Sf.append(match.group()[-38:-30])
     for match in re.compile(DIf).finditer(f): Df.append(match.group()[-38:-30])
     for match in re.compile(FQf).finditer(f): Ff.append(match.group()[-38:-30])
     for match in re.compile(FQf2).finditer(f): Ff.append(match.group()[-38:-30])
     for match in re.compile(MPf).finditer(f): Mf.append(match.group()[-38:-30])
     for match in re.compile(MPf2).finditer(f): Mf.append(match.group()[-38:-30])
     for match in re.compile(TQf).finditer(f): Tf.append(match.group()[-38:-30])
     for match in re.compile(TQf2).finditer(f): Tf.append(match.group()[-38:-30])
     for match in re.compile(Cpf).finditer(f): Cf.append(match.group()[-38:-30])
     for match in re.compile(Cpf2).finditer(f): Cf.append(match.group()[-38:-30])
     for match in re.compile(Apf).finditer(f): Af.append(match.group()[-38:-30])
     ID.sort()
     ID = list(set(ID))
     ID.sort()
     Ff.sort()
     Ff = list(set(Ff))
     Ff.sort()
     Mf.sort()
     Mf = list(set(Mf))
     Mf.sort()
     Tf.sort()
     Tf = list(set(Tf))
     Tf.sort()
     Cf.sort()
     Cf = list(set(Cf))
     Cf.sort()
     si1 = []
     if len(ID)-len(Adl)==1:
         si1.append(ID[-1])
         del ID[-1]
     # if si1[0] in Sl:
     #     Sl.remove(si1[0])
     else:
         print
     Af = [z if z in Af else "none" for z in Al]
     # if len(Dl) < len(Al):
     #     Dl = [z if z in Dl else z for z in Al]
     Df = [z if z in Df else "none" for z in ID]
     Ff = [z if z in Ff else "none" for z in ID]
     Mf = [z if z in Mf else "none" for z in ID]
     Tf = [z if z in Tf else "none" for z in ID]
     Tl = [z if z in Tl else "none" for z in ID]
     Cf = [z if z in Cf else "none" for z in ID]
     # Sf = list(set(ID))
     # Sf.sort()
     # Df = list(set(Df))
     # Df.sort()
     # Ff = list(set(Ff))
     # Ff.sort()
     # Fl = list(set(Fl))
     # Fl.sort()
     # Mf = list(set(Mf))
     # Mf.sort()
     # Tf = list(set(Tf))
     # Tf.sort()
     # Cf = list(set(Cf))
     # Cf.sort()
     # Af = list(set(Af))
     # Af.sort()
     if si1[0]>0:
         si = x
     else:
         si = y
     if Af[0]>0:
         if Al[0]==Af[0]:
             ae = x
         else:
             ae = y
     for i in range(len(ID)):
         if Df[i] in ID:
             Dr.append(x)
         else:
             Dr.append(y)
     for i in range(len(ID)):
         if Ff[i] in ID:
             Fr.append(x)
         else:
             Fr.append(y)
     for i in range(len(ID)):
         if Mf[i] in ID:
             Mr.append(x)
         else:
             Mr.append(y)
     for i in range(len(ID)):
         if Tf[i] in ID:
             Tr.append(x)
         else:
             Tr.append(y)
     for i in range(len(ID)):
         if Cf[i] in ID:
             Cr.append(x)
         else:
             Cr.append(y)

     # print Fduration
     # print len(Fl)
     # print Sl
     # print ae
     # print si1
     # print si

     # print Df
     # print Ff
     # print Ff
     # print Mf
     # print Tf
     # print Fl
     # print Ff
     # print Af

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
     print "<img src='/img/attlogo.png' HEIGHT=100 WIDTH=380 ALIGN=left>"
     print "<h1 id=Report ALIGN=left> AUTOMATION REPORT LIVE TV </h1>"
     print "<br>"
     print "<table id=Report>"
     print "<tr>"
     print "<th align = center>&nbsp&nbsp&nbsp&nbsp DAY / TIME  : </th>"
     print "<td>" + time.strftime("%d/%m/%Y") + "     " + time.strftime("%I:%M %p") + "</td>"
     print "</tr>"
     print "<tr>"
     print "<table style=width:1050px border='1'>"
     print "</tr>"
     print "<br>"
     print "<tr>"
     if len(pDate) > 0:
         print "<th align = left>" + "Date / Time DAI" + "</th><th>" + pDate[0] + "</th><tr>"
     if "372496" in f:
         print "<th align = left>" + "Profile" + "</th><th>" + "372496" + "</th><tr>"
     else:
         print
     if "live_SEC" in f:
         channel = "<img src='/img/sec.png' HEIGHT=30 WIDTH=90 ALIGN=right>"
     elif "live_ESPNU" in f:
         channel = "<img src='/img/espnu.png' HEIGHT=30 WIDTH=40 ALIGN=right>"
     elif "live_ESPNews" in f:
         channel = "<img src='/img/espnews.png' HEIGHT=20 WIDTH=130 ALIGN=right>"
     else:
         channel = ""
     if 'fire' or 'Fire' in f:
         print "<th align = left>" + "Device" + "</th><th>" + "FireTv" + "</th><tr>"
     elif 'roku' or "Roku" in f:
         print "<th align = left>" + "Device" + "</th><th>" + "Roku" + "</th><tr>"
     else:
         print
     if "AdBreakResolutionManager" in f:
         if 'csid=gmott_desktop_watch_live_SEC' in f:
             csid = x
             csidn = 'gmott_desktop_watch_live_SEC'
         elif 'csid=gmott_desktop_watch_live_ESPNU' in f:
             csid = x
             csidn = 'gmott_desktop_watch_live_ESPNU'
         elif 'csid=gmott_desktop_watch_live_ESPNews' in f:
             csid = x
             csidn = 'gmott_desktop_watch_live_ESPNews'
         elif 'gmott_ios_mobile_watch_live_SEC' in f:
             csid = x
             csidn = 'gmott_ios_mobile_watch_live_SEC'
         elif 'gmott_ios_mobile_watch_live_ESPNU' in f:
             csid = x
             csidn = 'gmott_ios_mobile_watch_live_ESPNU'
         elif 'gmott_ios_mobile_watch_live_ESPNews' in f:
             csid = x
             csidn = 'gmott_ios_mobile_watch_live_ESPNews'
         elif 'csid=gmott_android_watch_live_SEC' in f:
             csid = x
             csidn = 'gmott_android_watch_live_SEC'
         elif 'csid=gmott_android_watch_live_ESPNU' in f:
             csid = x
             csidn = 'gmott_android_watch_live_ESPNU'
         elif 'csid=gmott_android_watch_live_ESPNews' in f:
             csid = x
             csidn = 'gmott_android_watch_live_ESPNews'
         elif 'csid=gmott_android_tablet_watch_live_SEC' in f:
             csid = x
             csidn = 'gmott_android_tablet_watch_live_SEC'
         elif 'csid=gmott_android_tablet_watch_live_ESPNU' in f:
             csid = x
             csidn = 'gmott_android_tablet_watch_live_ESPNU'
         elif 'csid=gmott_android_tablet_watch_live_ESPNews' in f:
             csid = x
             csidn = 'gmott_android_tablet_watch_live_ESPNews'
         elif 'csid=gmott_ios_tablet_watch_live-SEC' in f:
             csid = x
             csidn = 'gmott_ios_tablet_watch_live_SEC'
         elif 'csid=gmott_ios_tablet_watch_live_SEC' in f:
             csid = x
             csidn = 'gmott_ios_tablet_watch_live_SEC'
         elif 'csid=gmott_ios_tablet_watch_live_ESPNU' in f:
             csid = x
             csidn = 'gmott_ios_tablet_watch_live_ESPNU'
         elif 'csid=gmott_ios_tablet_watch_live_ESPNews' in f:
             csid = x
             csidn = 'gmott_ios_tablet_watch_live_ESPNews'
         elif 'gmott' in f:
             csid = x
             csidn = 'gmott'
             print "<th align = left>" + "Site Section" + "</th><th>" + csidn + "</th><tr>"
         else:
             csid = y
             csidn = None
     if 'filler_YO' in f:
         print  "<th align = left>" + "Filler" + "</th><th>" + "ID:" + "&nbsp" + str(
             Filler[0]) + "&nbsp" + "&nbsp" + "&nbsp" + "Duration:" + "&nbsp" + str(
             Fduration[0]) + "&nbsp" + "sec" + "</th><tr>"
     if 'Innovid Ads<' in f:
         print  "<th align = left>" + "Third Party AD" + "</th><th>" + "Innovid Ads" + "</th><tr>"
     print  "<th align = left>" + "Slot Impression" +si+ "</th><th>" + "Ad Slot end"+ae + "</th><tr>"
     print  "<th align = left>" + "<a href="+pathl+">Log file</a>" +"</th><tr>"
     print "</tr>"
     print "</table>"
     print "</body>"
     print "<br>"
     print "<table id=Report>"
     print "<tr>"
     print "<table style=width:1050px border='1'>"
     print "</tr>"
     print "<tr>"
     print "<th>" + 'AD ID, total:' + str(len(Adl)) + "</th>"
     print "<th>Duration</th>"
     print "<th>Default Impression</th>"
     print "<th>First Quartile</th>"
     print "<th>Midpoint Quartile</th>"
     print "<th>Third Quartile</th>"
     print "<th>Complete</th>"
     print "</tr>"
     print "<tr>"
     #
     index = 0
     for index in range(len(ID)):
         for di in range(index, len(Dr)):
             for fq in range(index, len(Fr)):
                 for mq in range(index, len(Mr)):
                     for tq in range(index, len(Tr)):
                         for c in range(index, len(Cr)):
                             for cc in range(index, len(Aduration)):
                                 break
         print "<tr>"
         print "<td>" + ID[index]+ "</td"
         print "</tr>"
         print  "<td align = center>" + Aduration[index] + "</td>"
         print  "<td align = center>" + Dr[index] + "</td>"
         print  "<td align = center>" + Fr[index] + "</td>"
         print  "<td align = center>" + Mr[index] + "</td>"
         print  "<td align = center>" + Tr[index] + "</td>"
         print  "<td align = center>" + Cr[index] + "</td>"
     print "</table>"
     print "</body>"
     print "<br>"
     # # validation Ad request parameters for DAI Live
     hhidp = r'hhid=.*==&' # hhid=1/IeUAPXQJok3jGPc/9w+g==
     hhidr = []
     for match in re.finditer(hhidp, f): hhidr.append(match.group()[4:27])
     if len(hhidr) == 0:
         hhidr.append("Not found")
     comscore_devicep = r'&comscore_device=.*&com'  # &comscore_device=iPad6%2C11&n
     comscore_devicer = []
     if 'comscore_device=OS+X' in f:
         comscore_devicer.append('=OS+X')
     elif 'comscore_device=iPhone' in f:
         comscore_devicer.append('=iPhone')
     elif 'comscore_device=iPad' in f:
         comscore_devicer.append('=iPad')
     elif 'comscore_device=Android_Amazon_AFTS' in f:
         comscore_devicer.append('=Android_Amazon_AFTS')
     elif 'comscore_device=Android' in f:
         comscore_devicer.append('=Android')
     else:
         comscore_devicer.append('')
     nielsen_dev_groupp = r'&nielsen_dev_group=.*&_f'  # &nielsen_dev_group=devgrp%2CTAB&nie
     nielsen_dev_groupr = []
     for match in re.finditer(nielsen_dev_groupp, f): nielsen_dev_groupr.append(match.group()[-7:-4])
     #
     if 'prof=372496:dfw_' in f:
         prof = x
     else:
         prof = y
     if 'comscore_impl_type=a' in f:
         comscore_impl_type = x
         comscoreIT = 'comscore_impl_type=a'
     else:
         comscore_impl_type = y
         comscoreIT =''
     if 'comscore_platform=android' in f:
         comscore_platform = x
         comscoreP = 'comscore_platform=android'
     else:
         comscore_platform = y
         comscoreP = ''
     if 'comscore_device=Windows+Server+2008+R2+%2F+7' in f:
         comscore_device = x
     elif 'comscore_device=iPhone' in f:
         comscore_device = x
     elif 'comscore_device=Android_' in f:
         comscore_device = x
     elif 'comscore_device=iPad' in f:
         comscore_device = x
     elif 'comscore_device=OS' in f:
         comscore_device = x
     else:
         comscore_device = y
     if 'nielsen_dev_group=devgrp%2' in f:
         nielsen_dev_group = x
     elif 'nielsen_dev_group=devgrp,AMN' in f:
         nielsen_dev_group = x
         ndg = 'nielsen_dev_group=devgrp,AMN'
     else:
         nielsen_dev_group = y
     if 'nielsen_platform=plt%2CDSK' in f:
         nielsen_platform = x
     elif 'nielsen_platform=plt%2CMBL' in f:
         nielsen_platform = x
     elif 'nielsen_platform=plt,OTT' in f:
         nielsen_platform = x
         np = 'nielsen_platform=plt,OTT'
     else:
         nielsen_platform = y
     if 'fw_nielsen_app_id=P7CFE36DB-A8D9-4801-95FE-51C29101342C' in f:
         fw_nielsen_app_id = x
         fw_nielsen ='fw_nielsen_app_id=P7CFE36DB-A8D9-4801-95FE-51C29101342C'
     else:
         fw_nielsen_app_id = y
         fw_nielsen = ''
     if 'attnid=dfw001' in f:
         attnid = x
         attn='attnid = dfw001'
     else:
         attnid = y
         attn = ''
     if 'hhid=zhd0v7Tz%2FGHHjmqrX0Deqg%3D%3D' in f:
         hhid = x
     elif 'hhid=0EIDrf0ajacBgBY7IIX2Vw%3D%3D' in f:
         hhid = x
     elif 'hhid=1/IeUAPXQJok3jGPc/9w+g==' in f:
         hhid = x
     elif 'hhid=' in f:
         hhid = x
     else:
         hhid = y
     # table validation
     if 'AdBreakResolutionManager' in f:
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
         print "<tr>""<td>"+ comscore_impl_type + comscoreIT+"</td>""<td>"+attnid+attn+"</td>""<td>"+hhid+"hhid"+str(hhidr[-1])+"</td>""<td>"+ comscore_device+"comscore_device"+ str(comscore_devicer[-1])+"</td>""</tr>"
         print "<tr>""<td>"+nielsen_dev_group + ndg+ "</td>""<td>" + fw_nielsen_app_id + fw_nielsen + "</td>""<td>" + nielsen_platform + np + "</td>""<td>"+comscore_platform + comscoreP + "</td>""</tr>"
         print "</table>"
         print "</body>"
         print "</html>"
         print "</table>"
         print "</body>"
         print "</html>"
     else:
         print
     continue

