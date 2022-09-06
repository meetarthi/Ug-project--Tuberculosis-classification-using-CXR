#!C:\Program Files\Python310\python.exe
import cgi, cgitb
form=cgi.FieldStorage()
n=form.getvalue('symptoms_fileupload')
cgitb.enable()

# ## For Prediction
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

file = "./images/"+str(n)
cnn = load_model("./model/tf_model.h5")
img = image.load_img(file, target_size=(500, 500), color_mode='grayscale')

# Preprocessing the image
pp_img = image.img_to_array(img)
pp_img = pp_img/255
pp_img = np.expand_dims(pp_img, axis=0)

# predict
preds = cnn.predict(pp_img)

if preds >= 0.5:
    out = ('{:.2%} - Tuberculosis'.format(preds[0][0]))
else:
    out = ('{:.2%} - Normal'.format(1-preds[0][0]))




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
print("        </nav>")
print("    </div>")
print("")
print("    <div>  ")
print("<img src='{}' width='300' height='300'>".format(file))
print("<h1>Result is {}</h1>".format(out))
print("</div>")
print("</body></html>") 
#!C:\Users\Arthi\AppData\Local\Programs\Python\Python310\python.exe
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
print("")
print("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'>")
print("<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.8.1/css/all.css'>")
print("<link rel='stylesheet' href='dot.css'>")
print("")
print("    <script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script>")
print("    <script src='https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js' integrity='sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin='anonymous'></script>")
print("    <script src='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script>")
print("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("</head>")
print("<body>")
print("    <div>  ")
print("        <nav class='navbar navbar-expand-sm navbar-light' style='background-color:#98FB98'>")
print("            <a class='navbar-brand' >")
print("                <img src='Screenshot 2022-02-24 190456.png' width='100' height='100' /> RESPIRATORY ILLNESS </a>")
print("        </nav>")
print("     ")
print("    </div>")
print("         <center><h3><b>TB DIAGNOSIS</b></h3></center>")
print("<h1>{}</h1>".format(a))
print("<h1>{}</h1>".format(b))
print("<h1>{}</h1>".format(output))
# print("<h1>Result : {}</h1>".format(z))
print("</body></html>")
#!C:\Users\Arthi\AppData\Local\Programs\Python\Python310\python.exe
import cgi, cgitb
#import Mysqldb
cgitb.enable()
condition = [["Negative", "Not infected with TB"],
["1+", "Positive"],
["2+", "Positive"],
["3+", "Positive"],
["4+", "Positive"]]

f=cgi.FieldStorage()
a=f.getvalue('sputum_radiobox', "")
for i in condition:
    if a == i[0]:
        output = i[1]
        break
else:
    output = "NULL"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("    <title> RESPIRATORY ILLNESS </title>")
print("")
print("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'>")
print("<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.8.1/css/all.css'>")
print("<link rel='stylesheet' href='dot.css'>")
print("")
print("    <script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script>")
print("    <script src='https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js' integrity='sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin='anonymous'></script>")
print("    <script src='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script>")
print("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("</head>")
print("<body>")
print("    <div>  ")
print("        <nav class='navbar navbar-expand-sm navbar-light' style='background-color:#98FB98'>")
print("            <a class='navbar-brand' >")
print("                <img src='Screenshot 2022-02-24 190456.png' width='100' height='100' /> RESPIRATORY ILLNESS </a>")
print("        </nav>")
print("     ")
print("    </div>")
print("         <center><h3><b>TB DIAGNOSIS</b></h3></center>")
print("<h1>{}</h1>".format(a))
print("<h1>{}</h1>".format(output))
print("</body></html>")
