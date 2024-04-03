# JWT
Web
200 points
# Description
Сможешь понять, как это работает? http://158.160.35.89:8000/ <br />
python file is given
# Solution
Firstly let's follow the link. All we have there is a text saying that we need to take a look at the site source file. 

![image](https://github.com/danzyxd/CTFs/assets/144260597/bbe803f5-b537-499b-b6cf-a605320a48e4)

And here we can see two fuctions: first one is generating the jwt code, and the second is checking it and if it will have a "isAdmin" parameter as True it will return a flag.

![image](https://github.com/danzyxd/CTFs/assets/144260597/2b5a23b1-fbc5-43ab-902a-5779ade55387)

By using the gen-jwt fuction we got a jwt code.{"jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiZGFuenl4ZCIsImlzQWRtaW4iOmZhbHNlfQ.zT3t36AxqctJXZ8BqTlilNqFySA02CkaXnK3ekedjcs"}<br />
Let's decode it at jwt.io 

![image](https://github.com/danzyxd/CTFs/assets/144260597/432bf9fe-00b4-4084-9200-440978a39d35)

After the decoding we can change the "isAdmin":false to a "isAdmin":true and get the corrected jwt code. But it says that we need a secret to verify the signature and that secret is given in a python code at 4th string.

![image](https://github.com/danzyxd/CTFs/assets/144260597/37603c62-b177-42b4-901c-239dc9bfe686)

So after the getting a jwt code we need to use a second function: check-jwt.

![image](https://github.com/danzyxd/CTFs/assets/144260597/31fee150-17dc-4820-b356-2e436b4362a3)

A now it returns us a flag.

![image](https://github.com/danzyxd/CTFs/assets/144260597/879a8c21-69b6-45a0-b14d-8b14c32fc12a)<br />
![image](https://github.com/danzyxd/CTFs/assets/144260597/32cc9b8d-09e4-41d9-90b8-6425f4d7a1bf)

kxctf{v3ry_d1ff1cu1t_t0_h4ck_jwt}
