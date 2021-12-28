import os
import linecache
import xlwt
import config
# tempale path
path1='E:\\NKG_Source\\Tempale\\202108190720.txt'

# excel function
def Exl():
    workbook = xlwt.Workbook()
    return workbook

# change months function
def Mt(s):
    a=['1','2','3','4','5','6','7','8','9','10','11','12']
    month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in range(len(month)):
        if month[i]==s:
            return a[i]

def Co():
    mpath=config.config()
    mpl=list(mpath)
    mpl[0]=mpl[0].replace('\\','\\\\')
    print mpl[0]
    print mpl[1]
    mpl[2]=mpl[2].replace('\\','\\\\')
    mpl[2]=mpl[2]+'\\'
    print mpl[2]
    # config save value
    free_title_line=linecache.getline(mpl[1],4)
    free_title=int(free_title_line.split()[2])
    print free_title
    free_txt_line=linecache.getline(mpl[1],5)
    free_txt=int(free_txt_line.split()[2])
    print free_txt
    date_txt_line=linecache.getline(mpl[1],6)
    date_txt=int(date_txt_line.split()[2])
    print date_txt
    disk_title_line=linecache.getline(mpl[1],7)
    disk_title=int(disk_title_line.split()[2])
    print disk_title
    disk_txt_line=linecache.getline(mpl[1],8)
    disk_txt=int(disk_txt_line.split()[2])
    print  disk_txt
    # config save value
    workbook=Exl()
    worksheet = workbook.add_sheet('My Sheet')
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'Times New Roman' 
    font.height=25*11 
    style.font = font
    alignment = xlwt.Alignment() # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style.alignment = alignment # Add Alignment to Style
    worksheet.write_merge(0, 0, 0,16, 'Computer source',style)
    p=os.listdir(mpl[2])
    k=2
    j=1
    s=1
    ss=1
    sss=7
    ssss=7
    kk=2
    kkk=2
    kkkk=2
    l=1
    ll=13
    # free_title
    free1=linecache.getline(path1,free_title)
    for s in range(len(free1.split())):
        worksheet.write(1,s,free1.split()[s]+"(M)",style)
    # disk_title
    disk1=linecache.getline(path1,disk_title)
    alist=disk1.split()
    alist.remove(alist[0])
    for s in range(len(alist)-2):
        worksheet.write(1,sss,alist[s],style)
        sss=sss+1
    # date_title
    worksheet.write(1,6,'date',style)
    worksheet.write(1,11,'hostname',style)
    worksheet.write(1,12,'online(days)',style)
    worksheet.write(1,13,'SwapTotal(MB)',style)
    worksheet.write(1,14,'SwapUsed(MB)',style)
    worksheet.write(1,15,'SwapFree(MB)',style)
    for i in p:
        i=mpl[2]+i
        date=linecache.getline(i,date_txt)
        #print date.split()
        worksheet.write(k,6,date.split()[5]+"/"+Mt(date.split()[1])+"/"+date.split()[2]+' '+date.split()[3],style)
        free2=linecache.getline(i,free_txt)
        alist=free2.split()
        alist.remove(alist[0])
        #['Mem:', '11881', '8646', '3235', '0', '136', '4918']
        #['11881', '8749', '3132', '0', '136', '4982']
        for j in range(len(alist)):
            worksheet.write(k,j,alist[j],style)   
        disk2=linecache.getline(i,disk_txt)
        alist=disk2.split()
        alist.remove(alist[4])
        for ss in range(len(alist)):
            worksheet.write(k,ssss,alist[ss],style)
            ssss=ssss+1
        ssss=7
        k=k+1
        # note
        hostname=linecache.getline(i,23)
        worksheet.write(kk,11,hostname,style)
        kk=kk+1
        # online
        online=linecache.getline(i,20)
        online1=online.split()[2]+' '+online.split()[3]
        worksheet.write(kkk,12,online1,style)
        kkk=kkk+1
        #swap
        swap=linecache.getline(i,8)
        swap1=swap.split()
        swap1.remove(swap1[0])
        for l in range(len(swap1)):
            worksheet.write(kkkk,ll,swap1[l],style)
            ll=ll+1
        ll=13
        kkkk=kkkk+1
    exl_name_line=linecache.getline(mpl[1],3)
    exl_name=int(exl_name_line.split()[2])
    print exl_name
    exl_path=mpl[0]+'\\\\'+str(exl_name)+'.xls'
    print exl_path
    workbook.save(exl_path)

Co()






