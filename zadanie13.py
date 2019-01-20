import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import aseegg as ag

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 10

dane = pd.read_csv("sub-02_trial-03.csv", delimiter=',', engine='python')

czProbkowania=200
t = np.linspace (0, 38.01, czProbkowania*38.01)
sygnal=dane['sygnal']
plt.plot(t, sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

przefiltrowany1 = ag.pasmowozaporowy(sygnal, czProbkowania, -0.115, -0.123)
przefiltrowany2 = ag.pasmowoprzepustowy(przefiltrowany1, czProbkowania, -0.115, -0.110)

plt.plot(t, przefiltrowany2)
plt.show()
