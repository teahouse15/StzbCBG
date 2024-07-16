from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 公钥
public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5gsH+AA4XWONB5TDcUd+xCz7ejOFHZKlcZDx+pF1i7Gsvi1vjy
JoQhRtRSn950x498VUkx7rUxg1/ScBVfrRxQOZ8xFBye3pjAzfb22+RCuYApSVpJ3OO3KsEuKExftz9oFBv3ejxPl
Yc5yq7YiBO8XlTnQN0Sa4R4qhPO3I2MQIDAQAB
-----END PUBLIC KEY-----
"""

# 加载公钥
public_key = serialization.load_pem_public_key(public_key_pem.encode())

# 要加密的数据
message = b"1"

# 使用公钥加密数据
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("加密后的数据：", ciphertext)
