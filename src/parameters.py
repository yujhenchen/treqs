# information of developer
user  = "user"
email  = "email"

# requirement types
usReq = "US"
srReq = "SR"
qrReq = "QR"
tcReq = "TC"
atReq = "AT"

# column (array format)
us_columns = ['id', 'type', 'content', 'link_element', 'email', 'date']
sr_columns = ['id', 'type', 'content', 'link_us', 'link_element', 'email', 'date']
qr_columns = ['id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']
tc_columns = ['id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']

# column (generate custom_id and write)
us_columns_wr = ['id', 'custom_id', 'type', 'content', 'link_element', 'email', 'date']
sr_columns_wr = ['id', 'custom_id', 'type', 'content', 'link_us', 'link_element', 'email', 'date']
qr_columns_wr = ['id', 'custom_id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']
tc_columns_wr = ['id', 'custom_id', 'type', 'content', 'link_sr', 'link_element', 'email', 'date']

# key words
root_id = 'root'
uid = 'id'
custom_id = 'custom_id'
content ='content'
date = 'date'
link_us = 'link_us'
link_sr = 'link_sr'
link_element = 'link_element'
file_name = 'file_name'

sep_newline = '\n'
sep_dot = '.'
empty = 'null'
empty_str = ''
element_begin = '<element'
element_end = '</element>'

index_zero = 0