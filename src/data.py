import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_preprocess_data():
    file_path = 'data/housing_prices_data/train.csv'
    train_data = pd.read_csv(file_path, index_col="Id")

# Columns to be deleted
    columns_to_delete = ['MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']

# Delete the specified columns
    train_data_cleaned = train_data.drop(columns=columns_to_delete, axis=1)

# Define the input features (X) and the output (y)
    X = train_data_cleaned.drop('SalePrice', axis=1)
    y = train_data_cleaned['SalePrice']

# Identify the categorical columns in X
    categorical_columns = X.select_dtypes(include=['object']).columns

# Initialize a LabelEncoder for each categorical column
    label_encoders = {column: LabelEncoder() for column in categorical_columns}

# Apply Label Encoding to each categorical column
    for column in categorical_columns:
        X[column] = label_encoders[column].fit_transform(X[column])

# Display the first few rows of X to confirm the encoding
    print(X.head())


    from sklearn.model_selection import train_test_split

# Split the first dataset (X, y) into train and test sets with a 70% - 30% split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.30,random_state=42)

# Fill NaN values in X_train and X_val with the median of the respective columns
    X_train_filled = X_train.fillna(X_train.median())
    X_val_filled = X_val.fillna(X_val.median())

    print(X_train.shape, X_val.shape, y_train.shape, y_val.shape)

    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    from math import sqrt
# Create a Random Forest model
    rf_model = RandomForestRegressor(random_state=42)

# Train the model on the training data
    rf_model.fit(X_train_filled, y_train)

# Make predictions on the validation data
    y_val_pred_filled = rf_model.predict(X_val_filled)

# Calculate the RMSE on the validation data
    rmse_filled = sqrt(mean_squared_error(y_val, y_val_pred_filled))

# Print the RMSE
    print(f'RMSE on the validation data: {rmse_filled}')

    return X_train_filled, y_train, X_val_filled, y_val





def compute_metrics(sequential_time, threading_time, multiprocessing_time, num_threads, num_processes):
    speedup_thread = sequential_time / threading_time
    speedup_process = sequential_time / multiprocessing_time
    efficiency_thread = speedup_thread / num_threads
    efficiency_process = speedup_process / num_processes
    amdahl_speedup = 1 / ((1 - (1 / speedup_thread)) + (1 / speedup_thread) / num_threads)
    gustafson_speedup = num_threads - (1 - (1 / speedup_thread)) * (num_threads - 1)
    
    print("\nPerformance Metrics:")
    print(f"Speedup (Threads): {speedup_thread:.4f}")
    print(f"Efficiency (Threads): {efficiency_thread:.4f}")
    print(f"Amdahl's Law Speedup: {amdahl_speedup:.4f}")
    print(f"Gustafson's Law Speedup: {gustafson_speedup:.4f}")
    print(f"Speedup (Multiprocessing): {speedup_process:.4f}")
    print(f"Efficiency (Multiprocessing): {efficiency_process:.4f}")