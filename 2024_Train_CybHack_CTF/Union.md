# Union
Web | 200 points
# Description
Вот тебе таск посложнее! http://158.160.35.89:1234/login <br />
zip file is given.
# Solution
Let's again try to login as an admin.

![image](https://github.com/danzyxd/CTFs/assets/144260597/d2205728-47c6-49ac-a231-fed9026baef5)

That didn't work, so we have to register an account.

![image](https://github.com/danzyxd/CTFs/assets/144260597/f3719621-3019-4991-b767-c36d7cc2b8eb)
 
 We logged in and there we see a simple website with your notes.

 ![image](https://github.com/danzyxd/CTFs/assets/144260597/d1b219c2-2690-4948-b714-85fb78c6d74f) <br />
 ![image](https://github.com/danzyxd/CTFs/assets/144260597/533eaa44-3c08-4f83-ac89-aeae8be16e26)

By the name of the task we can assume that there is may be an union based SQl injection. So let's check it. We typed " ' order by 1-- " and it worked, now we need to know how many columns is there by rising "order by" number till website will show us an error. <br />
So at the " 'order by 4--" site showed us an error which means that there's 3 column's. Now we have to know what can we get from the server by that.

![image](https://github.com/danzyxd/CTFs/assets/144260597/7f710f5e-17da-4f91-b41f-c866c418deb5)

In the union.zip\union-based-ctf-task\web we can see the main.py file let's take a look at it. But there's no any functions that works with SQL, so keep up searching other .py files. Going by this path union.zip\union-based-ctf-task\web\database will show us an postgres.py file that contains SQL requests. <br />
By looking at the code we can find a function that creates a "username" and "password" column's and insert them into "users" base. By looking a little more we will find another function that creates a "user_id", "title", "message" and "time" columns and inserts them into "notes" base. So let's try to get them.

![image](https://github.com/danzyxd/CTFs/assets/144260597/ba2d490a-c0e2-4aa6-89e6-c486ce02a316)
![image](https://github.com/danzyxd/CTFs/assets/144260597/86de5020-c943-411a-9304-dfc44bcd4bbd)

By typing "' union select username, password, '01.01.2000' from users--" in the websites searching string we will get all users usernames and passwords and among them we can find admins password. kxctf{un10n_b4s3d_sql1_4r3_v3ry_34sy}

![image](https://github.com/danzyxd/CTFs/assets/144260597/dfe4c799-c937-48f8-a542-69d14fceae1d)

![image](https://github.com/danzyxd/CTFs/assets/144260597/f0a4eace-eb43-4676-9c02-09886be93817)
