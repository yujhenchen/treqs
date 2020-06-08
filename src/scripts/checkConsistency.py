from src import parameters as param
from src import utilities
import os
import re
import pandas as pd
from src.elements import UseElement

class Consistency(object):
    def __init__(self):
        self.useElement = UseElement.UseElement()
        self.df_cur = pd.DataFrame()
        self.req_cur = ""
        self.req_dir = ""
        self.log_path = ""


    def setDataframe(self):
        self.df_cur = self.useElement.getContent(self.req_cur)


    def getDataframe(self):
        return self.df_cur

    
    def setReqFilesDir(self, req_dir):
        self.req_dir = req_dir


    def creatLogFile(self):
        str_date = utilities.getDateTimeStr()
        self.log_path = os.path.join(self.req_dir, 'summary_'+str_date+'.txt')
        with open(self.log_path, 'w'):
            pass


    def readAllContent(self, filePattern=r'SR.*?\.md'):
        appended_data = []
        df_all = pd.DataFrame()
        try:
            for root, directories, filenames in os.walk(self.req_dir):
                # for directory in directories
                for filename in filenames:
                    # Only files matching the given pattern are scanned
                    match = re.search(filePattern, filename)
                    if match:
                        entry = os.path.join(root, filename)
                        # read each file into single dataframe
                        with open(entry, "r") as file:
                            self.useElement.readContent(self.req_cur, utilities.readFile(entry))
                            df = self.useElement.getContent(self.req_cur)
                            # add file name column
                            df[param.file_name] = entry
                            appended_data.append(df)
            if len(appended_data) > 0:
                df_all = pd.concat(appended_data)
            self.useElement.setContent(self.req_cur, df_all)
            return True
        except Exception:
            print("readAllContent Exception") 
            return False


    def prepareAllContent(self, requirement):
        filePattern = input(requirement+" file pattern:")
        self.req_cur = requirement
        return self.readAllContent(filePattern)


    def prepareTest(self):
        testcode_dir = input("Test code files directory:")
        appended_data = []
        try:
            for root, directories, filenames in os.walk(testcode_dir):
                for filename in filenames:
                    if filename.endswith((".py", ".json", ".cpp", ".java")):
                        entry = os.path.join(root, filename)
                        # print(os.path.join(root, fn))
                        # read all element tags into temp file with testcase requirements format
                        self.useElement.readContent(self.req_cur, utilities.readTestcodeElements(entry))
                        df = self.useElement.getContent(self.req_cur)
                        # add file name column
                        df[param.file_name] = entry
                        appended_data.append(df)
            if len(appended_data) > 0:
                df_all = pd.concat(appended_data)
            self.useElement.setContent(self.req_cur, df_all)
            #print(df_all)
        
        except Exception:
            print("prepareTest Exception") 
            return False


    def queryEmptyValue(self):
        try:
            df = self.df_cur[self.df_cur.isin([param.empty_str]).any(axis=1)]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.writeFileAppend(self.log_path, "=== requirements value missing ===", df.to_string())
                return False
        except Exception:
            print("queryEmptyValue Exception") 
            return False


    def queryDuplicate(self):
        try:
            df = self.df_cur[self.df_cur.duplicated([param.uid], keep=False)]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.writeFileAppend(self.log_path, "=== requirements id duplicate ===", df.to_string())
                return False
        except Exception:
            print("queryDuplicate Exception") 
            return False


    def querySelfMissing(self):
        try:
            # find link_element not in uid
            ls_uniq = self.df_cur[param.uid].unique()
            df = self.df_cur.loc[~self.df_cur[param.link_element].isin(ls_uniq)]
            # filter link_element == root
            df = df.loc[df[param.link_element] != param.root_id]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.writeFileAppend(self.log_path, "=== requirements link_element missing ===", df.to_string())
                return False
        except Exception:
            print("querySelfMissing Exception")
            return False


    def queryOtherMissing(self, requirement_link, column_link):
        if requirement_link == "" or column_link == "":
            return True
        try:
            df_link = self.useElement.getContent(requirement_link)
            # find link_element not in uid
            ls_uniq = df_link[param.uid].unique()
            df = self.df_cur.loc[~self.df_cur[column_link].isin(ls_uniq)]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.writeFileAppend(self.log_path, "=== requirements "+column_link+" missing ===", df.to_string())                
                return False
        except Exception:
            print("queryOtherMissing Exception")
            return False


    def check(self, requirement, req_link="", column_link=""):
        if self.prepareAllContent(requirement) != True:
            print("Read requirements files ERROR!")
            return False
        self.setDataframe()
        return (self.queryEmptyValue() and self.queryDuplicate() and self.querySelfMissing() and self.queryOtherMissing(req_link, column_link))



def stringToBool(str):
    if str == 'y':
        return True
    else:
        return False


def check():
    bool_us = stringToBool(input("Check user stories? (y or n):"))
    bool_sr = stringToBool(input("Check system requirement? (y or n):"))
    bool_qr = stringToBool(input("Check quality requirement? (y or n):"))
    bool_tc = stringToBool(input("Check test case? (y or n):"))
    
    consist = Consistency()
    req_dir = input("Elements files directory:")
    consist.setReqFilesDir(req_dir)
    consist.creatLogFile()
    ls_b = []
    if bool_us:
        ls_b.append(consist.check(param.usReq))
    if bool_sr:
        ls_b.append(consist.check(param.srReq, param.usReq, param.link_us))
    if bool_qr:
        ls_b.append(consist.check(param.qrReq, param.srReq, param.link_sr))
    if bool_tc:
        ls_b.append(consist.check(param.tcReq, param.srReq, param.link_sr))
        # check testcode
        consist.prepareTest()
        ls_b.append(consist.check(param.tcReq, param.srReq, param.link_sr))
   
    if False in ls_b:
        print("Consistency checking failed! Please check summary file")
    else:
        print("Consistency checking successed!")