## REMEMBER ME ##
-username in base html
-


## NAVBAR ##
aria-controls="navbarToggleContent"
Accessibility: tells screen readers what element this button controls.

aria-expanded="false"
Accessibility: tells whether the controlled element is expanded or collapsed (Bootstrap updates this automatically).

aria-label="Toggle navigation"
Accessibility: provides a text label for screen readers (“Toggle navigation”).

## URL FOR ##
In Flask, url_for() looks for the function name of your route, not the HTML filename.

So, if you have this route in your Flask app:
@app.route("/")
def index():
    return render_template("home.html")

Then the endpoint name is index, not home.

So this line in your HTML:
<a href="{{ url_for('home') }}" class="navbar-brand">Bellerin</a>

will fail — because Flask doesn’t have a route function named home.

## Step 4: Make Adjustability Minimal but Smart

Let users change only one of three things per anime:

“Finish by” date

“Episodes per day”

“Episodes watched so far”

And whenever they change one, you automatically recalculate the others.
That’s it — simple, reactive math. ##