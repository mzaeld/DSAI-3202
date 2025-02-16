import multiprocessing
import time
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from math import sqrt

def run_process(X_train_filled, y_train, X_val_filled, y_val):

        # Define the parameter ranges
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]  # None means using all features
    max_depth_range = [1, 2, 5, 10, 20, None]  # None means no limit
    
    best_rmse = float('inf')
    best_mape = float('inf')
    best_model = None
    best_parameters = {}
    
    start_time = time.time()
    processes = []
    
    def train_and_evaluate(n_estimators, max_features, max_depth):
        nonlocal best_rmse, best_mape, best_model, best_parameters
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
    
    for n_estimators in n_estimators_range:
        for max_features in max_features_range:
            for max_depth in max_depth_range:
                process = multiprocessing.Process(target=train_and_evaluate, args=(n_estimators, max_features, max_depth))
                processes.append(process)
                process.start()
    
    for process in processes:
        process.join()
    
    end_time = time.time()
    multiprocessing_time = end_time - start_time
    num_processes = len(processes)
    print(f"Best Parameters: {best_parameters} -> RMSE: {best_rmse}, MAPE: {best_mape}%")
    print(f"Multiprocessing execution time: {multiprocessing_time} seconds")
    
    return best_model, best_parameters, best_rmse, best_mape, multiprocessing_time,num_processes
