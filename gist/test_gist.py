import pytest


#   _____
# < marks >
#   -----
#          \   ^__^
#           \  (oo)\_______
#              (__)\       )\/\
#                  ||----w |
#                  ||     ||


def test_our_first_test() -> None:
    assert 1 == 1


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(1 != 2, reason="1 is different from two")
def test_should_skip_if() -> None:
    assert 1 == 2

    """_summary_
        A ﬂaky test is an analysis of web application code that fails to produce the same 
        result each time the same analysis is run. Whenever new code is written to develop or 
        update computer software, a web page or an app, it needs to be tested throughout 
        the development process to make sure the application does what it’s supposed to do 
        when it’s released for use.
    """


@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    # assert 1 == 2   #gist/test_gist.py::test_dont_care_if_fails XFAIL
    assert 1 == 1  # gist/test_gist.py::test_dont_care_if_fails XPASS

    """_summary_
        This mark should be registered in the pytest.ini.
    """


@pytest.mark.um_nome_qualquer
def test_with_a_custom_mark1() -> None:
    pass


@pytest.mark.um_nome_qualquer
def test_with_a_custom_mark2() -> None:
    pass


#   ________
# < fixtures >
#   --------
#          \   ^__^
#           \  (oo)\_______
#              (__)\       )\/\
#                  ||----w |
#                  ||     ||


class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"

    """_summary_
        Se o nome de uma fixture bater com o nome de um parâmetro, a função fixture
        será executada primeiro e o resultado será passado como parâmetro.
        Em outras palavras, uma fixture serve para inicializar uma função de teste.
    """


@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR")


def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")

    #   ___________
    # < parametrize >
    #   -----------
    #          \   ^__^
    #           \  (oo)\_______
    #              (__)\       )\/\
    #                  ||----w |
    #                  ||     ||

    """_summary_
        O nome do parâmetro 'company_name' bate com o da função, então é passado
        automaticamente e a função a ser testada será executada tantos forem
        os parâmetros.
    """


@pytest.mark.parametrize(
    "company_name",
    ["TikTok", "Instagram", "Twitch"],
    ids=["TIKTOK TEST", "INSTAGRAM TEST", "TWITCH TEST"],
)
def test_parametrized(company_name: str) -> None:
    print(f"Test with {company_name}")


#   _____________
# < python raises >
#   -------------
#          \   ^__^
#           \  (oo)\_______
#              (__)\       )\/\
#                  ||----w |
#                  ||     ||


def raise_covid19_exception() -> None:
    raise ValueError("Corona Virus Exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "Corona Virus Exception" == str(e.value)
