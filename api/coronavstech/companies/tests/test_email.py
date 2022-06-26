import json
import pytest
from unittest.mock import patch
from django.core import mail


# deve falhar por que nao esta configurado no settings
@pytest.mark.xfail
def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    assert len(mailoutbox) == 0

    mail.send_mail(
        "Cool Subject",
        "Cool Message",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )

    assert len(mailoutbox) == 1

    assert len(mailoutbox[0].subject) == "Cool Subject"

    assert len(mailoutbox[0].message) == "Cool Message"


@pytest.mark.xfail
def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch("coronavstech.companies.views.send_email") as mocked_send_email_function:

        response = client.post(path="/send-email")
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"

        mocked_send_email_function.assert_called_with(
            subject="Assunto legal",
            message="Mensagem bastante bacana",
            from_email="meu_amigo_pedro@gmail.com",
            recipient_list=["israeltechlayoffs@gmail.com"],
        )


@pytest.mark.xfail
def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path="/send-email")
    assert response.status_code == 200
    assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}
