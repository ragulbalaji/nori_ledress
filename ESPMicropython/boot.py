# ragulbalaji <3 2017
import esp
esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

#import network
#sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
#sta_if.connect("PHONEAPNAME", "<password>")                                                                                                 
#ap_if = network.WLAN(network.AP_IF)
#ap_if.config(essid="H4CKER", authmode=network.AUTH_WPA_WPA2_PSK, password="CHANGEMEPLS")

def execfile(f):
    exec(open(f).read())