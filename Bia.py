# This code imports the Flask library and some functions from it.
from flask import Flask,render_template

# Create a Flask application instance
app = Flask(__name__)



# Global variable for site name: Used in templates to display the site name
siteName = "BIA Opportunities" 
# Set the site name in the app context
@app.context_processor
def inject_site_name():
    return dict(siteName=siteName)

# Home Page
@app.route('/')
def index():
    # This defines a variable 'studentName' that will be passed to the output HTML
    sitename = "BIA Opportunities"
    # Render HTML with the name in a H1 tag
    return render_template('index.html', greeting="Welcome", sitename=sitename)

# About Page
# About Page
@app.route('/about')
def about():
    # Render HTML with the name in a H1 tag
    return render_template('about.html', title="About")


# Run application
#=========================================================
# This code executes when the script is run directly.
if __name__ == '__main__':
    print("Starting Flask application...")
    print("Open Your Application in Your Browser: http://localhost:81")
    # The app will run on port 81, accessible from any local IP address
    app.run(host='0.0.0.0', port=81, debug=True)
