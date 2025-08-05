from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="../templates")

@app.route('/')
def serve_index():
    return render_template('Word_Pronouncer.html')

if __name__ == '__main__':
    app.run(debug=True)
    # Ensure the templates directory is correctly set
    