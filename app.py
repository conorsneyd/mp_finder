from flask import Flask, render_template, request
from postcode_lookup import postcode_lookup

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])

def index():
    if request.method == "POST":
        #get postcode from form and use to query database
        postcode_raw = request.form["postcode"]
        postcode = postcode_raw.lower().replace(" ", "")
        mp_info = postcode_lookup(postcode)

        if mp_info:
            #extract variables from query result
            constituency = mp_info[0][0]
            mp_name = mp_info[0][1]
            mp_party = mp_info[0][2]
            mp_phone = mp_info[0][3]
            mp_email = mp_info[0][4]
            return render_template("results.html", constituency = constituency, mp_name = mp_name, mp_party = mp_party, mp_phone = mp_phone, mp_email = mp_email)
        else:
            #if no postcode match found, prompt user to enter new postcode
            return render_template("index.html", error = "Please enter a valid London postcode.") 
    
    else:
        return render_template("index.html") 

if __name__ == '__main__':
    app.run()