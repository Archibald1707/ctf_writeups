# TCP1P CTF

## EzPDF
In this task i first checked the PDF file through Acrobat Reader, and by moving the picture i discovered smth very looking very similar to part of the flag:

`_0N_pdf_f1L35_15_345y`

Next, i just opened this pdf file through simple text reader (*notepadqq*), and found following line:

`/Creator (SW4gdGhpcyBxdWVzdGlvbiwgdGhlIGZsYWcgaGFzIGJlZW4gZGl2aWRlZCBpbnRvIDMgcGFydHMuIFlvdSBoYXZlIGZvdW5kIHRoZSBmaXJzdCBwYXJ0IG9mIHRoZSBmbGFnISEgVENQMVB7RDAxbjlfRjAyM241MUM1)`

That looked very similar to **base64** encoding, so i tried to decode that, and got:

`In this question, the flag has been divided into 3 parts. You have found the first part of the flag!! TCP1P{D01n9_F023n51C5`

Great! So we've got 2 parts of 3 parts of the flag. Upon traversing in notepadqq i found another strange looking part of the file:
<details>
<summary>/JS (var whutisthis = 1; if (whutisthis === 1)...</summary>
/JS (var whutisthis = 1; if (whutisthis === 1) { this.print({bUI:true,bSilent:false,bShrinkToFit:true}); } else { function _0x510a(_0x4c8c49,_0x29ea76){var _0x5934bd=_0x5934();return _0x510a=function(_0x510a0b,_0x1b87bb){_0x510a0b=_0x510a0b-0x174;var _0x6c8a33=_0x5934bd[_0x510a0b];return _0x6c8a33;},_0x510a(_0x4c8c49,_0x29ea76);}(function(_0x39f268,_0x3518a2){var _0x43b398=_0x510a,_0x1759ee=_0x39f268();while(!![]){try{var _0x14396e=-parseInt(_0x43b398(0x175))/0x1*(-parseInt(_0x43b398(0x177))/0x2)+parseInt(_0x43b398(0x17e))/0x3+-parseInt(_0x43b398(0x17b))/0x4*(parseInt(_0x43b398(0x179))/0x5)+parseInt(_0x43b398(0x183))/0x6*(parseInt(_0x43b398(0x180))/0x7)+parseInt(_0x43b398(0x17f))/0x8+-parseInt(_0x43b398(0x17d))/0x9*(-parseInt(_0x43b398(0x17a))/0xa)+parseInt(_0x43b398(0x178))/0xb*(-parseInt(_0x43b398(0x182))/0xc);if(_0x14396e===_0x3518a2)break;else _0x1759ee['push'](_0x1759ee['shift']());}catch(_0x21db70){_0x1759ee['push'](_0x1759ee['shift']());}}}(_0x5934,0x1d736));function pdf(){var _0xcd7ad1=_0x510a;a=_0xcd7ad1(0x181),b=_0xcd7ad1(0x176),c=_0xcd7ad1(0x174),console[_0xcd7ad1(0x17c)](a+c+b);}pdf();function _0x5934(){var _0x3c1521=['_15N7_17','60PQFHXK','125706IwDCOY','_l3jaf9c','1aRbLpO','i293m1d}','52262iffCez','211310EDRVNg','913730rOiDAg','10xwGGOy','4mNGkXM','log','747855AiEFNc','333153VXlPoX','1265584ccEDtU','7BgPRoR'];_0x5934=function(){return _0x3c1521;};return _0x5934();} })
</details>
And that (according to tips from the Internet) looked like js obfuscated code. Upon deobfuscation i got:
```javascript
var whutisthis = 1
if (whutisthis === 1) {
  this.print({
    bUI: true,
    bSilent: false,
    bShrinkToFit: true,
  })
} else {
  function pdf() {
    a = '_15N7_17'
    b = 'i293m1d}'
    c = '_l3jaf9c'
    console.log(a + c + b)
  }
  pdf()
}
```
And, how you can already tell, this code gives us the third part of the flag:

`'_15N7_17_l3jaf9ci293m1d}`

So, the final flag will look like:

`TCP1P{D01n9_F023n51C5_0N_pdf_f1L35_15_345y_15N7_17_l3jaf9ci293m1d}`

## zipzipzip
This task consisted of the file zip-25000.zip and the password password.txt. After using the unzip command, it became clear that this is a nesting doll of 25000 zip files folded into each other, and with a password. To solve this task, I wrote code in Python that will do it for me:
```python
import os


zip_number=25000
cmd1 = "find . -name '*.zip' -exec unzip -o -P "
cmd2 = " {} \; -exec rm {} \;"


file = open("password.txt", "r")
pswd = (file.read()).strip()
file.close()

for i in range(1, zip_number):
	print('readed pswd number', i, ' - ', pswd)
	
	os.system(cmd1 + pswd + cmd2)
	
	file = open("password.txt", "r")
	pswd = (file.read()).strip()
	file.close()
	
	print('done for: ', i)
```

And in file named zip-1.zip we found file named flag.txt.

Flag: `TCP1P{1_TH1NK_U_G00D_4T_SCR1PT1N9_botanbell_1s_h3r3^_^}`

## Sanity Check
This task had a link to events discord server. Upon searching the flag, i found it in the bot's description.\
Flag: `TCP1P{Welcome To TCP1P Server}`


## Guess My Number
ELF file

## Bluffer Overflow
Simple buffer overflow

## Links
[Participation certificate](https://github.com/Archibald1707/ctf_writeups/edit/master/certificate.pdf)
