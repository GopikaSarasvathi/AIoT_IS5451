import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle


# Function to load data and create a dataframe
def load_data(filepath, label_value):
    with open(filepath, 'r') as file:
        data = json.load(file)
        record=[{'x': value['x'], 'y': value['y'], 'z': value['z']} for key, value in data['raw_data'].items()]
        df = pd.DataFrame(record)
        df.reset_index(drop=True, inplace=True)
        df['label'] = label_value
    return df

# Load datasets
df_not_fall = load_data(r'C:\Users\Leady\Documents\NUS\IS5451\Project\not fall.json', 0)
df_front_fall = load_data(r'C:\Users\Leady\Documents\NUS\IS5451\Project\front_fall.json', 1)
df_left_fall = load_data(r'C:\Users\Leady\Documents\NUS\IS5451\Project\front_left_fall.json', 1)
df_right_fall = load_data(r'C:\Users\Leady\Documents\NUS\IS5451\Project\front_right_fall.json', 1)
df_down_fall = load_data(r'C:\Users\Leady\Documents\NUS\IS5451\Project\down_fall.json', 1)
df_back_fall = load_data(r'C:\Users\Leady\Documents\NUS\IS5451\Project\back_fall.json', 1)

# Combine all datasets
combined_df = pd.concat([df_not_fall, df_front_fall, df_left_fall, df_right_fall, df_down_fall, df_back_fall])
combined_df.reset_index(drop=True, inplace=True)

# Splitting the dataset into features and target variable
X = combined_df.drop('label', axis=1)
y = combined_df['label']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
pickle.dump(clf, open(r'C:\Users\Leady\Documents\NUS\IS5451\Project\fallDetectTree.pkl', 'wb'))


