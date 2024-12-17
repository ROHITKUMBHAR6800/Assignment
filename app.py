from flask import Flask, request, render_template

app = Flask(
    __name__,
    template_folder='public/templates',
    static_folder='public/static'
)

# here request come from home page and this is route to conditional render requested form page 
@app.route('/get-form', methods=['POST'])
def get_form():

    # we need to get requested form page 'form_type' from POST request
    data = request.form
    form_type = data.get('form_type')

    # here we are going to conditionally render the requested form html template
    if form_type == "form1":
        return render_template('form1.html')
    elif form_type == "form2":
        return render_template('form2.html')
    else:
        return "<h1>Invalid form type</h1>", 400


# this is the default route to render homepage html template
@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html');


# this will use when we submit the form and it is route to process form submissions
@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.form
    return f"<h1>Form Submitted Successfully</h1>"
    # if we want to show the submitted data on the screen
    # return f"<h1>Form Submitted Successfully</h1><p>{data}</p>"


if __name__ == '__main__':
    app.run(debug=False)
