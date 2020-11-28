
#from getmac import get_mac_address
from playsound import playsound
import nmap

already_entered=[]
#ew_entry=get_mac_address(ip='192.168.0.2')
#already_entered.append(new_entry)
#print('welcome'+new_entry)

nmap_var= nmap.PortScanner()
while True:  
    nmap_var.scan(hosts='192.168.0.1/24',arguments='-sn')
    newHostList=nmap_var.all_hosts()
    if len(already_entered)>0:
        len1=len(already_entered)
        len2=len(newHostList)
        if len1<len2:
            print('new device',already_entered,'->',newHostList)
            playsound('explode.wav')
            already_entered=newHostList
        elif len1>len2:
            print('device left',already_entered,'->',newHostList)
            playsound('goodbye.wav')
            already_entered=newHostList
            
        else:
            already_entered=newHostList
            
    else:
        already_entered=newHostList
        print('start')
    
    
        
    




