from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    data = [
        quote
        for quote in quotes
        if quote['id'] == qid
    ]

    return data


def _quote_exists(existing_quote):
    for quote in quotes:
        if (
            quote['quote'] == existing_quote['quote']
            and
            quote['movie'] == existing_quote['movie']
        ):
            return True
    return False

@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    data = {
        "quotes": quotes
    }

    return jsonify(data)


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    data = {
        "quotes": _get_quote(qid)
    }

    if not data["quotes"]:
        abort(404)

    return jsonify(data)


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    quote = request.json

    if "movie" not in quote:
        abort(400)
    if "quote" not in quote:
        abort(400)

    if _quote_exists(quote):
        abort(400)

    quote['id'] = quotes[-1]['id'] + 1
    quotes.append(quote)

    return jsonify({"quote": quote}), 201


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    data = request.json

    if not data:
        abort(400)

    quote = _get_quote(qid)
    if not quote:
        abort(404)

    quote = quote[0]
    quote['quote'] = data['quote']
    quote['movie'] = data['movie']

    return jsonify({"quote": quote}), 200


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    if not _get_quote(qid):
        abort(404)

    global quotes
    quotes = [
        quote
        for quote in quotes
        if quote['id'] != qid
    ]
    return jsonify({"quotes": quotes}), 204
