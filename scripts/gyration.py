import numpy as np

def thermal_velocity(k, T, m_e):
	v = 3*(k*T/m_e)
	v =np.sqrt(v)
	# v = 8 *k * T/(np.pi*m_e)
	return v


def gyration_radius(m_e, q, B, v):
	rho_c = m_e*v/(q*B)
	return np.abs(rho_c)

# #Variables Run 1
# B = 50E-6
# T_ph = 3.48E4

# #Variables Run 2
# B = 50E-6
# T_ph = 3.48E5

#Variables MEO
B = 8.6E-7
T_ph = 3.48E4

#Constants
m_e = 9.10938E-31
q = 1.602177E-19
e = -q
k = 1.3806E-23


v = thermal_velocity(k, T_ph, m_e)

rho_c = gyration_radius(m_e, e, B, v)


# print v
print rho_c
