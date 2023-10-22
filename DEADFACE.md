# DEADFACE CTF
I took part in this CTF too late, so if i exclude trivial tasks, i was able to solve these challenges.

## Letter Soup

In this challenge we were presented with the crossword. After solving it,

![letter_soup_0](https://github.com/Archibald1707/ctf_writeups/blob/master/img/letter_soup_0.png)

and combining all remained letters to a single string, we got this:

`NVAVAOLSHZASPULMVYAOLMSHNHUZDLYAOHANVLZPUZPKLAOLIYHJRLAZZAVWNQWKDDEVWZLZTJNTHXSKEADVUCBVTRKLHSWEEBGBDTHHZAOLFMSFHJYVZZ`

Although it is not visible in the picture, the original picture contained a photo of an ancient person, who turned out to be Caesar. So I tried decoding this string with a Caesar cipher, and got:

`GOTOTHELASTLINEFORTHEFLAGANSWERTHATGOESINSIDETHEBRACKETSSTOPGJPDWWXOPSESMCGMAQLDXTWONVUOMKDEALPXXUZUWMAASTHEYFLYACROSS`

And as decoded text told if we decode only the last line from crossword, we get:

`ASTHEYFLYACROSS`

Great! Flag: `flag{ASTHEYFLYACROSS}`

## HamJam

In this challenge we were presented with **wav** file and were told to lookup their forum to find the encoded message. So, upon traversing their forum, i found this [post](https://ghosttown.deadface.io/t/rendezvous-lets-goooooo/127), where i found following image:

![hamjam_0](https://github.com/Archibald1707/ctf_writeups/blob/master/img/hamjam_0.png)

which appears to be barcode of **type**: *Codablock-F*. After decoding it we got:

`YEOOFIIGEHRJBMTJYYUSKPMOIK`

Next, i looked over to wav file. After hearing it *BLIP-BLOP* sounds it was obvious that it was morse encoded message. After decoding it we got:

`THEKEYISHACKTHEPLANET`

So, we got the key: `HACKTHEPLANET` and encoded message `YEOOFIIGEHRJBMTJYYUSKPMOIK`. Most commonly used cipher with key encoding in CTF challenges are AES and Vigenere. First, i tried Vigenere cipher since it is easier, and got the answer!

`REMEMBERTHEFIFTHOFNOVEMBER`

In challenge description was flag example, so the final flag will look like this:

FLag: `flag{NOVEMBER-5}`

## Syncopated Beat

In this challenge we were presented with 2 audio files. When we looked on the first one in Sonic Visualiser, we could see strange fragment:

![syncopated_beat_0](https://github.com/Archibald1707/ctf_writeups/blob/master/img/syncopated_beat_0.png)

When listening to it, unintelligible words were heard, and so I tried to reverse this fragment, I heard the following message:

`...You need to get the stego programm, used by Eliot in Mr.Robot, and use it on the audio file linked in the challenge. The password is the name of new CTO of Evil corp. All caps, no spaces...`

So, i googled that programm, and found out it was **DeepSound** that lets us hide files in audio files. Since the 2nd CTO of E corp from Mr.Robot was **Tyrell Wellick**, we tried opening second audio file in DeepSound with password **TYRELLWELLICK** and we get the image with the flag written on it.

Flag: `flag{Lookout_COVID_BATZ!!!}` *on an Ozzy Osbourne picture XD*