from _treqs import parameters as param
from _treqs.elements import Requirement


class USRequirement(Requirement.Requirement):

    #def readContent(self, path):
    #    super().readContent(path, param.us_columns)
    # def readContent(self, content):
    #     super().readContent(content, param.us_columns)


    # def getContent(self):
    #     return super().getContent()


    # def prepareCustomIds(self):
    #     super().prepareCustomIds(param.link_element, param.usReq)


    def writeContent(self, path):
        # sort datframe, custom_id desc
        try:
            super().sortDataFrame(param.custom_id)
            # loop dataframe, createElement into list
            df = super().getContent()
            fn = super().prepareWriteFile(path, param.usReq)
            with open(fn, "w") as f:
                for index, row in df.iterrows():
                    # ls_prepared.append(self.createElement(row[param.content], row[param.uid], row[param.link_element], row[param.email], row[param.date]))
                    f.write(row[param.custom_id]+" "+self.createElement(row[param.content], row[param.uid], row[param.link_element], row[param.email], row[param.date])+param.sep_newline+param.sep_newline)
        except Exception:
            print("writeContent Exception")


    def createElement(self, content, uid, link_element, email, dateTime):
        return (Requirement.element(content, id=uid, type=param.usReq, link_element=link_element, email=email, date=dateTime))

    
    # def queryDataFrame(self, column_query, value_query):
    #     return super().queryDataFrame(column_query, value_query)


    # def queryAllDataFrame(self, value_query):
    #     return super().queryAllDataFrame(value_query)


    # def queryDuplicate(self, column):
    #     return super().queryDuplicate(column)