import os 
import pandas as pd
from exp import preprocess_image

source_folder = "050224"

files = os.listdir(source_folder)
i = 0

all_data_df = pd.DataFrame()
not_pocessed = []
for file in files:
    file_path = os.path.join(source_folder, file)
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
          result = preprocess_image(file_path) #image_to_pdf(file_path, output_folder)
          result['file_path'] = file_path
          i += 1
          current_df = pd.DataFrame([result])
          all_data_df = pd.concat([all_data_df, current_df], ignore_index=True)
        except:
            not_pocessed.append(file_path)
        # if i == 2:
        #     break
    #elif file.lower().endswith('.docx'):
        #docx_to_pdf(file_path, output_folder)
    else:
        print(file)

# Define the path to save the Excel file
excel_file_path = "output.xlsx"

# Write the DataFrame to an Excel file
all_data_df.to_excel(excel_file_path, index=False)

print("Excel file saved successfully.")
print(not_pocessed)