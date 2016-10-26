import numpy as np
import matplotlib.pyplot as mpl

A = 0.1*0.1*0.1
k_b = 1.381*10**(-23) # m^2 kg s^-2 K^-1
T_i = 1500. #k 5000 for MEO
T_e = 3000. #K 5000 for MEO
T_ph = 5000.
n_ph = 1.0*10**(2)
n_i = (1.0*10**(5))/(500 + 1) # density. # ratio +1. 3d2 for MEO
n_e = n_i
e = 1.6*10**(-19)
m_e = 9.1*10**(-31)
m_i = 500*m_e 
v_bulk = 46000
phi_0 = 0

#OML
def erf(x):
	"""
	error function.
	"""
	points = 1000
	mesh = np.linspace(0,x,points) 
	integral = 0
	for i in range(points-1):
		#trapezodial integral
		integral += (mesh[i+1]-mesh[i])*((np.exp(-mesh[i+1]**2)+np.exp(-mesh[i]**2))/2.)
	return (2./np.sqrt(np.pi))*integral
	

def f(v,e,phi):
	"""
	streamingfunction from OML theory for streaming ions
	"""
	return np.sqrt(np.pi/4.)*v*((1+1./(2*v**2) + (e*phi)/(k_b*T_i*v**2))*erf(v) + 1./(np.sqrt(np.pi)*v)*np.exp(-v**2))

def I_e(phi):
	return -A*n_e*e*np.sqrt((8*k_b*T_e)/(np.pi*m_e))*np.exp((e*phi)/(k_b*T_e))

def I_i(phi):
	eta = v_bulk/np.sqrt((2.*k_b*T_i)/m_i)
	return A*n_i*e*np.sqrt((3.*k_b*T_i)/(m_i))*f(v_bulk,e,phi)

#def I_ph(phi):
#	return (1/6.)*A*n_ph*e*np.sqrt((8*k_b*T_ph)/(np.pi*m_e))*np.exp((e*phi)/(k_b*T_e))

"""
def I_e(phi):
	return -(1./4)*A*n_e*e*((8.*k_b*T_e)/(np.pi*m_e)+v_bulk)

def I_i(phi):
	return (1./4)*A*n_i*e*(np.sqrt((8.*k_b*T_i)/(np.pi*m_i))+v_bulk)*np.exp((-e*abs(phi-phi_0))/(k_b*T_i)) 
"""
phi = np.linspace(-30,10,1000)
array = np.zeros(1000)
for i in range(1,1000):
	array[i] = I_e(phi[i])+I_i(phi[i])
	#print I_i(phi[i])
	if array[i] < 0 and array[i-1] > 0:
		print phi[i]
	if array[i] > 0 and array[i-1] < 0:
		print phi[i]

mpl.plot(phi,array)
mpl.show()
