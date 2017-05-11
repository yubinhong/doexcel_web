#!/usr/bin/env python
#coding:utf-8
#__author__="ybh"
import xlrd, xlwt
import re
import os
import time,datetime


from backend.dh_func import daohang_path,dianshang_path,ruanjian_path,uniq

def yuming1(dir):
    dir=dir
    files=os.listdir(dir)
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"域名汇总")
    sheet.write(0, 0, u"时间")
    sheet.write(0, 1, u"域名")
    sheet.write(0, 2, u"IP")
    temp = 1
    for file in files:
        path=os.path.join(dir,file)
        print(path)
        wb = xlrd.open_workbook(path,encoding_override='gb2312')  # 打开文件
        sh = wb.sheet_by_index(0)  # 第一个表

        atime=sh.cell(3,0).value
        if not atime:
            atime=sh.cell(4,0).value

        #time=sh.cell(4,0).value
        atime=re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}",atime)[0]
        check1=sh.cell(5,1).value
        check2=sh.cell(7,1).value
        check3=sh.cell(4,1).value
        if check1=="URL地址":
            domainList = sh.col_values(start_rowx=6,colx=1)
            ipList = sh.col_values(start_rowx=6,colx=4)
            for i in range(0, len(ipList) - 2):
                sheet.write(i + temp, 0, atime)
                sheet.write(i + temp, 1, domainList[i])
                sheet.write(i + temp, 2, ipList[i])
            temp = temp + i + 1


        if check3=="浏览次数":
            if check2 == "浏览次数":
                domain = sh.cell(3, 0).value
                domain = re.findall('\((.*)\)-', domain)[0]
                timeList = sh.col_values(start_rowx=9, colx=0)
                ipList = sh.col_values(start_rowx=9, colx=3)
                for i in range(0, len(ipList) - 2):
                    sheet.write(i + temp, 0, timeList[i])
                    sheet.write(i + temp, 1, domain)
                    sheet.write(i + temp, 2, ipList[i])
                temp = temp + i + 1
            else:
                domainList = sh.col_values(start_rowx=6, colx=0)
                ipList = sh.col_values(start_rowx=6, colx=3)
                for i in range(0,len(ipList)-2):
                    sheet.write(i+temp,0,atime)
                    sheet.write(i+temp,1,domainList[i])
                    sheet.write(i+temp,2,ipList[i])
                temp=temp+i+1
    ctime=time.strftime("%Y-%m-%d",time.localtime())
    basedir=os.path.dirname(dir)
    filepath=os.path.join(basedir,u"域名汇总1-%s.xls" %(ctime))
    wbk.save(filepath)
    return filepath

def yuming2(dir):
    dir=dir
    files=os.listdir(dir)
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"域名汇总")
    sheet.write(0, 0, u"时间")
    sheet.write(0, 1, u"渠道子ID")
    sheet.write(0, 2, u"IP")
    temp = 1
    for file in files:
        path=os.path.join(dir,file)
        print(path)
        wb = xlrd.open_workbook(path,encoding_override='gb2312')  # 打开文件
        sh = wb.sheet_by_index(0)  # 第一个表

        qid = file.split(".")[0]
        atime=sh.cell(3,0).value
        if not atime:
            atime=sh.cell(4,0).value

        #time=sh.cell(4,0).value
        atime=re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}",atime)[0]
        check1=sh.cell(5,1).value
        check2=sh.cell(7,1).value
        check3=sh.cell(4,1).value
        if check1=="URL地址":
            domainList = sh.col_values(start_rowx=6,colx=1)
            ipList = sh.col_values(start_rowx=6,colx=4)
            for i in range(0, len(ipList) - 2):
                sheet.write(i + temp, 0, atime)
                sheet.write(i + temp, 1, qid)
                sheet.write(i + temp, 2, ipList[i])
            temp = temp + i + 1


        if check3=="浏览次数":
            if check2 == "浏览次数":
                domain = sh.cell(1, 1).value
                timeList = sh.col_values(start_rowx=9, colx=0)
                ipList = sh.col_values(start_rowx=9, colx=3)
                for i in range(0, len(ipList) - 2):
                    sheet.write(i + temp, 0, timeList[i])
                    sheet.write(i + temp, 1, qid)
                    sheet.write(i + temp, 2, ipList[i])
                temp = temp + i + 1
            else:
                domainList = sh.col_values(start_rowx=6, colx=0)
                ipList = sh.col_values(start_rowx=6, colx=3)
                for i in range(0,len(ipList)-2):
                    sheet.write(i+temp,0,atime.strip('\t').strip())
                    sheet.write(i+temp,1,qid)
                    sheet.write(i+temp,2,ipList[i])
                temp=temp+i+1
    ctime=time.strftime("%Y-%m-%d",time.localtime())
    basedir=os.path.dirname(dir)
    filepath=os.path.join(basedir,u"域名汇总2-%s.xls" %(ctime))
    wbk.save(filepath)
    return filepath

def daohang(dir):
    dir=dir
    files=os.listdir(dir)
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"导航汇总")
    sheet.write(0, 0, u"时间")
    sheet.write(0, 1, u"渠道子ID")
    sheet.write(0, 2, u"第三方浏览器量")
    sheet.write(0, 3, u"官方浏览器量")
    temp = 1
    style1 = xlwt.XFStyle()
    style1.num_format_str = 'YYYY-MM-DD'
    for file in files:
        path = os.path.join(dir, file)
        print(path)
        try:
            wb = xlrd.open_workbook(path, encoding_override='gb2312')  # 打开文件
        except Exception as e:
            newpath=daohang_path(path)
            wb = xlrd.open_workbook(newpath, encoding_override='gb2312')
        sh = wb.sheet_by_index(0)  # 第一个表

        #time=sh.cell(4,0).value
        check=sh.cell(0,1).value
        timeList = sh.col_values(start_rowx=1, colx=0)
        #print(type(timeList[0]))
        if timeList[-1]=="汇总" or timeList[-1]=="总计":
            timeList=timeList[:-1]
        if check=="通过2345浏览器":
            try:
                timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList]
            except Exception as e:
                timeList = [time.strptime(x, "%Y-%m-%d") for x in timeList]
                timeList = [datetime.datetime(*x[:3]) for x in timeList]
            browser1List = sh.col_values(start_rowx=1,colx=1)
            browser2List = sh.col_values(start_rowx=1, colx=3)
            #qid=re.findall(r"[0-9]{5}",file)
            qid=file.split(".")[0]
            for i in range(0,len(timeList)):
                sheet.write(i+temp,0,timeList[i].strftime('%Y-%m-%d').strip('\t').strip())
                sheet.write(i+temp,1,qid)
                sheet.write(i+temp,2,str(int(browser2List[i])).strip('\t').strip())
                sheet.write(i+temp,3,str(int(browser1List[i])).strip('\t').strip())
            temp=temp+i+1
        if check=="子账户号":
            try:
                timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList]
            except Exception as e:
                timeList = [time.strptime(x, "%Y-%m-%d") for x in timeList]
                timeList = [datetime.datetime(*x[:3]) for x in timeList]
            browser1List = sh.col_values(start_rowx=1, colx=2)
            qidList = sh.col_values(start_rowx=1, colx=1)
            qidList=[file.split(".")[0]+"-"+x for x in qidList]
            for i in range(0,len(timeList)):
                sheet.write(i+temp,0,timeList[i].strftime('%Y-%m-%d').strip('\t').strip())
                sheet.write(i+temp,1,qidList[i])
                sheet.write(i+temp,2,str(int(browser1List[i])).strip('\t').strip())
            temp=temp+i+1
        if check=="渠道代码":
            try:
                timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList]
            except Exception as e:
                try:
                    timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList[:-3]]
                except Exception as e:
                    timeList = [time.strptime(x, "%Y-%m-%d") for x in timeList]
                    timeList = [datetime.datetime(*x[:3]) for x in timeList]
            browser1List = sh.col_values(start_rowx=1, colx=2)
            qidList = sh.col_values(start_rowx=1, colx=1)
            try:
                qidList=[re.findall(r"[0-9]{5}",x)[0] for x in qidList]
            except Exception as e:
                qidList = [re.findall(r"[0-9]{5}", x)[0] for x in qidList[:-3]]
            qidList= [file.split(".")[0]+"-"+x for x in qidList]
            for i in range(0,len(timeList)):
                sheet.write(i+temp,0,timeList[i].strftime('%Y-%m-%d').strip('\t').strip())
                sheet.write(i+temp,1,qidList[i])
                sheet.write(i+temp,2,str(int(browser1List[i])).strip('\t').strip())
                sheet.write(i+temp,3,"")
            temp=temp+i+1
        if check == "第三方浏览器":
            try:
                timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList]
            except Exception as e:
                try:
                    timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList[:-3]]
                except Exception as e:
                    timeList = [time.strptime(x, "%Y-%m-%d") for x in timeList]
                    timeList = [datetime.datetime(*x[:3]) for x in timeList]
            browser1List = sh.col_values(start_rowx=1, colx=1)
            qid=file.split(".")[0]
            for i in range(0, len(timeList)):
                sheet.write(i + temp, 0, timeList[i].strftime('%Y-%m-%d').strip('\t').strip())
                sheet.write(i + temp, 1, qid)
                sheet.write(i + temp, 2, str(int(browser1List[i])).strip('\t').strip())
            temp = temp + i + 1

    ctime=time.strftime("%Y-%m-%d",time.localtime())
    basedir = os.path.dirname(dir)
    filepath = os.path.join(basedir, u"导航汇总-%s.xls" % (ctime))
    wbk.save(filepath)
    return filepath

def dianshang(dir):
    dir=dir
    files=os.listdir(dir)
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"电商汇总")
    sheet.write(0, 0, u"时间")
    sheet.write(0, 1, u"渠道子ID")
    sheet.write(0, 2, u"订单数")
    temp = 1
    style1 = xlwt.XFStyle()
    style1.num_format_str = 'YYYY-MM-DD'
    for file in files:
        path = os.path.join(dir, file)
        print(path)
        try:
            wb = xlrd.open_workbook(path, encoding_override='gb2312')  # 打开文件
        except Exception as e:
            path=dianshang_path(path)
            wb = xlrd.open_workbook(path, encoding_override='gb2312')
        sh = wb.sheet_by_index(0)  # 第一个表
        qid=file.split(".")[0]

        timeList = sh.col_values(start_rowx=1, colx=0)
        countList = sh.col_values(start_rowx=1, colx=1)
        #try:
         #   timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList]
        #except Exception as e:
        try:
            timeList = [time.strptime(x.strip(), "%Y%m%d") for x in timeList]

        except Exception as e:
            try:
                timeList = [time.strptime(x, "%Y/%m/%d %H:%M") for x in timeList]
            except Exception as e:
                try:
                    timeList = [time.strptime(x, "%Y/%m/%d") for x in timeList]
                except Exception as e:
                    try:
                        timeList = [time.strptime(x, "%Y-%m-%d") for x in timeList]
                    except Exception as e:
                        timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList]
        try:
            timeList = [datetime.datetime(*x[:3]) for x in timeList]
        except Exception as e:
            pass
        for i in range(0,len(timeList)):
            sheet.write(i+temp,0,timeList[i].strftime('%Y-%m-%d').strip('\t').strip())
            sheet.write(i+temp,1,qid)
            sheet.write(i+temp,2,str(int(countList[i])).strip('\t'))
        temp=temp+i+1


    ctime=time.strftime("%Y-%m-%d",time.localtime())
    basedir = os.path.dirname(dir)
    filepath = os.path.join(basedir, u"电商汇总-%s.xls" % (ctime))
    wbk.save(filepath)
    uniq(filepath)
    return filepath


def ruanjian(dir):
    dir=dir
    files = os.listdir(dir)
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"软件汇总")
    sheet.write(0, 0, u"时间")
    sheet.write(0, 1, u"渠道子ID")
    sheet.write(0, 2, u"安装量")
    temp = 1
    style1 = xlwt.XFStyle()
    style1.num_format_str = 'YYYY-MM-DD'
    for file in files:
        path = os.path.join(dir, file)
        print(path)
        try:
            wb = xlrd.open_workbook(path, encoding_override='gb2312')  # 打开文件
        except Exception as e:
            path = ruanjian_path(path)
            wb = xlrd.open_workbook(path, encoding_override='gb2312')
        sh = wb.sheet_by_index(0)  # 第一个表

        # time=sh.cell(4,0).value
        if sh.ncols == 2:
            timeList = sh.col_values(start_rowx=1, colx=0)
            countList = sh.col_values(start_rowx=1, colx=1)
        elif sh.ncols == 1:
            resultList=sh.col_values(start_rowx=1,colx=0)
            timeList=[x.split('\t')[0] for x in resultList]
            countList=[x.split('\t')[1] for x in resultList]
        elif sh.ncols==3:
            timeList = sh.col_values(start_rowx=1, colx=0)
            qidList=sh.col_values(start_rowx=1, colx=1)
            countList = sh.col_values(start_rowx=1, colx=2)
        try:
            timeList = [time.strptime(x.strip(), "%Y%m%d") for x in timeList]

        except Exception as e:
            try:
                timeList = [time.strptime(x, "%Y/%m/%d %H:%M") for x in timeList]
            except Exception as e:
                try:
                    timeList = [time.strptime(x, "%Y/%m/%d") for x in timeList]
                except Exception as e:
                    try:
                        timeList = [time.strptime(x, "%Y-%m-%d") for x in timeList]
                    except Exception as e:
                        timeList = [xlrd.xldate.xldate_as_datetime(x, 0) for x in timeList]
        try:
            timeList = [datetime.datetime(*x[:3]) for x in timeList]
        except Exception as e:
            pass
        #qid=re.findall(r'[0-9]{5}',file)
        qid=file.split(".")[0]
        if sh.ncols==3:
            qidList=[qid+"-"+str(x) for x in qidList]
            for i in range(0, len(timeList)):
                sheet.write(i + temp, 0, timeList[i].strftime('%Y-%m-%d').strip('\t').strip())
                sheet.write(i + temp, 1, qidList[i])
                sheet.write(i + temp, 2, str(int(countList[i])))
        else:
            for i in range(0, len(timeList)):
                sheet.write(i + temp, 0, timeList[i].strftime('%Y-%m-%d').strip('\t').strip())
                sheet.write(i + temp, 1, qid)
                sheet.write(i + temp, 2, str(int(countList[i])).strip('\t').strip())
        temp = temp + i + 1



    ctime = time.strftime("%Y-%m-%d", time.localtime())
    basedir = os.path.dirname(dir)
    filepath = os.path.join(basedir, u"软件汇总-%s.xls" % (ctime))
    wbk.save(filepath)

    return filepath

if __name__=="__main__":
    #yuming()
    daohang()
    #dianshang()
    #ruanjian()