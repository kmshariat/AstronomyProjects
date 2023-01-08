#Mega Parsec to Cm distance conversion
def MpctoCm(D):
  return D*3.086*10**24

#Observed wavelength to sourced wavelenght conversion
def lembdaS(lembdaO,z):
  return lembdaO/(1+z)

#Observed intensity to sourced intensity conversion
def intensityS(intensityO,z):
  return intensityO*(1+z)

#Flux Density using stephan-boltzman law
def Ldensity(intensityS,D):
  d = MpctoCm(D)
  return intensityS*(4*3.1416*d**2)
