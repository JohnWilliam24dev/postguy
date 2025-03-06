#!/usr/bin/env python3
import argparse
import json
import os

from . import postguy_service as ps


class PostguyCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="postguy",
            description="CLI criado para fazer teste em API de forma rápida e simples"
        )
        self.subparser = self.parser.add_subparsers(dest="comando", required=True)
        self._add_set_command()
        self._add_get_command()
        self._add_setjson_command()
        self._add_post_command()
        self._add_post_json_command()
        self._add_put_command()     
        self._add_patch_command()   
        self._add_delete_command()
        self._add_putj_command()    
        self._add_patchj_command()  

    def _add_set_command(self):
        set_parser = self.subparser.add_parser("set",help="Define a URL da API a ser testada")
        set_parser.add_argument("url", type=str, help="URL da API")
    def _add_setjson_command(self):
        setjson_parser = self.subparser.add_parser("setjson",help="[json-path] Define o caminho padrão do arquivo JSON a ser utilizado nas requisições")
        setjson_parser.add_argument("json_path", type=str, help="Caminho para o arquivo JSON")
    def _add_get_command(self):
        get_parser = self.subparser.add_parser("get", help="[endpoint][json] Realiza um teste GET na API")
        get_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        
    def _add_post_command(self):
        post_parser = self.subparser.add_parser("post", help="[endpoint][json] Realiza um teste POST na API")
        post_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        post_parser.add_argument("json", type=str, help="String JSON a ser enviada")

    def _add_put_command(self):
        put_parser = self.subparser.add_parser("put", help="[endpoint][json] Realiza um teste PUT na API")
        put_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        put_parser.add_argument("json", type=str, help="String JSON a ser enviada")

    def _add_patch_command(self):
        patch_parser = self.subparser.add_parser("patch", help="[endpoint][json] Realiza um teste PATCH na API")
        patch_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        patch_parser.add_argument("json", type=str, help="String JSON a ser enviada")

    def _add_delete_command(self):
        delete_parser = self.subparser.add_parser("delete", help="[endpoint] [--json] Realiza um teste DELETE na API")
        delete_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        delete_parser.add_argument("--json", help="String JSON a ser enviada (opcional)", default=None)
    def _add_post_json_command(self):
        postjson_parser = self.subparser.add_parser("postj", help="[endpoint] [json_path] Realiza um teste POST utilizando um arquivo JSON")
        postjson_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        postjson_parser.add_argument("json_path", nargs="?", default=None, help="Caminho para o arquivo JSON")

    def _add_putj_command(self):
        putj_parser = self.subparser.add_parser("putj", help="[endpoint] [json_path] Realiza um teste PUT utilizando um arquivo JSON")
        putj_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        putj_parser.add_argument("json_path", nargs="?", default=None, help="Caminho para o arquivo JSON")

    def _add_patchj_command(self):
        patchj_parser = self.subparser.add_parser("patchj", help="[endpoint] [json_path] Realiza um teste PATCH utilizando um arquivo JSON")
        patchj_parser.add_argument("endpoint", type=str, help="Endpoint da API a ser acessado")
        patchj_parser.add_argument("json_path", nargs="?", default=None, help="Caminho para o arquivo JSON")

    def run(self):
        args = self.parser.parse_args()
        comando = args.comando

        if comando == "set":
            ps.set_postguy(args.url)
        elif comando == "setjson":
            ps.set_default_json(args.json_path)
        else:
            base_url = ps.get_url()
            if not base_url:
                return
            full_url = base_url + args.endpoint

            if comando == "get":
                ps.get_postguy(full_url)
            elif comando == "post":
                try:
                    json_data = json.loads(args.json)
                except Exception as e:
                    print("Erro ao decodificar JSON:", e)
                    return
                ps.post_postguy(full_url, json_data)
            elif comando == "postj":
                ps.postj_postguy(full_url, args.json_path)
            elif comando == "put":
                try:
                    json_data = json.loads(args.json)
                except Exception as e:
                    print("Erro ao decodificar JSON:", e)
                    return
                ps.put_postguy(full_url, json_data)
            elif comando == "patch":
                try:
                    json_data = json.loads(args.json)
                except Exception as e:
                    print("Erro ao decodificar JSON:", e)
                    return
                ps.patch_postguy(full_url, json_data)
            elif comando == "delete":
                if args.json:
                    try:
                        json_data = json.loads(args.json)
                    except Exception as e:
                        print("Erro ao decodificar JSON:", e)
                        return
                else:
                    json_data = None
                ps.delete_postguy(full_url, json_data)
            elif comando == "putj":
                ps.putj_postguy(full_url, args.json_path)
            elif comando == "patchj":
                ps.patchj_postguy(full_url, args.json_path)


def main():
    cli = PostguyCLI()
    cli.run()


if __name__ == "__main__":
    main()
