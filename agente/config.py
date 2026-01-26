from pathlib import Path

KNOWLEDGE_BASE_PATH = Path(__file__).parent.parent / "instructions" / "knowledge"

CATEGORIES = {
    "always": {
        "keywords": [],
        "files": [
            "atendimento/comportamento.md",
            "atendimento/escalonamento.md"
        ]
    },
    "empresa": {
        "keywords": [
            "biond", "empresa", "quem são", "sobre vocês", "história",
            "quem é", "o que é a biond", "sobre a empresa", "conhecer vocês",
            "fundação", "fundada", "criada", "tocantins", "missão", "visão"
        ],
        "files": [
            "empresa/sobre_biond.md",
        ]
    },
    "soja": {
        "keywords": [
            "soja", "soybean", "ferrugem", "ferrugem asiática", "oídio",
            "mancha alvo", "mancha-alvo", "glycine max", "grão", "grãos",
            "plantio soja", "lavoura de soja", "cultura da soja"
        ],
        "files": [
            "manejo/soja/manejo_soja.md",
            "manejo/soja/biofungicidas_soja.md",
        ]
    },
    "arroz": {
        "keywords": [
            "arroz", "rice", "arrozeiro", "arrozeira", "rizicultura",
            "oryza", "lavoura de arroz", "cultura do arroz", "plantio arroz"
        ],
        "files": [
            "manejo/arroz/manejo_biond_arroz.md",
        ]
    },
    "produtos": {
        "keywords": [
            "produto", "produtos", "solução", "soluções", "linha",
            "catálogo", "portfólio",
            "sollum", "protec",
            "amy", "az", "bm", "bs", "trc",
            "protec bp", "protec bsf",
            "bacillus", "trichoderma", "azospirillum",
            "bacillus subtilis", "bacillus pumilus", "bacillus megaterium",
            "bacillus amyloliquefaciens", "trichoderma harzianum",
            "azospirillum brasilense",
            "biofungicida", "biofungicidas", "promotor de crescimento",
            "fixação de nitrogênio", "solubilização de fósforo",
            "controle biológico", "biocontrole"
        ],
        "files": [
            "produtos/amy.md",
            "produtos/az.md",
            "produtos/bm.md",
            "produtos/bs.md",
            "produtos/trc.md",
            "produtos/protec_bp.md",
            "produtos/protec_bsf.md",
        ]
    },
}
