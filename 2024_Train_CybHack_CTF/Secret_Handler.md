# Secret Handler
Web | 200 point
# Description
Сможешь найти секретный функционал? <br />
http://158.160.35.89:1717/login
# Solution
CTFs organitazors gave a big hint in their telegram post.

Directory fuzzing <br />
Each of us has noticed that web applications work with so-called “hands”. For example, the /login route usually contains the login page, and the /profile route usually contains the user information page. As part of penetration testing, it is often useful to have a list of all available handles to better understand how the site works. Directory fuzzing and utilities such as ffuf (https://www.freecodecamp.org/news/how-to-fuzz-hidden-directories-files-with-ffuf/), gobuster (https://hackertarget.com/gobuster-tutorial/) or dirsearch (https://www.kalilinux.in/2023/03/dirsearch.html) can help us with this, which search according to dictionaries of well-known and most popular routes
To make it easier for you to get acquainted with this technology, we have prepared a task on our platform. Try to solve it with all the tools and figure out which one you like better.

Link send us to a usual website, so, as the creaters said, we need to read about a few fuzzing programs and download them.  

![image](https://github.com/danzyxd/CTFs/assets/144260597/52fc3fa3-3e30-4fbf-b4a4-e1102021f2b0)

While i was waiting till the programs will download, I accidentally found the flag by writing http://158.160.35.89:1717/secret into the URL.

![image](https://github.com/danzyxd/CTFs/assets/144260597/a71de9f2-a96e-43a9-8141-f9449adf60ea)

kxctf{h3110_fr0m_th3_s3cr3t_h4nd13r}
