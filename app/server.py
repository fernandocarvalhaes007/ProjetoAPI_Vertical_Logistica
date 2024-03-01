from flask import Flask
from processFile import process_upload_data
import os 

app = Flask(__name__)

@app.route("/upload_data1", methods=['POST'])
def upload_data_1():
    file_path = os.path.join("data/data_1.txt")
    result = process_upload_data(file_path)   
    return result


@app.route("/upload_data2", methods=['POST'])
def upload_data_2():
    file_path = os.path.join("data/data_2.txt")
    result = process_upload_data(file_path)   
    return result
  

if __name__ == "__main__":
    app.run(debug=True)

