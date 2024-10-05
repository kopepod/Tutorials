# Basic Linux
The repository comprises basic commands to execute on linux. All commands' usage can be inspected as *man* [command], e.g. :
```bash
man pwd
```
See all previously executed commands
```bash
history
```
Run one previous command
```bash
!100
```
## Paths
1. List directories with flags
```bash
ls -lXh
```
2. Directory's tree
```bash
tree
```
3. Count the number of files inside a folder
```bash
ls -1 | wc -l
```
4. See file's contents (careful, only small files)
```bash
cat myFile
```
5. Find Files
```bash
find . -name \*.py
```
6. See current path
```bash
pwd
```
7. Read full path
```bash
readlink -f myFile
```
8. Change path
```bash
cd ~/Downloads/
```
9. Change above
```bash
cd ..
```
10. Change back
```bash
cd -
```
## Working remotely
1. Remote login
```bash
ssh user@host
```
2. Remote login with certificate
```bash
ssh -i cert.pem user@host
```
3. Remote copy single file to current working directory
```bash
scp user@host:PATH/File .
```
4. Remote copy multiple files to specific path
```bash
scp -r user@host:PATH/* ~/Downloads/
```
5. Remote copy verbose
```bash
scp -v myFile user@host:~
```
6. Download remote resource with *wget*
```bash
wget URL -o myFile.html
```
7. Logout
```bash
logout
```
## Files
1. Create/modify file
```bash
nano myFile.txt
```
2. Copy file showing progress
```bash
cp -v myFile ~/Downloads/
```
3. Move directory
```bash
mv MyDirectory ~/Downloads/
```
4. Remove directory
```bash
rm -rf MyDirectory
```
5. Generate dump zip file
```bash
zip -r0 myZip.zip MyFolder/
```
6. Unzip File
```bash
unzip myZip.zip
```
7. Change permissions
```bash
chmod 777 myfile
```
8. Create folder and loop
```bash
for i in {0..10}; do mkdir "$i"; done
```
9. Find and execute, example copying all jpg files into a new directory
```bash
find . -name \*.jpg -exec cp {} ~/Downloads/ \;
```
## Processes
1. See computing load by process
```bash
top
```
2. See RAM free memory
```bash
free -h
```
3. Enter daemon process 
```bash
nohup bash my.sh &
```
4. See GPU usage
```bash
watch -n 0.5 nvidia-smi
```
5. See memory disk usage
```bash
df -h
```
6. See folder disk usage
```bash
du -h ~/Downloads/
``` 
7. See sensors every 0.5 seconds
```bash
watch -n 0.5 sensors
```
