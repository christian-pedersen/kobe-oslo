import h5py
import numpy as np
import pylab as plt


phisp = h5py.File('../case4/phisp000-000.h5','r')
phisp = phisp['/phisp0000']
phisp = phisp[:,:,:]
phisp = np.transpose(phisp,(2,1,0))


emph = np.linspace(-64,64, 129)[::-1]
dx = 1.0E-2

induced_phi = emph*2.08*dx

plt.figure()

plt.plot(phisp[:,64,64])#-induced_phi)
#plt.plot(induced_phi)

plt.show()