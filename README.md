# Basic Linux
The repository comprises basis commands to execute on linux. All commands' usage can be inspected as *man* [command], e.g. :
```
man pwd
```
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
4. Find Files
```
find . -name \*.py
```
5. See current path
```
pwd
```
6. Read full path
```
readlink -f myFile
```
7. Change path
```
cd ~/Downloads/
```
8. Remote login
```
ssh user@host
```
9. Remote login with certificate
```
ssh -i cert.pem user@host
```
10. Remote copy single file to current working directory
```
scp user@host:PATH/File .
```
11. Remote copy multiple files to specific path
```
scp -r user@host:PATH/* ~/Downloads/
```
12. Remote copy verbose
```
scp -v myFile user@host:~
```
13. Download remote resource with *wget*
```
wget URL -o myFile.html
```
14. Create/modify file
```
nano myFile.txt
```
15. Copy file showing progress
```
cp -v myFile ~/Downloads/
```
16. Move directory
```
mv MyDirectory ~/Downloads/
```
17. Remove directory
```
rm -rf MyDirectory
```
18. Generate dump zip file
```
zip -r0 myZip.zip MyFolder/
```
19. Unzip File
```
unzip myZip.zip
```
20. Change permissions
```
chmod 777 myfile
```
21. Create folder and loop
```
for i in {0..10}; do mkdir "$i"; done
```
22. Find and execute, example copying all jpg files into a new directory
```
find . -name \*.jpg -exec cp {} ~/Downloads/ \;
```
