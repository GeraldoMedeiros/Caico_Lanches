# Caico_Lanches
O objetivo geral do nosso sistema web é permitir um ambiente intuitivo para que os usuários possam fazer seus pedidos com facilidade e rapidez. O cadastro de usuário é relativamente simples e seguro, e o foco da plataforma é despertar o interesse das pessoas que tem pouco tempo livre para se deslocar para uma lanchonete, tendo em vista as questões de trânsito e segurança da cidade.

Escolhemos Python com Django pois os dois juntos foram responsáveis por  uma grande quantidade de trabalhos no último ano e ainda está em crescimento. O Django atua como framework full-stack, ou seja, atende a todas as camadas de softwares – desde a conexão com o banco de dados até a geração da tela para o usuário final.

Os projetos implementados em Django seguem a modelagem MTV - Model (modelo de dados), Template (tela de interação com o usuário) e View (processamento de dados).

O model é responsável por organizar os dados para que o banco faça a persistência de dados, além disso é ele  também é responsável por atender a requisições de dados do view. No mundo relacional, ele implementa o ORM - Object-Relational Mapping.

O template é responsável por renderizar as telas para que o usuário tenha uma experiência agradável bem como coletar dados fornecidos pelos eles.

A view é o faz tudo da modelagem MTV, é ela quem implementa a lógica da aplicação fazendo uma ponte entre o que o usuário faz na tela e a base de dados, podendo fazer processamento interno e retornando informações úteis aos usuários.

É importante ressaltar que nesse modelo é ideal separar a lógica (views) da tela (templates), sendo que estes nunca devem rodar nenhuma lógica, apenas exibir o html para os browsers renderizarem. É ideal que para cada template seja associado uma view que a controla.
