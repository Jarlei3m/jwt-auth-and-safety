from .jwt_handler import JwtHandler

def test_jwt_handler():
    jwt_handler = JwtHandler()

    body = {
        "username": "John Doe",
        "any_key": "abc123"
    }

    token = jwt_handler.create_jwt_token(body)
    token_information = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_information["username"] == body["username"]
    assert token_information["any_key"] == body["any_key"]
