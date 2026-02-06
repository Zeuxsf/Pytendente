import requests
import os
from dotenv import load_dotenv


url = "https://api.github.com/users/Zeuxsf"
resp = requests.get(url)
dados = resp.json()

#print(resp.status_code)
print(dados)
#print(dados[5]['name'])
#print(dados[5]['description'])


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

resp = requests.post(
    url,
    json={"query": query},
    headers=headers
)

data = resp.json()

print(data)

def info_sobre_mim():
  pass
  #Vai pegar informações basicas sobre mim no github (seguidores, descrição, quantidade de repos públicas)

def principais_repos():
  pass
  #Vai mostrar informações sobre os principais repositórios que eu tenho (os que eu já deixo pinado no perfil, são os melhores)
  