
# JWT에 관련한 설정
class Config:
    JWT_SECRET_KEY = 'yhacademy1029##hello'
    # JWT_ACCESS_TOKEN_EXPIRES = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    # # True일 경우, (아마)3분 단위로 끊어진다.

    PROPAGATE_EXCEPTIONS = True
    # 메뉴얼에 있다.
