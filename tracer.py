import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Lire les fichiers de traces et extraire les données des colonnes spécifiques

# Lire les données du débit et du nombre d'UE à partir du fichier de traces
df = pd.read_csv('output.csv')

# Extraire les colonnes spécifiques 
distance = df.iloc[:, 0].tolist()  # Assuming distance data is in the first column (index 0)
latency = df.iloc[:, 1].tolist()  # Assuming n is in the second column (index 2)


# Tracer la courbe 
plt.plot(distance, latency)
plt.xlabel('Distance (m)')
plt.ylabel('latency (µs)')
plt.title('Latency=f(distance)')
plt.grid(True)
plt.show()
