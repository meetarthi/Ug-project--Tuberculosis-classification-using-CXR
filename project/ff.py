#!C:\Program Files\Python310\python.exe
import cgi, cgitb
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<form>")
print("<form action = 'a.py' method = 'POST' target = '_blank'>")
print("<input type = 'checkbox' name = 'maths' value = 'on' /> Maths")
print("<input type = 'checkbox' name = 'physics' value = 'on' /> Physics")
print("<input type = 'submit' value = 'Select Subject' />")
print("</form>")
print("</body>")
print("</html>")