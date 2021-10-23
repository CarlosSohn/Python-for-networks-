from pythonping import ping # Se importa el modulo para hacer ping. Dado que el
                            # modulo crea los paquetes ICMP, se requiere root.
                            # De lo contrario, no funcionará.
from tqdm import tqdm # Modulo para la barra de progreso
print("Network Scanner")
x = input("IP Gateway: ")
rang = int(input("Range (255 max): "))
y = x.rstrip(x[-1]) # Elimina el último simbolo de la cadena x
lista=[]
for i in tqdm(range(0, rang)): #Aqui se junta el range de la variable rang como
                               # el range de la barra de progreso
    ipad = y+str(i) # Generador de direcciones ip dentro de la red dada en x.
    ping_v = ping(ipad, count=1) # Almacena el resultado del ping. count=1 para
                                 # que el programa sea más rapido. Un número más
                                 # grande aumenta el tiempo de escaneo, pues
                                 # corresponde con el numero de paquetes a enviar.
    alt = str(ping_v) # Convierte el resultado de ping en una str para que pueda
                      # ser interpretada por el if siguiente.
    if "Reply from " in alt: # Si hay respuesta, entonce...
        lista.append(ipad) # Añade la dirección ip (ipad) en la lista
    else: # Si no ...
        continue
print(len(lista), "device(s) found: ")
for i in lista: # Imprime cada elemento de la lista
    print(i)
