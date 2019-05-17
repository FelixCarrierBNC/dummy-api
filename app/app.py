from flask import Flask, request
from flask_restplus import Resource, Api, fields, marshal
from flask_restplus import inputs
import random
import hashlib

app = Flask(__name__)
api = Api(app)


# ----- predictions ---------------

inputs_fields = api.model('Prediction', {
  'id': fields.String(required=True, description='Customer ID', default='C001', example="C001"),
  'city': fields.String(default='Montreal', example='Montreal'),
  'age': fields.Integer(default=54, example=54)
})

default_input = [
    {
      "id": "C-001",
      "city": "Montreal",
      "age": 54
    },
    {
      "id": "C-002",
      "city": "Quebec",
      "age": 43
    },
    {
      "id": "C-003",
      "city": "Laval",
      "age": 73
    }
  ]

inputs_fields_list = api.model('PredictionList', {
    'inputs': fields.List(fields.Nested(inputs_fields), default=default_input, example=default_input),
})

@api.route('/predictions')
class predictions(Resource):
    @api.expect(inputs_fields_list)
    def post(self):
        """Returns inputs and a score (float) between 0 and 1"""
        json_data = request.json
        inputs = dict(json_data)['inputs']

        def str_to_score(d):
            h = int(hashlib.sha1(d.encode('utf-8')).hexdigest(), 16)
            return abs(h%10000 / 10000)

        for i in inputs:
            i['predicted_score']= str_to_score(i['id'])

        return {'value':inputs}


        


# ---------- float ---------- 
parser_float = api.parser()
parser_float.add_argument('value', type=float, default=0.42)

@api.route('/a_float')
class a_float(Resource):
    @api.expect(parser_float)
    def get(self):
        args = parser_float.parse_args()
        return dict(args)


parser_random = api.parser()
parser_random.add_argument('n', type=int, default=1)
@api.route('/a_float/random')
class a_float_random(Resource):
    @api.expect(parser_random)
    def get(self):
        n = dict(parser_random.parse_args())['n']
        if n ==1:
            value = round(random.uniform(0, 1), 4)
            return {"value":value}
        else:
            value = [round(random.uniform(0, 1), 4) for i in range(n)]
            return {"value":value} 



parser_float_list = api.parser()
parser_float_list.add_argument('value', type=float,action='split', default=[0.43,0.85,0.12,0.98])

@api.route('/a_float/batch')
class a_float_batch(Resource):
    @api.expect(parser_float_list)
    def get(self):
        args = parser_float_list.parse_args()
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


@api.route('/a_int/random')
class a_int_random(Resource):
    @api.expect(parser_random)
    def get(self):
        n = dict(parser_random.parse_args())['n']
        if n==1:
            value = int(100*random.uniform(0, 1))
            return {"value":value}
        else:
            value = [int(100*random.uniform(0, 1)) for i in range(n)]
            return {"value":value}


parser_int_list = api.parser()
parser_int_list.add_argument('value', type=int,action='split', default=[25,43,78,6])

@api.route('/a_int/batch')
class a_int_batch(Resource):
    @api.expect(parser_int_list)
    def get(self):
        args = parser_int_list.parse_args()
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

names = ["Abbie",
"Nathan",
"Lance",
"Tiana",
"Danelle",
"Albert",
"Jovan",
"Chan",
"Bryant",
"Tamekia",
"Lecia",
"Constance",
"Mariana",
"Martha",
"Una",
"Stevie",
"Lorelei",
"Marylee",
"Elton",
"Mirta",
"Melanie",
"Evan",
"Lashell",
"Maranda",
"Wanetta",
"Agueda",
"David",
"Lynetta",
"Kaci",
"Jacquiline"]

@api.route('/a_string/random')
class a_string_random(Resource):
    @api.expect(parser_random)
    def get(self):
        n = dict(parser_random.parse_args())['n']
        if n==1:
            value = random.choice(names)
        else:
            value = [random.choice(names) for i in range(n)]
        return {"value":value}




parser_string_list = api.parser()
parser_string_list.add_argument('value', type=str,action='split', default=["John", "Marie", "Bob", "Charlotte"])

@api.route('/a_string/batch')
class a_string_batch(Resource):
    @api.expect(parser_string_list)
    def get(self):
        args = parser_string_list.parse_args()
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


list_bool = [True,False]
@api.route('/a_bool/random')
class a_bool_random(Resource):
    @api.expect(parser_random)
    def get(self):
        n = dict(parser_random.parse_args())['n']
        if n==1:
            value = random.choice(list_bool)
        else:
            value = [random.choice(list_bool) for i in range(n)]
        return {"value":value}



parser_bool_list = api.parser()
parser_bool_list.add_argument('value', type=inputs.boolean,action='split', default=[True, False, True, False])

@api.route('/a_bool/batch')
class a_bool_batch(Resource):
    @api.expect(parser_bool_list)
    def get(self):
        args = parser_bool_list.parse_args()
        return dict(args)


# ---------- mixed types ----------
parser_mixed = api.parser()
parser_mixed.add_argument('age', type=int, default=23)
parser_mixed.add_argument('name', type=str, default="John")
parser_mixed.add_argument('score', type=float, default=0.68)
parser_mixed.add_argument('is_customer', type=inputs.boolean, default=True)

@api.route('/mixed_types')
class mixed_types(Resource):
    @api.expect(parser_mixed)
    def get(self):
        args = parser_mixed.parse_args()
        return dict(args)


@api.route('/mixed_types/random')
class mixed_types_random(Resource):
    @api.expect(parser_random)
    def get(self):
        n = dict(parser_random.parse_args())['n']
        def mixed():
            return {
                "age":int(100*random.uniform(0.18, 0.85)),
                "name":random.choice(names),
                "score":round(random.uniform(0, 1), 4),
                "is_customer":random.choice(list_bool)

            }
        if n==1:
            return {"value":mixed()} 
        else:
            return {"value":[mixed() for i in range(n)]}



# ------ run ----------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')