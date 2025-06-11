import io
import plotly.io as pio
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import duckdb
import config as config
import numpy as np


def balkendiagramm(df):

    sql_query = """
        SELECT
            CONCAT(Year, '-', LPAD(Month, 2, '0')) AS year_month,
            SUM(Impressions) AS Impressions,
            AVG(CTR) AS CTR
        FROM
            db
        GROUP BY
            Year, Month
        ORDER BY
            Year, Month;
    """

    filtered_df = duckdb.sql(sql_query).df()

    analyze_month = '0' + str(config.analyze_month) if config.analyze_month < 10 else str(config.analyze_month)
    highlight_month = f"{config.analyze_year}-{analyze_month}"
    colors = [config.secondary_color if month == highlight_month else config.background_color for month in filtered_df['year_month']]
    # colors = ['#98D72E' if month == "2023-10" else '#f1f1f1' for month in filtered_df['year_month']]
                  
    ax = sns.barplot(x='year_month', y='Impressions', data=filtered_df, palette=colors, width=0.8, dodge=False)

    # Farbschemen: https://seaborn.pydata.org/tutorial/color_palettes.html
    sns.set(rc={'axes.facecolor':config.background_color, 'figure.facecolor':config.background_color, 'axes.edgecolor' : 'none', 'grid.color': '#ffffff', 'grid.linestyle': ':'})

    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

    ax.set(yticklabels=[])

    sns.despine(left=True, bottom=True)
    plt.ylabel('')
    plt.xlabel('')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)

    plt.close()
    return buffer, filtered_df
