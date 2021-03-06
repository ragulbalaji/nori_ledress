import machine, neopixel, socket, time, urandom, math
machine.freq(160000000)

numLEDs = 8

np = neopixel.NeoPixel(machine.Pin(15), numLEDs)

# Green Init Light
np[1] = (0, 128, 0)
np.write()

def stoi(str):
	return int(math.floor(float(str)))

def handleREQ(r):
	if(r.startswith("/FILL")):
		t = r.split("/FILL")[1].split(",")
		c = ( stoi(t[0]), stoi(t[1]), stoi(t[2]) )
		np.fill(c)
		np.write()
	elif(r.startswith("/HEARTSTART")):
		while True:
			for i in range(-255, 255, 10):                                                                                                            
				np.fill((abs(i),abs(i),abs(i)))                                                                                                       
				np.write()                                                                                                                            
				time.sleep(0.1)
	elif(r.startswith("/SPARKSTART")):
		while True:
			led = urandom.getrandbits(4) % numLEDs
			np.fill((0,0,0))
			for i in range(-255, 255, 10):                                                                                                            
				np[led] = (abs(i),abs(i),abs(i))                                                                                                    
				np.write()                                                                                                                            
				time.sleep(0.02)
	elif(r.startswith("/CLEAR")):
		np.fill((0,0,0))
		np.write()
	elif(r.startswith("/TEST")):
		np[1] = (urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8))
		np.write()


addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
	text = ''
	cl, addr = s.accept()
	cl_file = cl.makefile('rwb', 0)
	while True:
		line = str(cl_file.readline(), 'utf8')
		if not line or not line.startswith("GET"):
			break
		print((addr[0], line))
		req = line.split()[1]
		handleREQ(req)
	cl.send("OK")
	cl.close()
