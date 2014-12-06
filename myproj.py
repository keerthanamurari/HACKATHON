from wsgiref.simple_server import make_server
import sqlite3
import cgi
import cgitb
from collections import OrderedDict


conn = sqlite3.connect("Questions.sqlite") 
cursor = conn.cursor()
form_vals={}
list1=cursor.execute("select * from test_count").fetchall()
print(list1)
##def get_form_vals(post_str):
##  form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
##  print(post_str)
##  return form_vals
def get_form_vals(post_str):
        print(post_str)
        i=0
        x=0
        form_vals.clear();
        for item in post_str.decode().split("&"):
                i=i+1
                
                if(item.split("=")[0]!="submit" and item.split("=")[0]!="submit"):
                         x=x+1
                         x1=item.split("=")[0]
                         x2=item.split("=")[1]
                         x1=x1+str(x)
                         form_vals[x1] = x2
                         #print(x1)
                         #print(x2)
        print(form_vals)     
        return form_vals
def hello_world_app(environ, start_response):
    #print("ENVIRON:", environ)
    message="<head><style>body{background-color:#FFCC00}</style></head>"
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    if(environ['REQUEST_METHOD'] == 'POST'):
        #message += "<br>Your data has been recorded:"
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        form_vals = get_form_vals(request_body)
        form_vals=OrderedDict(sorted(form_vals.items(),key=lambda t:t[0]))
##        for key,value in form_vals.items():
##                if(key!="submit"):
##                message+=key+"  "
##                message+=value+"  "
                
           # for abc in list1:
                #print(form_vals[item])
                #print(abc[5])
                #if(form_vals[item]==abc[5]):
                   # print("correct")
            #message += "<br/>"+item + " = " + form_vals[item]
    message += "<h1>SOCIAL SITES<form method='POST'></h1>"
    message+="<form method='post'>"
    message += "<br>Search Query:<input type=text name='animal'>"
    message += "<br><br>Count:<input type=text name='count'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"
    return[bytes(message,'utf-8')]
##    i=0
##    for item in list1:
##            message+="<br>"+item[0]+"<br>"+item[1]+" "+item[2]+" "+item[3]+" "+item[4]+"<input type=text name='q'"+str(i)+">"
##            i+=1
##    
    #message += "<br><br>Count:<input type=text name='count'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"
    return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()
conn.close()
