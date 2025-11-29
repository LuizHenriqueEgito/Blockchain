import base64
from pathlib import Path

def create_pwd_cipher(pwd: str) -> str:
    pwd_bytes = pwd.encode('utf-8')
    if len(pwd_bytes) < 32:
        pwd_bytes = pwd_bytes.ljust(32, b'\0')
    elif len(pwd_bytes) > 32:
        pwd_bytes = pwd_bytes[:32]
    fernet_key = base64.urlsafe_b64encode(pwd_bytes)
    return fernet_key    

def save_token(token: bytes, token_path: Path = 'token.bin') -> None:
    if token_path.exists():
        print('Token já existente.')
    with open(token_path, 'wb') as f:
        f.write(token)
    return None

    