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

cas_res = resolveCAS(chemical_list[0])
liquid_ir = 'https://webbook.nist.gov/cgi/cbook.cgi?Spec=C' + str(cas_res) + '&Index=2&Type=IR&Large=on'




for item in chemical_list:
    cas_res = resolveCAS(item)
    liquid_ir = 'https://webbook.nist.gov/cgi/cbook.cgi?Spec=C' + str(cas_res) + '&Index=2&Type=IR&Large=on'
    solution = 'https://webbook.nist.gov/cgi/cbook.cgi?Spec=C' + str(cas_res) + '&Index=1&Type=IR&Large=on'
    solution_ir = 'https://webbook.nist.gov/cgi/inchi?Spec=C' + str(cas_res) + '&Index=2&Type=IR&Large=on'
    gas_ir = 'https://webbook.nist.gov/cgi/inchi?Spec=C' + str(cas_res) + '&Index=1&Type=IR&Large=on'
    
    html_text = requests.get(liquid_ir).content

    with open('onion.png', 'wb') as handler: 

       handler.write(html_text) 


