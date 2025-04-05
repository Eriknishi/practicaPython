#Ejercicio 10

def imprimir(ronda):
    print("| Jugador   | Kills | Asistencias | Muertes | MVP  | Puntos |")
    print();
    #print("-" * 59)
    
    for fila in ronda:
        print(
            f"| {fila['Nombre']:<10}| {fila['Kills']:<6}| {fila['Assists']:<11}| "
            f"{fila['Death']:<6}| {fila['MVP']:<6}| {fila['Puntos']:<6}|"
        )
        print("-" * 59) 



def ordenar(ronda):

    return sorted(ronda, key=lambda jugador: jugador['Puntos'], reverse=True)




def actualizarRonda(ronda, ActualizacionRonda, resultado, mvp):

    for jugador, datos in ActualizacionRonda.items(): 
        
        resultado[jugador]['kills'] += datos['kills']        
        resultado[jugador]['assists'] += datos['assists'] 
        resultado[jugador]['puntos'] += datos['puntos']   
                                                     
        
        if jugador == mvp:
            resultado[jugador]['mvp'] += 1  

        
        ronda.append({
            'Nombre': jugador,
            'Kills': resultado[jugador]['kills'],
            'Assists': resultado[jugador]['assists'],
            'Death': resultado[jugador]['deaths'],
            'MVP': resultado[jugador]['mvp'],  # Contador acumulado de MVP
            'Puntos': resultado[jugador]['puntos']
        })


def BuscarMvp(ActualizacionRonda, actualRound, mvp):
    
    max_puntos = -1  

    for jugador, datos in actualRound.items():   
        
        puntos = (datos['kills'] * 3) + datos['assists'] - (1 if datos['deaths'] else 0) 

        ActualizacionRonda[jugador] = {             
            'kills': datos['kills'],         
            'assists': datos['assists'],     
            'deaths': 1 if datos['deaths'] else 0,
            'puntos': puntos
        }
        
        
        if puntos > max_puntos:       
            max_puntos = puntos
            mvp = jugador
    
    return mvp   

def recorrerRondas(rounds, resultado):

    numeroRonda = 1  
    
    for actualRound in rounds: 
        
        if numeroRonda == 5:
            print("Ranking ronda Final")
        else:
            print();
            print(f"Ranking ronda {numeroRonda}")
        
        
        ronda = []   
        ActualizacionRonda = {}
        mvp = None
        
        
        mvp = BuscarMvp(ActualizacionRonda, actualRound, mvp)  
                                      

        actualizarRonda(ronda, ActualizacionRonda, resultado, mvp) 
        rondaOrdenada = ordenar(ronda)                                
        
        
        imprimir(rondaOrdenada)
        
        
        numeroRonda += 1


