#!/usr/bin/env python3
# SEU FOCO DE ATENÇÃO - Versão Web

import os
from flask import Flask, render_template_string, request, Response, send_from_directory, jsonify
import random
import markdown
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configurações para permitir iframe
def add_headers(response):
    response.headers['X-Frame-Options'] = 'ALLOW-FROM https://sites.google.com/'
    response.headers['Content-Security-Policy'] = "frame-ancestors 'self' https://sites.google.com"
    return response

app.after_request(add_headers)

# Mapeamento de perguntas para objetos de autoconhecimento
MAPEAMENTO = {
    "saude": "como-esta-sua-saude.md",
    "decisao": "como-voce-decide.md",
    "conflito": "como-voce-entra-em-conflito.md",
    "emocao": "como-voce-lida-com-emocoes.md",
    "pensamento": "como-voce-pensa-sobre-pensar.md",
    "apego": "como-voce-se-apega.md",
    "dependencia": "dependencias-que-te-prendem.md",
    "expressao": "emocoes-que-voce-expressa.md",
    "relacionamento": "habilidades-com-pessoas.md",
    "habito": "habitos-do-dia-a-dia.md",
    "historia": "historias-que-te-formaram.md",
    "linguagem": "idiomas-que-voce-fala.md",
    "comportamento": "jeito-de-se-comportar.md",
    "comunicacao": "jeito-de-se-comunicar.md",
    "apoio": "lacos-que-te-sustentam.md",
    "limite": "limites-que-voce-reconhece.md",
    "identidade": "marcos-da-sua-identidade.md",
    "afeto": "modelos-de-afeto-que-voce-repete.md",
    "feedback": "o-que-os-outros-te-dizem.md",
    "pratica": "praticas-que-te-aproximam-de-si.md",
    "cultura": "raizes-culturais.md",
    "reacao": "reacoes-que-se-repetem.md",
    "ritmo": "ritmos-do-seu-corpo.md",
    "ritual": "rituais-que-voce-vive.md",
    "sensacao": "sensacoes-do-corpo.md",
    "valor": "valores-que-te-guiam.md",
    "observacao": "capacidade-de-se-observar.md"
}

PERGUNTAS = {
    "saude": [
        "Qual aspecto da sua saúde mais te preocupa atualmente?",
        "O que você gostaria de melhorar na sua saúde?"
    ],
    "relacionamento": [
        "Qual tipo de relacionamento mais te preocupa?",
        "O que você busca nos seus relacionamentos?"
    ],
    "emocao": [
        "Qual emoção tem sido mais presente ultimamente?",
        "Como você lida com essa emoção?"
    ],
    "comportamento": [
        "Qual comportamento seu mais te preocupa?",
        "O que esse comportamento revela sobre você?"
    ],
    "valor": [
        "Qual valor pessoal está em questão?",
        "Como esse valor se manifesta na sua vida?"
    ]
}

OPCOES = {
    "saude": [
        ["Saúde física", "Saúde mental", "Hábitos de saúde", "Ritmos do corpo", "Sensações físicas"],
        ["Consciência corporal", "Rotinas saudáveis", "Equilíbrio emocional", "Autocuidado", "Prevenção"]
    ],
    "relacionamento": [
        ["Familiar", "Amoroso", "Profissional", "Amizades", "Com você mesmo"],
        ["Conexão emocional", "Respeito mútuo", "Comunicação eficaz", "Limites saudáveis", "Aprendizado"]
    ],
    "emocao": [
        ["Alegria", "Tristeza", "Raiva", "Medo", "Ansiedade"],
        ["Expressando", "Reprimindo", "Analisando", "Transformando", "Aceitando"]
    ],
    "comportamento": [
        ["Hábitos diários", "Reações automáticas", "Padrões repetitivos", "Formas de comunicação", "Atitudes sociais"],
        ["Necessidades não atendidas", "Crenças limitantes", "Histórico pessoal", "Valores internos", "Medos inconscientes"]
    ],
    "valor": [
        ["Honestidade", "Respeito", "Liberdade", "Justiça", "Amor"],
        ["Nas suas escolhas", "Nos seus relacionamentos", "No trabalho", "No autocuidado", "Na sociedade"]
    ]
}

@app.route('/iframe', methods=['GET', 'POST'])
def iframe():
    if request.method == 'GET':
        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>SEU FOCO DE ATENÇÃO</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
                    .question { background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
                    button { background: #3498db; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; }
                    button:hover { background: #2980b9; }
                </style>
            </head>
            <body style="margin:0;padding:0">
                <form method="POST">
                    <div class="question">
                        <h3>Qual é a principal área da sua vida que está te preocupando neste momento?</h3>
                        <label><input type="radio" name="contexto" value="saude" required> Saúde</label><br>
                        <label><input type="radio" name="contexto" value="relacionamento"> Relacionamentos</label><br>
                        <label><input type="radio" name="contexto" value="emocao"> Emoções</label><br>
                        <label><input type="radio" name="contexto" value="comportamento"> Comportamento</label><br>
                        <label><input type="radio" name="contexto" value="valor"> Valores pessoais</label>
                    </div>
                    <button type="submit">Continuar</button>
                </form>
            </body>
            </html>
        ''')
    
    contexto = request.form['contexto']
    return render_template_string(f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>SEU FOCO DE ATENÇÃO</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; }}
                .question {{ background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; }}
                button {{ background: #3498db; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; }}
                button:hover {{ background: #2980b9; }}
            </style>
        </head>
        <body style="margin:0;padding:0">
            <form method="POST" action="/iframe_resultado">
                <input type="hidden" name="contexto" value="{contexto}">
                <div class="question">
                    <h3>{PERGUNTAS[contexto][0]}</h3>
                    {'<br>'.join([f'<label><input type="radio" name="resposta1" value="{i}" required> {opcao}</label>' for i, opcao in enumerate(OPCOES[contexto][0], 1)])}
                </div>
                <div class="question">
                    <h3>{PERGUNTAS[contexto][1]}</h3>
                    {'<br>'.join([f'<label><input type="radio" name="resposta2" value="{i}" required> {opcao}</label>' for i, opcao in enumerate(OPCOES[contexto][1], 1)])}
                </div>
                <button type="submit">Obter Recomendação</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/iframe_resultado', methods=['POST'])
def iframe_resultado():
    contexto = request.form['contexto']
    resposta1 = int(request.form['resposta1'])
    resposta2 = int(request.form['resposta2'])
    
    # Lógica para mapear respostas para objetos
    chave = contexto
    
    if contexto == "saude":
        if resposta1 == 1:
            chave = "como-esta-sua-saude"
        elif resposta1 == 2:
            chave = "como-voce-lida-com-emocoes"
        elif resposta1 == 3:
            chave = "habitos-do-dia-a-dia"
        elif resposta1 == 4:
            chave = "ritmos-do-seu-corpo"
        else:
            chave = "sensacoes-do-corpo"
            
        if resposta2 == 1:
            chave = "capacidade-de-se-observar"
        elif resposta2 == 2:
            chave = "habitos-do-dia-a-dia"
        elif resposta2 == 3:
            chave = "como-voce-lida-com-emocoes"
        elif resposta2 == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "valores-que-te-guiam"
    
    elif contexto == "emocao":
        if resposta1 == 1:
            chave = "emocoes-que-voce-expressa"
        elif resposta1 == 2:
            chave = "como-voce-lida-com-emocoes"
        elif resposta1 == 3:
            chave = "reacoes-que-se-repetem"
        elif resposta1 == 4:
            chave = "modelos-de-afeto-que-voce-repete"
        else:
            chave = "como-voce-pensa-sobre-pensar"
            
        if resposta2 == 1:
            chave = "emocoes-que-voce-expressa"
        elif resposta2 == 2:
            chave = "dependencias-que-te-prendem"
        elif resposta2 == 3:
            chave = "como-voce-pensa-sobre-pensar"
        elif resposta2 == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "capacidade-de-se-observar"
    
    objeto = MAPEAMENTO.get(chave, random.choice(list(MAPEAMENTO.values())))
    objeto_formatado = objeto.replace('.md', '').replace('-', ' ').title()
    
    objeto_html = ler_objeto_md(objeto)
    return render_template_string(f'''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SEU FOCO DE ATENÇÃO - Resultado</title>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body {{ font-family: 'Montserrat', Arial, sans-serif; background: #f4f8fb; margin: 0; padding: 0; }}
                .container {{ max-width: 700px; margin: 40px auto; background: #fff; border-radius: 12px; box-shadow: 0 4px 24px #0001; padding: 32px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                .objeto {{ font-size: 1.5em; color: #2980b9; margin: 10px 0; font-weight: bold; }}
                .result {{ background: #e8f4f8; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center; }}
                .md-content {{ text-align: left; margin-top: 32px; }}
                button, .btn {{ background: #3498db; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-size: 1em; margin-top: 24px; }}
                button:hover, .btn:hover {{ background: #217dbb; }}
                a {{ color: #3498db; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
                @media (max-width: 800px) {{ .container {{ margin: 8px; padding: 12px; }} }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>SEU FOCO DE ATENÇÃO</h1>
                <div class="result">
                    <p>Baseado nas suas respostas, recomendamos que você explore:</p>
                    <div class="objeto">{objeto_formatado}</div>
                    <p>Este objeto de autoconhecimento pode te ajudar a refletir sobre sua preocupação atual.</p>
                </div>
                <div class="md-content">{objeto_html}</div>
                <a class="btn" href="/">Voltar ao início</a>
            </div>
        </body>
        </html>
    ''')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>SEU FOCO DE ATENÇÃO</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
                    h1 { color: #2c3e50; text-align: center; }
                    .question { background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
                    button { background: #3498db; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; }
                    button:hover { background: #2980b9; }
                </style>
            </head>
            <body>
                <h1>SEU FOCO DE ATENÇÃO</h1>
                <p>Vamos identificar qual objeto de autoconhecimento pode te ajudar agora.</p>
                <form method="POST">
                    <div class="question">
                        <h3>Qual é a principal área da sua vida que está te preocupando neste momento?</h3>
                        <label><input type="radio" name="contexto" value="saude" required> Saúde</label><br>
                        <label><input type="radio" name="contexto" value="relacionamento"> Relacionamentos</label><br>
                        <label><input type="radio" name="contexto" value="emocao"> Emoções</label><br>
                        <label><input type="radio" name="contexto" value="comportamento"> Comportamento</label><br>
                        <label><input type="radio" name="contexto" value="valor"> Valores pessoais</label>
                    </div>
                    <button type="submit">Continuar</button>
                </form>
            </body>
            </html>
        ''')
    
    contexto = request.form['contexto']
    return render_template_string(f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>SEU FOCO DE ATENÇÃO</title>
            <style>
                body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }}
                h1 {{ color: #2c3e50; text-align: center; }}
                .question {{ background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; }}
                button {{ background: #3498db; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; }}
                button:hover {{ background: #2980b9; }}
            </style>
        </head>
        <body>
            <h1>SEU FOCO DE ATENÇÃO</h1>
            <form method="POST" action="/resultado">
                <input type="hidden" name="contexto" value="{contexto}">
                <div class="question">
                    <h3>{PERGUNTAS[contexto][0]}</h3>
                    {'<br>'.join([f'<label><input type="radio" name="resposta1" value="{i}" required> {opcao}</label>' for i, opcao in enumerate(OPCOES[contexto][0], 1)])}
                </div>
                <div class="question">
                    <h3>{PERGUNTAS[contexto][1]}</h3>
                    {'<br>'.join([f'<label><input type="radio" name="resposta2" value="{i}" required> {opcao}</label>' for i, opcao in enumerate(OPCOES[contexto][1], 1)])}
                </div>
                <button type="submit">Obter Recomendação</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/resultado', methods=['POST'])
def resultado():
    contexto = request.form['contexto']
    resposta1 = int(request.form['resposta1'])
    resposta2 = int(request.form['resposta2'])
    
    # Lógica para mapear respostas para objetos
    chave = contexto
    
    if contexto == "saude":
        if resposta1 == 1:
            chave = "como-esta-sua-saude"
        elif resposta1 == 2:
            chave = "como-voce-lida-com-emocoes"
        elif resposta1 == 3:
            chave = "habitos-do-dia-a-dia"
        elif resposta1 == 4:
            chave = "ritmos-do-seu-corpo"
        else:
            chave = "sensacoes-do-corpo"
            
        if resposta2 == 1:
            chave = "capacidade-de-se-observar"
        elif resposta2 == 2:
            chave = "habitos-do-dia-a-dia"
        elif resposta2 == 3:
            chave = "como-voce-lida-com-emocoes"
        elif resposta2 == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "valores-que-te-guiam"
    
    elif contexto == "emocao":
        if resposta1 == 1:
            chave = "emocoes-que-voce-expressa"
        elif resposta1 == 2:
            chave = "como-voce-lida-com-emocoes"
        elif resposta1 == 3:
            chave = "reacoes-que-se-repetem"
        elif resposta1 == 4:
            chave = "modelos-de-afeto-que-voce-repete"
        else:
            chave = "como-voce-pensa-sobre-pensar"
            
        if resposta2 == 1:
            chave = "emocoes-que-voce-expressa"
        elif resposta2 == 2:
            chave = "dependencias-que-te-prendem"
        elif resposta2 == 3:
            chave = "como-voce-pensa-sobre-pensar"
        elif resposta2 == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "capacidade-de-se-observar"
    
    objeto = MAPEAMENTO.get(chave, random.choice(list(MAPEAMENTO.values())))
    objeto_formatado = objeto.replace('.md', '').replace('-', ' ').title()
    
    objeto_html = ler_objeto_md(objeto)
    return render_template_string(f'''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SEU FOCO DE ATENÇÃO - Resultado</title>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body {{ font-family: 'Montserrat', Arial, sans-serif; background: #f4f8fb; margin: 0; padding: 0; }}
                .container {{ max-width: 700px; margin: 40px auto; background: #fff; border-radius: 12px; box-shadow: 0 4px 24px #0001; padding: 32px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                .objeto {{ font-size: 1.5em; color: #2980b9; margin: 10px 0; font-weight: bold; }}
                .result {{ background: #e8f4f8; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center; }}
                .md-content {{ text-align: left; margin-top: 32px; }}
                button, .btn {{ background: #3498db; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-size: 1em; margin-top: 24px; }}
                button:hover, .btn:hover {{ background: #217dbb; }}
                a {{ color: #3498db; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
                @media (max-width: 800px) {{ .container {{ margin: 8px; padding: 12px; }} }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>SEU FOCO DE ATENÇÃO</h1>
                <div class="result">
                    <p>Baseado nas suas respostas, recomendamos que você explore:</p>
                    <div class="objeto">{objeto_formatado}</div>
                    <p>Este objeto de autoconhecimento pode te ajudar a refletir sobre sua preocupação atual.</p>
                </div>
                <div class="md-content">{objeto_html}</div>
                <a class="btn" href="/">Voltar ao início</a>
            </div>
        </body>
        </html>
    ''')

@app.route('/api/perguntas', methods=['GET'])
def api_perguntas():
    return jsonify({"perguntas": PERGUNTAS, "opcoes": OPCOES})

@app.route('/api/resultado', methods=['POST'])
def api_resultado():
    data = request.get_json()
    contexto = data.get('contexto')
    resposta1 = int(data.get('resposta1'))
    resposta2 = int(data.get('resposta2'))
    chave = contexto
    if contexto == "saude":
        if resposta1 == 1:
            chave = "como-esta-sua-saude"
        elif resposta1 == 2:
            chave = "como-voce-lida-com-emocoes"
        elif resposta1 == 3:
            chave = "habitos-do-dia-a-dia"
        elif resposta1 == 4:
            chave = "ritmos-do-seu-corpo"
        else:
            chave = "sensacoes-do-corpo"
        if resposta2 == 1:
            chave = "capacidade-de-se-observar"
        elif resposta2 == 2:
            chave = "habitos-do-dia-a-dia"
        elif resposta2 == 3:
            chave = "como-voce-lida-com-emocoes"
        elif resposta2 == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "valores-que-te-guiam"
    elif contexto == "emocao":
        if resposta1 == 1:
            chave = "emocoes-que-voce-expressa"
        elif resposta1 == 2:
            chave = "como-voce-lida-com-emocoes"
        elif resposta1 == 3:
            chave = "reacoes-que-se-repetem"
        elif resposta1 == 4:
            chave = "modelos-de-afeto-que-voce-repete"
        else:
            chave = "como-voce-pensa-sobre-pensar"
        if resposta2 == 1:
            chave = "emocoes-que-voce-expressa"
        elif resposta2 == 2:
            chave = "dependencias-que-te-prendem"
        elif resposta2 == 3:
            chave = "como-voce-pensa-sobre-pensar"
        elif resposta2 == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "capacidade-de-se-observar"
    objeto = MAPEAMENTO.get(chave, random.choice(list(MAPEAMENTO.values())))
    objeto_formatado = objeto.replace('.md', '').replace('-', ' ').title()
    objeto_html = ler_objeto_md(objeto)
    return jsonify({
        "objeto": objeto_formatado,
        "conteudo_html": objeto_html
    })

@app.route('/objetos/<path:filename>')
def serve_objeto(filename):
    return send_from_directory('objetos', filename)

def ler_objeto_md(objeto):
    caminho = os.path.join('objetos', objeto)
    if os.path.exists(caminho):
        with open(caminho, encoding='utf-8') as f:
            return markdown.markdown(f.read())
    return '<p>Conteúdo não encontrado.</p>'

if __name__ == '__main__':
    print("Para executar o aplicativo, use Gunicorn. Consulte o README.md para mais detalhes.")