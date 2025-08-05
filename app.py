from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_file('Word_Pronouncer.html')

if __name__ == '__main__':
    app.run(debug=True)
