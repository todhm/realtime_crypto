from hashlib import sha256 


def find_hash(num_zeros): 
    nonce = 0 
    dog = "Moose"

    while True: 
        dog_nonce = dog + str(nonce)
        dog_nonce_encoded = dog_nonce.encode('utf-8')
        _hash_ = sha256(dog_nonce_encoded).hexdigest()
        if _hash_.startswith(num_zeros*"0"): 
            return nonce,_hash_ 

        else: 
            nonce += 1


