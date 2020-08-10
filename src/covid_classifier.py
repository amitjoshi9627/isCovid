import engine


def get_prediction(img):
    result = engine.get_results(img)
    if result == 0:
        return "Covid Positive"
    else:
        return "Covid Negative"
