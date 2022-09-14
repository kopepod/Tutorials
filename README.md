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
4 See file's contents (careful, only small files)
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
10. Remote login
```
ssh user@host
```
11. Remote login with certificate
```
ssh -i cert.pem user@host
```
12. Remote copy single file to current working directory
```
scp user@host:PATH/File .
```
13. Remote copy multiple files to specific path
```
scp -r user@host:PATH/* ~/Downloads/
```
14. Remote copy verbose
```
scp -v myFile user@host:~
```
15. Download remote resource with *wget*
```
wget URL -o myFile.html
```
16. Create/modify file
```
nano myFile.txt
```
17. Copy file showing progress
```
cp -v myFile ~/Downloads/
```
18. Move directory
```
mv MyDirectory ~/Downloads/
```
19. Remove directory
```
rm -rf MyDirectory
```
20. Generate dump zip file
```
zip -r0 myZip.zip MyFolder/
```
21. Unzip File
```
unzip myZip.zip
```
22. Change permissions
```
chmod 777 myfile
```
23. Create folder and loop
```
for i in {0..10}; do mkdir "$i"; done
```
24. Find and execute, example copying all jpg files into a new directory
```
find . -name \*.jpg -exec cp {} ~/Downloads/ \;
```
