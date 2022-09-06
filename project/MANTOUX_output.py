#!C:\Program Files\Python310\python.exe
import cgi, cgitb
#import Mysqldb
cgitb.enable()
condition = [[["5mm"],["HIV positive / immunodeficiency state","Recent contact with active TB patient","X ray finding of old Tb","Organ transplant"], "Positive"],
[["10mm"],["IV drug user","Mycobacteriology Lab personnel","Children <4 years old","Co-morbid conditions","IV drug users","Nursing home residents","Malnutrition, Steroid use, Diabetes","Organ transplant","Travellers from endemic or high risk areas of TB","Homeless","Prisoners","Chronic fever"], "Positive"],
[["15mm"],["No known risk factors"], "Positive"]]

f=cgi.FieldStorage()
a=f.getvalue('mantoux_checkbox', "")
b=f.getvalue('risk_factor_checkbox', [])
output = "Negative"
for i in condition:
    if a in i[0]:
        if type(b) == str:
            b = [b]
        for j in b:
            if j not in i[1]:
                break
        else:
            output = i[2]
    if output != "Negative":
        break


# c=f.getvalue('fvc', 0)
# z=int(a)+int(b)+int(c)
'''
if z<= 60:
    n='high'
elif z<=150:
    n='less'
    '''
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("    <title> RESPIRATORY ILLNESS </title>")
print("   ")
print("    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'>")
print("<script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script>")
print("<script src='https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js' integrity='sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin='anonymous'></script>")
print("<link rel='stylesheet' href='dot.css'>")
print("</head>")
print("")
print("<body>")
print("    <div>  ")
print("        <nav class='navbar navbar-expand-sm navbar-light' style='background-color:#98FB98'>")
print("            <a class='navbar-brand' >")
print("                <img src='logo.png' width='100' height='100' /> RESPIRATORY ILLNESS </a>")
print("            <ul class='navbar-nav ml-auto'>")
print("                <li class='nav-item'>")
print("                    <a class='nav-link' href='main.py'>Home</a>")
print("                </li>")
print("                     <li class='nav-item'>")
print("                    <a class='nav-link' href='#'>About </a>")
print("                </li>")
print("                     <li class='nav-item'>")
print("                    <a class='nav-link' href='#'>Contact us</a>")
print("                </li>")
print("            </ul>")
print("        </nav>")
print("    </div>")
print("")
print("     ")
print("    </div>")
print("         <center><h3><b>MANTOUX TEST RESULT</b></h3></center>")
print("<h1>{}</h1>".format(a))
print("<h1>{}</h1>".format(b))
print("<h1><b>{}</b></h1>".format(output))
# print("<h1>Result : {}</h1>".format(z))
print("</body></html>")