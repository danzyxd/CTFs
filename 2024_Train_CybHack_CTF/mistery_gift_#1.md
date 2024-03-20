# mistery gift #1
200 points
# Description
заберешь подарок ?) вот тут http://158.160.35.89:5000/
# Solution
Let's visit that website.
All we see here is a message 'To get the gift..' and two 'Login' and 'Regestration' buttons below.
![image](https://github.com/danzyxd/CTFs/assets/144260597/dd3dd709-288b-40fe-becb-b35128805b6e)
Firslty let's try the very basic SQL injection, trying login as an admin. All we have to do is type "admin'--" in the login string and anything in the password(doesn't matter what, i typed '123').
![image](https://github.com/danzyxd/CTFs/assets/144260597/9f333113-85e9-4607-9935-32ed45880f54)
After the entering as an admin all we see is the string with the flag in it. kxctf{th1s_1s_v3ry_s1mpL3_sql_1nj3ct10n}
![image](https://github.com/danzyxd/CTFs/assets/144260597/b5f04e8e-4bb3-44f6-a674-1689a60afc33)
