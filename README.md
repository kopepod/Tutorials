# Basic Linux
The repository comprises basic commands to execute on linux. All commands' usage can be inspected as *man* [command], e.g. :
```bash
man pwd
```
See all previously executed commands
```
history
```
Run one previous command
```
!100
```
## Paths
1. List directories with flags
```
ls -lXh
```
2. Directory's tree
```
tree
```
3. Count the number of files inside a folder
```
ls -1 | wc -l
```
4. See file's contents (careful, only small files)
```
cat myFile
```
5. Find Files
```
find . -name \*.py
```
6. See current path
```
pwd
```
7. Read full path
```
readlink -f myFile
```
8. Change path
```
cd ~/Downloads/
```
9. Change above
```
cd ..
```
10. Change back
```
cd -
```
## Working remotely
1. Remote login
```
ssh user@host
```
2. Remote login with certificate
```
ssh -i cert.pem user@host
```
3. Remote copy single file to current working directory
```
scp user@host:PATH/File .
```
4. Remote copy multiple files to specific path
```
scp -r user@host:PATH/* ~/Downloads/
```
5. Remote copy verbose
```
scp -v myFile user@host:~
```
6. Download remote resource with *wget*
```
wget URL -o myFile.html
```
7. Logout
```
logout
```
## Files
1. Create/modify file
```
nano myFile.txt
```
2. Copy file showing progress
```
cp -v myFile ~/Downloads/
```
3. Move directory
```
mv MyDirectory ~/Downloads/
```
4. Remove directory
```
rm -rf MyDirectory
```
5. Generate dump zip file
```
zip -r0 myZip.zip MyFolder/
```
6. Unzip File
```
unzip myZip.zip
```
7. Change permissions
```
chmod 777 myfile
```
8. Create folder and loop
```
for i in {0..10}; do mkdir "$i"; done
```
9. Find and execute, example copying all jpg files into a new directory
```
find . -name \*.jpg -exec cp {} ~/Downloads/ \;
```
## Processes
1. See computing load by process
```
top
```
2. See RAM free memory
```
free -h
```
3. Enter daemon process 
```
nohup bash my.sh &
```
4. See GPU usage
```
watch -n 0.5 nvidia-smi
```
5. See memory disk usage
```
df -h
```
6. See folder disk usage
```
du -h ~/Downloads/
``` 
7. See sensors every 0.5 seconds
``` 
watch -n 0.5 sensors
```
