from src import parameters
from src.elements import USElement, SRElement, TCElement, QRElement#, mATElement


class UseElement:

    def __init__(self):
        self.usElement = USElement.USElement()
        self.reqElement = SRElement.SRElement()
        self.qrElement = QRElement.QRElement()
        self.tcElement = TCElement.TCElement()

    
    def setContent(self, requirement, df):
        if(requirement == parameters.usReq):
            return self.usElement.setContent(df)
        if(requirement == parameters.srReq):
            return self.reqElement.setContent(df)
        if(requirement == parameters.qrReq):
            return self.qrElement.setContent(df)
        if(requirement == parameters.tcReq):
            return self.tcElement.setContent(df)

    
    def getContent(self, requirement):
        if(requirement == parameters.usReq):
            return self.usElement.getContent()
        if(requirement == parameters.srReq):
            return self.reqElement.getContent()
        if(requirement == parameters.qrReq):
            return self.qrElement.getContent()
        if(requirement == parameters.tcReq):
            return self.tcElement.getContent()


    def readContent(self, requirement, content):
        if(requirement == parameters.usReq):
            self.usElement.readContent(content, parameters.us_columns)
        if(requirement == parameters.srReq):
            self.reqElement.readContent(content, parameters.sr_columns)
        if(requirement == parameters.qrReq):
            self.qrElement.readContent(content, parameters.qr_columns)
        if(requirement == parameters.tcReq):
            self.tcElement.readContent(content, parameters.tc_columns)


    def createElement(self, content, uid, requirement, link_other, link_element, email, dateTime):
        if(requirement == parameters.usReq):
            return self.usElement.createElement(content, uid, link_element, email, dateTime)
        if(requirement == parameters.srReq):
            return self.reqElement.createElement(content, uid, link_other, link_element, email, dateTime)
        if(requirement == parameters.qrReq):
            return self.qrElement.createElement(content, uid, link_other, link_element, email, dateTime)
        if(requirement == parameters.tcReq):
            return self.tcElement.createElement(content, uid, link_other, link_element, email, dateTime)


    def prepareCustomIds(self, requirement):
        if(requirement == parameters.usReq):
            self.usElement.prepareCustomIds(parameters.usReq)
        if(requirement == parameters.srReq):
            self.reqElement.prepareCustomIds(parameters.srReq)
        if(requirement == parameters.qrReq):
            self.qrElement.prepareCustomIds(parameters.qrReq)
        if(requirement == parameters.tcReq):
            self.tcElement.prepareCustomIds(parameters.tcReq)


    def writeContent(self, requirement, path):
        if(requirement == parameters.usReq):
            self.usElement.writeContent(path)
        if(requirement == parameters.srReq):
            self.reqElement.writeContent(path)
        if(requirement == parameters.qrReq):
            self.qrElement.writeContent(path)
        if(requirement == parameters.tcReq):
            self.tcElement.writeContent(path)