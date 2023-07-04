# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:11:07 2023

@author: HP
"""

import pandas as pd

# Read URLs from text file
with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

# Extract dates from URLs
dates = [url.split('/')[4:7] for url in urls]

# Create DataFrame with URLs and dates
data = {'URL': urls, 'Date': dates}
df = pd.DataFrame(data)

# Filter URLs for the years 2021 to 2023
df['Year'] = df['Date'].apply(lambda x: int(x[0]))
df = df[(df['Year'] >= 2021) & (df['Year'] <= 2023)]

# Sort URLs by date
df['Date'] = pd.to_datetime(df['Date'].apply(lambda x: '/'.join(x)), format='%Y/%m/%d')
df = df.sort_values(by='Date')

# Write sorted URLs to CSV file
df.to_csv('sorted_urls.csv', index=False)
