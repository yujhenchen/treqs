from src import parameters as param
from src.elements import Element


class TCElement(Element.Element):

    #def readContent(self, path):
    #    super().readContent(path, param.tc_columns)
    # def readContent(self, content):
    #     super().readContent(content, param.tc_columns)


    # def getContent(self):
    #     return super().getContent()
        

    # def prepareCustomIds(self):
    #     super().prepareCustomIds(param.link_element, param.tcReq)


    def writeContent(self, path):
        # sort datframe, custom_id desc
        try:
            super().sortDataFrame(param.custom_id)
            # loop dataframe, createElement into list
            df = super().getContent()
            fn = super().prepareWriteFile(path, param.tcReq)
            with open(fn, "w") as f:
                for index, row in df.iterrows():
                    #ls_prepared.append(self.createElement(row[param.content], row[param.uid], row[param.link_sr], row[param.link_element], row[param.email], row[param.date]))
                    f.write(row[param.custom_id]+" "+self.createElement(row[param.content], row[param.uid], row[param.link_sr], row[param.link_element], row[param.email], row[param.date])+param.sep_newline+param.sep_newline)
        except Exception:
            print("writeContent Exception")


    def createElement(self, content, uid, link_sr, link_element, email, dateTime):
        return (Element.element(content, id=uid, type=param.tcReq, link_sr=link_sr, link_element=link_element, email=email, date=dateTime))


    # def queryDataFrame(self, column_query, value_query):
    #     return super().queryDataFrame(column_query, value_query)


    # def queryAllDataFrame(self, value_query):
    #     return super().queryAllDataFrame(value_query)
        

    # def queryDuplicate(self, column):
    #     return super().queryDuplicate(column)