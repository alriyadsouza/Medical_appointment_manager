import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('doc_deatails.csv')

# Select only the rows with the required specialists
required_specialists = ['Cardiologist', 'Dermatologist', 'Orthopedic Surgeon', 'Gynecologist', 
                        'Neurologist', 'Psychiatrist', 'Oncologist', 'Gastroenterologist', 
                        'Pediatrician', 'Ophthalmologist']

filtered_df = df[df['speciality'].isin(required_specialists)]

# Add a unique time parameter for each specialist
time_values = []
for specialist in required_specialists:
    specialist_data = filtered_df[filtered_df['speciality'] == specialist]
    time = [f"{random.randint(9, 17)}:{random.choice(['00', '15', '30', '45'])}" for _ in range(specialist_data.shape[0])]
    time_values.extend(time)

# Update the DataFrame with the time values
filtered_df['time'] = time_values

# Write the updated data to a new CSV file
filtered_df.to_csv('filtered_doc_details.csv', index=False)
