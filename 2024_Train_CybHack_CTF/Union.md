# Union
200 points
# Description
Вот тебе таск посложнее! http://158.160.35.89:1234/login
# Solution
Let's again try to login as an admin.

![image](https://github.com/danzyxd/CTFs/assets/144260597/d2205728-47c6-49ac-a231-fed9026baef5)

That didn't work, so we have to register an account.

![image](https://github.com/danzyxd/CTFs/assets/144260597/f3719621-3019-4991-b767-c36d7cc2b8eb)
 
 We logged in and there we see a simple website with your notes.

 ![image](https://github.com/danzyxd/CTFs/assets/144260597/d1b219c2-2690-4948-b714-85fb78c6d74f) ![image](https://github.com/danzyxd/CTFs/assets/144260597/533eaa44-3c08-4f83-ac89-aeae8be16e26)

By the name of the task we can assume that there is may be an union based SQl injection. So let's check it. We typed " ' order by 1-- " and it worked, now we need to know how many columns is there by rising "order by" number till website will show us an error.
So at the " 'order by 4--" site showed us an error which means that there's 3 column's. Now we have to know what can we get from the server by that.

![image](https://github.com/danzyxd/CTFs/assets/144260597/7f710f5e-17da-4f91-b41f-c866c418deb5)

