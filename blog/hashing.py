from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password: str):
        hash_password = pwd_context.hash(password)
        return hash_password

    def verify(hash_password,plain_password):
        return pwd_context.verify(plain_password, hash_password)
 