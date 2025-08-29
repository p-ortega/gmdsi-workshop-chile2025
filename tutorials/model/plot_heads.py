import flopy
import matplotlib.pyplot as plt


sim = flopy.mf6.MFSimulation.load()
gwf = sim.get_model()
hds = flopy.utils.HeadFile("model.hds",model=gwf)
for totim in hds.get_times():
	hds.plot(totim=totim)
	plt.show()