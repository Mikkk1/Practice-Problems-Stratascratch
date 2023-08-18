# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.head()
forbes_global_2010_2014 = forbes_global_2010_2014.sort_values(by = ["profits"], ascending = False)
forbes_global_2010_2014.head()
cols = ['company','profits']
Top_3_companies = forbes_global_2010_2014[cols]
Top_3_companies.head(3)
