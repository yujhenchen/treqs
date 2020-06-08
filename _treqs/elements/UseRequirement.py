from _treqs import parameters
from _treqs.elements import USRequirement, SRRequirement, TCRequirement, QRRequirement#, mATRequirement


class UseRequirement:

    def __init__(self):
        self.usRequirement = USRequirement.USRequirement()
        self.reqRequirement = SRRequirement.SRRequirement()
        self.qrRequirement = QRRequirement.QRRequirement()
        self.tcRequirement = TCRequirement.TCRequirement()

    
    def setContent(self, requirement, df):
        if(requirement == parameters.usReq):
            return self.usRequirement.setContent(df)
        if(requirement == parameters.srReq):
            return self.reqRequirement.setContent(df)
        if(requirement == parameters.qrReq):
            return self.qrRequirement.setContent(df)
        if(requirement == parameters.tcReq):
            return self.tcRequirement.setContent(df)

    
    def getContent(self, requirement):
        if(requirement == parameters.usReq):
            return self.usRequirement.getContent()
        if(requirement == parameters.srReq):
            return self.reqRequirement.getContent()
        if(requirement == parameters.qrReq):
            return self.qrRequirement.getContent()
        if(requirement == parameters.tcReq):
            return self.tcRequirement.getContent()


    def readContent(self, requirement, content):
        if(requirement == parameters.usReq):
            self.usRequirement.readContent(content, parameters.us_columns)
        if(requirement == parameters.srReq):
            self.reqRequirement.readContent(content, parameters.sr_columns)
        if(requirement == parameters.qrReq):
            self.qrRequirement.readContent(content, parameters.qr_columns)
        if(requirement == parameters.tcReq):
            self.tcRequirement.readContent(content, parameters.tc_columns)


    def createElement(self, content, uid, requirement, link_other, link_element, email, dateTime):
        if(requirement == parameters.usReq):
            return self.usRequirement.createElement(content, uid, link_element, email, dateTime)
        if(requirement == parameters.srReq):
            return self.reqRequirement.createElement(content, uid, link_other, link_element, email, dateTime)
        if(requirement == parameters.qrReq):
            return self.qrRequirement.createElement(content, uid, link_other, link_element, email, dateTime)
        if(requirement == parameters.tcReq):
            return self.tcRequirement.createElement(content, uid, link_other, link_element, email, dateTime)


    def prepareCustomIds(self, requirement):
        if(requirement == parameters.usReq):
            self.usRequirement.prepareCustomIds(parameters.usReq)
        if(requirement == parameters.srReq):
            self.reqRequirement.prepareCustomIds(parameters.srReq)
        if(requirement == parameters.qrReq):
            self.qrRequirement.prepareCustomIds(parameters.qrReq)
        if(requirement == parameters.tcReq):
            self.tcRequirement.prepareCustomIds(parameters.tcReq)


    def writeContent(self, requirement, path):
        if(requirement == parameters.usReq):
            self.usRequirement.writeContent(path)
        if(requirement == parameters.srReq):
            self.reqRequirement.writeContent(path)
        if(requirement == parameters.qrReq):
            self.qrRequirement.writeContent(path)
        if(requirement == parameters.tcReq):
            self.tcRequirement.writeContent(path)