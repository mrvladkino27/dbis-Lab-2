select max(Ball100) as "Results", year_no as "Year"
  FROM public.test WHERE status = 'Зараховано' AND year_no IN (2019, 2020)
  GROUP BY year_no
  ORDER BY year_no