# server.py
from flask import Flask, request
from processFile import process_upload_data

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        
        if 'data' not in request.files:
            return 'Nenhum arquivo enviado', 400

        file = request.files['data']
        
        if file.filename == '':
            return 'Nome do arquivo vazio', 400

        file_lines = [line.decode('utf-8') for line in file]

        result = process_upload_data(file_lines)
        return result , 200

    except Exception as e:
        print(f"Erro ao processar o arquivo enviado: {e}")
        return "Ocorreu um erro ao processar o arquivo enviado", 500

if __name__ == "__main__":
    app.run(debug=True)
