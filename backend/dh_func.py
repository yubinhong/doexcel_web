#!/usr/bin/env python
#coding:utf-8
#__author__="ybh"
import xlwt,xlrd
import os,time
import codecs
import chardet
import pandas
#file=open("D:\余斌宏\数据模板\导航\\2345导航33883子渠道导出.xls",'r')
#result=file.readlines()
#for i in range(len(result)-1):

#    print(result[i])


def daohang_path(path):
    code=bianma(path)
    file=open(path,'r',encoding=code)
    result=file.readlines()
    file.close()
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("sheet1")
    for i in range(len(result)):
        list=result[i].strip('\n').split()
        #print(list)

        for y in range(len(list)):
            sheet.write(i,y,list[y])
            #print(list[y])
    file_name=os.path.basename(path)
    dir_name=os.path.dirname(path)
    newpath="%s%snew%s" %(dir_name,os.sep,file_name)
    wbk.save(u"%s" % (newpath))
    return newpath


def dianshang_path(path):

    code=bianma(path)

    f = open(path, 'r', encoding=code)
    lines=f.readlines()
    f.close()
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("sheet1")
    for i in range(len(lines)):
        if "," in lines[i]:
            list=lines[i].strip().split(',')
        else:
            list = lines[i].strip().split('\t')
        for y in range(len(list)):
            sheet.write(i, y, list[y].strip().strip("\ufeff").strip("\"").strip())
                #print(list[y].strip("\"").strip("￥"))
    file_name = os.path.basename(path)
    file_name = file_name.split('.')[0]
    dir_name = os.path.dirname(path)
    newpath = "%s%snew%s.xlsx" % (dir_name, os.sep, file_name)
    wbk.save(u"%s" % (newpath))
    return newpath

def ruanjian_path(path):
    code=bianma(path)
    f = open(path, 'r',encoding=code)

    lines = f.readlines()
    f.close()
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("sheet1")
    for i in range(len(lines)):
        list = lines[i].strip('\n').split(',')
        for y in range(len(list)):
            sheet.write(i, y, list[y].strip("\"").strip("\r\n").strip(" "))
            # print(list[y].strip("\"").strip("￥"))
    file_name = os.path.basename(path)
    file_name = file_name.split('.')[0]
    dir_name = os.path.dirname(path)
    newpath = "%s%snew%s.xlsx" % (dir_name, os.sep, file_name)
    wbk.save(u"%s" % (newpath))
    return newpath



def bianma(path):
    file=codecs.open(path,'rb')
    data=file.read()
    code=chardet.detect(data)['encoding']
    file.close()
    return code


#对电商相同的日期进行相加
def uniq(path='D:\python\\电商汇总-2017-04-07.xls'):
    wb=xlrd.open_workbook(path,encoding_override='gb2312')
    sh=wb.sheet_by_index(0)
    timeList=sh.col_values(start_rowx=1,colx=0)
    qidList=sh.col_values(start_rowx=1,colx=1)
    countList=sh.col_values(start_rowx=1,colx=2)
    countList=[int(x) for x in countList]
    data=pandas.DataFrame()
    data['timeList']=timeList
    data['countList']=countList
    data=data.groupby(['timeList','qidList']).sum()
    data_dict=data.to_dict()
    timeList=list(data_dict['countList'].keys())
    countList=list(data_dict['countList'].values())

    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"电商汇总",cell_overwrite_ok=True)
    sheet.write(0, 0, u"时间")
    sheet.write(0, 1, u"渠道子ID")
    sheet.write(0, 2, u"订单数")
    for i in range(0, len(timeList)):
        sheet.write(i, 0, timeList[i])
        sheet.write(i, 1, qidList[i])
        sheet.write(i, 2, str(countList[i]))

    wbk.save(path)






if __name__=="__main__":
    #get_newpath()
    #dianshang_path()
    uniq()


