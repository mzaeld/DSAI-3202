import time
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from math import sqrt

def run_sequential(X_train_filled, y_train, X_val_filled, y_val):
    start_time = time.time()

    # Define the parameter ranges
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]  # None means using all features
    max_depth_range = [1, 2, 5, 10, 20, None]  # None means no limit

    # Initialize variables to store the best model and its RMSE and parameters
    best_rmse = float('inf')
    best_mape = float('inf')
    best_model = None
    best_parameters = {}

    # Loop over all possible combinations of parameters
    for n_estimators in n_estimators_range:
        for max_features in max_features_range:
            for max_depth in max_depth_range:
                # Create and train the Random Forest model
                rf_model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_features=max_features,
                    max_depth=max_depth,
                    random_state=42
                )
                rf_model.fit(X_train_filled, y_train)

                # Make predictions and compute RMSE
                y_val_pred = rf_model.predict(X_val_filled)
                rmse = sqrt(mean_squared_error(y_val, y_val_pred))
                # Compute MAPE
                mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
                print(f"The parameters: {n_estimators}, {max_features}, {max_depth}. RMSE: {rmse}, MAPE: {mape}%")
                
                # If the model is better than the current best, update the best model and its parameters
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_mape = mape
                    best_model = rf_model
                    best_parameters = {
                        'n_estimators': n_estimators,
                        'max_features': max_features,
                        'max_depth': max_depth
                    }

    print(f"The best parameters {best_parameters} for RMSE = {best_rmse}, MAPE: {best_mape}%")
    
    end_time = time.time()
    sequential_time = end_time - start_time
    
    print(f"The sequential execution time is {sequential_time}")

    return best_model, best_parameters, best_rmse, best_mape, sequential_time


