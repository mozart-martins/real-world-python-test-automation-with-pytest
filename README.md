# Real World Python Test Automation with Pytest

## Rever a secao 17 (Server Agnostic API Testing) do curso para rever como testar API de forma agnostica com o requests e como fazer o mock com o responses: ambos deve ser instalados pip install requests responses. 

DICA: O diretório gist dá a visão geral do Pytest.

> pip install pytest pytest-django

Entrar no diretório gist:
> pytest gist/test_gist.py -v -s -p no:warnings -m um_nome_qualquer

> -v significa modo verboso

> -p no:warnings esconde os warnings

> -m um_nome_qualquer é o nome de uma custom mark

> -s Exibe os prints de dentro de uma função de testes

> --durations=0 Exibe a duração dos testes

> -k "palavra-chave and not outra-coisa" Executa todos os testes cujos nomes possuam a palavra chave e não executa os que contenham outra-coisa.
