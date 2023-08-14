from fastapi import FastAPI

# Construção do servidor
app = FastAPI()

# Dados da visão geral da TOTVS
totvs_visao_geral = {
    "nome": "TOTVS",
    "fundacao": 1983,
    "sede": "São Paulo, Brasil",
    "setores_atuacao": ["Gestão", "Techfin", "Business Performance"],
    "receita_anual": "R$ 4,3 bilhões (2023)",
    "ceo": "Dennis Herszkowicz"
}

# Lista de setores de atuação da TOTVS
setores_atuacao = totvs_visao_geral["setores_atuacao"]

# Dados dos produtos da TOTVS
totvs_produtos = {
    "Gestão": {"id": "id_p01", "descricao": "Sistemas de Gestão Empresarial"},
    "Techfin": {"id": "id_p02", "descricao": "Soluções de crédito, pagamentos e serviços financeiros"},
    "Business Performance": {"id": "id_p03", "descricao": ["Marketing Digital", "Digital Commerce", "Soluções de Customer Experience (CX)"]}
}

# Transformando listas de descrição de produtos em tuplas para evitar modificações acidentais
for produto_info in totvs_produtos.values():
    if isinstance(produto_info["descricao"], list):
        produto_info["descricao"] = tuple(produto_info["descricao"])

# Dados sobre inovação na TOTVS
totvs_inovacao = {
    "inovacao": "Foco em inovação constante para oferecer soluções tecnológicas atualizadas.",
    "parcerias": ["Itaú", "IBM", "Salesforce", "AWS"],
    "laboratorios_inovacao": 2,
    "patentes_registradas": "Mais de 100 patentes registradas"
}

# Dados sobre prêmios recebidos pela TOTVS
totvs_premios = {
    "premios": [
        "Melhor Empresa de Software da América Latina (2020)",
        "Marca Mais Valiosa do Brasil em Software (2021)",
        "Top of Mind de RH (2022)"
    ],
    "reconhecimento": [
        "Reconhecida como uma das 100 empresas mais inovadoras do Brasil (2022)",
        "Inclusa no ranking Forbes das Empresas mais Inovadoras do Mundo (2019)"
    ]
}

# Dados sobre responsabilidade social da TOTVS
totvs_social = {
    "projetos_sociais": ["TOTVS Educação", "Programa de Voluntariado Corporativo"],
    "sustentabilidade": "Compromisso com práticas sustentáveis e responsabilidade ambiental.",
    "inclusao": "Programas de inclusão e diversidade, incluindo TOTVS Autism at Work."
}

# Rota principal da API
@app.get("/")
def home():
    return "Boas vindas à API TOTVS"

# Rotas para cada conjunto de dados
@app.get("/totvs_visao_geral")
def visaogeral():
     return totvs_visao_geral

@app.get("/totvs_produtos")
def produtos():
     return totvs_produtos

@app.get("/totvs_inovacao")
def inovacao():
     return totvs_inovacao

@app.get("/totvs_premios")
def premios():
     return totvs_premios

@app.get("/totvs_social")
def social():
     return totvs_social

# Rota para obter os setores de atuação
@app.get("/setores_atuacao")
def setores():
     return setores_atuacao

# Rota para obter informações de um produto específico por ID
@app.get("/{id_produto}")
def idp(id_produto: str):
    produto_info = None
    for _, info in totvs_produtos.items():
        if info["id"] == id_produto:
            produto_info = info
            break
    if produto_info is None:
        return "Produto não encontrado."
    
    return produto_info 