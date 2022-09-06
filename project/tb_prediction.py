#!C:\Program Files\Python310\python.exe
import cgi, cgitb
form=cgi.FieldStorage()
n=form.getvalue('symptoms_fileupload')
cgitb.enable()
import sys
sys.path.append("c:/users/arthi/appdata/roaming/python/python310/site-packages")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# For Prediction
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
preds = cnn.predict(pp_img, verbose=0)

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
print("    </div>")
print("         <center><h3><b>TB PREDICTION</b></h3></center>")
print("<br>")

print("    <div>  ")
print("<img src='{}' width='300' height='300'>".format(file))
print("<h1>Result is {}</h1>".format(out))
print("</div>")
print("</body></html>") 