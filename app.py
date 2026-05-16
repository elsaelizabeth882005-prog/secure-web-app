from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Student Capstone Project</title>
    </head>
    <body style="text-align:center; margin-top:100px; font-family:Arial;">
        <h1>Student Capstone Project</h1>
        <h2>Secure Web Application Deployment</h2>
        <p>Developed by Elsa Elizabeth Issac</p>
        <p>Hosted on AWS using Docker and Nginx</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)