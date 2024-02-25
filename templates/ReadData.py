#import CreateData
import RatingScale
import os
import pandas as pd
import psycopg2


# Accessing data from the DataFrame
#for index, row in df.iterrows():
    #print(f"Satisfied: {row['Satisfied']}, WorklifeBalance: {row['WorklifeBalance']}, Review: {row['Review']}")
#print(df.row())
# Iterate over each row
for index, row in df.iterrows():
    for column in df.columns:
        scale = row[column]
        print(f'Cell value at row {index}, column {column}: {scale}')
    # Iterate over each column
        # Access cell value using iloc or loc
       # or df.loc[i, df.columns[j]]


k = RatingScale.final()
if(k=="red"):
    #send the note to HR saying that might terminate and the employer would look into the employee
    j = "Terminate or look for new hire with similar skillset"
elif(k =="yellow"):
    j = "Talk to the employe and learn more about the changes that he/she might want. Might want to hire with similar skilset to improve productivity, designs and analysis."
else:
     j =  "Everything is going good"

      
        


    