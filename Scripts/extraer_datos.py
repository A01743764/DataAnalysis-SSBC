import json
import pandas as pd
import os

CARPETA_JSON = r"C:\Users\Oscar Flores\Documents\Escola\Programacion\JF\py\DA_SSBC\torneos_JSON"

def procesar_torneos_v2(carpeta):
    lista_partidas = []

    # Buscar .json recursivamente (sim01, sim02, ... dentro de subcarpetas)
    rutas_json = []
    for root, _, files in os.walk(carpeta):
        for f in files:
            if f.lower().endswith(".json"):
                rutas_json.append(os.path.join(root, f))

    rutas_json.sort()  # opcional: para que vaya en orden
    print(f"Se encontraron {len(rutas_json)} archivos JSON (recursivo).")

    for ruta_completa in rutas_json:
        archivo = os.path.basename(ruta_completa)
        print(f"\n📄 Leyendo archivo: {archivo}")

        try:
            with open(ruta_completa, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Validación mínima de estructura
            if "tournament" not in data:
                print(f"   Saltado: no existe la llave 'tournament' en {archivo}")
                continue

            torneo_info = data["tournament"]
            nombre_torneo = torneo_info.get("name", "SIN_NOMBRE")
            fecha_torneo = torneo_info.get("started_at", None)

            print(f"   Torneo: {nombre_torneo}")

            # Participantes
            participantes = torneo_info.get("participants", [])
            matches = torneo_info.get("matches", [])

            print(f"   participantes: {len(participantes)} | matches: {len(matches)}")

            # 1) MAPA DE JUGADORES
            mapa_jugadores = {}
            for p in participantes:
                p_data = p.get("participant", {})
                if "id" not in p_data:
                    continue

                p_nombre = p_data.get("display_name") or p_data.get("name") or p_data.get("username") or "Desconocido"
                main_id = p_data["id"]
                mapa_jugadores[main_id] = p_nombre

                group_ids = p_data.get("group_player_ids") or []
                for g_id in group_ids:
                    mapa_jugadores[g_id] = p_nombre

            # 2) PROCESAR PARTIDAS
            agregadas = 0
            completas = 0

            for m in matches:
                match = m.get("match", {})
                if match.get("state") != "complete":
                    continue
                completas += 1

                winner_id = match.get("winner_id")
                loser_id  = match.get("loser_id")

                winner_name = mapa_jugadores.get(winner_id, "Desconocido")
                loser_name  = mapa_jugadores.get(loser_id, "Desconocido")

                p1_id = match.get("player1_id")
                p2_id = match.get("player2_id")
                p1_name = mapa_jugadores.get(p1_id, "Desconocido")
                p2_name = mapa_jugadores.get(p2_id, "Desconocido")

                es_grupo = match.get("group_id") is not None
                fase = "Pools" if es_grupo else "Bracket"

                fila = {
                    "Archivo": archivo,  # 👈 útil para rastrear de qué sim viene
                    "Torneo": nombre_torneo,
                    "Fecha": fecha_torneo,
                    "Ronda": match.get("round"),
                    "Fase": fase,
                    "Player_1": p1_name if p1_name != "Desconocido" else winner_name,
                    "Player_2": p2_name if p2_name != "Desconocido" else loser_name,
                    "Ganador": winner_name,
                    "Perdedor": loser_name,
                    "Score": match.get("scores_csv"),
                }
                lista_partidas.append(fila)
                agregadas += 1

            print(f"   matches completos: {completas}  filas agregadas: {agregadas}")

        except Exception as e:
            print(f"   Error leyendo {archivo}: {e}")

    return pd.DataFrame(lista_partidas)


if __name__ == "__main__":
    df_final = procesar_torneos_v2(CARPETA_JSON)

    if not df_final.empty:
        desconocidos = df_final[df_final["Ganador"] == "Desconocido"]

        print("\nProcesamiento completado.")
        print(f"   Filas Totales: {len(df_final)}")
        print(f"   Filas todavía 'Desconocido': {len(desconocidos)}")

        df_final.to_csv("master_partidas_v2.csv", index=False, encoding="utf-8-sig")
        print("Guardado como 'master_partidas_v2.csv'")
    else:
        print("No se generaron datos.")
