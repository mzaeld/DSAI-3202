import multiprocessing
import time
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from math import sqrt

def evaluate_model(params):
    X_train_filled, y_train, X_val_filled, y_val, n_estimators, max_features, max_depth = params
    rf_model = RandomForestRegressor(n_estimators=n_estimators, max_features=max_features, max_depth=max_depth, random_state=42)
    rf_model.fit(X_train_filled, y_train)
    y_val_pred = rf_model.predict(X_val_filled)
    
    rmse = sqrt(mean_squared_error(y_val, y_val_pred))
    mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
    
    print(f"Params: {n_estimators}, {max_features}, {max_depth} -> RMSE: {rmse}, MAPE: {mape}%")
    return (rmse, mape, {'n_estimators': n_estimators, 'max_features': max_features, 'max_depth': max_depth})

def run_process(X_train_filled, y_train, X_val_filled, y_val):
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]
    max_depth_range = [1, 2, 5, 10, 20, None]

    param_combinations = [(X_train_filled, y_train, X_val_filled, y_val, n, f, d)
                          for n in n_estimators_range for f in max_features_range for d in max_depth_range]

    start_time = time.time()
    
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(evaluate_model, param_combinations)
    
    best_rmse, best_mape, best_parameters = min(results, key=lambda x: x[0])  # Sort by lowest RMSE

    end_time = time.time()
    multiprocessing_time = end_time - start_time
    num_processes = len(param_combinations)

    print(f"Best Parameters: {best_parameters} -> RMSE: {best_rmse}, MAPE: {best_mape}%")
    print(f"Multiprocessing execution time: {multiprocessing_time} seconds")

    return best_parameters, best_rmse, best_mape, multiprocessing_time, num_processes

