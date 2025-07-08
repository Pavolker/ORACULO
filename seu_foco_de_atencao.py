#!/usr/bin/env python3
# SEU FOCO DE ATENÇÃO - Aplicativo de autoconhecimento

import random

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
        "Qual aspecto da sua saúde mais te preocupa atualmente?\n1. Saúde física\n2. Saúde mental\n3. Hábitos de saúde\n4. Ritmos do corpo\n5. Sensações físicas\n",
        "O que você gostaria de melhorar na sua saúde?\n1. Consciência corporal\n2. Rotinas saudáveis\n3. Equilíbrio emocional\n4. Autocuidado\n5. Prevenção\n"
    ],
    "relacionamento": [
        "Qual tipo de relacionamento mais te preocupa?\n1. Familiar\n2. Amoroso\n3. Profissional\n4. Amizades\n5. Com você mesmo\n",
        "O que você busca nos seus relacionamentos?\n1. Conexão emocional\n2. Respeito mútuo\n3. Comunicação eficaz\n4. Limites saudáveis\n5. Aprendizado\n"
    ],
    "emocao": [
        "Qual emoção tem sido mais presente ultimamente?\n1. Alegria\n2. Tristeza\n3. Raiva\n4. Medo\n5. Ansiedade\n",
        "Como você lida com essa emoção?\n1. Expressando\n2. Reprimindo\n3. Analisando\n4. Transformando\n5. Aceitando\n"
    ],
    "comportamento": [
        "Qual comportamento seu mais te preocupa?\n1. Hábitos diários\n2. Reações automáticas\n3. Padrões repetitivos\n4. Formas de comunicação\n5. Atitudes sociais\n",
        "O que esse comportamento revela sobre você?\n1. Necessidades não atendidas\n2. Crenças limitantes\n3. Histórico pessoal\n4. Valores internos\n5. Medos inconscientes\n"
    ],
    "valor": [
        "Qual valor pessoal está em questão?\n1. Honestidade\n2. Respeito\n3. Liberdade\n4. Justiça\n5. Amor\n",
        "Como esse valor se manifesta na sua vida?\n1. Nas suas escolhas\n2. Nos seus relacionamentos\n3. No trabalho\n4. No autocuidado\n5. Na sociedade\n"
    ]
}

def main():
    print("\nSEU FOCO DE ATENÇÃO\n")
    print("Vamos identificar qual objeto de autoconhecimento pode te ajudar agora.\n")
    
    # Pergunta inicial para determinar o contexto
    print("Qual é a principal área da sua vida que está te preocupando neste momento?")
    print("1. Saúde")
    print("2. Relacionamentos")
    print("3. Emoções")
    print("4. Comportamento")
    print("5. Valores pessoais")
    
    while True:
        try:
            contexto = int(input("Sua escolha (1-5): "))
            if 1 <= contexto <= 5:
                break
            print("Por favor, escolha um número entre 1 e 5.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    # Mapeia escolha inicial para contexto
    contextos = ["saude", "relacionamento", "emocao", "comportamento", "valor"]
    contexto_selecionado = contextos[contexto-1]
    
    # Perguntas específicas do contexto
    respostas = []
    for i, pergunta in enumerate(PERGUNTAS[contexto_selecionado], 1):
        while True:
            try:
                resposta = int(input(f"\nPergunta {i}: {pergunta}\nSua escolha (1-5): "))
                if 1 <= resposta <= 5:
                    respostas.append(resposta)
                    break
                print("Por favor, escolha um número entre 1 e 5.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    # Lógica para mapear respostas para objetos
    chave = contexto_selecionado
    
    # Mapeamento específico para cada contexto
    if contexto_selecionado == "saude":
        if respostas[0] == 1:
            chave = "como-esta-sua-saude"
        elif respostas[0] == 2:
            chave = "como-voce-lida-com-emocoes"
        elif respostas[0] == 3:
            chave = "habitos-do-dia-a-dia"
        elif respostas[0] == 4:
            chave = "ritmos-do-seu-corpo"
        else:
            chave = "sensacoes-do-corpo"
            
        if respostas[1] == 1:
            chave = "capacidade-de-se-observar"
        elif respostas[1] == 2:
            chave = "habitos-do-dia-a-dia"
        elif respostas[1] == 3:
            chave = "como-voce-lida-com-emocoes"
        elif respostas[1] == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "valores-que-te-guiam"
    
    elif contexto_selecionado == "emocao":
        if respostas[0] == 1:
            chave = "emocoes-que-voce-expressa"
        elif respostas[0] == 2:
            chave = "como-voce-lida-com-emocoes"
        elif respostas[0] == 3:
            chave = "reacoes-que-se-repetem"
        elif respostas[0] == 4:
            chave = "modelos-de-afeto-que-voce-repete"
        else:
            chave = "como-voce-pensa-sobre-pensar"
            
        if respostas[1] == 1:
            chave = "emocoes-que-voce-expressa"
        elif respostas[1] == 2:
            chave = "dependencias-que-te-prendem"
        elif respostas[1] == 3:
            chave = "como-voce-pensa-sobre-pensar"
        elif respostas[1] == 4:
            chave = "praticas-que-te-aproximam-de-si"
        else:
            chave = "capacidade-de-se-observar"
    
    objeto = MAPEAMENTO.get(chave, random.choice(list(MAPEAMENTO.values())))
    
    print(f"\nBaseado nas suas respostas, recomendamos que você explore:\n\n{objeto.replace('.md', '').replace('-', ' ').title()}\n")
    print("Este objeto de autoconhecimento pode te ajudar a refletir sobre sua preocupação atual.\n")

if __name__ == "__main__":
    main()