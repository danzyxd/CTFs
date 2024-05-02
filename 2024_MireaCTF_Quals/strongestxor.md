# StrongestXor
crypto | ~350 points
# Description
Ты сильнейшее шифрование, потому что у тебя ключ 8 байт, или у тебя ключ 8 байт, потому что ты сильнейшее шифрование?

png file is given
# Solution
We cant open a picture because its broken, so we need a 8 byte key to xor a file.
By reading about PNG file on wiki we can findout what it was a hex file header which is exactly 8 bytes.

![image](https://github.com/danzyxd/CTFs/assets/144260597/4f727145-2c88-454e-b4ab-bbcafe8d53fd)

We can XOR a file with that 8 bytes (\x89\x50\x4E\x47\x0D\x0A\x1A\x0A) and the first 8 bytes of XORed file will be a key.
All we have to do now is to decrypt a file with a found key.

![image](https://github.com/danzyxd/CTFs/assets/144260597/88a2a849-46d5-4d51-a4c5-60213b0bd3e4)
![new](https://github.com/danzyxd/CTFs/assets/144260597/51f71362-2f23-4b7f-83ee-a95397b3e37d)
