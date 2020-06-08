import os
import datetime
from src import parameters as param
from src import utilities
import pandas as pd
from html.parser import HTMLParser
from htmltag import element


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        self.links.append(attr)

    def handle_data(self, data):
        #if data == param.sep_newline:
        if data.rstrip() == "":
            return
        dic = {param.content: data}
        self.contents.append(dic)



class Element(object):
    def __init__(self):
        self.df = pd.DataFrame()


    #def readContent(self, path, columns_f):
    def readContent(self, content, columns_f):
        # get list of file content and convert into pandas table
        ls_row = []
        #ls_elements = self.readElementsToList(path)
        ls_elements = self.readElementsToList(content)
        try:
            for map_item in ls_elements:
                ls_row_item = [map_item[item] for item in columns_f]
                ls_row.append(ls_row_item)
            self.df = pd.DataFrame(ls_row, columns = columns_f)
        except Exception:
            print("readContent Exception")


    def setContent(self, df):
        self.df = df


    def getContent(self):
        return self.df

# ============================================================
    # def queryDataFrame(self, column_query, value_query):
    #     try:
    #         return self.df.loc[self.df[column_query] == value_query]
    #     except Exception:
    #         print("queryDataFrame Exception")    


    # def queryAllDataFrame(self, value_query):
    #     try:
    #         return self.df[self.df.isin([value_query]).any(axis=1)]
    #     except Exception:
    #         print("queryAllDataFrame Exception") 


    # def queryDuplicate(self, column):
    #     try:
    #         return self.df[self.df.duplicated([column], keep=False)]
    #     except Exception:
    #         print("queryDuplicate Exception") 


    # def querySelfMissing(self, column, column_target):
    #     try:
    #         return self.df[self.df.apply(lambda x: x[column] not in x[column_target], axis=1)]
    #     except Exception:
    #         print("querySelfMissing Exception") 
# ============================================================


    def sortDataFrame(self, col_sort):
        self.df = self.df.sort_values(by=[col_sort])


    def updateCustomId(self, parent, customIdReqType, column_parent):
        id_count = 1
        # get row ids which column link_sr == parent
        ls_idx = self.df.index[self.df[column_parent] == parent].tolist()
        for idx in ls_idx:
            self.df.loc[idx, param.custom_id] = customIdReqType + str(id_count)
            id_count = id_count + 1


    def prepareCustomIds(self, idReqType):
        try:
            # reset all custom_ids
            self.df[param.custom_id] = param.empty
            #print((self.df_SR.loc[self.df_SR[param.link_sr] == param.root_id]))
    
            # list unique parent
            ls_parent = self.df[param.link_element].unique()
            # get custom_id of parent
            for parent in ls_parent:
                if parent == param.root_id:
                    customIdReqType = idReqType
                else:
                    customIdReqType = self.df.loc[self.df[param.uid] == parent, param.custom_id].values[0] + param.sep_dot
                self.updateCustomId(parent, customIdReqType, param.link_element)
        except Exception:
            print("prepareCustomIds Exception")


    def prepareWriteFile(self, path, requirement):
        str_date = utilities.getDateTimeStr()
        try:
            dir_path = os.path.split(path)
            # datetime_obj = datetime.datetime.now()
            # str_date = datetime_obj.strftime("-%b%d%Y-%H%M%S")
            # str_date = str(datetime_obj.year)+str(datetime_obj.month)+str(datetime_obj.day)+'-'+str(datetime_obj.hour)+str(datetime_obj.minute)+str(datetime_obj.second)
            return dir_path[param.index_zero]+"/"+requirement+"_"+str_date+".md"
        except Exception:
            print("prepareWriteFile Exception")
            return path+requirement+str_date+".md"
        
    
    def writeContent(self):
        print("")


    def formatData(self):
        print("")


    # read _.md file
    #def readElementsToList(self, f_path):
    def readElementsToList(self, content):
        # read file
        # try:
        #     with open(f_path) as f:
        #         content = f.read()
        # except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        #     print("readElementsToList Error: file error!")
        #     return []
        # parser = MyHTMLParser()
        # parser.links = []
        # parser.contents = []
        # parser.feed(content)
        # # combine tag list and content list
        # ls = [{**dic, **dic_content} for dic, dic_content in zip(parser.links, parser.contents)]
        # return ls
        try: 
        #    with open(f_path) as f:
        #        content = f.read()
            parser = MyHTMLParser()
            parser.links = []
            parser.contents = []
            parser.feed(content)
            # combine tag list and content list
            ls = [{**dic, **dic_content} for dic, dic_content in zip(parser.links, parser.contents)]
            return ls
        except Exception:
            print("readElementsToList Exception")
            return []


    def createElement(self, content, uid, link_other, link_element, email, dt):
        print("")