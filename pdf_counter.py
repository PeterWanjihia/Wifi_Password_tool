import os
import csv
from datetime import datetime

def count_pdfs_and_save_to_csv(output_csv_path):
    # Create a CSV file and write the header
    with open(output_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Folder', 'Date_Saved']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Walk through the entire file system and count PDF files
        for foldername, subfolders, filenames in os.walk('/'):
            for filename in filenames:
                if filename.lower().endswith('.pdf'):
                    # Get the file creation date
                    full_path = os.path.join(foldername, filename)
                    date_saved = datetime.fromtimestamp(os.path.getctime(full_path)).strftime('%Y-%m-%d %H:%M:%S')

                    # Write data to CSV
                    csv_writer.writerow({'Name': filename, 'Folder': foldername, 'Date_Saved': date_saved})

if __name__ == "__main__":
    output_csv_path = input("Enter the output CSV file path: ")

    count_pdfs_and_save_to_csv(output_csv_path)

    print("Process completed. Check the CSV file for the results.")
