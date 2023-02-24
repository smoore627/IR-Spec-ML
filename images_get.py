import requests 
from bs4 import BeautifulSoup
import chemicals

chemical_list = ['benzene',
                'p-xylene',
                'toluene',
                'hexane',
                'isoborneol',
                'methanol']

def resolveCAS(chemical_name):
    cas_num = chemicals.identifiers.CAS_from_any(chemical_name).replace('-','')
    return cas_num






for item in chemical_list:
    cas_res = resolveCAS(item)
    for i in range(3):
        ir_graph_1 = 'https://webbook.nist.gov/cgi/cbook.cgi?Spec=C' + str(cas_res) + '&Index=' + str(i) + '&Type=IR&Large=on'
        ir_graph_2 = 'https://webbook.nist.gov/cgi/inchi?Spec=C' + str(cas_res) + '&Index=' + str(i) + '&Type=IR&Large=on'
        image_1 = requests.get(ir_graph_1).content
        image_2 = requests.get(ir_graph_2).content
        with open('IR Spec Images/' + str(cas_res) + '_' + str(i) + '_cb.png', 'wb') as handler:  # change to specific path eventually
            handler.write(image_1) 
        with open('IR Spec Images/' + str(cas_res) + '_' + str(i) + '_in.png', 'wb') as handler: 
            handler.write(image_2)


