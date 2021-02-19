import matplotlib.pyplot as pyp
import matplotlib.animation as animation
 
# Criando figura
figure = pyp.figure()
 
# Criando uma subplot x, y, z = 1
subplot = figure.add_subplot(1, 1, 1)
 
# Funcao que lê o arquivo cpu.txt e alimenta a subplot
def animation_function(i):

    cpu_data = open("D:\\Documents\\Python\\device configuration\\cpu.txt").readlines()
    
    x = []
    
    # Adicionando valores na nossa lista
    for each_value in cpu_data:
        if len(each_value) > 1:
            x.append(float(each_value))
    
    # Limpando a figura
    subplot.clear()
    
    # Plotando valores da lista
    subplot.plot(x)
 
# Criando gráfico
graph_animation = animation.FuncAnimation(figure, animation_function, interval = 10000)
 
# Mostrando gráfico
pyp.show()