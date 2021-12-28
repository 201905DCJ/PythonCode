import os
import commands

name='date +%Y%m%d%H%M'
(s,o)=commands.getstatusoutput(name)
fo=open("/home/dcj/"+str(o)+".txt","w")

def Data():
    path="/home/data.txt"
    order=os.popen("awk -F '\n' '{print $0}' %s"%path)
    return order

def MW(s,ss,sss):
    fo.write("Memory status is "+sss+"  "+ss+": "+str(s)+"MB\n")

def SW(a,b):
    fo.write(a+": "+str(b)+"MB\n")

def SysLook():
    order=Data()
    for i in order:
        print "--------------------"+i
        os.system(i)
        print "------------------------------------------------\n"

def SysWrite():
    order=Data()
    for i in order:
        fo.write("--------------------"+i) 
        ss=os.popen(i)
        for ii in ss.readlines():
            fo.write(str(ii))
        fo.write("------------------------------------------------\n")

def Co_K_t_M(s):
    return int(s)/1024

def SysMem():
    # Note path splicing in Python
    # path1="/proc/meminfo"
    # p="{print $2}'"
    # total="awk '/MemTotal/"+p+" "+path1
    path1="/proc/meminfo"
    p="{print $2}'"
    MT="awk '/MemTotal/"+p+" "+path1
    (s,o)=commands.getstatusoutput(MT)
    MemTol=Co_K_t_M(o)
    MF="awk '/MemFree/"+p+" "+path1
    (s,o)=commands.getstatusoutput(MF)
    MemFree=Co_K_t_M(o)
    MemUsed=MemTol-MemFree
    fo.write("\n----------------------------------the result of memory------------------------------\n")
    SW("MemUsed",MemUsed)
    BF="awk '/Buffers/"+p+" "+path1
    (s,o)=commands.getstatusoutput(BF)
    Buffers=Co_K_t_M(o)
    CA="awk '/^Cached/"+p+" "+path1
    (s,o)=commands.getstatusoutput(CA)
    Cached=Co_K_t_M(o)
    AppUsed=MemTol-MemFree-Buffers-Cached
    SW("AppUsed",AppUsed)
    MM=MemTol/2
    if MM>=MemUsed:
        MW(MemUsed,"MemUsed","OK")
    elif MM<MemUsed:
        MS=MemFree+MM
        if MS>=MemUsed:
            MW(MemUsed,"MemUsed","OK")
            MW(MemFree,"MemFree","OK")
        elif MS<MemUsed:
            FA=Cached+MemFree
            if FA>=MemUsed:
                MW(MemUsed,"MemUsed","OK")
                MW(MemFree,"MemFree","OK")
                MW(Cached,"Cached","OK")
            else:
                MW(MemUsed,"MemUsed","Bad")
                MW(MemFree,"MemFree","Bad")
                MW(Cached,"Cached","Bad")
    SwapTotal="awk '/SwapTotal/"+p+" "+path1
    (s,o)=commands.getstatusoutput(SwapTotal)
    ST=Co_K_t_M(o)
    SwapFree="awk '/SwapFree/"+p+" "+path1
    (s,o)=commands.getstatusoutput(SwapFree)
    SF=Co_K_t_M(o)
    SU=ST-SF
    if SU!=0:
        SW("SwapUsed",SU)
        SM=ST/2
        if SU<SM:
            SW("SwapTotal",ST)
            SW("SwapFree",SF)
            fo.write("Swap is used but not beyond on half Please note that\n")
        elif SU==SM:
            SW("SwapTotal",ST)
            SW("SwapFree",SF)
            fo.write("Swap is used one half Please note that\n")
        else:
            SW("SwapTotal",ST)
            SW("SwapFree",SF)
            fo.write("Please expand the memory, otherwise the system will make an error\n")
    else:
        fo.write("Swap is not used  SwapUsed: "+str(SU)+"MB\n")
    fo.close()



SysLook()
SysWrite()
SysMem()
