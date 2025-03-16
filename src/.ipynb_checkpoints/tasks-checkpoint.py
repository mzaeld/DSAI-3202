from celery import Celery

app = Celery("tasks", broker = "pyamqp://guest@localhost//", backend="rpc://"
) #the name of the file has to be same name o fth efirst quotiation

@app.task
def power(number, power):
    return number ** power


