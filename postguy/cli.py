#!/usr/bin/env python3
import argparse
import json
import os
import requests

CONFIG_FILE = "config.json"

def set_postguy(url: str):
    """Armazena a URL no arquivo de configuração."""
    config = {"url": url}
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f)
    print("URL configurada:", url)
    return url

def get_url():
    """Lê a URL armazenada; se não existir, solicita que seja configurada."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("url")
    else:
        print("Nenhuma URL configurada. Use o comando 'set' para definir a URL da API.")
        return None

def get_postguy(url: str):
    """Realiza uma requisição GET."""
    response_get = requests.get(url)
    if response_get.status_code < 300:
        print("GET:", response_get.content)
    else:
        print("Não foi possível conectar")
        print("Status:", response_get.status_code)

def post_postguy(url: str, json_data):
    """Realiza uma requisição POST com um objeto JSON passado como string."""
    response_post = requests.post(url, json=json_data)
    print("POST code:", response_post.status_code)

def postj_postguy(url: str, json_path: str):
    """Realiza uma requisição POST lendo os dados de um arquivo JSON."""
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

class PostguyCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="postguy",
            description="CLI criado para fazer teste em API de forma rápida e simples"
        )
        self.subparser = self.parser.add_subparsers(dest="comando", required=True)
        self._add_set_command()
        self._add_get_command()
        self._add_post_command()
        self._add_post_json_command()

    def _add_set_command(self):
        set_parser = self.subparser.add_parser(
            "set",
            help="Define a URL da API a ser testada"
        )
        set_parser.add_argument("url", type=str, help="URL da API")

    def _add_get_command(self):
        self.subparser.add_parser("get", help="Realiza um teste GET na API")

    def _add_post_command(self):
        post_parser = self.subparser.add_parser("post", help="Realiza um teste POST na API")
        post_parser.add_argument("json", help="String JSON a ser enviada")

    def _add_post_json_command(self):
        postjson_parser = self.subparser.add_parser("postj", help="Realiza um teste POST utilizando um arquivo JSON")
        postjson_parser.add_argument("json_path", help="Caminho para o arquivo JSON")

    def run(self):
        args = self.parser.parse_args()
        comando = args.comando

        if comando == "set":
            set_postguy(args.url)
        else:
            url = get_url()
            if not url:
                return

            if comando == "get":
                get_postguy(url)
            elif comando == "post":
                try:
                    json_data = json.loads(args.json)
                except Exception as e:
                    print("Erro ao decodificar JSON:", e)
                    return
                post_postguy(url, json_data)
            elif comando == "postj":
                postj_postguy(url, args.json_path)

if __name__ == "__main__":
    cli = PostguyCLI()
    cli.run()
