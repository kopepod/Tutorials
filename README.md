# Basic Linux
The repository comprises basic commands to execute on linux. All commands' usage can be inspected as *man* [command], e.g. :
```bash
man pwd
```bash
See all previously executed commands
```bash
history
```bash
Run one previous command
```bash
!100
```bash
## Paths
1. List directories with flags
```bash
ls -lXh
```bash
2. Directory's tree
```bash
tree
```bash
3. Count the number of files inside a folder
```bash
ls -1 | wc -l
```bash
4. See file's contents (careful, only small files)
```bash
cat myFile
```bash
5. Find Files
```bash
find . -name \*.py
```bash
6. See current path
```bash
pwd
```bash
7. Read full path
```bash
readlink -f myFile
```bash
8. Change path
```bash
cd ~/Downloads/
```bash
9. Change above
```bash
cd ..
```bash
10. Change back
```bash
cd -
```bash
## Working remotely
1. Remote login
```bash
ssh user@host
```bash
2. Remote login with certificate
```bash
ssh -i cert.pem user@host
```bash
3. Remote copy single file to current working directory
```bash
scp user@host:PATH/File .
```bash
4. Remote copy multiple files to specific path
```bash
scp -r user@host:PATH/* ~/Downloads/
```bash
5. Remote copy verbose
```bash
scp -v myFile user@host:~
```bash
6. Download remote resource with *wget*
```bash
wget URL -o myFile.html
```bash
7. Logout
```bash
logout
```bash
## Files
1. Create/modify file
```bash
nano myFile.txt
```bash
2. Copy file showing progress
```bash
cp -v myFile ~/Downloads/
```bash
3. Move directory
```bash
mv MyDirectory ~/Downloads/
```bash
4. Remove directory
```bash
rm -rf MyDirectory
```bash
5. Generate dump zip file
```bash
zip -r0 myZip.zip MyFolder/
```bash
6. Unzip File
```bash
unzip myZip.zip
```bash
7. Change permissions
```bash
chmod 777 myfile
```bash
8. Create folder and loop
```bash
for i in {0..10}; do mkdir "$i"; done
```bash
9. Find and execute, example copying all jpg files into a new directory
```bash
find . -name \*.jpg -exec cp {} ~/Downloads/ \;
```bash
## Processes
1. See computing load by process
```bash
top
```bash
2. See RAM free memory
```bash
free -h
```bash
3. Enter daemon process 
```bash
nohup bash my.sh &
```bash
4. See GPU usage
```bash
watch -n 0.5 nvidia-smi
```bash
5. See memory disk usage
```bash
df -h
```bash
6. See folder disk usage
```bash
du -h ~/Downloads/
```bash 
7. See sensors every 0.5 seconds
```bash 
watch -n 0.5 sensors
```bash
