# BasicLinux
The repository comprises basis commands to execute on linux

All commands' usage can be inspected as *man* [command], e.g. :
```
man pwd
```

1. List directories with flags

```
ls -lXh
```

2. See current path

```
pwd
```

3. Change path

```
cd ~/Downloads/
```

4. Remote login
```
ssh user@host
```

5. Remote login with certificate
```
ssh -i cert.pem user@host
```
6. Remote copy single file to current working directory
```
scp user@host:PATH/File .
```
7. Remote copy multiple files to specific path
```
scp -r user@host:PATH/* ~/Downloads/
```

