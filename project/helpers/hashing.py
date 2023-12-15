import hashlib

class JHashHelper():
    def sha256(self,value):
        encoded_value=value.encode('utf-8')
        hash_value=hashlib.sha256(encoded_value).hexdigest()
        return hash_value