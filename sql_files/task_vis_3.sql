SELECT Season, (SUM(FullTimeHomeGoals) + SUM(FullTimeAwayGoals)) as Goals
FROM games
GROUP BY Season
HAVING Season != 'Ses1899/1900'
ORDER BY Season
;