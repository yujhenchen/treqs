from src import parameters as param
from src.elements import USElement, SRElement, TCElement, QRElement#, mATElement


class UseElement:

    def __init__(self):
        self.usElement = USElement.USElement()
        self.reqElement = SRElement.SRElement()
        self.qrElement = QRElement.QRElement()
        self.tcElement = TCElement.TCElement()

    
    def set_content(self, requirement, df):
        if(requirement == param.US_REQ):
            return self.usElement.set_content(df)
        if(requirement == param.SR_REQ):
            return self.reqElement.set_content(df)
        if(requirement == param.QR_REQ):
            return self.qrElement.set_content(df)
        if(requirement == param.TC_REQ):
            return self.tcElement.set_content(df)

    
    def get_content(self, requirement):
        if(requirement == param.US_REQ):
            return self.usElement.get_content()
        if(requirement == param.SR_REQ):
            return self.reqElement.get_content()
        if(requirement == param.QR_REQ):
            return self.qrElement.get_content()
        if(requirement == param.TC_REQ):
            return self.tcElement.get_content()


    def read_content(self, requirement, content):
        if(requirement == param.US_REQ):
            self.usElement.read_content(content, param.US_COLUMNS)
        if(requirement == param.SR_REQ):
            self.reqElement.read_content(content, param.SR_COLUMNS)
        if(requirement == param.QR_REQ):
            self.qrElement.read_content(content, param.QR_COLUMNS)
        if(requirement == param.TC_REQ):
            self.tcElement.read_content(content, param.TC_COLUMNS)


    def create_element(self, content, uid, requirement, link_other, link_element, email, dateTime):
        if(requirement == param.US_REQ):
            return self.usElement.create_element(content, uid, link_element, email, dateTime)
        if(requirement == param.SR_REQ):
            return self.reqElement.create_element(content, uid, link_other, link_element, email, dateTime)
        if(requirement == param.QR_REQ):
            return self.qrElement.create_element(content, uid, link_other, link_element, email, dateTime)
        if(requirement == param.TC_REQ):
            return self.tcElement.create_element(content, uid, link_other, link_element, email, dateTime)


    def prepare_customids(self, requirement):
        if(requirement == param.US_REQ):
            self.usElement.prepare_customids(param.US_REQ)
        if(requirement == param.SR_REQ):
            self.reqElement.prepare_customids(param.SR_REQ)
        if(requirement == param.QR_REQ):
            self.qrElement.prepare_customids(param.QR_REQ)
        if(requirement == param.TC_REQ):
            self.tcElement.prepare_customids(param.TC_REQ)


    def write_content(self, requirement, path):
        if(requirement == param.US_REQ):
            self.usElement.write_content(path)
        if(requirement == param.SR_REQ):
            self.reqElement.write_content(path)
        if(requirement == param.QR_REQ):
            self.qrElement.write_content(path)
        if(requirement == param.TC_REQ):
            self.tcElement.write_content(path)