import os
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
        #if data == param.SEP_NEWLINE:
        if data.rstrip() == "":
            return
        dic = {param.CONTENT: data}
        self.contents.append(dic)



class Element(object):
    def __init__(self):
        self.df = pd.DataFrame()


    def read_content(self, content, columns_f):
        # get list of file content and convert into pandas table
        ls_row = []
        ls_elements = self.read_elements_to_list(content)
        try:
            for map_item in ls_elements:
                ls_row_item = [map_item[item] for item in columns_f]
                ls_row.append(ls_row_item)
            self.df = pd.DataFrame(ls_row, columns = columns_f)
        except Exception:
            print("read_content Exception")


    def set_content(self, df):
        self.df = df


    def get_content(self):
        return self.df

# ============================================================
    # def query_dataFrame(self, column_query, value_query):
    #     try:
    #         return self.df.loc[self.df[column_query] == value_query]
    #     except Exception:
    #         print("query_dataFrame Exception")    


    # def query_all_dataFrame(self, value_query):
    #     try:
    #         return self.df[self.df.isin([value_query]).any(axis=1)]
    #     except Exception:
    #         print("query_all_dataFrame Exception") 


    # def query_duplicate(self, column):
    #     try:
    #         return self.df[self.df.duplicated([column], keep=False)]
    #     except Exception:
    #         print("query_duplicate Exception") 


    # def query_self_missing(self, column, column_target):
    #     try:
    #         return self.df[self.df.apply(lambda x: x[column] not in x[column_target], axis=1)]
    #     except Exception:
    #         print("query_self_missing Exception") 
# ============================================================


    def sort_dataframe(self, col_sort):
        self.df = self.df.sort_values(by=[col_sort])


    def update_customid(self, parent, custom_id_req_type, column_parent):
        id_count = 1
        # get row ids which column link_sr == parent
        ls_idx = self.df.index[self.df[column_parent] == parent].tolist()
        for idx in ls_idx:
            self.df.loc[idx, param.CUSTOM_ID] = custom_id_req_type + str(id_count)
            id_count = id_count + 1


    def prepare_customids(self, id_req_type):
        try:
            # reset all custom_ids
            self.df[param.CUSTOM_ID] = param.EMPTY
            #print((self.df_SR.loc[self.df_SR[param.LINK_SR] == param.ROOT_ID]))
    
            # list unique parent
            ls_parent = self.df[param.LINK_ELEMENT].unique()
            # get custom_id of parent
            for parent in ls_parent:
                if parent == param.ROOT_ID:
                    custom_id_req_type = id_req_type
                else:
                    custom_id_req_type = self.df.loc[self.df[param.UID] == parent, param.CUSTOM_ID].values[0] + param.SEP_DOT
                self.update_customid(parent, custom_id_req_type, param.LINK_ELEMENT)
        except Exception:
            print("prepare_customids Exception")


    def prepare_write_file(self, path, requirement):
        str_date = utilities.get_datetime(True)
        try:
            dir_path = os.path.split(path)
            return dir_path[param.INDEX_ZERO]+"/"+requirement+"_"+str_date+".md"
        except Exception:
            print("prepare_write_file Exception")
            return path+requirement+str_date+".md"
        
    
    def write_content(self):
        print("")


    def format_data(self):
        print("")


    # read _.md file
    def read_elements_to_list(self, content):
        try: 
            parser = MyHTMLParser()
            parser.links = []
            parser.contents = []
            parser.feed(content)
            # combine tag list and content list
            ls = [{**dic, **dic_content} for dic, dic_content in zip(parser.links, parser.contents)]
            return ls
        except Exception:
            print("read_elements_to_list Exception")
            return []


    def create_element(self, content, uid, link_other, link_element, email, dt):
        print("")