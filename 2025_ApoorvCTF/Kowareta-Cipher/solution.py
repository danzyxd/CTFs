from pwn import remote
from Crypto.Util.number import long_to_bytes

HOST = "chals1.apoorvctf.xyz"
PORT = 4001

conn = remote(HOST, PORT)

response = conn.recvline().strip()
# print(response)
response = conn.recvline().strip()
# print(response)


# TEST
# Enter your input: Ciphertext: bcccba7d8d9b7acc8e3933d4291d386b
# Enter your input: Ciphertext: bad8fcf126a8d1fa2bd3ed076b31b290

# conn.sendline((b'0'*14).hex())
# response = conn.recvline().strip()#[24:]
# print(f"{response}, flag bytes length: {len(response[6:])/2 - 2}")
# conn.sendline((b'0'*14 + b'ap').hex())
# response = conn.recvline().strip()#[24:]
# print(f"{response}, flag bytes length: {len(response[6:])/2 - 2}")


# SOLUTION

flag = b'apoorvctf{3cb_3' # b'a' -> 0x61
# flag = b'a'

if len(flag) == 0:
    for byte in range(16):
        conn.sendline((b'A' * (15 - byte)).hex())
        
        # print((b'A' * (15 - byte) + flag).hex())
        
        ans = conn.recvline().strip()[30:62] # [24:24+38]
        for j in range(32, 127):
            conn.sendline((b'A' * (15 - byte) + flag + long_to_bytes(j)).hex())

            # print((b'A' * (15 - byte) + flag + long_to_bytes(j)).hex())
            
            temp_response = conn.recvline().strip()[30:62] # [24:24+38]
            if temp_response == ans:
                flag += long_to_bytes(j)
                break
        print(flag) #, ans, temp_response, byte)
        continue
if len(flag) == 15:
    for byte in range(15, 32):
        conn.sendline((b'A' * (31 - byte)).hex())
        
        # print((b'A' * (15 - byte) + flag).hex())
        
        ans = conn.recvline().strip()[46:78] # [24:24+38]
        for j in range(32, 127):
            conn.sendline((b'A' * (31 - byte) + flag + long_to_bytes(j)).hex())

            # print((b'A' * (15 - byte) + flag + long_to_bytes(j)).hex())
            
            temp_response = conn.recvline().strip()[46:78] # [24:24+38]
            if temp_response == ans:
                flag += long_to_bytes(j)
                break
        print(flag) #, ans, temp_response, byte)
        continue
