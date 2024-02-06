
from sage.all import *

p = 19
q = 11
n = p * q
fn = (p - 1) * (q - 1)

# Calcul de c
c = 0
while gcd(fn,c) != 1 :
  c = randrange(2,fn)

# Calcul de d 
d = inverse_mod(c, fn)

# Les clé sont des tuples
# Clé publique {c, n}
cle_publique = (c, n)


# Clé privée {d, n}
cle_privee = (d, n)

# Message à chiffrer
M = 200

# Chiffrement
C = power_mod(M, c, n)

# Déchiffrement
D = power_mod(C, d, n)

print("fn:", fn)
print("\n")
print("Clé publique {c, n}:", cle_publique)
print("Clé privée {d, n}:", cle_privee)
print("\n")
print("Message chiffré:", C)
print("Message déchiffré:", D)

########################################################################################


def nb_premier(t):
    # Générer un nombre premier aléatoire de t bits
    a = pow(2,t)
    b = pow(2,t+1) - 1
  
    numBP = next_prime(randrange(a,b))
    while a > numPB > b:
       numBP = next_prime(randrange(a,b))
    
    return numB


def paireCles(t):
    # Générer deux nombres premiers de t/2 bits chacun
    p = next_prime(2 ** (t // 2))
    q = next_prime(2 ** (t // 2))

    n = p * q
    fn = (p - 1) * (q - 1)

    c = 0
    while gcd(fn,c) != 1 :
       c = randrange(2,fn)

    d = inverse_mod(c, fn)

    
    cle_publique = (c, n)
    cle_privee = (d, n)

    return cle_publique, cle_privee

t = 128
##print(nombre_premier_aleatoire(t))
print("\n")
cle_publique, cle_privee = paireCles(t)
print("\n")
print("Clé publique {c, n}:", cle_publique)
print("Clé privée {d, n}:", cle_privee)


########################################################################################


def casserRSA(cle_pb,message_code):
   # Factoriser n
   n = cle_pb[1]
   p = factor(n)[0]
   q = factor(n)[1]

   # Calculer fn
   fn = (p[0] - 1) * (q[0] - 1)

   # Calculer d 
   c = cle_pb[0]
   d = inverse_mod(c, fn)

   # Clé privée 
   cle_pv = (d, n)

   # Déchiffrement
   message_initial = power_mod(message_code, d, n)

   return message_initial


cle_pb = (32224920548891884277319616150846179881012498534099,58597520734673306150541084479283572700664905911323)
message_code = 8129784680929258452176883926768050912307760882691

print("n: ",cle_pb[0])
print("\n")
print("message_code: ",message_code)
print("\n")
print("message_initial: ",casserRSA(cle_pb,message_code))