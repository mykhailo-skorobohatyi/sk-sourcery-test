import pandas as pd
import re


def process_data(value):
    # Remove commas used as thousands separators
    value = value.replace(',', '')

    # Remove everything after the second slash
    parts = value.split(' / ')[:2]

    # Remove decimal places and convert to integer
    parts = [str(int(float(part))) for part in parts]

    # Divide by 100 and format result
    parts = [str(int(int(part) / 100)) for part in parts]

    # Join with comma
    return ', '.join(parts)


# Load the Excel file
file_path = 'hard_drive_2.xlsx'
df = pd.read_excel(file_path)

# Process the first column
df['Processed'] = df.iloc[:, 0].apply(process_data)

# Save the result to a new Excel file
output_file = 'processed_hard_drive2.xlsx'
df.to_excel(output_file, index=False)

print(f'Processed file saved as {output_file}')
