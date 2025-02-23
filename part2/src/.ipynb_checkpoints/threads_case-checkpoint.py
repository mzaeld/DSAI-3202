import time
import concurrent.futures
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from math import sqrt

def train_and_evaluate(n_estimators, max_features, max_depth, X_train_filled, y_train, X_val_filled, y_val):
    """Train and evaluate a RandomForest model with given parameters."""
    rf_model = RandomForestRegressor(n_estimators=n_estimators, max_features=max_features, max_depth=max_depth, random_state=42)
    rf_model.fit(X_train_filled, y_train)
    y_val_pred = rf_model.predict(X_val_filled)
    rmse = sqrt(mean_squared_error(y_val, y_val_pred))
    mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
    
    return (rmse, mape, rf_model, {'n_estimators': n_estimators, 'max_features': max_features, 'max_depth': max_depth})

def run_threads(X_train_filled, y_train, X_val_filled, y_val):
    """Runs hyperparameter tuning in parallel using threads."""
    best_rmse = float('inf')
    best_mape = float('inf')
    best_model = None
    best_parameters = {}

    # Define parameter ranges
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]
    max_depth_range = [1, 2, 5, 10, 20, None]

    # Start timing
    start_time = time.time()

    # Use ThreadPoolExecutor to parallelize training
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for n_estimators in n_estimators_range:
            for max_features in max_features_range:
                for max_depth in max_depth_range:
                    futures.append(
                        executor.submit(train_and_evaluate, n_estimators, max_features, max_depth, X_train_filled, y_train, X_val_filled, y_val)
                    )

        # Collect results
        for future in concurrent.futures.as_completed(futures):
            rmse, mape, model, params = future.result()
            print(f"Params: {params} -> RMSE: {rmse}, MAPE: {mape}%")

            # Update best model if current one is better
            if rmse < best_rmse:
                best_rmse = rmse
                best_mape = mape
                best_model = model
                best_parameters = params

    # End timing
    end_time = time.time()
    execution_time = end_time - start_time
    num_threads = len(futures)

    # Print results
    print(f"Best Parameters: {best_parameters} -> RMSE: {best_rmse}, MAPE: {best_mape}%")
    print(f"Threaded execution time: {execution_time} seconds")

    return best_model, best_parameters, best_rmse, best_mape, execution_time, num_threads

