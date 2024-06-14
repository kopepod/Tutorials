# Linux Specific Commands


1. CPU freq controller

```bash
sudo apt-get install indicator-cpufreq cpufrequtils
```

2. Wake on lan

```bash
sudo apt-get install wakeonlan 
wakeonlan -i 137.205.115.48 AC:9E:17:F0:A3:10
```

3. remove text of files

```bash
sed -i 's/opencv2/\/dcs\/pg13\/rleyva\/Public\/OCV\/include\/opencv2/g' *.cpp
```

```bash
find . -type f -exec sed -i 's/opencv2/\/dcs\/pg13\/rleyva\/Public\/OCV\/include\/opencv2/g'
```


4. ssh problems:

```bash
sudo ufw allow ssh
sudo service ssh start
sudo systemctl enable ssh
sudo systemctl enable sshd.service
```

5. gedit terminal

```bash
sudo apt-get install gedit-plugins dconf-tools
nano dconf-editor
```

org->gnome->gedit->plugins->terminal 

6. chmod only files

```
find . -name "*.md" -exec chmod -x {} \;
```


7. pause key
```bash
xmodmap -e "keycode 180 = Pause"
```

8. Rename several files

```bash
find -name "* *" -type f | rename 's/ /_/g'
find -name "* *" -type f | rename 's/\(|\[|\]|\)//g'
```

9. Rename folders
```bash
find -name "* *" -type d | rename 's/ /_/g'
```


10. Grep

```bash
grep -o -P '(?<=( #start#  )).*(?=( #end#  ))' file
```

11. Linux Additions Guest VM add shared drive
```bash
sudo apt-get install dkms
sudo bash ./VBoxLinuxAdditions.run
sudo adduser $USER vboxsf
```

12. Change user to access media && Permissons external drive

```bash
sudo chown <user>:<user> <path>
```

18. Change not to execute

```bash
chmod -x myfile
chmod 777 myfile
```

19. Check number of files inside folder
ls -1 | wc -l
N=$(ls -1 | wc -l)

20. Video Lenght FFMPEG
ffmpeg -i new.aac 2>&1 | grep "Duration"

21. Extract Audio
ffmpeg -i 0.mp4 -vn -ss 00:00:00 -t 00:00:30 -acodec aac new.aac

21. zip terminal no compression
zip -r -0 newfile.zip folder/

22. disk space
df -h

23. ffmpeg x264
conda install -c conda-forge x264
conda install -c conda-forge ffmpeg

24. Replace string in file
sed -e 's/@@@/#/g' FILE.sh > temp_exec.sh

24. Replace string in file and rewrite
sed -i 's/mp4/jpg/g' FILE.sh


sed -i "s/mylist.txt//g" mylist.txt 
sed -i "s/mp4/mp4'/g" mylist.txt 
sed -i "s/2018/file '2018/g" mylist.txt 


25. Replace string bash
firstString="I love Suzi and Marry"
secondString="Sara"
echo "${firstString/Suzi/$secondString}"

26. IDT opencv non free
sudo add-apt-repository --remove ppa:xqms/opencv-nonfree
sudo add-apt-repository --yes ppa:jeff250/opencv
sudo apt-get update
sudo apt-get install libopencv-dev
sudo apt-get install libopencv-nonfree-dev

27. pdfjoin pdfunite

pdfunite 

28. Apache

sudo apt install apache2 libapache2-mod-php mysql-server mysql-client php-mysql

sudo ufw app list
sudo ufw allow 'Apache'
sudo ufw status

sudo systemctl restart apache2

29. SQL
sudo apt-get install mysql-server
sudo ufw allow mysql
systemctl start mysql

sudo systemctl enable mysql

sudo mysql_secure_installation

mysql -u root -p

sudo mysql -u root # I had to use "sudo" since is new installation

mysql>

======

USE mysql;
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'pa55w0rd';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';
UPDATE user SET plugin='caching_sha2_password' WHERE User='newuser';
FLUSH PRIVILEGES;
exit;

mysql -u newuser -p

===

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'


$ sudo service mysql restart


30. Resize pdf image size
ps2pdf -dPDFSETTINGS=/ebook fullPa55.pdf 0.pdf

31. Pa55

ERROR 1698 (28000): Access denied for user 'root'@'localhost'


32. vectorise with inkscape

sudo add-apt-repository universe
sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt-get update
sudo apt install inkscape

pip install scour


Path -> Trace Bitmap Item

    Select the object(s) to export.
    Open the document properties window (Ctrl+Shift+D)
    Select "Resize page to drawing or selection"
    File > Save As Copy…
    Select Optimized SVG as the format if you want to use it on the web.

Path BREAK APART

Path/Exclusion

inkscape -D colab.svg  -o colab.pdf 


33. VLC screeshoot path

34. Compile LaTeX Biber / bibtex

Compile with Biber

Options > Configure Maker > Commands > Bib(la)tex :

# Set 

biber %

# Put it back

bibtex %.aux

You can set the output directory from Preferences -> Video -> Video Snapshots to "." (a simple dot without quotes). Then save, exit and restart VLC.

35. Split zip file
```bash
zip -0 -s 1700M STB_UCF101.zip UCF101_BIDT_MBH.mat

echo "-n in bytes, below is 1MB"
zipsplit -n 1048576 archive.zip




```

36. find text in subfiles and replace

```bash
grep -iRl "theft" ./

grep -irlw "theft" ./

grep -wr "tick" --include "*.py"

find ./ -type f -exec sed -i 's/old_string/new_string/g' {} \;

```

37. warwick mount drive
sudo mkfs -t ext4 /dev/sda1
sudo chown rleyva:rleyva /media/tb18/

# after ready 
sudo mount /dev/sda1 /media/tb18/

38. Create sudo user create user

```bash
sudo adduser yuqi
sudo passwd yuqi

sudo usermod -aG sudo yuqi

echo "add folders access"
setfacl -R -m u:rob_run:rwx /mnt/GB480/

```

39. Copy specific file extension keeping structure

```bash
find . -name \*.py -exec cp --parents  {} /media/u53r/64GB/MediaEval/ \;
```

only files

```bash
find . -name \*.JPEG -exec cp {} ./Real_ILSVRC \;
```

40. Disable VM keyboard
xinput set-int-prop 11 "Device Enabled" 8 0;
xinput set-int-prop 11 "Device Enabled" 8 1;

41. Download audio from youtube
* List the formats
youtube-dl -F https://www.youtube.com/watch?v=lE_9u7sTiyw
* Download only the desired format
youtube-dl  https://www.youtube.com/watch?v=lE_9u7sTiyw -f 140

42. Terminator geometry
terminator --geometry=960x640

43. New USB permisons

sudo chown u53r:u53r /media/u53r/64GB/

44. update youtube-dl
pip install --upgrade youtube-dl

45. default python3 first line of file
nano ~/.bashrc
alias python=python3
source ~/.bashrc

sudo apt install python-is-python3

46. Copy files with folder name
find * -path "archive" -prune -o -type f -exec bash -c 'IN=${1};IN=(${IN//_/ }); cp "$1" "${IN}"' find_bash '{}' \;

47. list all urls on page
lynx -dump https://www.linkedin.com/feed/update/urn:li:activity:6646389624849727488

48. Remove all small files
find . -name "*.tif" -type 'f' -size -160k -delete
find -name '*.jpg' -size 0 -delete

49. HFS MAC disk problem

sudo mount -t hfsplus -o remount,force,rw /dev/sdc2 /media/u53r/G-DRIVE\ USB/

sudo chown u53r:u53r /media/u53r/G-DRIVE\ USB/

50. Rename part of the file name

rename 's/ABC/XYZ/' *.csv

51. vp9 libvpx

conda install -c anaconda libvpx

52. move into subfolders
```bash
for i in `seq 1 10`; do mkdir -p "Sub_folder_$i"; find . -type f -maxdepth 1 | head -n 10000 | xargs -i mv "{}" "Sub_folder_$i"; done

```


53. log file from shell execution

exec > logfile.txt

54. pytorch path

WARNING: The scripts f2py, f2py3 and f2py3.8 are installed in '/home/kldf848/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts convert-caffe2-to-onnx and convert-onnx-to-caffe2 are installed in '/home/kldf848/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

gedit ~/.bashrc 
export PYTHONPATH="${PYTHONPATH}:/home/kldf848/.local/bin"
source ~/.bashrc

55. python3 is python2

sudo apt install python-is-python3

56. i7 overclocking processor
sudo apt-get install i7z
sudo i7z

57. pdfunite

pdfunite ET_* new.pdf

58. suspend
sleep 3600;systemctl suspend

59. Monday first date

sudo gedit /etc/default/locale

LANG="en_US.UTF-8"
LC_TIME="en_GB.UTF-8"
LC_PAPER="en_GB.UTF-8"
LC_MEASUREMENT="en_GB.UTF-8"

60. copy folders only not files
cd /path/to/directories &&
find . -type d -exec mkdir -p -- /path/to/backup/{} \;

61. find and execute command
find . -name \*.wav -exec ffmpeg -i "{}" -q 5 -acodec libmp3lame "{}.mp3"  \;

62. Leave open ssh running a program

nohup python3.7 myfile.py & exit

63. Find all href

sed -n 's/.*href="\([^"]*\).*/\1/p' page.html

64. chrome no snap
sudo apt remove chromium-browser chromium-browser-l10n chromium-codecs-ffmpeg-extra
sudo add-apt-repository ppa:saiarcot895/chromium-beta
sudo apt-get update && sudo apt-get install chromium-browser


65. find string in files

grep -inr --include \*.py  '512' --color='auto'

grep 'Enrique'  *.txt



66. cam recorder

sudo apt install guvcview

68. desktop screen recorder

sudo apt install kazam

69. firefox night

sudo add-apt-repository ppa:ubuntu-mozilla-daily/ppa -y
sudo apt update && sudo apt install firefox-trunk

70. change date start day
to GB

sudo gedit /etc/default/locale

LANG="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"


71. R studio

curve(x^3-x^2+x-5, from=-10, to=10, , xlab="x", ylab="y")
curve(x^3-9*x^2+24*x, from=0, to=6, , xlab="x", ylab="y")

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
sudo apt update
sudo apt install r-base
sudo apt install  gdebi-core
sudo gdebi rstudio-1.4.1717-amd64.deb 


72. terminator --geometry 960x640

75. Add more space windows

a.
VBoxManage modifyhd YOUR_HARD_DISK.vdi --resize SIZE_IN_MB

b. 

To access it, click File -> Virtual Media Manager ...

Windows: Disk Management

Second click
Extend Volume ...

76. IDLE python

sudo apt-get install idle3

77. pdf search 

pdfgrep -R 'a pattern to search recursively from path' /some/path

78. samba

sudo nano /etc/samba/smb.conf

>>>>>>>>>>>>>>>>>>>>>>>>>
[global]
workgroup = HOME
server string = Linux Lite Shares
netbios name = linux
security = user
username map = /etc/samba/smbusers
map to guest = bad user
guest account = nobody
dns proxy = no
local master = yes
preferred master = yes
#======================= Share Definitions ===================================
[liteshare]
comment = Samba on Ubuntu
path = /mnt/TB1/liteshare
available = yes
valid users = %U %G tub687
write list = %U
browsable = yes
public = no
writable = yes
guest ok = no
read only = no
printable = no
locking = no
strict locking = no
force user = ip75f
>>>>>>>>>>>>>>>>>>>>>>>>


sudo service smbd restart
sudo adduser <other_user>  
sudo smbpasswd -a <other_user>

chown -R <user_me> /mnt/TB1/liteshare

79. pdf rotate

qpdf in.pdf out.pdf --rotate=[+|-]angle[:page-range].


80. replace with sed variable string

s1=Patil
s2=2015PatilSonali

echo "$s1 --> $s2"

sed -i "s/$s1/$s2/g" /mnt/TB1/liteshare/Report/Main.tex

sed -i "s/$s1/$s2/g" /mnt/TB1/liteshare/Report/DATA/FIGS/FIG_threatgroups.tex

sed -i "s/$s1/$s2/g" /mnt/TB1/liteshare/Report/DATA/refs.bib

81. Fonts install

https://askubuntu.com/questions/18357/how-to-install-otf-fonts

cp Gulliver.otf /usr/share/fonts/opentype/
sudo cp Gulliver.otf /usr/share/fonts/opentype/
sudo fc-cache -f -v

83. remove text pdf

qpdf --stream-data=uncompress IN.pdf unc.pdf
sed 's/University\ of\ Warwick/ThreeLittlePigs/g' < unc.pdf > mod_unc.pdf
sed 's/January\ 19,2022\ at\ 19:50:41/Date/g' < mod_unc.pdf > mod_unc_2.pdf

84. copy / move all files of particular extension

find . -name \*.jpg -exec cp {} /mnt/TB1/Documents/CHAYITO/Galaxy_A01/FOTOS \;

find . -name \*G421.avi -exec cp -v {} ~/Downloads/MEVA_G420/ \;

85. spyder3

sudo apt install spyder3

86. change mozilla firefox default tmp

https://superuser.com/questions/506367/change-the-tmp-folder-of-firefox

87. Linux run process background

gedit &

88. error 

How can I fix a 404 Error when using a PPA or updating my package lists?

https://askubuntu.com/questions/65911/how-can-i-fix-a-404-error-when-using-a-ppa-or-updating-my-package-lists

/etc/apt/sources.list

89. remote xgo server

```bash
sudo apt-get install x2goserver x2goserver-xsession

sudo apt install xfce4
```

90. run remote ssh closing the connection

https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session

nohup long-running-command &

91. grep history

history | grep conda --color

92. find all files in a directory

find . -name \*.png -exec echo "{}" \;

93. Android - requires virtualization not meant for VM

sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386

sudo apt install snapd

sudo snap install androidsdk

androidsdk "platform-tools" "platforms;android-28"

sudo snap install android-studio --classic

93. Miniconda

bash Miniconda

yes to init


94. concatenate files

```bash
cat *csv > combined.csv
```

95. keep unique strings

sort url.txt | uniq

96. keep what is after matching a pattern

grep  "pattern" Page.html | cut -d\   -f2 > url


96. kotlin shell
https://kotlinlang.org/docs/command-line.html#sdkman

sudo snap install --classic kotlin

kotlinc hello.kt -include-runtime -d hello.jar

java -jar hello.jar

kotlinc-jvm

97. google pub key


http://dl.google.com/linux/chrome/deb stable InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY

wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

98. list folder size

du -sh *

du -sh * .[^.]*

99. Samsung Screen

https://forums.linuxmint.com/viewtopic.php?t=339672

sudo gedit /etc/default/grub

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash video=HDMI-A-1:e"

sudo update-grub

> Set display at 30Hz

100. key error repos

Key is stored in legacy trusted.gpg 

W: http://linux.dropbox.com/ubuntu/dists/disco/Release.gpg: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.

sudo apt-key list

take the last 8 numbers of the public key, i.e., 5044912E

pub   rsa2048 2010-02-11 [SC]
      1C61 A265 6FB5 7B7E 4DE0  F4C1 FC91 8B33 5044 912E
uid           [ unknown] Dropbox Automatic Signing Key <linux@dropbox.com>


sudo apt-key export 5044912E | sudo gpg --dearmour -o /etc/apt/trusted.gpg

replace

add the repostory new key

sudo gedit /etc/apt/sources.list.d/dropbox.list

deb [arch=amd64 signed-by=/etc/apt/trusted.gpg] http://linux.dropbox.com/ubuntu/dists/disco stable main

101. add process at the beggining, run command at start

crontab -e

@reboot [part to shell script]

```bash
@reboot sleep 10 && /usr/sbin/ifconfig > /home/rob/Dropbox/prosage_address.txt
@hourly /usr/sbin/ifconfig > /home/rob/Dropbox/prosage_address.txt
```

102. cmake

```bash
sudo apt-get install build-essential libssl-dev cmake
cmake --version

```

103. Rename as counter

ls -v | cat -n | while read n f; do mv -n "$f" "$n.jpeg"; done

104. crate directories recursively

mkdir -p 

105. grep watch videos youtube

grep "watch" file.txt

106. Use sudo with password as parameter

[https://stackoverflow.com/questions/11955298/use-sudo-with-password-as-parameter]

sudo chmod +s myscript

107. youtube download issues

```bash
pip install yt-dlp
```

108. encrypt file

```bash
gpg -c filename

gpg filename.gpg
 
```

104. Mathematica font error

https://askubuntu.com/questions/1140921/wolfram-mathematica-after-upgrade-to-ubuntu-19-04-symbol-lookup-error-usr-lib

https://support.wolfram.com/12406


105. F5 VPN chrome xdg-open

Open F5 VPN from whisker menu first
Login and lauch from chrome


106. convert png to jpg

for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done

107. sed split, select odd lines, prepend string and insert new first line, 

```bash
sed 's/seed/\n/g' FakesSGAN2.csv > New.csv
sed -n 'n;p' New.csv > New2.csv
sed -e 's/^/seed/' $line New2.csv > New3.csv
sed  -i '1i File' New3.csv
```

108. unzip to directory
```bash
unzip -q file.zip -d /DIR 
```

109. for list
```bash
for i in {1..25};
do
	echo "$i";
done
```

110. URL from youtube

```bash
echo "remove blank spaces"

sed -i -e 's/^ *//g' File.html

echo "remove duplicates"

sort File.html | uniq > runme.sh

echo "select only those with watch"

sed  -i -e '/watch?v=/!d' runme.sh

echo "select only those without &pp= &list &t="

sed -i -e '/&pp=/d' runme.sh

sed -i -e '/&list/d' runme.sh

sed -i -e '/&t=/d' runme.sh

echo "insert yt-dlp command"

sed -i -e 's/</yt-dlp /g' runme.sh

sed -i -e 's/>//g' runme.sh

echo "insert sleep"

sed -i -e 's/>//g' runme.sh



```

111. edit GRUB boot parameters

# https://wiki.ubuntu.com/Kernel/KernelBootParameters
# https://askubuntu.com/questions/19486/how-do-i-add-a-kernel-boot-parameter
# https://www.kernel.org/doc/html/v4.14/admin-guide/kernel-parameters.html

```bash
sudo nano /etc/default/grub
```
```bash
pci=nommconf
pcie_aspm=off
acpi=off
pcie_ports=native

pcie_pme=nomsi

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash foo=bar"

GRUB_CMDLINE_LINUX_DEFAULT="pci=nobios pcie_ports=native"

```

112. Set display

```bash
xrandr --output DP1 --same-as LVDS1

xrandr --output DVI-D-1 --same-as DP-1

xrandr --fb 1920x1080 --output DP-1 --mode 1680x1050 --scale-from 1920x1080 --output DVI-D-1 --mode 1920x1080 --scale 1x1 --same-as DP-1

```

113. transparency

```bash
transset -p --dec 0.05
```

114. kill process

How to force kill process in Linux

    Use the pidof command to find the process ID of a running program or app
    pidof appname
    To kill process in Linux with PID immediately:
    kill -9 pid
    Want to kill process in Linux with application name forcefully? Try:
    killall -9 appname
    You can sent -15 (SIGTERM) signal to process requesting it to terminate gracefully:
    killall -15 your-app-name
    AND
    kill -15 pid



# debian
sudo update-grub

# fedora
sudo grub2-mkconfig -o /etc/grub2.cfg


```bash

sudo mkfs.ext4 /dev/sdb
sudo mount -t ext4 /dev/sdb  /mnt/TB0/


##### Ubuntu Tablet
1. Remove amazon
sudo apt purge ubuntu-web-launchers

2. Wireless
sudo cp brcmfcam43455-sdio.txt /lib/firmware/brcm/

####### Raspberry 3

1. PI OS Lite

download:

2021-01-11-raspios-buster-armhf-lite.zip
balena-etcher-elctron_1.5.116_amd64.deb

run etcher move zip to SD card

move ssh file into boot unit

user: pi
password: raspberry

change password immediately

psswd

2. Lubuntu install

* run balena Etcher from whisker menu

* select lubuntu-16.04-desktop-armhf-raspberry-pi.img.xz 

* flash the sd card

## dcs

sudo apt install libexo-1-0
sudo apt-get install -y xfce4-terminal












