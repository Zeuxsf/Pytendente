![ssss](https://github.com/user-attachments/assets/b12a7eba-6369-4f1a-b2a6-3e14e47e85bb)
# Pytendente: Atendente virtual feito em Python!

### O que é o Pytendente?

O Pytendente é um chatbot de atendimento virtual/meu portifólio falante. Ele compara a pergunta do usuário com as perguntas na qual ele foi treinado e devolve uma resposta pré-definida, quanto mais informação ele tiver, mais naturais ficam as respostas. O sistema utilizado para as comparações foi a biblioteca **scikit** e os modelos utilizados foram: *TfidfVectorizer* para transformar as palavras em vetores/números para que possam ser comparadas e o *cosine_similarity* que vai fazer o trabalho de comparar esses vetores. Eu poderia ter usado a biblioteca **fuzzywuzzy** para esse tipo de chatbot, é simples e direto, porém o scikit me permite treinar um modelo e salvar em *.pkl*, oque melhora a velocidade na hora de comparar as mensagens. Velocidade essa que é muito necessária, já que eu empacotei todas as funções do chatbot e outras funções em endpoints, criando uma API rest. 

### Front-End

O front-end do pytendente foi feito usando streamlit para uma entrega rápida, funcional e agradável estéticamente, é a primeira vez que utilizo esse recurso em um projeto mas com certeza usarei mais, sua simplicidade não tira o poder que essa interface possui.

### Funcionalidades

Funcionalidades interessantes nesse projeto: envio de emails utilizando o método **SMTP**, que permite um contato direto do usuário com o desenvolvedor sem sair do site. Eu incluí redirecionamentos dinâmicos no front-end do chatbot, assim que ele identifica que o usuário está falando sobre uma determinada função, ele redireciona o usuário automaticamente pra aba de interesse.

### Tecnologias utilizadas

- IDE: VSCode
- Linguagem: Python 3.12
- Docker
- FastAPI
- StreamLit
- SQLalchemy
- Alembic
- SciKit
- Válido mencionar que eu utilizei o gerenciador de pacotes UV

### Como clonar e utilizar o repositório (Utilizando UV)
Caso não tenha UV, use: `pip install uv`

- Clonando o Repositório: `git clone https://github.com/Zeuxsf/Pytendente.git`
- Abra o repositório na sua IDE favorita e use: `uv sync`
- Inicie o Venv: `uv venv` e depois  `source .venv/bin/activate`
- Instale as dependências do código: Use `uv pip install -r requirements.txt`
- Esse projeto possui uma dockefile, use `docker build -t pytendente-api .` para montar a imagem

Pronto, agora é só configurar o *.env* e utilizar o projeto.

### Sobre o desenvolvimento
A criação do Pytendente partiu do princípio de querer explorar novas tecnologias e cair dentro de um projeto um pouco mais complexo do que estou habituado. Além de todos os porquês, o pytendente foi o meu primeiro deploy, o primeiro serviço que é possível acessar de qualquer lugar que possua internet, um marco na minha trajetória como desenvolvedor. O pytendente é um projeto/portifólio, ele expõe outros projetos, fala um pouco sobre mim e oferece meios de contato para quem se interessar.

--------------

*Criado por: Alexandre S. de França*
