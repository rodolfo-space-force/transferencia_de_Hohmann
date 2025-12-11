#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/


import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dados de entrada
print('Transferência de Hohmann\n')

# Constantes
raio_terra = 6371  # Raio médio da Terra em km

# Parâmetros da órbita
r1 = float(input("Digite o raio da órbita inicial (r1) em km: "))  # Órbita inicial (perigeu, menor raio)
r2 = float(input("Digite o raio da órbita final (r2) em km: "))    # Órbita final (apogeu, maior raio)

# Cálculos para a órbita de transferência de Hohmann
a_transfer = (r1 + r2) / 2  # Semi-eixo maior da órbita de transferência
b_transfer = math.sqrt(r1 * r2)  # Semi-eixo menor da órbita de transferência

# Visualização gráfica da transferência de Hohmann
fig, ax = plt.subplots()

# Desenhando a Terra no centro
terra = plt.Circle((0, 0), raio_terra, color='blue', label='Terra', alpha=0.6)

# Desenhando as órbitas circulares inicial e final
orbita_inicial = plt.Circle((0, 0), r1, edgecolor='black', facecolor='none', lw=2, label='Órbita Inicial (r1)')
orbita_final = plt.Circle((0, 0), r2, edgecolor='red', facecolor='none', lw=2, label='Órbita Final (r2)')

# Desenhando a órbita de transferência Hohmann (elipse)
ellipse_hohmann = patches.Ellipse(((r2 - r1) / 2, 0), width=r2 + r1, height=2 * b_transfer, 
                                  edgecolor='orange', facecolor='none', lw=2, label='Órbita Transferência Hohmann')

# Adicionando a Terra, as órbitas e a elipse de transferência ao gráfico
ax.add_patch(terra)
ax.add_patch(orbita_inicial)
ax.add_patch(ellipse_hohmann)
ax.add_patch(orbita_final)


# Plotando o perigeu e apogeu corretamente
plt.scatter([-r1], [0], color='yellow', label='Perigeu (r1)', zorder=5)  # Perigeu ajustado para 180°
plt.scatter([r2], [0], color='green', label='Apogeu (r2)', zorder=5)  # Apogeu no ponto correto

# Ajustando as setas para os delta-v
# Delta-v no perigeu ajustado (seta tangente à órbita inicial no lado oposto)
plt.arrow(-r1, 0, 0, 1000, head_width=1000, head_length=1000, fc='black', ec='black', zorder=6)  # Tangente à órbita inicial

# Delta-v no apogeu permanece correto
plt.arrow(r2, 0, 0, -1000, head_width=1000, head_length=1000, fc='black', ec='black', zorder=6)  # Delta-v no apogeu

# Adicionando texto para indicar os delta-v
plt.text(-r1, 1500, r'$\Delta v_1$', horizontalalignment='center', color='black')
plt.text(r2, -2000, r'$\Delta v_2$', horizontalalignment='center', color='black')

# Configurações do gráfico
ax.set_aspect('equal')
max_radius = max(r1, r2)
ax.set_xlim([-(max_radius + 5000), max_radius + 5000])
ax.set_ylim([-(max_radius + 5000), max_radius + 5000])

# Exibir o gráfico
plt.grid(True)
plt.legend()
plt.show()

# Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.

