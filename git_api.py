import requests
import os
from dotenv import load_dotenv

url = "https://api.github.com/graphql"

load_dotenv()
headers = {
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"
}

query = """
query {
  user(login: "Zeuxsf") {
    pinnedItems(first: 6, types: REPOSITORY) {
      nodes {
        ... on Repository {
          name
          description
          url
          stargazerCount
          primaryLanguage {
            name
          }
        }
      }
    }
  }
}
"""

response = requests.post(
    url,
    json={"query": query},
    headers=headers
)
data = response.json()
datatwo = data['data']['user']['pinnedItems']['nodes']

repos = []

def principais_repos():
  #Vai retornar informações sobre os principais repositórios que eu tenho (os que eu já deixo pinado no perfil)
  return datatwo

#print(principais_repos())  

if __name__ == '__main__':
  confirma = 1 #testes testes testes

  if confirma == 1:
    for item in datatwo:
      #Exemplo de uso do datatwo
      print(f'Nome: {item['name']}')
      print(f'Descrição: {item['description']}')
      print(f'Estrelas: {item['stargazerCount']}')
      print(f'Linguagem Principal do Projeto: {item['primaryLanguage']['name']}')
      print(f'Link do Repositório: {item['url']}')
      print('---')