import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Read the Excel file
df = pd.read_excel(os.path.abspath('./spreedsheet_reader/serpro_2023_provisorio.xlsx'))

column_name = 'Nota (Cálculo Final)'

# Count the occurrences of the number
value_counts = df[column_name].value_counts()

# Create a bar plot of the value counts
plt.bar(value_counts.index, value_counts.values)

# Add a title and axis labels
plt.title('Número de Ocorrências da Nota Final em {}'.format(column_name))
plt.xlabel('Nota')
plt.ylabel('Número de Ocorrências')

# Show the plot
plt.show()

