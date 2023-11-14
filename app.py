import config as config
import charts as charts

from pres import Deliverable
from data import functions as data_f

# pip3 install numpy matplotlib plotly plotly-express python-pptx seaborn python-dotenv duckdb pandas

if __name__ == "__main__":

    try:

    # init

        df = data_f.staging_data()    
        top_posts = {}
        top_posts = data_f.prepare_top_postings(df, top_posts)

        highlight_month = f"{config.analyze_year}-{config.analyze_month}"

    finally: 
                    
        report = Deliverable.OneSecondDeck(config.output_file, config.output_folder, config.input_file, config.input_folder, config.answers, df)

        print("Init erfolgreich abgeschlossen")

    # SLIDE 1
    try:            
        slide = 1 # Titelfolie
        report.insertImageOnSlide(f'https://images.unsplash.com/photo-1682917595484-41b62dc54320?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2487&q=80', slide, 'Titel 1', 1, 1, 3.3, 0.8)
        report.insertTextOnSlide("Facebook Report", slide, "Titel 1")
        report.insertTextOnSlide("Meine Kampagne", slide, "Untertitel 2") 
        report.insertImageOnSlide(f'{config.img_folder}{config.title_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.title_fix == 1 else None

    finally: 
        print(f"#### Slide {slide} done ####")

    # SLIDE 2
    try: 
        slide = 2 # Verwendeter Master-Slide: Dashboard
        report.insertTextOnSlide(f"Ergebnisse {highlight_month}", slide, "Titel 22")
        report.insertChartOnSlide(df, charts.balkendiagramm, slide, 'Titel 22', 2, 4, 18, 14)
    
        # dashboard init
        df = df[(df['Year'] == config.analyze_year) & (df['Month'] == config.analyze_month)]
        number_posts = len(df)
        impressions_sum = df['Impressions'].sum()
        interactions_sum = df['Interactions'].sum()
        er_mean = round(round(df['ER'].mean(),3)*100,2)
        ctr_mean = round(round(df['CTR'].mean(),3)*100,2)
        clicks_sum = df['Clicks'].sum()

        # insert on dashboard
        report.insertTextOnSlide(f'{impressions_sum}', slide, "Inhaltsplatzhalter 23")
        report.insertTextOnSlide(f'{er_mean}% ({ctr_mean}%)', slide, "Inhaltsplatzhalter 24")
        report.insertTextOnSlide(f'{number_posts}', slide, "Inhaltsplatzhalter 28")

        report.insertTextOnSlide("Impressionen", slide, "Inhaltsplatzhalter 25")
        report.insertTextOnSlide("Reaktionsrate (Klickrate)", slide, "Inhaltsplatzhalter 26")
        report.insertTextOnSlide("Postings", slide, "Inhaltsplatzhalter 27")

        #report.insertImageOnSlide(f'{config.img_folder}{config.background_picture}', slide, 'Titel 23', 0, 0, 33.87, 19.05, True) if config.background_fix == 1 else None

    finally: 
        print(f"#### Slide {slide} done ####")

    # SLIDE 3
    try:
        slide = 3 # Verwendeter Master-Slide: Drei Inhalte
            
        report.insertTextOnSlide("Das lief am besten", slide, "Titel 22")

        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_top1']['Veröffentlichungszeit']}", slide, "Inhaltsplatzhalter 7")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_top1']['Impressionen']}", slide, "Inhaltsplatzhalter 4")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_top1']['Interaktionen']}", slide, "Inhaltsplatzhalter 5")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_top1']['Clicks']}", slide, "Inhaltsplatzhalter 6")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_top1']['Permalink']}", slide, "Inhaltsplatzhalter 8")

        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_top1']['Veröffentlichungszeit']}", slide, "Inhaltsplatzhalter 12")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_top1']['Impressionen']}", slide, "Inhaltsplatzhalter 9")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_top1']['Interaktionen']}", slide, "Inhaltsplatzhalter 10")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_top1']['Clicks']}", slide, "Inhaltsplatzhalter 11")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_top1']['Permalink']}", slide, "Inhaltsplatzhalter 13")

        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_top1']['Veröffentlichungszeit']}", slide, "Inhaltsplatzhalter 17")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_top1']['Impressionen']}", slide, "Inhaltsplatzhalter 14")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_top1']['Interaktionen']}", slide, "Inhaltsplatzhalter 15")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_top1']['Clicks']}", slide, "Inhaltsplatzhalter 16")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_top1']['Permalink']}", slide, "Inhaltsplatzhalter 18")

    finally: 
        print(f"#### Slide {slide} done ####")

    # SLIDE 4
    try:
        slide = 4

        report.insertTextOnSlide("Optimieren", slide, "Titel 22")

        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_flop1']['Veröffentlichungszeit']}", slide, "Inhaltsplatzhalter 7")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_flop1']['Impressionen']}", slide, "Inhaltsplatzhalter 4")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_flop1']['Interaktionen']}", slide, "Inhaltsplatzhalter 5")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_flop1']['Clicks']}", slide, "Inhaltsplatzhalter 6")
        report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_flop1']['Permalink']}", slide, "Inhaltsplatzhalter 8")

        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_flop1']['Veröffentlichungszeit']}", slide, "Inhaltsplatzhalter 12")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_flop1']['Impressionen']}", slide, "Inhaltsplatzhalter 9")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_flop1']['Interaktionen']}", slide, "Inhaltsplatzhalter 10")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_flop1']['Clicks']}", slide, "Inhaltsplatzhalter 11")
        report.insertTextOnSlide(f"{top_posts['facebook_Interaktionen_flop1']['Permalink']}", slide, "Inhaltsplatzhalter 13")

        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_flop1']['Veröffentlichungszeit']}", slide, "Inhaltsplatzhalter 17")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_flop1']['Impressionen']}", slide, "Inhaltsplatzhalter 14")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_flop1']['Interaktionen']}", slide, "Inhaltsplatzhalter 15")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_flop1']['Clicks']}", slide, "Inhaltsplatzhalter 16")
        report.insertTextOnSlide(f"{top_posts['facebook_Klicks_flop1']['Permalink']}", slide, "Inhaltsplatzhalter 18")

    finally: 
        print(f"#### Slide {slide} done ####")

    report.createPres()