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


    def set_dataframe(self):
        self.df_cur = self.useElement.get_content(self.req_cur)


    def get_dataframe(self):
        return self.df_cur

    
    def set_req_files_dir(self, req_dir):
        self.req_dir = req_dir


    def creat_log_file(self):
        str_date = utilities.get_datetime(True)
        self.log_path = os.path.join(self.req_dir, 'summary_'+str_date+'.txt')
        with open(self.log_path, 'w'):
            pass


    def read_all_content(self, filePattern=r'SR.*?\.md'):
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
                            self.useElement.read_content(self.req_cur, utilities.read_file(entry))
                            df = self.useElement.get_content(self.req_cur)
                            # add file name column
                            df[param.FILE_NAME] = entry
                            appended_data.append(df)
            if len(appended_data) > 0:
                df_all = pd.concat(appended_data)
            self.useElement.set_content(self.req_cur, df_all)
            return True
        except Exception:
            print("read_all_content Exception") 
            return False


    def prepare_all_content(self, requirement):
        filePattern = input(requirement+" file pattern:")
        self.req_cur = requirement
        return self.read_all_content(filePattern)


    def prepare_test(self):
        testcode_dir = input("Test code files directory:")
        appended_data = []
        try:
            for root, directories, filenames in os.walk(testcode_dir):
                for filename in filenames:
                    if filename.endswith((".py", ".json", ".cpp", ".java")):
                        entry = os.path.join(root, filename)
                        # print(os.path.join(root, fn))
                        # read all element tags into temp file with testcase requirements format
                        self.useElement.read_content(self.req_cur, utilities.read_testcode_elements(entry))
                        df = self.useElement.get_content(self.req_cur)
                        # add file name column
                        df[param.FILE_NAME] = entry
                        appended_data.append(df)
            if len(appended_data) > 0:
                df_all = pd.concat(appended_data)
            self.useElement.set_content(self.req_cur, df_all)
            #print(df_all)
        
        except Exception:
            print("prepare_test Exception") 
            return False


    def query_empty_value(self):
        try:
            df = self.df_cur[self.df_cur.isin([param.EMPTY_STR]).any(axis=1)]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.write_file_append(self.log_path, "=== requirements value missing ===", df.to_string())
                return False
        except Exception:
            print("query_empty_value Exception") 
            return False


    def query_duplicate(self):
        try:
            df = self.df_cur[self.df_cur.duplicated([param.UID], keep=False)]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.write_file_append(self.log_path, "=== requirements id duplicate ===", df.to_string())
                return False
        except Exception:
            print("query_duplicate Exception") 
            return False


    def query_self_missing(self):
        try:
            # find link_element not in uid
            ls_uniq = self.df_cur[param.UID].unique()
            df = self.df_cur.loc[~self.df_cur[param.LINK_ELEMENT].isin(ls_uniq)]
            # filter link_element == root
            df = df.loc[df[param.LINK_ELEMENT] != param.ROOT_ID]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.write_file_append(self.log_path, "=== requirements link_element missing ===", df.to_string())
                return False
        except Exception:
            print("query_self_missing Exception")
            return False


    def query_other_missing(self, requirement_link, column_link):
        if requirement_link == "" or column_link == "":
            return True
        try:
            df_link = self.useElement.get_content(requirement_link)
            # find link_element not in uid
            ls_uniq = df_link[param.UID].unique()
            df = self.df_cur.loc[~self.df_cur[column_link].isin(ls_uniq)]
            if len(df.index) == 0:
                return True
            else:
                # write dataframe into log files
                utilities.write_file_append(self.log_path, "=== requirements "+column_link+" missing ===", df.to_string())                
                return False
        except Exception:
            print("query_other_missing Exception")
            return False


    def check(self, requirement, req_link="", column_link=""):
        if self.prepare_all_content(requirement) != True:
            print("Read requirements files ERROR!")
            return False
        self.set_dataframe()
        return (self.query_empty_value() and self.query_duplicate() and self.query_self_missing() and self.query_other_missing(req_link, column_link))