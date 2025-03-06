import os
import requests
import json

CONFIG_FILE = "config.json"

def set_postguy(url: str):
    
    config = {"url": url}
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f)
    print("URL configurada:", url)
    return url
def set_default_json(json_path: str):
    
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            try:
                config = json.load(f)
            except Exception:
                config = {}
    config["default_json"] = json_path
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f)
    print("Caminho padrão do JSON configurado:", json_path)

def get_url():
    
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("url")
    else:
        print("Nenhuma URL configurada. Use o comando 'set' para definir a URL da API.")
        return None

def get_postguy(url: str):
   
    response_get = requests.get(url)
    if response_get.status_code < 300:
        print("GET:", response_get.content)
    else:
        print("Não foi possível conectar")
        print("Status:", response_get.status_code)

def post_postguy(url: str, json_data):
    
    response_post = requests.post(url, json=json_data)
    print("POST code:", response_post.status_code)

def get_default_json():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("default_json")
    else:
        return None

def postj_postguy(url: str, json_path: str = None):
    if json_path is None:
        json_path = get_default_json()
        if json_path is None:
            print("Caminho do JSON não informado e nenhum padrão foi configurado. Use 'setjson' para definir um caminho.")
            return
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except Exception as e:
        print("Erro ao ler o arquivo JSON:", e)
        return
    response_postj = requests.post(url, json=dados)
    print("POST code:", response_postj.status_code)
    try:
        print("POST response:", response_postj.json())
    except Exception:
        print("Não foi possível decodificar a resposta como JSON.")

def put_postguy(url: str, json_data):
    
    response_put = requests.put(url, json=json_data)
    print("PUT code:", response_put.status_code)
    try:
        print("PUT response:", response_put.json())
    except Exception:
        print("Não foi possível decodificar a resposta como JSON.")

def patch_postguy(url: str, json_data):
    
    response_patch = requests.patch(url, json=json_data)
    print("PATCH code:", response_patch.status_code)
    try:
        print("PATCH response:", response_patch.json())
    except Exception:
        print("Não foi possível decodificar a resposta como JSON.")

def delete_postguy(url: str, json_data=None):
    
    if json_data is not None:
        response_delete = requests.delete(url, json=json_data)
    else:
        response_delete = requests.delete(url)
    print("DELETE code:", response_delete.status_code)
    try:
        print("DELETE response:", response_delete.json())
    except Exception:
        print("Não foi possível decodificar a resposta como JSON.")

def putj_postguy(url: str, json_path: str = None):
    
    if json_path is None:
        json_path = get_default_json()
        if json_path is None:
            print("Caminho do JSON não informado e nenhum padrão foi configurado. Use 'setjson' para definir um caminho.")
            return
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except Exception as e:
        print("Erro ao ler o arquivo JSON:", e)
        return
    response_putj = requests.put(url, json=dados)
    print("PUT code:", response_putj.status_code)
    try:
        print("PUT response:", response_putj.json())
    except Exception:
        print("Não foi possível decodificar a resposta como JSON.")

def patchj_postguy(url: str, json_path: str = None):
    
    if json_path is None:
        json_path = get_default_json()
        if json_path is None:
            print("Caminho do JSON não informado e nenhum padrão foi configurado. Use 'setjson' para definir um caminho.")
            return
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except Exception as e:
        print("Erro ao ler o arquivo JSON:", e)
        return
    response_patchj = requests.patch(url, json=dados)
    print("PATCH code:", response_patchj.status_code)
    try:
        print("PATCH response:", response_patchj.json())
    except Exception:
        print("Não foi possível decodificar a resposta como JSON.")
