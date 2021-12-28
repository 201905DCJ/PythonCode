# coding= utf-8
import os,sys,re
import linecache
from collections import Counter

FileContextDateTime=19
FileContextDate=5

def FilesPath():
    with open('path.txt') as file_obj:
        PathContent = file_obj.read()
        return PathContent

def FolderContext():
    FolderPath=FilesPath()
    result=os.listdir(FolderPath)
    for FileName in result:
        return FileName

def FileNameChanged(folder):
    p=FilesPath()
    p=p+"\\"
    F=folder.split(' ')
    FileDate=F[0].split('-')
    NewFileName=''
    for i in FileDate:
        NewFileName=NewFileName+i
    NewFileNameType=NewFileName+'.txt'
    os.rename(p+folder,p+NewFileNameType)
    return p+NewFileNameType

def FileContext():
    p=FilesPath()
    p=p+"\\"
    FlieNameSearch=re.search("-",FolderContext())
    FileDateTimeList=[]
    FileDateList=[]
    if FlieNameSearch!=None:
        for FileLine in open(FileNameChanged(FolderContext())):
            FileContext=FileLine.split('\t')
            FileContext2=FileContext[FileContextDate]
            FileDateList=FileDateList+FileContext2.split()
            FileContext=FileContext[FileContextDateTime].split(':')[0]
            FileDateTimeList=FileDateTimeList+FileContext.split()
        count2=Counter(FileDateList)
        print " "
        for k,v in count2.items():
            print ("       加油日期: "+str(k)+" 日"+" "+"油单数据: "+str(v)+" 条").decode('utf-8')
        count=Counter(FileDateTimeList)
        return count

    else:
        for FileLine in open(p+FolderContext()):
            FileContext=FileLine.split('\t')
            FileContext2=FileContext[FileContextDate]
            FileDateList=FileDateList+FileContext2.split()
            FileContext=FileContext[FileContextDateTime].split(':')[0]
            FileDateTimeList=FileDateTimeList+FileContext.split()
        count2=Counter(FileDateList)
        print " "
        for k,v in count2.items():
            print ("       加油日期: "+str(k)+" 日"+" "+"油单数据: "+str(v)+" 条").decode('utf-8')
        count=Counter(FileDateTimeList)
        return count

def CountTimes(count):
    for k,v in count.items():
        print ("          加油时间段: "+str(k)+" 时"+"   "+"加油总架次: "+str(v)+" 架次").decode('utf-8')
        print ' '

CountTimes(FileContext())