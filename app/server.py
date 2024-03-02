from flask import Flask, request
from processFile import process_upload_data

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    print(request.path)
    file_path = request.files.get('data')
    print(file_path)

    texto = file_path.readlines()
    for linha in texto:
     print(linha)  

    result = process_upload_data(file_path)   
    return result

if __name__ == "__main__":
    app.run(debug=True)

