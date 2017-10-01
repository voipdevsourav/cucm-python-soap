from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor
from suds.client import Client
import ssl
cmserver = '192.168.231.60'
cmport = '8443'
wsdl = 'https://192.168.231.60:8443/realtimeservice/services/RisPort?wsdl'
location = 'https://' + cmserver + ':' + cmport + '/realtimeservice/services/RisPort'
username = 'CCMAdmin'
password = 'c1sc0'

ssl._create_default_https_context = ssl._create_unverified_context
tns = 'http://schemas.cisco.com/ast/soap/'
imp = Import('http://schemas.xmlsoap.org/soap/encoding/', 'http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add(tns)

client = Client(wsdl,location=location, username=username, password=password, plugins=[ImportDoctor(imp)])

result = client.service.SelectCmDevice('',{'SelectBy':'Name', 'Class':'Any'})
#result = client.service.SelectCmDevice('',{'SelectBy':'Name','Status':'Unknown',  'Class':'Phone'})

print result['SelectCmDeviceResult']['TotalDevicesFound']

for node in result['SelectCmDeviceResult']['CmNodes']:
    for device in node['CmDevices']:
        print device['Name'],device['Class'],device['IpAddress'], device['DirNumber'], device['Description'],device['Status']

