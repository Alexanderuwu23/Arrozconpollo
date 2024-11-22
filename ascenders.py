from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def get_version():
    try:
        with open("version.txt", "r") as file:
            version = file.read().strip()
        return jsonify({"version": version})
    except FileNotFoundError:
        return jsonify({"error": "El archivo version.txt no se encuentra"}), 404

@app.route('/download', methods=['GET'])
def download_file():
    try:
        return send_file("ascenders.zip", as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "El archivo ascenders.zip no se encuentra"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
