import requests 
from bs4 import BeautifulSoup
import chemicals

chemical_list = ['benzene',
                'p-xylene',
                'toluene',
                'hexane',
                'isoborneol']

def resolveCAS(chemical_name):
    cas_num = chemicals.identifiers.CAS_from_any(chemical_name).replace('-','')
    return cas_num



for item in chemical_list:
    cas_res = resolveCAS(item)
    liquid_ir = 'https://webbook.nist.gov/cgi/cbook.cgi?Spec=C' + str(cas_res) + '&Index=2&Type=IR&Large=on'
    print(cas_res,': liquid ir: ', liquid_ir)
    
    


