-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres
WHERE id NOT IN
(SELECT tv_show_genres.genre_id
FROM tv_shows
RIGHT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
RIGHT OUTER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.name;
