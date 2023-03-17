WITH all_goals as (
    SELECT Season, 
    COUNT(Season) as NumberGames,
    SUM(HalfTimeHomeGoals) as SumHalfHomeGoals,
    SUM(HalfTimeAwayGoals) as SumHalfAwayGoals, 
    (SUM(FullTimeHomeGoals) - SUM(HalfTimeHomeGoals)) as SumFullGoalsHome,
    (SUM(FullTimeAwayGoals) - SUM(HalfTimeAwayGoals)) as SumFullGoalsAway
    FROM games
    WHERE HalfTimeHomeGoals < 9999 AND HalfTimeAwayGoals < 9999 
    GROUP BY Season
    HAVING Season != 'Ses1899/1900'
    ORDER BY Season)
SELECT ag.Season, 
(ag.SumHalfHomeGoals + ag.SumHalfAwayGoals) as SumFirstHalfGoals, 
(ag.SumFullGoalsHome + ag.SumFullGoalsAway) as SumSecoundHalfGoals,
ROUND(((ag.SumHalfHomeGoals + ag.SumHalfAwayGoals)/ag.NumberGames),2) as AvgFirstHalfGoals,
ROUND(((ag.SumFullGoalsHome + ag.SumFullGoalsAway)/ag.NumberGames),2) as AvgSecoundHalfGoals
FROM all_goals ag
GROUP BY Season
ORDER BY Season;