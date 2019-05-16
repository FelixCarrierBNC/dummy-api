from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import inputs

app = Flask(__name__)
api = Api(app)


# ---------- float ---------- 
parser_float = api.parser()
parser_float.add_argument('value', type=float, default=0.42)

@api.route('/a_float')
class a_float(Resource):
    @api.expect(parser_float)
    def get(self):
        args = parser_float.parse_args()
        return dict(args)


# ---------- int ----------
parser_int = api.parser()
parser_int.add_argument('value', type=int, default=23)

@api.route('/a_int')
class a_int(Resource):
    @api.expect(parser_int)
    def get(self):
        args = parser_int.parse_args()
        return dict(args)


# ---------- string ----------
parser_string = api.parser()
parser_string.add_argument('value', type=str, default="Hello World!")

@api.route('/a_string')
class a_string(Resource):
    @api.expect(parser_string)
    def get(self):
        args = parser_string.parse_args()
        return dict(args)


# ---------- bool ----------
# How to expect a bool:
# https://github.com/noirbizarre/flask-restplus/issues/199#issuecomment-276645303
parser_bool = api.parser()
parser_bool.add_argument('value', type=inputs.boolean, default=True)

@api.route('/a_bool')
class a_bool(Resource):
    @api.expect(parser_bool)
    def get(self):
        args = parser_bool.parse_args()
        return dict(args)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')