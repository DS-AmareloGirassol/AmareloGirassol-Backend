from subjects.models import Subject

software_subjects = [
	{
	    "name": "Cálculo 1",
	    "code": "MAT0025",
	    "carga": "90",
	    "semestre": "1"
	},
	{
	    "name": "Algoritmos e Programação de Computadores",
	    "code": "CIC0004",
	    "carga": "90",
	    "semestre": "1"
	},
	{
	    "name": "Desenho Industrial Assistido por Computador",
	    "code": "FGA0168",
	    "carga": "90",
	    "semestre": "1"
	},
	{
	    "name": "Engenharia e Ambiente",
	    "code": "FGA0161",
	    "carga": "60",
	    "semestre": "1"
	},
	{
	    "name": "Introdução à Engenharia",
	    "code": "FGA0163",
	    "carga": "30",
	    "semestre": "1"
	},
	{
	    "name": "Cálculo 2",
	    "code": "MAT0026",
	    "carga": "90",
	    "semestre": "2"
	},
	{
	    "name": "Física",
	    "code": "IFD0171",
	    "carga": "60",
	    "semestre": "2"
	},
	{
	    "name": "Física Experimental",
	    "code": "IFD0173",
	    "carga": "30",
	    "semestre": "2"
	},
	{
	    "name": "Introdução à Àlgebra Linear",
	    "code": "MAT0031",
	    "carga": "60",
	    "semestre": "2"
	},
	{
	    "name": "Probabilidade e Estátistica Aplicado à Engenharia",
	    "code": "FGA0157",
	    "carga": "60",
	    "semestre": "2"
	},
	{
	    "name": "Desenvolvimento de Software",
	    "code": "FGA0084",
	    "carga": "60",
	    "semestre": "2"
	},
	{
	    "name": "Métodos Numéricos para Engenharia",
	    "code": "FGA0160",
	    "carga": "60",
	    "semestre": "3"
	},
	{
	    "name": "Engenharia Econômica",
	    "code": "FGA0133",
	    "carga": "60",
	    "semestre": "3"
	},
	{
	    "name": "Humanidades e Cidadania",
	    "code": "FGA0164",
	    "carga": "60",
	    "semestre": "3"
	},
	{
	    "name": "Teoria de Eletrônica Digital 1",
	    "code": "FGA0073",
	    "carga": "60",
	    "semestre": "3"
	},
	{
	    "name": "Prática de Eletrônica Digital 1",
	    "code": "FGA0071",
	    "carga": "30",
	    "semestre": "4"
	},
	{
	    "name": "Orientação a Objetos",
	    "code": "FGA0158",
	    "carga": "60",
	    "semestre": "3"
	},
	{
	    "name": "Matemática Discreta 1",
	    "code": "FGA0085",
	    "carga": "60",
	    "semestre": "3"
	},
	{
	    "name": "Gestão de Produção e Qualidade",
	    "code": "FGA0184",
	    "carga": "60",
	    "semestre": "4"
	},
	{
	    "name": "Métodos de Desenvolvimento de Software",
	    "code": "FGA0138",
	    "carga": "60",
	    "semestre": "4"
	},
	{
	    "name": "Estruturas de Dados 1",
	    "code": "FGA0147",
	    "carga": "60",
	    "semestre": "4"
	},
	{
	    "name": "Fundamentos de Arquiteturas de Computadores",
	    "code": "FGA0142",
	    "carga": "60",
	    "semestre": "4"
	},
	{
	    "name": "Matemática Discreta 2",
	    "code": "FGA0108",
	    "carga": "60",
	    "semestre": "4"
	},
	{
	    "name": "Projeto Integrador de Engenharia 1",
	    "code": "FGA0150",
	    "carga": "60",
	    "semestre": "4"
	},
	{
	    "name": "Interação Humano Computador",
	    "code": "FGA0173",
	    "carga": "60",
	    "semestre": "5"
	},
	{
	    "name": "Sistemas de Banco de Dados 1",
	    "code": "FOA0137",
	    "carga": "60",
	    "semestre": "5"
	},
	{
	    "name": "Fundamentos de Sistema Operacional",
	    "code": "FGA0170",
	    "carga": "60",
	    "semestre": "5"
	},
	{
	    "name": "Compiladores 1",
	    "code": "FGA0003",
	    "carga": "60",
	    "semestre": "5"
	},
	{
	    "name": "Estruturas de Dados 2",
	    "code": "FGA0030",
	    "carga": "60",
	    "semestre": "5"
	},
	{
	    "name": "Qualidade de Software",
	    "code": "FGA0278",
	    "carga": "60",
	    "semestre": "6"
	},
	{
	    "name": "Testes de Software",
	    "code": "FGA0238",
	    "carga": "60",
	    "semestre": "6"
	},
	{
	    "name": "Arquitetura e Desenho de Software",
	    "code": "FGA0208",
	    "carga": "60",
	    "semestre": "6"
	},
	{
	    "name": "Fundamentos de Redes de Computadores",
	    "code": "FGA0211",
	    "carga": "60",
	    "semestre": "6"
	},
	{
	    "name": "Sistemas de Banco de Dados 2",
	    "code": "FGA0060",
	    "carga": "60",
	    "semestre": "6"
	},
	{
	    "name": "Projeto e Análise de Algoritmos",
	    "code": "FGA0124",
	    "carga": "60",
	    "semestre": "6"
	},
	{
	    "name": "Técnicas de Programação em Plataformas Emergentes",
	    "code": "FGA0242",
	    "carga": "60",
	    "semestre": "7"
	},
	{
	    "name": "Paradigmas de Programação",
	    "code": "FGA0210",
	    "carga": "60",
	    "semestre": "7"
	},
	{
	    "name": "Fundamentos de Sistemas Embarcados",
	    "code": "FGA0103",
	    "carga": "60",
	    "semestre": "7"
	},
	{
	    "name": "Programação para Sistemas Paralelos e Distribuídos",
	    "code": "FGA0244",
	    "carga": "60",
	    "semestre": "7"
	},
	{
	    "name": "Engenharia de Produtos de Software",
	    "code": "FGA0206",
	    "carga": "60",
	    "semestre": "8"
	},
	{
	    "name": "Gerência de Configuração e Evolução de Software",
	    "code": "FGA0240",
	    "carga": "60",
	    "semestre": "8"
	},
	{
	    "name": "Estágio Supervisionado",
	    "code": "FGA0288",
	    "carga": "210",
	    "semestre": "8"
	},
	{
	    "name": "Trabalho de Conclusão de Curso",
	    "code": "FGA0287",
	    "carga": "60",
	    "semestre": "9"
	},
	{
	    "name": "Projeto Integrador de Engenharia 2",
	    "code": "FGA0250",
	    "carga": "60",
	    "semestre": "9"
	},
	{
	    "name": "Trabalho de Conclusão de Curso 2",
	    "code": "FGA0290",
	    "carga": "90",
	    "semestre": "9"
	},
]

for subject in software_subjects:
    Subject.objects.create(
        name = subject['name'],
        code = subject['code'],
        workload = subject['carga'],
        default_semester = subject['semestre']
    )