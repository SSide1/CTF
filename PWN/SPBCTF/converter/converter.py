from pwn import *

p = remote('109.233.56.90',11573)
while(1):
    string = p.recvuntil('Convert ')
    string2 = p.recvuntil(' to')
    #print(string)
    string2 = string2.decode()
    string2 = string2[:-3]
    res = int(string2)
    print(res)
    #parser of int
    stringich = p.recv()
    if stringich == b'\n _   _             \r\n| | | |  ___ __  __\r\n| |_| | / _ \\\\ \\/ /\r\n|  _  ||  __/ >  < \r\n|_| |_| \\___|/_/\\_\\\r\n                   \r\n':
        payload = hex(res)
        payload = payload[2:]
        print(payload)
        #convert to hex
    elif stringich == b'\n  ___         _           _ \r\n / _ \\   ___ | |_   __ _ | |\r\n| | | | / __|| __| / _` || |\r\n| |_| || (__ | |_ | (_| || |\r\n \\___/  \\___| \\__| \\__,_||_|\r\n                            \r\n':
        payload = oct(res)
        payload = payload[2:]
        print(payload)
        #convert to octal
    elif stringich == b"\n _      _  _    _    _         _____             _  _                 __    _  _   \r\n| |    (_)| |_ | |_ | |  ___  | ____| _ __    __| |(_)  __ _  _ __   / /_  | || |  \r\n| |    | || __|| __|| | / _ \\ |  _|  | '_ \\  / _` || | / _` || '_ \\ | '_ \\ | || |_ \r\n| |___ | || |_ | |_ | ||  __/ | |___ | | | || (_| || || (_| || | | || (_) ||__   _|\r\n|_____||_| \\__| \\__||_| \\___| |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n                                                                                   \r\n":
        payload = p64(res,endian='little')
        #payload = payload[2:-1]
        print(payload)
        #convert to little endian format
    elif stringich == b"\n ____   _          _____             _  _                 __    _  _   \r\n| __ ) (_)  __ _  | ____| _ __    __| |(_)  __ _  _ __   / /_  | || |  \r\n|  _ \\ | | / _` | |  _|  | '_ \\  / _` || | / _` || '_ \\ | '_ \\ | || |_ \r\n| |_) || || (_| | | |___ | | | || (_| || || (_| || | | || (_) ||__   _|\r\n|____/ |_| \\__, | |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n           |___/                                                       \r\n":
        payload = p64(res,endian='big')
    
        print(payload)
        #convert to big endian format

    p.sendline(payload)
#endless while(working untill answer)    
p.interactive()
