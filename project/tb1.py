#!C:\Program Files\Python310\python.exe
import cgi, cgitb
#from sqlite3 import connect
import MySQLdb
form=cgi.FieldStorage()
n=form.getvalue('symptoms_fileupload')
cgitb.enable()
con=MySQLdb.connect("localhost","root","","project")
cur=con.cursor()
cur.execute("select * from normal")
row=cur.fetchall()
for r in row:
    id=r[0]
    img=r[1]
    if n!=img:
        t="1"
    else:
        t="0"
    #t=t.append(img)

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("    <title> RESPIRATORY ILLNESS </title>")
print("   ")
print("    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'>")
print("	<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.8.1/css/all.css'>")
print("	<link rel='stylesheet' href='dot.css'>")
print("</head>")
print("<body>")
print("    <div>  ")
print("<h1>Result is {}</h1>".format(t))
print("</div>")
print("</body></html>")