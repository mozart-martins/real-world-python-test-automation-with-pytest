# Real World Python Test Automation with Pytest

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

![image](https://user-images.githubusercontent.com/49461099/173208797-af4395d7-488b-4436-b32e-e483c55e476e.png)

