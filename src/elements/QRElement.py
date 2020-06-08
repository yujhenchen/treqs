from src import parameters as param
from src.elements import Element


class QRElement(Element.Element):

    def write_content(self, path):
        try:
            # sort datframe, custom_id desc
            super().sort_dataframe(param.CUSTOM_ID)
            # loop dataframe, create_element into list
            df = super().get_content()
            fn = super().prepare_write_file(path, param.QR_REQ)
            with open(fn, "w") as f:
                for index, row in df.iterrows():
                # ls_prepared.append(self.create_element(row[param.CONTENT], row[param.UID], row[param.LINK_SR], row[param.LINK_ELEMENT], row[param.EMAIL], row[param.DATE]))
                    f.write(row[param.CUSTOM_ID]+" "+self.create_element(row[param.CONTENT], row[param.UID], row[param.LINK_SR], row[param.LINK_ELEMENT], row[param.EMAIL], row[param.DATE])+param.SEP_NEWLINE+param.SEP_NEWLINE)
        except Exception:
            print("write_content Exception")


    def create_element(self, content, uid, link_sr, link_element, email, dateTime):
        return (Element.element(content, id=uid, type=param.QR_REQ, link_sr=link_sr, link_element=link_element, email=email, date=dateTime))