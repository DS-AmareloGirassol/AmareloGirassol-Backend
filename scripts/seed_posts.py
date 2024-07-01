from posts.models import Post

from persons.models import Person

# Usuários

user1 = Person.objects.create(
    name="João da Silva",
    email='joao@aluno.br',
    password='joao',
    description='Sou João, um estudante do terceiro semestre apaixonado por tecnologia e inovação. Sempre busco novos conhecimentos e desafios para aprimorar minhas habilidades. Adoro resolver problemas complexos e estou determinado a fazer a diferença no mundo da tecnologia.',
    semester_being_attended=3
)

user2 = Person.objects.create(
    name="José Santos",
    email='jose@aluno.br',
    password='jose',
    description='Me chamo José e estou no quinto semestre. Tenho um forte interesse em desenvolvimento de software e sou ativo na comunidade acadêmica. Participo de projetos de pesquisa e grupos de estudo, e gosto de liderar e colaborar em equipe para alcançar grandes resultados.',
    semester_being_attended=5
)

user3 = Person.objects.create(
    name="Augusto Maia",
    email='augusto@aluno.br',
    password='augusto',
    description='Sou Augusto, atualmente no sétimo semestre. Tenho uma paixão por inteligência artificial e aprendizado de máquina. Com uma abordagem analítica, gosto de explorar novas tecnologias. Também atuo como mentor, ajudando colegas mais novos a superar desafios acadêmicos.',
    semester_being_attended=7
)

user4 = Person.objects.create(
    name="Marcelo Alves",
    email='marcelo@aluno.br',
    password='marcelo',
    description='Meu nome é Marcelo e estou no nono semestre. Sou entusiasta de redes de computadores e segurança da informação. Tenho um perfil investigativo e adoro entender o funcionamento interno dos sistemas. Participo de projetos de código aberto e valorizo muito a partilha de conhecimento.',
    semester_being_attended=9
)


# Postagens

posts_list = [
    {
       "title": "Engenharia de Software Telegram" ,
       "description": "Grupo formado pelos estudantes de software da FGA",
       "link": "https://web.telegram.org/a/#-1001383799472",
       "user": user1
    },
    {
       "title": "1.24 PIBIC e PIBEX @UnBConnect",
       "description": "Grupo de Comunicação entre os alunos com objetivo de compartilhar informações, dúvidas e oportunidades de PIBIC.",
       "link": "https://chat.whatsapp.com/L7589d0tzeH7dqlukVwIQ8",
       "user": user2
    },
    {
       "title": "Cardápio RU",
       "description": "Cardápio do RU Café da Manhã/ Almoço/ Jantar",
       "link": "https://unbru.vercel.app/",
       "user": user3
    },
    {
       "title": "Guardiões da Saúde",
       "description": "Grupo de Informes da Disciplina DSC0172 - VIGILÂNCIA EPIDEMIOLÓGICA PARTICIPATIVA",
       "link": "https://chat.whatsapp.com/IJFtdBLxNiq6sHpH48WolN",
       "user": user4
    },
    {
       "title": "UNB - FGA 2024.1" ,
       "description": "Grupo formado por calouros da FGA 2024.1",
       "link": "https://chat.whatsapp.com/ENx92rSEU2c8raAoBRK0Ad",
       "user": user1
    },
    {
       "title": "Mural da FGA" ,
       "description": "Grupo de informações da FGA, aqui vamos postar notícias, vagas de estágio, processos seletivos ou quaisquer outra coisa relevante para os alunos!",
       "link": "https://chat.whatsapp.com/KHR34U0R4xQ7FYm9jDdlke",
       "user": user2
    },
    {
       "title": "Comunidade GNU/Linux" ,
       "description": "Passando aqui só para dar uma visão geral do que tinha pensado sobre o grupo. Queria juntar vocês para a gente se ajudar em eventuais dúvidas, ajudar o pessoal novato a instalar distros, ajudar o pessoal a fazer dualboot, ajudar em customização, erros, e para a gente divulgar também mais sobre FLOSS no campus. Conto com a ajuda de vocês para",
       "link": "https://chat.whatsapp.com/HllYnbbsa4z6PxJGOuWBz4",
       "user": user3
    }
]

try:
    for postagem in posts_list:
        Post.objects.create(
            title = postagem['title'],
            description = postagem['description'],
            link = postagem['link'],
            user = postagem['user']
        )
except Exception as error:
    print(error)