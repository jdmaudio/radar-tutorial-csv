#!/usr/bin/env python
# coding: utf-8

# import OS module
import os
import csv
from bs4 import BeautifulSoup

# Get the list of all files and directories (change this path to your own)
path = "C:\\Users\\jdmau\\Documents\\RadarTutorialCSV\\radartutorial\\19.kartei"

# Open the CSV file in write mode
with open('table.csv', 'wt+', newline='', encoding='utf-8-sig') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile,delimiter=',', dialect='excel')
    
    # Write the header row
    writer.writerow(['File name','Radar name', 'Frequency', 'PRT', 'PRF', 'Pulsewidth', 'Receiving time', 'Dead time', 'Peak Power', 'Average Power', 'Instrumented Range', 'Range Resolution', 'Accuracy', 'Beamwidth', 'Hits per scan', 'Antenna Rotation', 'MTBCF', 'MTTR'])

    # dirs=directories
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if 'en.html' in f: # English files only here
                print("Processing: " + os.path.join(root, f))
                with open(os.path.join(root, f), 'r', encoding='utf-8-sig') as myFile:
                    html = myFile.read()
                    
                    # Parse the HTML using BeautifulSoup
                    soup = BeautifulSoup(html, 'html.parser')

                    # Find the table in the HTML
                    table = soup.find('table',  { 'class' : 'ttd' })

                    # Find radar name
                    name = soup.find('h4',  { 'class' : 'hh_yes' })

                    # Create a list to store the table data
                    data = []
                
                    if table:
                        # Iterate over the rows in the table
                        for row in table.find_all('tr'):
                            
                            # Extract the cells in each row
                            cells = row.find_all('td', {'class' : ''})

                            if cells:
                                x = cells[0].text.strip()
                                data.append(x)

                            # Store the cells in the data list
                            #data.append([cell.text.strip() for cell in cells])
                                
                        # Write the cells to the CSV file
                        if data:
                            data.insert(0, f)
                            if name:
                                data.insert(1, name.text)
                            writer.writerow(data)

