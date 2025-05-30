# Paso 1: Cargar las librerias necesarias y los datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Crear un conjunto de datos ficticio
data = {
    'Matematica': np.random.randint(50, 100, size=100),
    'Fisica': np.random.randint(40, 95, size=100),
    'Quimica': np.random.randint(45, 90, size=100),
    'Biologia': np.random.randint(50, 100, size=100),
}

df = pd.DataFrame(data)

# Paso 2: Descripcion general de los datos
print("Primeras filas del conjunto de datos:")
print(df.head())

print("\nResumen estadístico de las variables numericas:")
print(df.describe())

print("\nInformacion sobre el tipo de datos y valores nulos:")
df.info()  # No necesitas poner print()

# Paso 3: Medidas de tendencia central y dispersión
print("\nMedidas de tendencia central:")
print(f"Media:\n{df.mean()}")
print(f"Mediana:\n{df.median()}")
print(f"Moda:\n{df.mode().iloc[0]}")

print("\nMedidas de dispersion:")
print(f"Desviacion estandar:\n{df.std()}")
print(f"Varianza:\n{df.var()}")
print(f"Minimo:\n{df.min()}")
print(f"Maximo:\n{df.max()}")

# Paso 4: Visualizacion de los datos

# Histograma
plt.figure(figsize=(12, 8))
df.hist(bins=10, edgecolor='black', grid=False, figsize=(10, 8))
plt.suptitle('Histograma de las calificaciones', size=16)
plt.tight_layout()
plt.show()

# Boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(data=df)
plt.title('Boxplot de las calificaciones', size=16)
plt.show()

# Diagramas de dispersión
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Diagramas de dispersión entre Asignaturas', size=16, y=1.02)
plt.show()


