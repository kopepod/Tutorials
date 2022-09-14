# Basic Linux
The repository comprises basis commands to execute on linux

All commands' usage can be inspected as *man* [command], e.g. :
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
6. Change path
```
cd ~/Downloads/
```
7. Remote login
```
ssh user@host
```
8. Remote login with certificate
```
ssh -i cert.pem user@host
```
9. Remote copy single file to current working directory
```
scp user@host:PATH/File .
```
10. Remote copy multiple files to specific path
```
scp -r user@host:PATH/* ~/Downloads/
```
11. Remote copy verbose
```
scp -v myFile user@host:~
```
