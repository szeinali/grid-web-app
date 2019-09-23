import pandas as pd
import flask
import flask_paginate
app = flask.Flask(__name__)



filename = "data_fullstack.csv"
data = pd.read_csv(filename, header=0)
flat_data = list(data.values)
total = len(flat_data)


def get_rows(offset=0, per_page=10):
    return flat_data[offset: offset + per_page]

@app.route('/')
def index():

    page, per_page, offset = flask_paginate.get_page_args(page_parameter='page',
                                                          per_page_parameter='per_page')
    rows = get_rows(offset=offset,
                    per_page=per_page)
    pagination = flask_paginate.Pagination(page=page,
                                           per_page=per_page,
                                           total=total,
                                           css_framework='bootstrap4')

    return flask.render_template('index.html', rows=rows, page=page, per_page=per_page, pagination=pagination)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=True)