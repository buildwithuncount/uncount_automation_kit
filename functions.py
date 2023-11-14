import config as config

import pandas as pd
import duckdb


def staging_data(file = config.data_input):
    #df = pd.read_excel(file, sheet_name="OVERALL DATA", index_col=None, na_values=['NA'], usecols = "A:N")
    df = pd.read_csv(file, index_col=None, na_values=['NA'], sep=';')
    
    df = config.modifyMetrics(df)
    print(df)
    connection = duckdb.connect(database=':memory:', read_only=False)
    
    # Daten aus dem DataFrame in die DuckDB-Tabelle "db" laden
    duckdb.sql("CREATE TABLE db AS SELECT * FROM df")
    # SQL-Abfrage auf die Daten ausführen
    #result = connection.execute("SELECT * FROM db")

    # Ergebnisse in ein Pandas DataFrame laden
    result_df = duckdb.sql("SELECT * FROM db").df()

    # Verbindung zur DuckDB-Datenbank schließen
    connection.close()

    #print(result_df)

    return df

def modifyMetrics(df):

    # für project1
    
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['Spendings_pro_Impression'] = df['Spendings']/df['impressions']
    
    return df
    
def prepare_top_postings(df, top_posts):

    # FB IMPRESSIONEN

    top_posts["facebook_Impressionen_top1"] = read_top_performer(df, "facebook", "feed", "Impressionen", 1, "top")
    top_posts["facebook_Interaktionen_top1"] = read_top_performer(df, "facebook", "feed", "Interaktionen", 1, "top")
    top_posts["facebook_Klicks_top1"] = read_top_performer(df, "facebook", "feed", "Clicks", 1, "top")

    top_posts["facebook_Impressionen_flop1"] = read_top_performer(df, "facebook", "feed", "Impressionen", 1, "flop")
    top_posts["facebook_Interaktionen_flop1"] = read_top_performer(df, "facebook", "feed", "Interaktionen", 1, "flop")
    top_posts["facebook_Klicks_flop1"] = read_top_performer(df, "facebook", "feed", "Clicks", 1, "flop")

    return top_posts

def read_top_performer(df, channel, content_type, kpi, nr, outcome):
    
    try:
        df.reset_index(drop=True, inplace=True)

        nr -= 1

        # if content_type != "feed":
        #     filtered_df = df[(df['Platform'] == channel) & (df['Content type'] == content_type)]
        # else:
        #     filtered_df = df[(df['Platform'] == channel) & ((df['Content type'] == 'post.photo') | (df['Content type'] == 'post.carousel') | (df['Content type'] == 'post.reel'))]

        if outcome != "flop":
            sort_less_first = False # top posts
        else:
            sort_less_first = True  # flop posts

        filtered_df = df[(df['Month'] == config.analyze_month)]

        sorted_df = filtered_df.sort_values(by=kpi, ascending=sort_less_first)

        if len(sorted_df) >= 2:
            # Zugriff auf den zweitbesten Post (Index 1 entspricht dem zweitbesten Post, da Indexe bei 0 beginnen)
            read_post = sorted_df.iloc[nr]
            return read_post

        else:
            nr += 1
            read_post = "N/A"
            print(f"Es gibt nicht genügend Einträge im DataFrame, um für diesen Rang einen Eintrag zu finden. Es fehlt: {channel, content_type, kpi, nr}")
    
    except:
            nr += 1
            print(f"Es gibt nicht genügend Einträge im DataFrame, um für diesen Rang einen Eintrag zu finden. Es fehlt: {channel, content_type, kpi, nr}")

# def für calculating growth rate (screenshot in iphone fotos)

def perc_difference(n1, n2):
    # perc_difference(50, 60)
    return ((n2-n1)/n1)*100
