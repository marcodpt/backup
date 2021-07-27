# backup
> File backup script in python3 with JSON config file

## Usage
```sh
./dump.py
```

## config.json
 - array of objects: items properties:
   - string `source`: the source file, maybe be remote machine
`user`@`IP`:`filePath`
   - string `target`: the target file, always local machine, use `*` for
current timestamp
   - number `limit`: the max number of files of this type on the target dir
   - boolean `compress`: should be compressed

## decompress backup
```sh
tar -zxf {filename}
```
