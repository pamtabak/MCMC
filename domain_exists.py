import os
import socket
import random
import matplotlib.pyplot as plt

def number_to_domain(number):
    domain = ""
    while number > 0:
        number, remainder = divmod(number - 1, 26)
        domain = chr(65 + remainder) + domain
    return domain

#print(number_to_domain(28))


#generate domains using uniform distribution
def generate_domains (samples, k):
	Ak = 0
	Nk = 0
	for i in range(1, k+1):
		Nk += 26**i
	for i in range(0, samples):
		try:
			i = "www." + number_to_domain(int(random.uniform(1, Nk))) + ".ufrj.br"
			socket.gethostbyname(i.strip())
			#print(i + " exists")
			Ak += 1
		except socket.gaierror:
			# do nothing
			Ak = Ak
			#print "unable to get address for", i
	return Ak

sample_sizes = [1, 10, 100, 500, 1000, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 7500, 8000, 9000, 10000]
#k_sizes 	 = [2, 3, 4, 5]
k_sizes = [4]
k_colors     = ['ro', 'bo', 'yo', 'go']
for k in range(0, len(k_sizes)):
	for s in sample_sizes:
		plt.plot (generate_domains(s, k_sizes[k]), s, k_colors[k])
plt.ylabel('Numero de Amostras')
plt.xlabel('Quantidade de dominios encontrados')
plt.show()