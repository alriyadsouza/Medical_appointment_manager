import pandas as pd
from sklearn.preprocessing import LabelEncoder
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Load the merged dataset
df = pd.read_csv('merged_dataset.csv')

# Data type conversion
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Label encoding for categorical variables
label_encoder = LabelEncoder()
df['Neighbourhood'] = label_encoder.fit_transform(df['Neighbourhood'])

# Text preprocessing for a specific column
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\.', '', text)  # Remove full stops
    words = text.split()
    words = [word for word in words if word not in stop_words]  # Remove stop words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]  # Lemmatize words
    return ' '.join(lemmatized_words)

df['Specific_Column'] = df['Specific_Column'].apply(preprocess_text)  # Replace 'Specific_Column' with the actual column name

# Data normalization
scaler = StandardScaler()
df['Age'] = scaler.fit_transform(df['Age'].values.reshape(-1, 1))

# Save the preprocessed dataset
df.to_csv('preprocessed_dataset.csv', index=False)