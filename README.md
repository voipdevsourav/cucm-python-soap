cisco callmanager device status list from serviceability api


wsdl = 'https://192.168.231.60:8443/realtimeservice/services/RisPort?wsdl'
location = 'https://' + cmserver + ':' + cmport + '/realtimeservice/services/RisPort'
run the program and get similar output as below

root@ubuntu-VirtualBox:~/axl# python axlcucm.py

total device found 7
SEP000C295D19D3 Phone 192.168.231.1 1119-UnRegistered SEP000C295D19D3 UnRegistered
cvp SIP Trunk 192.168.231.60 None None Unknown
gw SIP Trunk 192.168.231.60 None None Unknown
ANN_2 MediaResources 192.168.231.60 None ANN_cucm8 UnRegistered
CFB_2 MediaResources 192.168.231.60 None CFB_cucm8 UnRegistered
MOH_2 MediaResources 192.168.231.60 None MOH_cucm8 UnRegistered
MTP_2 MediaResources 192.168.231.60 None MTP_cucm8 UnRegistered
