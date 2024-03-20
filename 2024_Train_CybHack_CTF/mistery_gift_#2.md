# mistery gift #2
200 points
# Description
заберешь еще один подарок?) вот тут http://158.160.35.89:5100/
# Solution
Everything is same as in the mistery gift #1 so let's try to login as an admin again.
![image](https://github.com/danzyxd/CTFs/assets/144260597/57fc7f0e-1c7d-4431-8b5b-0d39172f7e0c)
We successfully entered as an admin and now we see the "Take the present" button.
![image](https://github.com/danzyxd/CTFs/assets/144260597/8f130b22-130f-4c3a-b0bf-0bd77e3995ef)
After the pressing the button all we see is a picture. But there's nothing we can do with it. But we can notice that in the URL we a string "?filename=gift.jpg", what if we will find a flag.txt with it? So let's try to put a "flag.txt" instead of "gift.jpg".
![image](https://github.com/danzyxd/CTFs/assets/144260597/8a46578b-6bdf-47d3-8eaa-ed5d54c8a7d1)
It gives us an error page, seems like there's no flag.txt file, so let's try in other directory, especially an upper one< to do it we have to put "../" before the "flag.txt".
![image](https://github.com/danzyxd/CTFs/assets/144260597/10bbf30d-dccf-46be-9908-ba869fe5d17d)
Here we go. kxctf{th1s_1s_v3ry_s1mpL3_path_trav3rsal}
![image](https://github.com/danzyxd/CTFs/assets/144260597/167ee4ec-3648-433b-9c07-2ffe65af03d8)
