"""
Quick Hacky Implementation of RSA
"""

#P = 13
#Q = 17

P = 170007611163882156467583070449223838584656753148867131633512190380283049593667937234054209916788376143894984910718820080485130228317492395177494053588704733242066260215738749826985323020318900966858054745093276666701971181051299894745771442097807356197274229456637808451705389506462483315002459525647
Q = 481643715591972638598218313298174701613643321254523884689569786332541775926781293302556117738302307356981609721753075739005830996780920022755885174107599088199228946117515541982018885577402946246815718309298010594221374531947169982607824253065171036917904012166986458504590468987728792073331236197449

#e = 5
e = pow(2,16) + 1

N = P * Q
phi = (P-1)*(Q-1)

e2 = e
d = 1
top1 = phi
top2 = phi
while e2 != 1:
    k = top1//e2
    
    oldTop1 = top1
    oldTop2 = top2

    top1 = e2
    top2 = d

    e2 = oldTop1 - k * e2
    d  = oldTop2 - k * d

    if d < 0:
        d = d % phi


print("RSA Components:")
print()
print("P:   ", P)
print()
print("Q:   ", Q)
print()
print("N:   ", N)
print()
print("phi: ", phi)
print()
print("e:   ", e)
print()
print("d:   ", d)
print()


# Bob's part
def encrypt(plainText, publicKey):
    e = publicKey[0]
    N = publicKey[1]

    ciphertext = ""
    for i in range(0, len(plainText)):
        
        # "B" -> 66
        ch = ord(plainText[i]) # converts character to ASCII (integer)
        
        # 66 -> 066
        if ch < 100:
            ch = "0" + str(ch)
        else:
            ch = str(ch)
        
        ciphertext += ch # string concatenation

    
    m = int(ciphertext)
    print("plaintext as integer:", m)
    c = pow(m,e,N)
    return str(c)


plaintext = "Hello, World! !@#$%^"
print("plaintext: ", plaintext)
ciphertext = encrypt(plaintext,[e,N])
# Bob sends this variable to Alice

print("Ciphertext: ", ciphertext)
print()


def decrypt(ciphertext, privateKey):
    d = privateKey[0]
    N = privateKey[1]

    c = int(ciphertext)
    m = pow(c,d,N)

    plaintext = str(m)
    # m = 66 -> plaintext = "66"

    if len(plaintext)%3 != 0:
        plaintext = "0" + plaintext
    # plaintext -> "066"

    message = ""

    for i in range(0, len(plaintext), 3):
        ch = plaintext[i:i+3]

        message += chr(int(ch))

    return message


message = decrypt(ciphertext, [d,N])
print("Message after decryption: ", message)
print()

