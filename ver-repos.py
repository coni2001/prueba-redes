import requests

base_url = "https://api.github.com"

def obt_repo_user(usuario):
    url = f"{base_url}/users/{usuario}/repos"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        repositories_data = respuesta.json()
        return repositories_data
    else:
        return None

usuario = "coni2001"

user_repos = obt_repo_user(usuario)
if user_repos:
    print(f"Repositoerios de {usuario}:")
    for repo in user_repos:
        print(repo["name"])
else:
    print(f"No se pudieron recuperar los repositorios.")
