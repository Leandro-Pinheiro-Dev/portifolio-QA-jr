from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

db_config = {
    'host': '127.0.0.1',
    'user': 'developer',
    'password': '@Pinheiro10',
    'database': 'banco_tintas',
    'port': 3306
}

CORES_VALIDAS = ['azul', 'azul bebe', 'cinza claro', 'cinza mais claro', 'preto', 'vinho']
ACABAMENTOS_VALIDOS = ['fosco', 'brilhante', 'satinado']
CONDICOES_VALIDAS = ['novo', 'usado']

MAPA_CONDICAO = {
    'novo': 'novo',
    'nova': 'novo',
    'usado': 'usado',
    'usada': 'usado'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API Banco de Tintas rodando"}), 200

@app.route('/cadastrar_tinta', methods=['POST', 'OPTIONS'])
@cross_origin()
def cadastrar_tinta():
    if not request.is_json:
        return jsonify({"error": "Content-Type deve ser application/json"}), 415

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON inválido ou vazio"}), 400

    campos = ['nome','tipo','cor','acabamento','quantidade','validade','condicao']
    for campo in campos:
        if campo not in data or data[campo] in ['', None]:
            return jsonify({"error": f"Campo obrigatório ausente: {campo}"}), 400

    nome = data['nome'].strip()
    tipo = data['tipo'].strip()
    cor = data['cor'].strip().lower()
    acabamento = data['acabamento'].strip().lower()
    condicao_raw = data['condicao'].strip().lower()
    validade = data['validade']

    # 🔹 Mapear condição para ENUM
    condicao = MAPA_CONDICAO.get(condicao_raw)
    if not condicao:
        return jsonify({"error": f"Condição inválida: {condicao_raw}. Use 'novo' ou 'usado'"}), 400

    if cor not in CORES_VALIDAS:
        return jsonify({"error": "Cor inválida"}), 400
    if acabamento not in ACABAMENTOS_VALIDOS:
        return jsonify({"error": "Acabamento inválido"}), 400

    try:
        quantidade = int(data['quantidade'])
        if quantidade <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Quantidade deve ser um número inteiro maior que zero"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 🔹 DEBUG: imprime os valores antes do insert
        print("Valores a inserir:", nome, tipo, cor, acabamento, quantidade, validade, condicao)

        cursor.execute("""
            INSERT INTO tinta (nome, tipo, cor, acabamento, quantidade, validade, condicao)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nome, tipo, cor, acabamento, quantidade, validade, condicao))

        conn.commit()
        return jsonify({"message": "Tinta cadastrada com sucesso!"}), 201

    except mysql.connector.Error as err:
        print("Erro MySQL:", err)
        return jsonify({"error": str(err)}), 500

    finally:
        if cursor: cursor.close()
        if conn: conn.close()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
