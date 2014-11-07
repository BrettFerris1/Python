from wsgiref.simple_server import make_server
import psutil, datetime
def server_health_app(environ, start_response):
  boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
  cpu_util = psutil.cpu_percent(interval=1, percpu=True)
  mem = psutil.virtual_memory()
  message = ""
  status = '200 OK'
  headers = [('Content-type', 'html; charset=utf-8')]
  start_response(status, headers)
  message += "<h1>Server Health</h1>"
  message += "<table border =\"1\" allign=\"center\">"
  message += "<tr>"#row 1
  message += "<td><b>BOOT TIME:</td>"
  message += "<td>{}".format(boot_time)+"</td>"
  message += "</tr>"
  message += "<tr>"#row 2
  message += "<td><b>CPU UTILIZATION:</td>"
  message += "<td>"
  i=1
  for cpu in cpu_util:
    if cpu > 10:
      message += "<font color = \"red\">"
    else:
      message += "<font color = \"black\">"
    message += "CPU {} : {}%<br>".format(i, cpu)
    i+=1
  message += "</td>"	
  message += "<tr><td><b>AVAILABLIE MEMORY:</td>" #row 3
  message += "<td>{}</tr>".format(mem.available)
  message += "<tr><td><b>USED MEMORY:</td>"#row 4
  message += "<td>{}</td></tr>".format(mem.used)
  message += "<tr><td><b>USED PERCENTAGE:</td>"#row 5
  message += "<td>{}</td></tr>".format(mem.percent)
 
  return[bytes(message,'utf-8')]

httpd = make_server('', 8000, server_health_app)
print("Serving on port 8000...")

httpd.serve_forever()

