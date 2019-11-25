-- Displays the max temperature of each state (ordered by State name).
SELECT
	state, MAX(value) as max_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY state
ORDER BY
	MAX(value) DESC
LIMIT 3;
