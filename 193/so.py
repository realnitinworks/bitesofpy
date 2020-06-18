import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    content = requests.get(cached_so_url)
    content.raise_for_status()

    soup = BeautifulSoup(content.text, 'html.parser')

    questions_genexp = (links.getText() for links in soup.select('.question-hyperlink'))
    votes_genexp = (votes.getText() for votes in soup.select('.vote-count-post'))
    views_genexp = (views.getText() for views in soup.select('.views'))

    most_voted_questions = (
       (question, int(votes))
       for question, votes, views in zip(questions_genexp, votes_genexp, views_genexp)
       if "m" in views  # Million views
    )

    # sorted on the votes in descending order.
    yield from sorted(most_voted_questions, key=lambda x: x[1], reverse=True)
