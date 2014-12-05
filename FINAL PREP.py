from wsgiref.simple_server import make_server
import re
import sqlite3
from tkinter import *


def Graph(names,data):
  space=100
  i=0
  base=Tk()
  base.title("ZOO GRAPH")
  canvas = Canvas(base, bg="white", height=1000, width=1000)
  canvas.pack()
  for value in data:
    space+=50
    canvas.create_text(40,space, anchor=W, text=names[i])
    canvas.create_line(100, space, 10*value+100, space, fill="black") #x, y to x, y
    
    i+=1
  base.mainloop()

def hello_world_app(environ, start_response):
        
  
  global entry
  entry = []
  entryList=[]
  names=[]
  data=[]
  message=""
  status = '200 OK'
  headers = [('Content-type', 'html; charset=utf-8')]
  start_response(status, headers)
  if(len(environ['QUERY_STRING'])>1):
    message += "<br> Your data has been recieved:"
    for param in environ['QUERY_STRING'].split("&"):
      message += "<br>"+param
      a=param.split("=")
      if "Submit" in a:
        continue
      entry.append(a[1])
    entry = tuple(entry)
    conn = sqlite3.connect("zoo.sqlite")
    cursor = conn.cursor()
    try:
      list(entry)
      int(entry[1])
      cursor.execute("insert into animal_count(name, count) values(?, ?)", entry )
      
####      int(entry[0])
####      raise SyntaxError("My own error")
####    
##    except SyntaxError:
##      message += "<br><font color = \"blue\">AN ERROR HAS OCCURED"      
##      #cursor.execute("insert into animal_count(name, count) values(?, ?)", entry )
    except (ValueError,TypeError):
      message += "<br><font color = \"red\">AN ERROR HAS OCCURED"
      message += "<h1>Welcome to the Zoo</h1>"
      message += "<form><br>Animal:<input name='member'>"
      message += "<br><br>Count:<input name='count'>"
      message += "<br><br><input type='submit' name='Submit' ></form>"
      return[bytes(message,'utf-8')]
      
##    try:
##      int(entry[0])
##      raise SyntaxError("My own error")
##    except SyntaxError:
##      message += "<br><font color = \"blue\">AN ERROR HAS OCCURED"
##    
##    cursor.execute("insert into animal_count(name, count) values(?, ?)", entry )
    result = cursor.execute("select * from animal_count")
    message+="<table><font color = \"black\">"
    for row in result:
      list(row)
      message+="<tr>"
      message += "<td>"+str(row[0])+"</td><td>"+str(row[1])+"</td>"
      names.append(row[0])
      data.append(row[1])
    message+="</table>"  
    conn.commit()
    conn.close()
    Graph(names,data)
  
  message += "<h1>Welcome to the Zoo</h1>"
  message += "<form><br>Animal:<input name='member'>"
  message += "<br><br>Count:<input name='count'>"
  message += "<br><br><input type='submit' name='Submit' ></form>"
  
  
  return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)

print("Serving on port 8000...")

##conn = sqlite3.connect("zoo.sqlite")
##cursor = conn.cursor()
##cursor.execute("create table animal_count (name text, count integer)")
##animals=[('Frog', 10), ('Snake', 5), ('Turtle', 11)]
##cursor.executemany("insert into animal_count(name, count) values(?, ?)", animals)
##result = cursor.execute("select * from animal_count")
##conn.commit()
##conn.close()

httpd.serve_forever()
##printe("entry =" )
