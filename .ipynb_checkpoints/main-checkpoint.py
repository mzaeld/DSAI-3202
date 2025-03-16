from src.tasks import power
from src.dispatch_task import dispatch


if __name__ == "__main__":
    results = dispatch()
    print(results[:10])