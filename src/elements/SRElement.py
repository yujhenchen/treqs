from src import parameters as param
from src.elements import Element


class SRElement(Element.Element):

    def write_content(self, path):
        # sort datframe, custom_id desc
        try:
            super().sort_dataframe(param.CUSTOM_ID)
            # loop dataframe, create_element into list
            df = super().get_content()
            fn = super().prepare_write_file(path, param.SR_REQ)
            with open(fn, "w") as f:
                for index, row in df.iterrows():
                    #ls_prepared.append(self.create_element(row[param.CONTENT], row[param.UID], row[param.LINK_US], row[param.LINK_ELEMENT], row[param.EMAIL], row[param.DATE]))
                    f.write(row[param.CUSTOM_ID]+" "+self.create_element(row[param.CONTENT], row[param.UID], row[param.LINK_US], row[param.LINK_ELEMENT], row[param.EMAIL], row[param.DATE])+param.SEP_NEWLINE+param.SEP_NEWLINE)
        except Exception:
            print("write_content Exception")
        

    def create_element(self, content, uid, link_us, link_element, email, dateTime):
        return (Element.element(content, id=uid, type=param.SR_REQ, link_us=link_us, link_element=link_element, email=email, date=dateTime))