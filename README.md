# Password generator by rootshellace
A Python program that helps you generate a random password!

## Characters that can be used

You have the option to use in the generated password any combination
of uppercase characters, lowercase characters, numeric characters or
symbol characters. If you don't choose any and will press generate,
you will get a pop-up letting you know that you didn't select anything
and lowercase will be set as default option.

## Password length

There are 2 available length intervals but also the option to
choose a custom length between 4 and 50 characters. For those 2 
intervals, one of them offers the possibility to get a password 
between 8 and 12 characters and the other one a password between
13 and 16 characters. If you want a specific length, just choose
the custom option and type the length you want (make sure it is 
between 4 and 50).

## Troubleshooting

On some Linux distributions (e.g. Linux Mint), tkinter might not be installed by default.
This will generate an error when running the script.
Fortunately, this problem is easy to fix.
Just install it via the following command:
```bash
sudo apt-get install python3-tk
```

