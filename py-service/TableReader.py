# file_path kosong karena fitur atur akses dan Login/Register belum ada
# Upload pola kuman menunggu fitur atur akses dan Login/Register 

from flask import Flask, jsonify, request
import pandas

app = Flask(__name__)

def load_excel_data(file_path):
    return pandas.read_excel(file_path)

@app.route('/api/data', methods=['GET'])
def get_data():
    file_path = ''
    
    try:
        df = load_excel_data(file_path)
        
        data = df.to_dict(orient='records')
        
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500