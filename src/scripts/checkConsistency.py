from src import parameters as param
from src import utilities
from src.scripts import Consistency


def check():
    bool_us = utilities.string_to_bool(input("Check user stories? (y or n):"))
    bool_sr = utilities.string_to_bool(input("Check system requirement? (y or n):"))
    bool_qr = utilities.string_to_bool(input("Check quality requirement? (y or n):"))
    bool_tc = utilities.string_to_bool(input("Check test case? (y or n):"))
    
    consist = Consistency.Consistency()
    req_dir = input("Elements files directory:")
    consist.set_req_files_dir(req_dir)
    consist.creat_log_file()
    ls_b = []
    if bool_us:
        ls_b.append(consist.check(param.US_REQ))
    if bool_sr:
        ls_b.append(consist.check(param.SR_REQ, param.US_REQ, param.LINK_US))
    if bool_qr:
        ls_b.append(consist.check(param.QR_REQ, param.SR_REQ, param.LINK_SR))
    if bool_tc:
        ls_b.append(consist.check(param.TC_REQ, param.SR_REQ, param.LINK_SR))
        # check testcode
        consist.prepare_test()
        ls_b.append(consist.check(param.TC_REQ, param.SR_REQ, param.LINK_SR))
   
    if False in ls_b:
        print("Consistency checking failed! Please check summary file")
    else:
        print("Consistency checking successed!")