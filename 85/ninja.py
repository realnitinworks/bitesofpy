scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))
CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG = 'Set new score to {score}'


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for score in reversed(scores):
            if new_score >= score:
                return BELTS[score].capitalize()
        return None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError("Score must be an integer")

        if new_score < self._score:
            raise ValueError("Score cannot be lower than previous")

        belt = self._get_belt(new_score)
        if belt != self._last_earned_belt:
            self._last_earned_belt = belt
            print(CONGRATS_MSG.format(score=new_score, rank=belt))
        else:
            self._score = new_score
            print(NEW_SCORE_MSG.format(score=new_score))
