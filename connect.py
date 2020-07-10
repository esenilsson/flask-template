# import the necessary packages
import flask
import json
import pymysql
import requests
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# configuration used to connect to MariaDB
config = {
    'host':'192.168.4.23', 
    'port':36033,
    'user':'root',
    'password':'gems729',
    'db':'bearfood',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
}

# route to return all people
@app.route('/api/users', methods=['GET'])
def users():
   conn = pymysql.connect(**config)
   cur = conn.cursor()
   cur.execute("select * from users")
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for r in rv:
      json_data.append(dict(r))
   return json.dumps(json_data)

# route to return ingredients
@app.route('/api/ingredients', methods=['GET'])
def ingredients():
   conn = pymysql.connect(**config)
   cur = conn.cursor()
   cur.execute("select * from ingredients")
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for r in rv:
      json_data.append(dict(r))
   return json.dumps(json_data)

# route to return tours
@app.route('/api/<user_id>/tours', methods=['GET'])
def tours():
   conn = pymysql.connect(**config)
   cur = conn.cursor()
   cur.execute("select * from tours where user_id = {:s}".format(user_id))
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for r in rv:
      json_data.append(dict(r))
   return json.dumps(json_data)


# route to return meals
@app.route('/api/<user_id>/meals', methods=['GET'])
def meals():
   conn = pymysql.connect(**config)
   cur = conn.cursor()
   cur.execute("select * from meals where user_id = {:s}".format(user_id))
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for r in rv:
      json_data.append(dict(r))
   return json.dumps(json_data)



# route to return tours
@app.route('/api/<user_id>/<tour_id>', methods=['GET'])
def get_tour():
   conn = pymysql.connect(**config)
   cur = conn.cursor()
   cur.execute("select * from tours where user_id = {:s} and id = {:s}".format(user_id, tour_id))
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for r in rv:
      json_data.append(dict(r))
   return json.dumps(json_data)






# route to add user
@app.route('/api/add_user/', methods=['POST'])
def add_user():
    item = request.get_json()
    print("insert into users (name, email) values ('{:s}','{:s}');".format(item['name'],item['email']))
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute("insert into users (name, email) values ('{:s}','{:s}');".format(item['name'],item['email']))
    conn.commit()
    return item

app.run()





# x = [{"id": 2, "email": "katy.ho@outlook.com", "name": "Katy"}]

# for item in x:
#     item['name']