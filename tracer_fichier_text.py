import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Lire les fichiers de traces et extraire les données des colonnes spécifiques

# Lire les données du fichier de traces
df = pd.read_csv('DlDataSinr.txt', delimiter='\t')

# Extraire les colonnes spécifiques 
time = df["Time"].tolist()  
SINR = df["SINR(dB)"].tolist()  

#next step: calculer le SINR moyen pour chaque simulation et nouvelle distance

# Tracer la courbe 
plt.plot(time, SINR)
plt.xlabel('Time(s)')
plt.ylabel('SINR (dB)')
plt.title('SINR=f(Time)')
plt.grid(True)
plt.show()



