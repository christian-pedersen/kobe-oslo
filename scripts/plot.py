import h5py
import numpy as np
import pylab as plt
import mayavi as mlab


from mayavi import mlab

def plotPlanesOfGrid(name, grid):
	mlab.figure()
	im = mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(grid),
	                            plane_orientation='x_axes',
	                            slice_index=grid.shape[0]/2,
	                        )

	mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(grid),
	                            plane_orientation='y_axes',
	                            slice_index=grid.shape[1]/2,
	                        )
	mlab.title(name)
	mlab.colorbar(im)
	mlab.axes()

	return


rho_e = h5py.File('../run_sideways/rhoe.h5','r')
rho_e = rho_e['/rhoe0000']
rhoe = rho_e[:,:,:]
rhoe = np.transpose(rhoe,(2,1,0))

rhoi = h5py.File('../run_sideways/rhoi.h5','r')
rhoi = rhoi['/rhoi0000']
rhoi = rhoi[:,:,:]
rhoi = np.transpose(rhoi,(2,1,0))

rhop = h5py.File('../run_sideways/rhop.h5','r')
rhop = rhop['/rhop0000']
rhop = rhop[:,:,:]
rhop = np.transpose(rhop,(2,1,0))

phisp = h5py.File('../run_sideways/phisp.h5','r')
phisp = phisp['/phisp0000']
phisp = phisp[:,:,:]
phisp = np.transpose(phisp,(2,1,0))


plotPlanesOfGrid("rhoe", rhoe)
plotPlanesOfGrid("rhoi", rhoi)
plotPlanesOfGrid("rhop", rhop)
plotPlanesOfGrid("phi", phisp)


mlab.show()
#
# x = np.arange(rho.shape[0])
# y = np.arange(rho.shape[1])
#
# X,Y = np.meshgrid(x,y)
#
# rho = rho[:,59:69,:]
# print rho.shape
# rho = np.average(rho, axis = 1)
#
# fig, ax = plt.subplots(1)
# im = ax.contourf(X,Y,rho, 50)
#
# fig.subplots_adjust(bottom = 0.25)
# cbar_rho = fig.add_axes([0.10, 0.05, 0.8, 0.10])
# fig.colorbar(im, cax=cbar_rho, orientation = "horizontal")

plt.show()
