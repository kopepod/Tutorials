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

13. Change not to execute

```bash
chmod -x myfile
chmod 777 myfile
```

14. Check number of files inside folder
```bash
ls -1 | wc -l
N=$(ls -1 | wc -l)
```

15. Video Lenght FFMPEG
```bash
ffmpeg -i new.aac 2>&1 | grep "Duration"
```

16. Extract Audio
```bash
ffmpeg -i 0.mp4 -vn -ss 00:00:00 -t 00:00:30 -acodec aac new.aac
```

17. zip terminal no compression
```bash
zip -r -0 newfile.zip folder/
```

18. disk space

```bash
df -h
```

19. Replace string in file
```bash
sed -e 's/@@@/#/g' FILE.sh > temp_exec.sh
```

20. Replace string in file and rewrite
```bash
sed -i 's/mp4/jpg/g' FILE.sh

sed -i "s/mylist.txt//g" mylist.txt 
sed -i "s/mp4/mp4'/g" mylist.txt 
sed -i "s/2018/file '2018/g" mylist.txt 
```


21. Replace string bash
```bash
firstString="I love Suzi and Marry"
secondString="Sara"
echo "${firstString/Suzi/$secondString}"
```

22. pdfjoin pdfunite
```bash
pdfunite 
```

23. Apache
```bash
sudo apt install apache2 libapache2-mod-php mysql-server mysql-client php-mysql

sudo ufw app list
sudo ufw allow 'Apache'
sudo ufw status

sudo systemctl restart apache2
```

24. SQL
```bash
sudo apt-get install mysql-server
sudo ufw allow mysql
systemctl start mysql

sudo systemctl enable mysql

sudo mysql_secure_installation

mysql -u root -p

sudo mysql -u root # I had to use "sudo" since is new installation
```

```bash
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

```

```bash
sudo service mysql restart
```


25. Resize pdf image size
```bash
ps2pdf -dPDFSETTINGS=/ebook <file.pdf> 0.pdf
```

27. vectorise with inkscape

```bash
sudo add-apt-repository universe
sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt-get update
sudo apt install inkscape

```

Path -> Trace Bitmap Item

    Select the object(s) to export.
    Open the document properties window (Ctrl+Shift+D)
    Select "Resize page to drawing or selection"
    File > Save As Copy…
    Select Optimized SVG as the format if you want to use it on the web.

Path BREAK APART

Path/Exclusion

```bash
inkscape -D colab.svg  -o colab.pdf 
```

28. Split zip file
```bash
zip -0 -s 1700M STB_UCF101.zip UCF101_BIDT_MBH.mat
echo "-n in bytes, below is 1MB"
zipsplit -n 1048576 archive.zip
```

29. find text in subfiles and replace

```bash
grep -iRl "theft" ./

grep -irlw "theft" ./

grep -wr "tick" --include "*.py"

find ./ -type f -exec sed -i 's/old_string/new_string/g' {} \;

```

30. Create sudo user create user

```bash
sudo adduser <user>
sudo passwd <user>

sudo usermod -aG sudo <user>

echo "add folders access"
setfacl -R -m u:<user>:rwx <path>

```

39. Copy specific file extension keeping structure, copy only first n files

```bash
find . -name \*.py -exec cp --parents  {} /media/u53r/64GB/MediaEval/ \;
```

only files

```bash
find . -name \*.JPEG -exec cp {} ./Real_ILSVRC \;
```

```bash
echo "Copy only 10 files"
find . -maxdepth 1 -type f | head -10 | xargs cp -t "$destdir"
```

40. Disable VM keyboard
```bash
xinput set-int-prop 11 "Device Enabled" 8 0;
xinput set-int-prop 11 "Device Enabled" 8 1;
```

41. Terminator geometry
terminator --geometry=960x640


42. Copy files with folder name
```bash
find * -path "archive" -prune -o -type f -exec bash -c 'IN=${1};IN=(${IN//_/ }); cp "$1" "${IN}"' find_bash '{}' \;
```

43. list all urls on page
```bash
lynx -dump https://www.linkedin.com/feed/update/urn:li:activity:6646389624849727488
```

44. Remove all small files
```bash
find . -name "*.tif" -type 'f' -size -160k -delete
find -name '*.jpg' -size 0 -delete
```

45. Rename part of the file name
```bash
rename 's/ABC/XYZ/' *.csv
```

46. move into subfolders
```bash
for i in `seq 1 10`; do mkdir -p "Sub_folder_$i"; find . -type f -maxdepth 1 | head -n 10000 | xargs -i mv "{}" "Sub_folder_$i"; done

```


47. pdfunite
```bash
pdfunite ET_* new.pdf
```

48. copy randomly from directory
```bash
find . -type f -name "*.JPEG" -print0 | head -50000 | xargs -0 shuf -e -n 8 -z | xargs -0 cp --parents -t <TargetPATH>
```

58. suspend
```bash
sleep 3600;systemctl suspend
```

59. Monday first date
```bash
sudo nano /etc/default/locale
```
```bash
LANG="en_US.UTF-8"
LC_TIME="en_GB.UTF-8"
LC_PAPER="en_GB.UTF-8"
LC_MEASUREMENT="en_GB.UTF-8"
```

60. copy folders only not files
```bash
cd /path/to/directories &&
find . -type d -exec mkdir -p -- /path/to/backup/{} \;
```

61. find and execute command
```bash
find . -name \*.wav -exec ffmpeg -i "{}" -q 5 -acodec libmp3lame "{}.mp3"  \;
```

62. Leave open ssh running a program
```bash
nohup python3.7 myfile.py & exit
```

63. Find all href
```bash
sed -n 's/.*href="\([^"]*\).*/\1/p' page.html
```

64. chrome no snap
```bash
sudo apt remove chromium-browser chromium-browser-l10n chromium-codecs-ffmpeg-extra
sudo add-apt-repository ppa:saiarcot895/chromium-beta
sudo apt-get update && sudo apt-get install chromium-browser
```


65. find string in files
```bash
grep -inr --include \*.py  '512' --color='auto'
grep 'Enrique'  *.txt
```

66. cam recorder
```bash
sudo apt install guvcview
```

67. desktop screen recorder

sudo apt install kazam

68. firefox night

sudo add-apt-repository ppa:ubuntu-mozilla-daily/ppa -y
sudo apt update && sudo apt install firefox-trunk

69. R studio
```bash
curve(x^3-x^2+x-5, from=-10, to=10, , xlab="x", ylab="y")
curve(x^3-9*x^2+24*x, from=0, to=6, , xlab="x", ylab="y")
```
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
sudo apt update
sudo apt install r-base
sudo apt install  gdebi-core
sudo gdebi rstudio-1.4.1717-amd64.deb 
```

70. pdf search 
```bash
pdfgrep -R 'a pattern to search recursively from path' /some/path
```

71. samba
```bash
sudo nano /etc/samba/smb.conf
```

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

```bash
sudo service smbd restart
sudo adduser <other_user>  
sudo smbpasswd -a <other_user>
```
```bash
chown -R <user_me> </path>
```

72. pdf rotate
```bash
qpdf in.pdf out.pdf --rotate=[+|-]angle[:page-range].
```


73. replace with sed variable string

```bash
s1=Patil
s2=2015PatilSonali

echo "$s1 --> $s2"

sed -i "s/$s1/$s2/g" /mnt/TB1/liteshare/Report/Main.tex

sed -i "s/$s1/$s2/g" /mnt/TB1/liteshare/Report/DATA/FIGS/FIG_threatgroups.tex

sed -i "s/$s1/$s2/g" /mnt/TB1/liteshare/Report/DATA/refs.bib
```

74. remove text pdf
```bash
qpdf --stream-data=uncompress IN.pdf unc.pdf
sed 's/University\ of\ Warwick/ThreeLittlePigs/g' < unc.pdf > mod_unc.pdf
sed 's/January\ 19,2022\ at\ 19:50:41/Date/g' < mod_unc.pdf > mod_unc_2.pdf
```

75. copy / move all files of particular extension
```bash
find . -name \*.jpg -exec cp {} <path> \;
find . -name \*G421.avi -exec cp -v {} <path> \;
```

76. remote xgo server

```bash
sudo apt-get install x2goserver x2goserver-xsession

sudo apt install xfce4
```

77. concatenate files

```bash
cat *csv > combined.csv
```

78. keep unique strings
```bash
sort url.txt | uniq
```

79. keep what is after matching a pattern
```bash
grep  "pattern" Page.html | cut -d\   -f2 > url
```


80. kotlin shell
https://kotlinlang.org/docs/command-line.html#sdkman

```bash
sudo snap install --classic kotlin

kotlinc hello.kt -include-runtime -d hello.jar

java -jar hello.jar

kotlinc-jvm
```

81. list folder size
```bash
du -sh *

du -sh * .[^.]*
```

82. add process at the beggining, run command at start

```bash
crontab -e
```bash
@reboot [part to shell script]

@reboot sleep 10 && /usr/sbin/ifconfig > <file>
@hourly /usr/sbin/ifconfig > <file>
```

83. cmake

```bash
sudo apt-get install build-essential libssl-dev cmake
cmake --version

```

84. Rename as a counter
```bash
ls -v | cat -n | while read n f; do mv -n "$f" "$n.jpeg"; done
```


85. encrypt file

```bash
gpg -c filename

gpg filename.gpg
 
```


86. convert png to jpg
```bash
for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done
```

87. sed split, select odd lines, prepend string and insert new first line, 

```bash
sed 's/seed/\n/g' FakesSGAN2.csv > New.csv
sed -n 'n;p' New.csv > New2.csv
sed -e 's/^/seed/' $line New2.csv > New3.csv
sed  -i '1i File' New3.csv
```

88. unzip to directory
```bash
unzip -q file.zip -d /DIR 
```

89. for list
```bash
for i in {1..25};
do
	echo "$i";
done
```

90. URL from youtube

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

91. edit GRUB boot parameters

* https://wiki.ubuntu.com/Kernel/KernelBootParameters
* https://askubuntu.com/questions/19486/how-do-i-add-a-kernel-boot-parameter
* https://www.kernel.org/doc/html/v4.14/admin-guide/kernel-parameters.html

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

92. Set display

```bash
xrandr --output DP1 --same-as LVDS1

xrandr --output DVI-D-1 --same-as DP-1

xrandr --fb 1920x1080 --output DP-1 --mode 1680x1050 --scale-from 1920x1080 --output DVI-D-1 --mode 1920x1080 --scale 1x1 --same-as DP-1

```

93. transparency

```bash
transset -p --dec 0.05
```

95. convert PDF 2 images and insert border

```bash
mkdir OUT
pdftoppm in.pdf ./OUT/new.pdf -png
for i in *.png; do convert "$i" -shave 40x40 -bordercolor black -border 10 "./OUT/$i"; done;
convert ./OUT/*.png new.pdf
rm -rf OUT/ *.png
```

95. xcfe install

```bash
sudo apt install libexo-1-0
sudo apt-get install -y xfce4-terminal
```

96. Media player controls

```bash
sudo apt install playerctl
playerctl play-pause
playerctl next
playerctl previous
playerctl stop
```

97. hash string

```bash
echo -n foobar | sha256sum
```

## Raspberry 3

1. PI OS Lite

download:

2021-01-11-raspios-buster-armhf-lite.zip
balena-etcher-elctron_1.5.116_amd64.deb

run etcher move zip to SD card

move ssh file into boot unit

user: <user>
password: <password>

change password immediately

psswd

2. Lubuntu install

* run balena Etcher from whisker menu

* select lubuntu-16.04-desktop-armhf-raspberry-pi.img.xz 

* flash the sd card










