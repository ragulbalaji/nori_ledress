import machine, neopixel, socket, time, urandom
machine.freq(160000000)

np = neopixel.NeoPixel(machine.Pin(15), 20)

# Green Init Light
np[1] = (0, 128, 0)
np.write()

def handleREQ(r):
	if(r.startswith("/TEST")):
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