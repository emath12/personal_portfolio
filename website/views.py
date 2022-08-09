from flask import Blueprint, render_template, redirect, url_for
views = Blueprint('views', __name__)

@views.route('/') # whenever we go to / url, whatever is inside home function will run
def home():
    return render_template('home.html')


    
    # render_template("home.html")


# redirect(url_for("index")+"#myFormId")





# @auth.route('/login', methods=['GET', 'POST']) # prefix + whatever this is
# def login():
#     return render_template("login.html", boolean=True)

# @auth.route('/sign-up', methods=['GET', 'POST'])
# def signup():
#     return render_template("sign_up.html")  