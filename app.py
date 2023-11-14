from flask import Flask, render_template

app = Flask(__name__)

# Your individual route handlers are removed

# This route will handle the dropdown menu rendering based on a parameter
@app.route('/<selected_item>')
def dropdown(selected_item):
    return render_template(f'{selected_item}.html')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
