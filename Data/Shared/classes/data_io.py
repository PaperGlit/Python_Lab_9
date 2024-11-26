"""Used to load/upload files"""
import os
import pandas as pd
from mpld3 import fig_to_html
from Data.Shared.functions.logger import logger


class DataIO:
    """Class to load/upload files"""
    @staticmethod
    def load_data(file_path):
        """Loads data from file"""
        try:
            data = pd.read_csv(file_path)
            print("Data loaded successfully!")
            return data
        except FileNotFoundError as e:
            logger.error("[Lab 8] Error loading data: %s", e)
            print(f"Error loading data: {e}")
        return None

    @staticmethod
    def save_visualization(fig, filename):
        """Saves figure to file"""
        fig.savefig(f"Exports/{filename}.png")
        print(f"Saved: {filename}.png")
        try:
            html_content = fig_to_html(fig)
            with open(f"Exports/{filename}.html", "w", encoding="utf-8") as html_file:
                html_file.write(html_content)
            print(f"Saved: {filename}.html (interactive)")
        except IOError as e:
            print(f"Failed to save {filename}.html: {e}")

    @staticmethod
    def upload_to_file(data):
        """Uploads data to file"""
        while True:
            file_name = input("Enter file name: ")
            if file_name.strip() != "":
                if not file_name.endswith(".txt"):
                    file_name += ".txt"
                try:
                    if not os.path.exists("Exports/"):
                        os.makedirs("Exports/")
                    with open("Exports/" + file_name, 'w', encoding="utf-8") as f:
                        f.write(data)
                    print("The art was uploaded successfully")
                    break
                except IOError as e:
                    print(f"Error uploading data: {e}")
            else:
                print("Please enter a valid file name")
