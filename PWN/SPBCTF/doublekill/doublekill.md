TASK
_____________

it is necessary to grind the address return through the moved pointer

nc 109.233.56.90 11604


https://pwn.spbctf.ru/tasks/pwn2_doublekill
_____________


![image](https://user-images.githubusercontent.com/76822573/113007021-851b5580-917e-11eb-953a-e51e5a790924.png)

Let's open the binary file in the IDA PRO utility. The main function immediately redirects us to the play function,
which looks like this:

![image](https://user-images.githubusercontent.com/76822573/113007311-c90e5a80-917e-11eb-8e1e-c5dd65d6bddd.png)

It becomes clear that U: is a pointer to the beginning of the username array. Also, the size of the array is 40 bytes,
and 48 elements are read. We can take advantage of this and write an exploit.

![image](https://user-images.githubusercontent.com/76822573/113007883-42a64880-917f-11eb-9dec-f993397a9cfa.png)

from this stack you can see that we need to add 56 bytes to the beginning of the array and then we will get into
the memory area responsible for the return adress
But the size of our input will not allow us to enter 56 bytes at once, we can only overwrite the password_ptr
pointer. Let's write there the return address of the array, and change password_ptr to the address of the win
function, which contains the answer

![image](https://user-images.githubusercontent.com/76822573/113008652-e3950380-917f-11eb-995a-170fd249503b.png)

(*Python3 code attached*)

The answer is: spbctf{bytecode}
