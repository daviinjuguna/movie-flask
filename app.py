from flask import Flask, app, request, jsonify,render_template
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import json
from flask_paginate import Pagination, get_page_args
import os


# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


f = open('movies.json', encoding="utf8")
data = json.loads(f.read())


def get_movies(offset=0, per_page=10):
    return data[offset: offset + per_page]


@app.route('/', methods=['GET'])
def init():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(data)
    paginated_movies = get_movies(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template('index.html',
                           movies=paginated_movies,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


# runserver
if __name__ == '__main__':
    app.run(debug=True)
