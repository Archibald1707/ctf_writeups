# Questcon CTF
A little CTF for newbies, i enjoed it. The one thing i'll mention - forensic chals weren't so fun, so i just ignored them.

## Sparrow's Cryptographic Treasure

In this challenge we are presented with txt file that contains this:

```
N = 882564595536224140639625987659416029426239230804614613279163
E = 65537
C = 164269225538436495685306542268826436068505673594249194166792
```

It was pretty obvious that it was RSA encrypted text, so i solved it using [factordb](http://factordb.com/) and the new resourse i found for such challenges, named [RSA calculator](https://www.tausquared.net/pages/ctf/rsa.html), as you can see in the picture below.

![sparrows_crypto_treasure](https://github.com/Archibald1707/ctf_writeups/blob/master/img/sparrows_crypto_treasure.png)

## Web Explorer's Journey

When we enter the site we can see this:

![web_explorers_journey](https://github.com/Archibald1707/ctf_writeups/blob/master/img/web_explorers_journey.png)

Digging further, in raw  html view i found another flag which was `81856983846779781238751669551888076488251829549839552875183487751125`. Then, proceeding to look for clues, in sources i found script.js

###### **`script.js`**
```js
let flag = "flag{Test_Flag}";
let encryptedFlag = "";
function encodeFlag() {
  for (let i = 0; i < flag.length; i++) {
    encryptedFlag += flag.charCodeAt(i);
  }
}

encodeFlag();
document.getElementById("flag").innerHTML = encryptedFlag;
```
, that tells us:
1. how to decode flag
2. that the flag, showing on the page, is the test flag

So, upon trying decode real one , *with simple python script*, we get it.
flag: `QUESTCON{W3B_3XPL0R3R_1S_4W3S0M3}`

## Mystery

In this challenge we are presented with this picture:

![pirate.jpg](https://github.com/Archibald1707/ctf_writeups/blob/master/img/pirate.jpg)

So, to start things off, i tried using stegsolve, but didn’t find anything. So, since this is a jpg file  i tried using steghide, that provided me with a file that contained a suspicious line:

```����JFIF���ExifMM*>FL�iRHackerAlertAlert�0230��0100� )�UVVFU1RDT057TXk1dDNyeV8xc180dzNzMG1lIX0=��C        ''#*" "*#>1++1>H<9<HWNNWmhm�����hh�����D�gWvK�`�[�:���Z�̀[dj�}�ʺ���ֱ����kl���r���ڀo}1α@t��/```

And in particular, this part: `UVVFU1RDT057TXk1dDNyeV8xc180dzNzMG1lIX0=`, that lookes remotely similar to base64 encoding. Upon decoding it we get the flag.

Flag: `QUESTCON{My5t3ry_1s_4w3s0me!}`

## Mystery 2.0

Here, we are presented with:

![another_mystery.jpg](https://github.com/Archibald1707/ctf_writeups/blob/master/img/another_mystery.png)

i tried using
* strings with grep
* stegsolve
* exiftool
* pngcheck
* Steganographic Decoder (futureboy)

and none of them gave any results.So, then tried using zsteg, which gave this:

```bash
[archibald@hostbomb Downloads]$ zsteg -a another_mystery.png
b1,g,lsb,xy         .. file: OpenPGP Public Key
b1,abgr,msb,xy      .. text: "}wwwwwww;"
b2,r,lsb,xy         .. text: "Y?*[*LkB"
b2,g,lsb,xy         .. text: "EAUUUUUUUU"
b2,b,msb,xy         .. text: "jUUv}VU}%c"
b2,rgba,lsb,xy      .. text: "QUESTCON{P1raT3s_Ar3_M7s!3rY}\n"
b2,abgr,msb,xy      .. text: "KKKKGOOO"
```

Flag: `QUESTCON{P1raT3s_Ar3_M7s!3rY}`

## Pirate's Port Paradox

This challenge gives us this string:

`((((WHOIS + QOTD) * CHARGEN) - XFER) % ECHO) * (DCE + NNTP) * NSCA`

So it seems we need to get port numbers of this protocols. After googling them for a couple of minutes and pasting them in python

###### **`port_solve.py`**
```python
WHOIS = 43
QOTD = 17
CHARGEN = 19
XFER = 82
ECHO = 7
DCE = 135
NNTP = 119
NSCA = 5667

print(((((WHOIS + QOTD) * CHARGEN) - XFER) % ECHO) * (DCE + NNTP) * NSCA)
```

, we get following number: `1439418`. And after wrapping it we get the flag.

Flag: QUESTCON{1439418}

## Hexa Pirate's Code

In this task we are given an archive with many (*1000+*) files. Names of the files are hex strings. We get no correct decryption when trying to decode them from hex, so i tried traversing files for a little bit.

Firstly i found file named 843r93iedmsklnu3209e3dfmksmcklds since length of that file's name (*32 characters*) was shorter than others (*64 characters*). inside we found:

`QUESTCON{djsciodjdkodsk;l,c}`

i had no idea how to decode it, so i moved on, trying to find any clues. After a while i found file named:

`cc53495bb42e4f6563b68cdbdd5e4c2a9119b498b488f53c0f281d751a368f19.save`

which had .save on end in contrast to the other filenames. That file also had a pair, named exactly the same excluding that .save part. Upon opening .save file we get [savefile](https://github.com/Archibald1707/ctf_writeups/blob/master/img/additional_content/savefile.txt), which seems to be a description of accessing the database with a request string `""+"6f777d-0000-0000-000000000000"`

Then i checked pair to that file, where i found 2nd string `"5155455354434f4e7b426c34636b42333472645f4d616c773472335f50697234"+"7433737d-0000-0000-000000000000"`, that decodes as:

Flag: `QUESTCON{Bl4ckB34rd_Malw4r3_Pir4t3s}`

i still didn’t understand whether there were additional flags in this task, so i decided to move on to the next challenges, and take up this task again later

## Riddle of the Hidden Scrolls

Here we are presented with the following string:

```VUUEV2QGW364QGN3YE:MN16eUGMpaE:La2:VMDty`03>```

This one took a while for me, i was just blindly trying everything, untill i noticed something while trying to perform XOR bruteforce. i noticed that the result with the key = 03 looks like this:

`UVVFU1RDT057RDM0ZF9NM25fVDNsbF9Ob19UNGwzc30=`

And by now we all know what a **`=`** in the end of string means. So we try base64 decode and we finally get the flag! ~~*it took too long, send some help*~~

Flag: `QUESTCON{D34d_M3n_T3ll_No_T4l3s}`