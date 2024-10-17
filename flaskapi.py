from flask import Flask,request
from main import Main
app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_query():
    # Country is present in the request or not
    country = request.json.get('country')
    if not country:
        raise ValueError("Invalid country present in request")


    program=Main()
    response=program.run(country)
    # Check if response contains or not
    if not response:
        raise ValueError("No response generated")

    # Return the response as a JSON object
    return {'response': response}


if __name__ == '__main__':
    app.run(debug=True)