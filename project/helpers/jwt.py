import jwt
class JawadJwtHelper:
    def __init__(self,secret,algorithm):
        self.secret=secret
        self.algorithm=algorithm
    def encode(self,payload):
        encode_jwt=jwt.encode(payload,self.secret,algorithm=self.algorithm)
        return encode_jwt
    def decode(self,encode_jwt):
        payload=jwt.decode(encode_jwt,self.secret,algorithm=[self.algorithm])
        return payload