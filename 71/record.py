class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.max_score = None

    def __call__(self, score):
        if self.max_score is None or self.max_score < score:
            self.max_score = score

        return self.max_score
