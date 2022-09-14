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
2. Tree directory
```
tree
```
3. Count the number of files inside a folder
```
ls -1 | wc -l
```
4. See current path
```
pwd
```
5. Change path
```
cd ~/Downloads/
```
6. Remote login
```
ssh user@host
```
7. Remote login with certificate
```
ssh -i cert.pem user@host
```
8. Remote copy single file to current working directory
```
scp user@host:PATH/File .
```
9. Remote copy multiple files to specific path
```
scp -r user@host:PATH/* ~/Downloads/
```
10. Remote copy verbose
```
scp -v myFile user@host:~
```
