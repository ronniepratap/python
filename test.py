
import pandas as pd

# Read the Excel sheet
file_path = '/Users/vijay.gupta/Desktop/py/1-NORTH-1 OPSC AUG-2023 week-2.xlsx'
sheet_name = 'N-1 OPSC WEEK-1'  
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Sort the data based on the territory name (assuming it's in the first column)
start_row = 8  # Change this to your desired start row (1-indexed)
end_row = 899   # Change this to your desired end row (1-indexed)

# Extract the specified range of rows to sort
sorted_data_range = data[start_row - 1:end_row].sort_values(by=data.columns[2])

# Create a new DataFrame with the sorted range
updated_data = pd.concat([data.iloc[:start_row - 1], sorted_data_range, data.iloc[end_row:]], ignore_index=True)

# Create a new Excel file in the same directory for the updated data
updated_file_path = file_path.replace('.xlsx', '_updated.xlsx')
updated_data.to_excel(updated_file_path, index=False, sheet_name=sheet_name, engine='openpyxl')

print(f"Data sorted and saved to '{updated_file_path}' successfully!")