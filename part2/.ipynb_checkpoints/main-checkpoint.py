from src.data import *
from src.seq_case import *
from src.threads_case import *
from src.process_case import *

X_train_filled, y_train, X_val_filled, y_val = load_preprocess_data()

best_model, best_parameters, best_rmse, best_mape, sequential_time = run_sequential(X_train_filled, y_train, X_val_filled, y_val)
best_model, best_parameters, best_rmse, best_mape, threading_time,num_threads = run_threads(X_train_filled, y_train, X_val_filled, y_val)

best_parameters, best_rmse, best_mape, multiprocessing_time,num_processes = run_process(X_train_filled, y_train, X_val_filled, y_val)

compute_metrics(sequential_time, threading_time, multiprocessing_time, num_threads, num_processes)

