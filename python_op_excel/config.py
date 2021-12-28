import os
def mkpath(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        print path+' is ok'
        return path
    else:
        print path+' is already build'
        return path
# write funtion for config
def fw(a,b,fo):
    fo.write(a+' '+'='+' '+str(b)+'\n')
# input function
def config():
    print 'example: E:\\NKG_Source\\1\\STS\\date\\tw\\'
    # input a value or default
    a=raw_input('please input your data fodle(1): ')
    b=raw_input('please input your data2 fodle(STS): ')
    print 'example: E:\\NKG_Source\\1\\result\\excels\\tw.xls'
    d=raw_input('please input your xls name(tw.xls): ')
    mpath1='E:\\NKG_Source\\'+a+'\\result\\'
    mpath11=mkpath(mpath1)
    mpath11=mpath1.replace('\\','\\\\')
    new_mapth_config=mpath11+'config.txt'
    fo=open(new_mapth_config,'w+')
    fw('data1',a,fo)
    fw('data2',b,fo)
    fw('name',d,fo)
    data_path='E:\\NKG_Source\\'+a+'\\'+b
    YN=raw_input('please input your choose changed(Y/N) :') or 'N'
    print YN
    if YN=='Y' or YN=='y':
        free_title=int(raw_input('please input free_title_line (=5):') or '5') 
        free_txt=int(raw_input('please input free_txt_line (=6):') or '6')
        date_txt=int(raw_input('please input date_txt_line (=2):') or '2')
        disk_title=int(raw_input('please input disk_title_line (11):') or '11')
        disk_txt=int(raw_input('please input disk_txt_line (=13):') or '13')
        fw('free_title_line',free_title,fo)
        fw('free_txt_line',free_txt,fo)
        fw('date_txt_line',date_txt,fo)
        fw('disk_title_line',disk_title,fo)
        fw('disk_txt_line',disk_txt,fo)
    else:
        free_title=5
        free_txt=6
        date_txt=2
        disk_title=11
        disk_txt=13
        fw('free_title_line',free_title,fo)
        fw('free_txt_line',free_txt,fo)
        fw('date_txt_line',date_txt,fo)
        fw('disk_title_line',disk_title,fo)
        fw('disk_txt_line',disk_txt,fo)
    mpath2='E:\\NKG_Source\\'+a+'\\result\\excels\\'
    mpath3=mkpath(mpath2)
    return mpath3,new_mapth_config,data_path

