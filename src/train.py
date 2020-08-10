import engine
from model import CovidModel

if __name__ == "__main__":
    model = CovidModel()
    engine.train_fn(model)
