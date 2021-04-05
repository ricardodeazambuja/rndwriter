# rndwriter
Write random data to random positions

This program is for when you are in a rush, you already used shred on this file / disk (you think), so you don't have time to write random stuff on ALL the file / disk again. It defaults to 30% of your disk will be randomly written with random data.
**USE IT AT YOUR OWN RISK!!!**

How to install:  
```
$ pip install git+git://github.com/ricardodeazambuja/rndwriter --upgrade
```


How to use (it will ask you your password because `dd` needs `sudo` for drives):  
```
$ rndwriter <file_you_want_to_write_random_stuff>
```

```
$ rndwriter /dev/<drive_you_want_to_write_random_stuff>
```