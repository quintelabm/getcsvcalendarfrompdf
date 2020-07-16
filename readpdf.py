# import tabula
# pip install tabula-py

from tabula import read_pdf, convert_into
import pandas as pd
import numpy as np
from numpy.core.defchararray import add
import os.path

def exportcalendartocsv():
    if not os.path.isfile('calendario.csv'):

        print('Processing...wait...')
        print('------------------------------')

        # possible output_formats JSON, CSV, TSV 
        convert_into("CALENDARIO-DE-BOLSAS-2020.1.pdf", "calendario.csv", output_format="csv")

        # Subject,Start Date,End Date
        # Lançamento Janeiro, 16/01/20, 21/01/20

        # Need first and second column and change date format
        data = pd.read_csv("calendario.csv")

        # remove unecesary columns
        data.drop(data.columns[[2,3]], axis=1, inplace=True)

        data = data.iloc[2:]
        data = data.drop([14,15,16])

        #print(data)

        # remove unecessary dates from column
        data['LANÇAMENTO DE'] = data['LANÇAMENTO DE'].str[:8]

        # Using DataFrame.insert() to add a column for end date 
        # and format the dates
        data.insert(2, "Data Fim", data['LANÇAMENTO DE'].str[4:7]+ [f'/{i:02d}/2020' for i in range(1, len(data) + 1)], True) 
        data['LANÇAMENTO DE'] = data['LANÇAMENTO DE'].str[:2]+ [f'/{i:02d}/2020' for i in range(1, len(data) + 1)]

        # Using DataFrame.insert() to add a column description
        data.insert(3, "Description", "Periodo para lancamento de frequencia no SIGA") 

        data.assign(new=[f'str_{i}' for i in range(1, len(data) + 1)])

        #print(data)

        # update columns names
        data.columns = ['Subject', 'Start Date', 'End Date','Description']

        data['Subject'] = 'Lançamento de Frequencia de ' + data['Subject']

        #print(data)

        with open('calendario.csv', 'w') as f:
            data.to_csv(f,index=False)

        print('------------------------------')
        print('Calendar saved: calendario.csv')
        print('------------------------------')

    else:
        print('Calendar already saved.')
        print('Nothing to be done.')
        print('--------------Bye-------------')


