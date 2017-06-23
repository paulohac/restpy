#!flask/bin/python
from flask import Flask, jsonify, abort
from flask_restful import reqparse, Api, Resource
from flasgger import Swagger

from prezi import PAGE_SIZE
import db
import psycopg2
import uuid
import traceback

app = Flask(__name__)
api = Api(app)
app.config['SWAGGER'] = {
    'title': 'Prezi API',
}
Swagger(app)


index_parser = reqparse.RequestParser()
index_parser.add_argument('title', type=str, default=None, location='args')
index_parser.add_argument('page', type=int, default=1, location='args')


def row_to_prezi(row):
    return {
        'id': row[0],
        'title': row[1],
        'picture': row[2],
        'createdAt': str(row[3]),
        'creator': {
            'id': row[4],
            'name': row[5]
        }
    }


class Prezi(Resource):

    def get(self, prezi_id):
        """
        Get a single Prezi from database

        ---
        required:
         - id
        tags:
         - prezi
        parameters:
         - in: path
           name: prezi_id
           description: uuid of the prezi
           type: string
        responses:
         200:
           description: A single prezi
        """

        try:
            prezi_id = uuid.UUID(prezi_id)
        except:
            return '%s is not a valid uuid!' % prezi_id, 400

        prezi = {}
        try:
            with db.connection.cursor() as cursor:
                cursor.execute('SELECT * FROM prezis WHERE id=%s', (str(prezi_id), ))
                row = cursor.fetchone()
                if row:
                    prezi = row_to_prezi(row)

            return prezi, 200

        except:
            print(traceback.format_exc())
            return {}, 500


class PreziIndex(Resource):

    def get(self):
        """
        Returns a list of Prezi's

        ---
        tags:
         - prezi
        parameters:
         - in: query
           name: title
           type: string
           description: phrase to search for in prezi titles
         - in: query
           name: page
           type: integer
           description: page number
        responses:
         200:
           description: Lists of prezis
        """
        args = index_parser.parse_args(strict=True)

        sql_query = 'SELECT * FROM prezis'
        sql_params = []
        if args['title']:
            sql_query += " WHERE title ILIKE %s"
            sql_params.append('%'+ args['title'] + '%')

        sql_query  += ' ORDER BY id ASC OFFSET %s LIMIT %s'
        sql_params.append((args['page']-1) * PAGE_SIZE)
        sql_params.append(PAGE_SIZE)

        prezis = []
        with db.connection.cursor() as cursor:
            cursor.execute(sql_query, sql_params)
            rows = cursor.fetchall()
            for row in rows:
                prezis.append(row_to_prezi(row))

        return prezis, 200


api.add_resource(PreziIndex, '/prezi')
api.add_resource(Prezi, '/prezi/<prezi_id>')



if __name__ == '__main__':
    db.init()
    app.run(debug=True, host="0.0.0.0")
