import os
import socket
import random

def number_to_domain(number):
    domain = ""
    while number > 0:
        number, remainder = divmod(number - 1, 26)
        domain = chr(65 + remainder) + domain
    return domain

#print(number_to_domain(28))


#generate domains using uniform distribution
def generate_domains (samples, k):
	Nk = 0
	for i in range(1, k+1):
		Nk += 26**i
	for i in range(0, samples):
		try:
			i = "www." + number_to_domain(int(random.uniform(1, Nk))) + ".ufrj.br"
			socket.gethostbyname(i.strip())
			print(i + " exists")
		except socket.gaierror:
			print "unable to get address for", i

generate_domains(10, 2)