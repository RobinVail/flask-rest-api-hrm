from flask import Flask, jsonify, make_response, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "hrm"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/hrm", methods=["GET"])
def get_hrm():
    data = data_fetch("""select * from employees_ext_involvements""")
    return make_response(jsonify(data), 200)
@app.route("/hrm/<int:id>", methods=["GET"])
def get_hrm_by_id(id):
    data = data_fetch("""select * from employees_ext_involvements where employees_idemployees = {}""".format(id))
    return make_response(jsonify(data), 200)


@app.route("/hrm/<int:id>/departments", methods=["GET"])
def get_employee_departments(id):
    query = """
        SELECT departments.dept_name, employees_unitassignments.transfer_date
        FROM employees
        INNER JOIN employees_unitassignments
        ON employees.idemployees = employees_unitassignments.employees_idemployees
        INNER JOIN departments
        ON employees_unitassignments.departments_iddepartments = departments.iddepartments
        WHERE employees.idemployees = {}
        """.format(id)
    data = data_fetch(query)
    return make_response(jsonify({"employee_id": id, "count": len(data), "departments": data}), 200)


@app.route("/skills", methods=["POST"])
def add_skill():
    cur = mysql.connection.cursor()
    info = request.get_json()

    # Extract data from the JSON request
    idskills = info.get("idskills")
    skill_type = info.get("skill_type")
    skill_description = info.get("skill_description")

    query = """
    INSERT INTO skills (idskills, skill_type, skill_description)
    VALUES (%s, %s, %s)
    """
    cur.execute(query, (idskills, skill_type, skill_description))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    return make_response(jsonify({"message": "Skill added successfully", "rows_affected": rows_affected}), 201)


@app.route("/skills/<int:idskills>", methods=["PUT"])
def update_skill(idskills):
    cur = mysql.connection.cursor()
    info = request.get_json()

    # Extract data from the JSON request
    skill_type = info.get("skill_type")
    skill_description = info.get("skill_description")

    query = """
    UPDATE skills
    SET skill_type = %s, skill_description = %s
    WHERE idskills = %s
    """
    cur.execute(query, (skill_type, skill_description, idskills))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    if rows_affected == 0:
        return make_response(jsonify({"message": "Skill not found"}), 404)

    return make_response(jsonify({"message": "Skill updated successfully", "rows_affected": rows_affected}), 200)

@app.route("/skills/<int:idskills>", methods=["DELETE"])
def delete_skill(idskills):
    cur = mysql.connection.cursor()
    query = "DELETE FROM skills WHERE idskills = %s"
    cur.execute(query, (idskills,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    if rows_affected == 0:
        return make_response(jsonify({"message": "Skill not found"}), 404)

    return make_response(jsonify({"message": "Skill deleted successfully", "rows_affected": rows_affected}), 200)


if __name__ == "__main__":
    app.run(debug=True)