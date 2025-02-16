import time
import threading
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from math import sqrt

def run_threads(X_train_filled, y_train, X_val_filled, y_val):
    global best_rmse, best_mape, best_model, best_parameters

    best_rmse = float('inf')
    best_mape = float('inf')
    best_model = None
    best_parameters = {}

    # Define parameter ranges
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]  # None means using all features
    max_depth_range = [1, 2, 5, 10, 20, None]  # None means no limit

    # Start timing
    start_time = time.time()
    threads = []

    # Launch threads for parameter tuning
    for n_estimators in n_estimators_range:
        for max_features in max_features_range:
            for max_depth in max_depth_range:
                def run(n_estimators=n_estimators, max_features=max_features, max_depth=max_depth):
                    global best_rmse, best_mape, best_model, best_parameters
                    rf_model = RandomForestRegressor(n_estimators=n_estimators, max_features=max_features, max_depth=max_depth, random_state=42)
                    rf_model.fit(X_train_filled, y_train)
                    y_val_pred = rf_model.predict(X_val_filled)
                    rmse = sqrt(mean_squared_error(y_val, y_val_pred))
                    mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
                    
                    if rmse < best_rmse:
                        best_rmse = rmse
                        best_mape = mape
                        best_model = rf_model
                        best_parameters = {'n_estimators': n_estimators, 'max_features': max_features, 'max_depth': max_depth}
                    
                    print(f"Params: {n_estimators}, {max_features}, {max_depth} -> RMSE: {rmse}, MAPE: {mape}%")

                thread = threading.Thread(target=run)
                threads.append(thread)
                thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    threading_time = end_time - start_time
    num_threads = len(threads)
    # Print results
    print(f"Best Parameters: {best_parameters} -> RMSE: {best_rmse}, MAPE: {best_mape}%")
    print(f"Threaded execution time: {threading_time} seconds")

    return best_model, best_parameters, best_rmse, best_mape, threading_time,num_threads
