import pandas as pd

df = pd.read_csv("C:\\Users\\Oscar Flores\\Documents\\Escola\\Programacion\\JF\\master_partidas_v2.csv")

df.dropna(inplace = True)

# print(df.to_string())

# Reemplazar Nombres de personajes mal escritos

cols = ["Player_1", "Player_2", "Ganador", "Perdedor"]
for col in cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# PASO 2: Diccionario de Correcciones

correcciones = {
    "Dr. Mario": "Dr Mario",
    "Dr.Mario": "Dr Mario",
    "Doc": "Dr Mario",
    "Drmario": "Dr Mario",
    "Mtea Knight": "Meta Knight",
    "Metaknight": "Meta Knight",
    "Gnw": "Mr. Game & Watch",    
    "Game And Watch": "Mr. Game & Watch",
    "Dk": "Donkey Kong",
    "Flaco": "Falco",
    "R.O.B": "ROB",
    "Rob": "ROB",
    "Crono": "Chrono",
    "S.mario": "S Mario",
    "S. Mario": "S Mario",
    "S.Mario": "S Mario",
    "Smario": "S Mario",
    "S.Ryu" : "S Ryu",
    "S. Ryu" : "S Ryu",
    "Pacman": "Pac-Man",
    "Capt. Falcon": "Captain Falcon",
    "Cap. Falcon": "Captain Falcon",
    "Falcon": "Captain Falcon",
    "K.Sonic": "K. Sonic",
    "S.Luigi": "S. Luigi",
    # Agregar más correcciones según sea necesario
}


# PASO 3: Aplicar las correcciones
df[cols] = df[cols].replace(correcciones)

# PASO 4: Verificación
todos_los_nombres = pd.unique(df[cols].values.ravel())
todos_los_nombres.sort()
# Imprimir la lista de nombres únicos después de las correcciones

# 2. LIMPIEZA DE RONDAS (Traducir números a Texto)

def etiquetar_ronda(row):
    ronda = row['Ronda']
    fase = row['Fase'] # Pools o Bracket
    
    if fase == "Pools":
        return "Fase de Grupos"
    
    # Lógica para Bracket
    if ronda > 0:
        return f"Winners Round {ronda}"
    elif ronda < 0:
        return f"Losers Round {abs(ronda)}"
    elif ronda == 0:
        return "Third Place Round"
    return "Desconocido"

df['Etapa_Torneo'] = df.apply(etiquetar_ronda, axis=1)

# Reordenamos las columnas para que se vea bonito
columnas_ordenadas = [
    'Archivo', 'Torneo', 'Fecha', 'Etapa_Torneo', 'Fase', 
    'Player_1', 'Player_2', 'Ganador', 'Perdedor', 
    'Score'
]

# Seleccionamos solo las columnas que existen (por si acaso)
cols_finales = [c for c in columnas_ordenadas if c in df.columns]

df_final = df[cols_finales]

def extraer_puntos(score_str):
    try:
        partes = str(score_str).split('-')
        
        if len(partes) == 2:
            n1 = int(partes[0])
            n2 = int(partes[1])
            
            # --- EL TRUCO ESTÁ AQUÍ ---
            # No importa si viene "3-1" o "1-3",
            # siempre devolvemos (Mayor, Menor)
            return max(n1, n2), min(n1, n2)
            
        return 0, 0 
    except:
        return 0, 0
# Aplicamos la función
df_final['Score_Ganador'], df_final['Score_Perdedor'] = zip(*df_final['Score'].apply(extraer_puntos))

# OJO: Faltaba esta línea. Sin ella, el paso 4 falla porque no existe la columna
df_final['Diferencia_Juegos'] = df_final['Score_Ganador'] - df_final['Score_Perdedor']

print(df_final[['Score', 'Score_Ganador', 'Score_Perdedor']].head(10).to_string())

# 4. ETIQUETA CUALITATIVA
def categorizar_victoria(row):
    g = row['Score_Ganador']
    p = row['Score_Perdedor']
    diff = row['Diferencia_Juegos']
    
    if diff == 1:
        return "Reñido"
    
    if g == 3 and p == 0:
        return "Victoria Contundente"
    
    return "Victoria"  

df_final['Tipo_Victoria'] = df_final.apply(categorizar_victoria, axis=1)

# Verificamos cómo se ve
print(df_final[['Ganador', 'Score', 'Diferencia_Juegos', 'Tipo_Victoria']].head(10).to_string())

# Guardar
df_final.to_csv("master_partidas_limpio.csv", index=False, encoding='utf-8-sig')