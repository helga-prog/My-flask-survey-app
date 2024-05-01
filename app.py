from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def survey():
    # HTML code remains the same as in your last update.
    return render_template_string(HTML)

@app.route('/submit', methods=['POST'])
def submit():
    response_data = request.form
    response_html = "<h1>Thank you for your participation!</h1>"
    response_html += "<h2>Submitted Data:</h2><ul>"
    
    # This will loop through each form input and display its value(s)
    for key in response_data.keys():
        # If the form input has multiple values (like checkboxes), join them with a comma
        values = request.form.getlist(key)
        formatted_values = ", ".join(values) if values else "None"
        
        # Include 'Other' text input specifically for factors if it exists
        if key == 'factors_other' and response_data['factors_other'].strip():
            response_html += f"<li><strong>Other factors:</strong> {response_data['factors_other']}</li>"
        else:
            response_html += f"<li><strong>{key.replace('_', ' ').capitalize()}:</strong> {formatted_values}</li>"
    
    response_html += "</ul>"
    response_html += '<a href
