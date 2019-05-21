from hashlib import sha256 

dog = "Moose"
dog_encoded = dog.encode("utf-8")
temp = sha256(dog_encoded).hexdigest()
print(temp)