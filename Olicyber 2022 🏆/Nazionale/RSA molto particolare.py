from Crypto.Util.number import *

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y
    
# inizialmente risolto con factordb.com
n = 22714782753220015042573603265764327669650408033887636001879315184259375362820403603936005525717891771936636443451884119703671427781729492224095091855683005507053963590222220410804649184763035006811331809382943132022500027644637621163477965898393682291084319795270435040869951140803612012610686322537800900791300826066574059761090027917447672155092101024934115081690160104897792167626579027888190943470746383568651182247114083165294856136382262206643466869528191984416012578579746005217713198188905067819779002232496897304974008305258471888110945562966313488702125793402335565466499907920044056450331308275860705662078
for i in range(2, n):
    if n % i == 0:
        p, q = i, n//i
        break
e = 65537
phi = (p-1)*(q-1)
f = bytes_to_long(bytes.fromhex("388244a02eb9e2c2c06bcbc932422e0d181156ea4e08710b6987aad4f16e55e137b45ed9776b6baaffad78006db8131526e0c941b759e4493f38a697caba8d1a8e81300baa86d7b0a63b542e661b3bda502f6c09bf5636dbf567c21a3f3b10dcf9054ed4c485755df1d6d2f4a05814281eea0f4cb43d4e623a92c62473e2a2315e29e46ac31ff37e2a8feddba8f6d11a31aa7941d7edef3087582e43f2faa83a0555a598c1248568d8a268d993c8b47e8cc7c76d9ce95df1933d6b32fa331c1fcb154ebd65681945c958d8f0f10c015a478cc03fa4e31c1b5a4c55dc3da7b9c9ee5e0f24481b81a75af306dc9b766913c234f03673e9dc1cf35eb7f338d12e1f"))
gcd, d, b = egcd(e, phi)
m = pow(f, d, n)
print(long_to_bytes(m).decode(), end="")