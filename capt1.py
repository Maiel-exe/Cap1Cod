import numpy as np
import matplotlib.pyplot as plt

# Define um eixo de tempo(teste ok)
time = np.linspace(0, 2 * np.pi, 500)
f = 1

# Define as ondas senoidais para a Figura 2.5a:
# Mesma amplitude (1), em fase (deslocamento de 0)
onda_a1 = np.sin(f * time)
onda_a2 = np.sin(2 * f * time)
soma_onda_a = onda_a1 + onda_a2

# Plota os gráficos
plt.figure(figsize=(8, 6))
plt.plot(time, onda_a1, label='$sin(t)$')
plt.plot(time, onda_a2, label='$sin(2t)$')
plt.plot(time, soma_onda_a, label='Soma', linewidth=2, linestyle='--')
plt.title('Figura 2.5a: Soma de duas ondas senoidais em fase')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('figure_2_5a.png')