from wsgiref.simple_server import make_server
import re
import sqlite3

def hello_world_app(environ, start_response):
        
  print("ENVIRON:", environ)
  global entry
  entry = []
  message=""
  status = '200 OK'
  headers = [('Content-type', 'html; charset=utf-8')]
  start_response(status, headers)
  if(len(environ['QUERY_STRING'])>1):
    message += "<br> Your data has been recieved:"
    for param in environ['QUERY_STRING'].split("&"):
      message += "<br>"+param
      print("param=", param)
      for param2 in str(param).split("="):
        print("param2 = ",param2)
        if (str(param2).lower() != "animal" or "count" or "submit"):
          print("add: ")
          entry.append(param2)
          print("entry =",entry)
              
  message += "<h1>Welcome to the Zoo</h1>"
  message += "<form><br>Animal:<input type=text name='animal'>"
  message += "<br><br>Count:<input type=text name='count'>"
  message += "<br><br><input type='submit' name='Submit' ></form>"
  return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)

print("Serving on port 8000...")

##conn = sqlite3.connect("zoo.sqlite")
##cursor = conn.cursor()
##animals=[('Frog', 10), ('Snake', 5), ('Turtle', 11)]
##cursor.executemany("insert into animal_count(name, count) values(?, ?)", animals)
##result = cursor.execute("select * from animal_count")
##conn.commit()
##conn.close()

httpd.serve_forever()
printe("entry =" )
