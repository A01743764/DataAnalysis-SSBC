SELECT TOP (1000) [Archivo]
      ,[Torneo]
      ,[Fecha]
      ,[Etapa_Torneo]
      ,[Fase]
      ,[Player_1]
      ,[Player_2]
      ,[Ganador]
      ,[Perdedor]
      ,[Score]
      ,[Score_Ganador]
      ,[Score_Perdedor]
      ,[Diferencia_Juegos]
      ,[Tipo_Victoria]
  FROM [Matches].[dbo].[master_partidas_limpio]
  SELECT TOP 15
    Ganador as Jugador,
    COUNT(*) as Total_Victorias,
    
    CAST(
        (SUM(CASE WHEN Tipo_Victoria = 'Victoria Contundente' THEN 1 ELSE 0 END) * 100.0) 
        / COUNT(*) 
    AS DECIMAL(5,1)) as Pct_Aplastante,

    CAST(
        (SUM(CASE WHEN Tipo_Victoria = 'Reñido' THEN 1 ELSE 0 END) * 100.0) 
        / COUNT(*) 
    AS DECIMAL(5,1)) as Pct_Suffering

FROM master_partidas_limpio 
GROUP BY Ganador
HAVING COUNT(*) >= 5  
ORDER BY Total_Victorias DESC;
SELECT 
    Ganador,
    COUNT(*) as Grand_Finals_Ganadas
FROM master_partidas_limpio
WHERE Etapa_Torneo LIKE '%Grand Final%' 
GROUP BY Ganador
ORDER BY Grand_Finals_Ganadas DESC;