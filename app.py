from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import xmltodict
import mysql.connector

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hrm"
)

cursor = db.cursor()

class Relative(Resource):
    def get(self, id):
        cursor.execute("SELECT * FROM relatives WHERE idrelatives = %s", (id,))
        relative = cursor.fetchone()
        if relative:
            result = {
                "idrelatives": relative[0],
                "first_name": relative[1],
                "middle_name": relative[2],
                "last_name": relative[3],
                "name_extension": relative[4],
                "Occupation": relative[5],
                "Emp_business": relative[6],
                "business_address": relative[7],
                "telephone": relative[8],
                "birthdate": relative[9]
            }
            if 'format' in request.args and request.args['format'] == 'xml':
                return xmltodict.unparse({"relative": result}), 200, {'Content-Type': 'application/xml'}
            else:
                return jsonify(result)
        else:
            return {"message": "Relative not found"}, 404

    def post(self):
        data = request.get_json()
        cursor.execute("INSERT INTO relatives (first_name, middle_name, last_name, name_extension, Occupation, Emp_business, business_address, telephone, birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (data['first_name'], data['middle_name'], data['last_name'], data['name_extension'], data['Occupation'], data['Emp_business'], data['business_address'], data['telephone'], data['birthdate']))
        db.commit()
        return {"message": "Relative added"}, 201

    def put(self, id):
        data = request.get_json()
        cursor.execute("UPDATE relatives SET first_name = %s, middle_name = %s, last_name = %s, name_extension = %s, Occupation = %s, Emp_business = %s, business_address = %s, telephone = %s, birthdate = %s WHERE idrelatives = %s",
                       (data['first_name'], data['middle_name'], data['last_name'], data['name_extension'], data['Occupation'], data['Emp_business'], data['business_address'], data['telephone'], data['birthdate'], id))
        db.commit()
        return {"message": "Relative updated"}, 200

    def delete(self, id):
        cursor.execute("DELETE FROM relatives WHERE idrelatives = %s", (id,))
        db.commit()
        return {"message": "Relative deleted"}, 200

api.add_resource(Relative, "/relative", "/relative/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
