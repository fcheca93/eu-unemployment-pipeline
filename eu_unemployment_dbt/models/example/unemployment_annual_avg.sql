SELECT
    EXTRACT(YEAR FROM date::date) AS year,
    ROUND(AVG(unemployment_rate)::numeric, 2) AS avg_unemployment_rate
FROM {{ source('public', 'unemployment_rate_germany') }}
GROUP BY 1
ORDER BY 1