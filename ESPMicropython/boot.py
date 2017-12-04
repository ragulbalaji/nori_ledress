# ragulbalaji <3 2017
import esp
esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

def execfile(f):
    exec(open(f).read())