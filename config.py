import os

project = "magic_report"

analyze_month = 10
analyze_year = 2023

#analyze_month = analyzer_month

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Design

background_fix = 0
background_picture = "lush.jpg"

title_fix = 1
title_picture = "lush.jpg"

primary_color = "#333333"
secondary_color = "#649AA8" 
background_color = "#f1f1f1"
chart_fontsize = 8

activate_ki = 1
single_ki = 0

seiten = "Seiten"
info = "None"
answers = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# AI prompts

# none

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# File Paths

title = "Facebook Report Light"

userfolder_path = os.path.dirname(os.path.abspath(__file__))
userfolder_path = f"{userfolder_path}/" 

# Pfad zum Eingangsordner (masters) und zur Eingabe-Datei (Master.pptx)
input_folder = f"{userfolder_path}masters/{project}"
input_file = f"{project}.pptx"

# Pfad zum Ausgabeordner (output) und zum Ausgabe-Dateinamen
output_folder = f"{userfolder_path}output/{project}"
output_file = f"{project}_edited.pptx"

data_input = f"{userfolder_path}input/{project}/Facebook_Insights_Export.csv"

img_folder = f"{userfolder_path}img/{project}/"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Modify metrics

import pandas as pd

def modifyMetrics(df):

    # For testing add rows to data
    # new_rows = [
    #     {"Veröffentlichungszeit": "07/20/2023 18:00", "Interaktionen": 200, "Impressionen": 400, "Klicks insgesamt": 33},
    #     {"Veröffentlichungszeit": "08/20/2023 18:00", "Interaktionen": 2000, "Impressionen": 500, "Klicks insgesamt": 20},
    #     {"Veröffentlichungszeit": "10/08/2023 18:00", "Interaktionen": 542, "Impressionen": 543, "Klicks insgesamt": 22},
    #     {"Veröffentlichungszeit": "08/20/2023 18:00", "Interaktionen": 4300, "Impressionen": 460, "Klicks insgesamt": 330},
    #     {"Veröffentlichungszeit": "09/20/2023 18:00", "Interaktionen": 300, "Impressionen": 400, "Klicks insgesamt": 0}
    # ]

    # # Convert the list of dictionaries to a DataFrame
    # new_rows_df = pd.DataFrame(new_rows)

    # # Concatenate the new DataFrame with the existing one
    # df = pd.concat([df, new_rows_df], ignore_index=True)

    df['Month'] = pd.to_datetime(df['Veröffentlichungszeit'], format='%m/%d/%Y %H:%M').dt.month
    #print(df['Month'])
    df['Year'] = pd.to_datetime(df['Veröffentlichungszeit'], format='%m/%d/%Y %H:%M').dt.year
    df['Page name'] = df['Seitenname']
    df['Veröffentlichungszeit'] = pd.to_datetime(df['Veröffentlichungszeit'], format="%m/%d/%Y %H:%M").dt.strftime("%Y-%m-%d")


    df['ER'] = df['Interaktionen']/df['Impressionen']
    df['Impressions'] = df['Impressionen']
    df['Interactions'] = df['Interaktionen']
    df['Clicks'] = df['Klicks insgesamt']
    df['CTR'] = df['Klicks insgesamt']/df['Impressionen']
    #print(df)

    return df
