#!C:\Program Files\Python310\python.exe
import cgi, cgitb
#import Mysqldb
cgitb.enable()

f=cgi.FieldStorage()
a=f.getvalue('fev1', -1)
b=f.getvalue('fvc1', -1)
c=f.getvalue('fvc2', -1)


fev1=int(a)
fvc1=int(b)
fvc2=int(c)
if (fev1 > 80) and (fvc1 >80 ) and (fvc2 >70):
    n="normal"
elif (fev1 < 80) and (fvc1 > 80) and (fvc2 <70):
    n="Obstructive pattern- This kind of pattern may be due to underlying conditions like Asthma,Bronchitis, COPD,emphysema. "
elif (fev1 > 80 ) and (fvc1 < 80) and (fvc2 <70):
    n="Restrictive pattern- This kind of pattern may be due to underlying conditions like Pulmonary fibrosis, Neuromuscular disorders,Congestive heart failure, Sarcoidosis."    
else:
    n=""

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
print("")
print("     ")
print("    </div>")
print("    <br></br>")
print("    <div class='container'>")
print("        <div>")
print("            <center><h3><b><U>SPIROMETRY INTERPRETATION</U></b></h3></center>")
print("        </div>")
print("        <br/>")   
print("        </div> <br/><br/>     ")
print("<div class='form-group container'>")
print("     <div class='row'>")
print("     <div class='col-sm'>")
print("<br/>")
print("<br/>")
print("<form action='asthma.py' method='GET/POST'>")
print("<label for='fev1'>FEV1:</label>")
print("<input type='text' id='fev1' name='fev1'><br/><br/><br/>")
print("")
print("<label for='fvc'>FVC:</b></label>")
print("<input type='text' id='fvc1' name='fvc1'><br/><br/><br/>")
print("")
print("<label for='fvc'>FEV1/FVC:</b></label>")
print("<input type='text' id='fvc2' name='fvc2'><br/><br/><br/>")
print("")
print("        <button type='submit' class='btn btn-primary'>Submit</button></form>")
print("        </div>")
print("     <div class='col-sm'>")
print("         <div class='card'>")
print("           <div class='card-body'>")
print("<h4><b><center>RESULT</center></b></h4>")
print("<h1>{}</h1>".format(n))
print("</div>")
print("         </div>")
print("</div>")
print(" ")
print("<br/><br/>")
print("       </div>")
print("</div>  ")
print("    </div>  ")
print("</body>")
print("<script type='text/javascript'>")
print("    $('.dropdown-toggle').dropdown()")
print("</script>")
print("</html>")