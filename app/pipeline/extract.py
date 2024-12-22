import requests

def api_authentication(api_key: str):
    """
    função que realiza método POST para autenticar usuário através de token

    args:
    api_key: str

    return: str
    """
    api_url = 'https://api.olhovivo.sptrans.com.br/v2.1'
    auth_endpoint = f'{api_url}/Login/Autenticar'

    authentication = requests.post(auth_endpoint, params={'token': api_key})

    if authentication.status_code == 200 and authentication.text == 'true':
        print('Autenticação realizada com sucesso!')
    else:
        return (f'Falha na autenticação. Erro {authentication.status_code}: {authentication.text}')
    
# def extract_api_data():
#     """
#     função que realiza método GET para trazer o JSON da API
#     """
#     api_url = 'https://api.olhovivo.sptrans.com.br/v2.1'
#     get_endpoint = f'{api_url}/Posicao'

#     request = requests.get(get_endpoint, params=)