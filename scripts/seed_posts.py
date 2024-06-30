from posts.models import Post

posts_list = [
    {
       "title": "Engenharia de Software Telegram" ,
       "description": "Grupo formado pelos estudantes de software da FGA",
       "link": "https://web.telegram.org/a/#-1001383799472"
    },
    {
       "title": "1.24 PIBIC e PIBEX @UnBConnect",
       "description": "Grupo de Comunicação entre os alunos com objetivo de compartilhar informações, dúvidas e oportunidades de PIBIC.",
       "link": "https://chat.whatsapp.com/L7589d0tzeH7dqlukVwIQ8"
    },
    {
       "title": "Cardápio RU",
       "description": "Cardápio do RU Café da Manhã/ Almoço/ Jantar",
       "link": "https://unbru.vercel.app/"
    },
    {
       "title": "Guardiões da Saúde",
       "description": "Grupo de Informes da Disciplina DSC0172 - VIGILÂNCIA EPIDEMIOLÓGICA PARTICIPATIVA",
       "link": "https://chat.whatsapp.com/IJFtdBLxNiq6sHpH48WolN"
    },
    {
       "title": "UNB - FGA 2024.1" ,
       "description": "Grupo formado por calouros da FGA 2024.1",
       "link": "https://chat.whatsapp.com/ENx92rSEU2c8raAoBRK0Ad"
    },
    {
       "title": "Mural da FGA" ,
       "description": "Grupo de informações da FGA, aqui vamos postar notícias, vagas de estágio, processos seletivos ou quaisquer outra coisa relevante para os alunos!",
       "link": "https://chat.whatsapp.com/KHR34U0R4xQ7FYm9jDdlke"
    },
    {
       "title": "Comunidade GNU/Linux" ,
       "description": "Passando aqui só para dar uma visão geral do que tinha pensado sobre o grupo. Queria juntar vocês para a gente se ajudar em eventuais dúvidas, ajudar o pessoal novato a instalar distros, ajudar o pessoal a fazer dualboot, ajudar em customização, erros, e para a gente divulgar também mais sobre FLOSS no campus. Conto com a ajuda de vocês para",
       "link": "https://chat.whatsapp.com/HllYnbbsa4z6PxJGOuWBz4"
    }
]

try:
    for postagem in posts_list:
        Post.objects.create(
            title = postagem['title'],
            description = postagem['description'],
            link = postagem['link'],
        )
except Exception as error:
    print(error)