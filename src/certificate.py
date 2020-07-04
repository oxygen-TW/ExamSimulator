#from Crypto.PublicKey import RSA
#from Crypto.Random import get_random_bytes
#from Crypto.Cipher import AES, PKCS1_OAEP
import requests
import os

def upload(url, path):
    files = {'file': open(path, 'rb')}

    r = requests.post(url, files=files)
    return r.text

def RSAcheck(code, keyPath, id):
    data = code.encode("utf-8")
    file_out = open("encrypted_data.bin", "wb")

    recipient_key = RSA.import_key(open(keyPath).read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()

    return str(upload("http://127.0.0.1:5000/check/" + id, "encrypted_data.bin"))

def checkLocalFile(id):
    if (not(os.path.isfile("certificate/{0}.pub".format(id)))):
        return False
    else:
        return True

def RSAnewKey(id, url):
    if(not(checkLocalFile(id))):
        r = requests.get(url+"/newKey/"+id)
        with open("certificate/"+id+".pub", "w") as f:
            f.write(r.text)
            f.close()

    #check(id, "client/"+id+".pem", id)
    


if __name__ == "__main__":
    main()