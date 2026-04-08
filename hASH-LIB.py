import hashlib 
data = input("enter your username:  ")
hash_object = hashlib.sha256(data.encode())
hash_hex = hash_object.hexdigest()
print("SHA-256 Hash:", hash_hex)

hash_object_md5 = hashlib.md5(data.encode())
print("MD5 Hash:", hash_object_md5.hexdigest())
