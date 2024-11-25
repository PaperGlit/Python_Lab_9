import pandas as pd
from mpld3 import fig_to_html
import os
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

class DataIO:
    @staticmethod
    def load_data(file_path):
        try:
            data = pd.read_csv(file_path)
            print("Data loaded successfully!")
            return data
        except Exception as e:
            logger.error(f"[Lab 8] Error loading data: {e}")
            raise FileNotFoundError(f"Error loading data: {e}")

    @staticmethod
    def save_visualization(fig, filename):
        fig.savefig(f"Exports/{filename}.png")
        print(f"Saved: {filename}.png")
        try:
            html_content = fig_to_html(fig)
            with open(f"Exports/{filename}.html", "w") as html_file:
                html_file.write(html_content)
            print(f"Saved: {filename}.html (interactive)")
        except Exception as e:
            print(f"Failed to save {filename}.html: {e}")

    @staticmethod
    def upload_to_file(data):
        while True:
            file_name = input("Enter file name: ")
            if file_name.strip() != "":
                if not file_name.endswith(".txt"):
                    file_name += ".txt"
                try:
                    if not os.path.exists("Exports/"):
                        os.makedirs("Exports/")
                    with open("Exports/" + file_name, 'w') as f:
                        f.write(data)
                    print("The art was uploaded successfully")
                    break
                except IOError:
                    raise IOError("The file could not be uploaded, please try again")
            else:
                print("Please enter a valid file name")