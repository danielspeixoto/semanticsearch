def map(correct, questions):
    ids = [question['id'] for question in questions]
    return float(1)/(ids.index(correct) + 1)
