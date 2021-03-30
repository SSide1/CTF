TASK
_______________
Converter
Author: Ilya Glebov (@returnint)
Convert 'Em All!

nc -nv 109.233.56.90 11573
https://pwn.spbctf.ru/tasks/pwn1_converter
_______________

The meaning of the task is clear at once. The server sends us a value that needs to be converted from one 
format to another. The very appearance of the required conversion looks unusual. In order to solve, let's
write a script using Python3 and pwntools

![image](https://user-images.githubusercontent.com/76822573/113010278-623e7080-9181-11eb-80c2-ea15a95621b4.png)

The first step is to write a parser that will retrieve the required value.

After that, you need to write the conditions in which the difference between one required conversion from another
will be visible

if stringich == b'\n _   _             \r\n| | | |  ___ __  __\r\n| |_| | / _ \\\\ \\/ /\r\n|  _  ||  __/ >  < \r\n|_| |_| \\___|/_/\\_\\\r\n                   \r\n':
        payload = hex(res)
        payload = payload[2:]
        print(payload)
        
Such a string will be for translation into hex, the rest will be done by analogy. The main thing is to make a loop that
will run until the values stop flowing

After executing the script and converting several hundred values, the server returns the required correct answer

![image](https://user-images.githubusercontent.com/76822573/113011023-04f6ef00-9182-11eb-9efe-d8f832ee124c.png)

The answer is: spbctf{You_ARE_CONveRTEr_MSW600}
