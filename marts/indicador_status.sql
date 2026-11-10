SELECT
    g."Status",
    COUNT(*) AS quantidade_obras
FROM obras_gerais AS g
JOIN obras_financeiras AS f
    ON g.id_registro = f.id_registro
GROUP BY g."Status"
ORDER BY quantidade_obras DESC;