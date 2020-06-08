# information of developer
USER  = "user"
EMAIL  = "email"

# requirement types
US_REQ = "US"
SR_REQ = "SR"
QR_REQ = "QR"
TC_REQ = "TC"
AT_REQ = "AT"

# column (array format)
US_COLUMNS = ['id', 'type', 'content', 'link_element', 'email', 'date']
SR_COLUMNS = ['id', 'type', 'content', 'link_us', 'link_element', 'email', 'date']
QR_COLUMNS = ['id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']
TC_COLUMNS = ['id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']

# column (generate custom_id and write)
US_COLUMNS_wr = ['id', 'custom_id', 'type', 'content', 'link_element', 'email', 'date']
SR_COLUMNS_wr = ['id', 'custom_id', 'type', 'content', 'link_us', 'link_element', 'email', 'date']
QR_COLUMNS_wr = ['id', 'custom_id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']
TC_COLUMNS_wr = ['id', 'custom_id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']

# key words
ROOT_ID = 'root'
UID = 'id'
CUSTOM_ID = 'custom_id'
CONTENT ='content'
DATE = 'date'
LINK_US = 'link_us'
LINK_SR = 'link_sr'
LINK_ELEMENT = 'link_element'
FILE_NAME = 'file_name'

SEP_NEWLINE = '\n'
SEP_DOT = '.'
EMPTY = 'null'
EMPTY_STR = ''
ELEMENT_BEGIN = '<element'
ELEMENT_END = '</element>'

INDEX_ZERO = 0