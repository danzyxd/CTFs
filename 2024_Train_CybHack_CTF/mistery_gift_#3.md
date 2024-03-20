# mistery gift #3
200 point
# Description
Сможешь обойти эту проверку? http://158.160.35.89:5200/ <br />
zip file with the website directories is given.
# Solution
We see the same page as in "mistery gift #1" and "mistery gift #2" so let's just do the same things as before.

<img src="https://github.com/danzyxd/CTFs/assets/144260597/0f08f7f9-5c58-41b1-aae2-cf8cb9d99031" width=70% height=70%>

But typing "../flag.txt" gives us nothing, so let's just take a look at the zip file.

<img src="https://github.com/danzyxd/CTFs/assets/144260597/a11db32e-8a58-4ce3-8d59-7ecceaa639be" width=70% height=70%>

The first thing we see is of course the flag.txt file, but it is not a real flag, the real one lays on the server, so lets find the gift.jpg

<img src="https://github.com/danzyxd/CTFs/assets/144260597/bf36956b-a002-4828-9f10-73e0c308d49e" width=70% height=70%>

So we found a picture in the "uploads" folder. But going up by "../" to get a flag.txt didnt work. Let's check the main website code(app.py) file then.

<img src="https://github.com/danzyxd/CTFs/assets/144260597/5b57e218-231b-415b-8887-46af9ee7d2d9" width=70% height=70%>

