pefile_to_maec
==============

PEFile to MAEC translation utility/native integration

### Requirements ###
* CybOX
* MAEC

### Standalone Usage ###
```
$ python pefile_to_maec.py samples/<exe> out.maec
```
### Pre-release ###
#### [v0.1.0a1][4]  => Add ability to print headers from pefile module
#### [v0.1.0a2][5]  => Map pe headers from pefile.PE object
#### [v0.1.0a3][11] => Map pe optional header from pefile.PE object
#### [v0.1.0a4][6]  => Map pe sections from pefile.PE object
#### [v0.1.0a5][7]  => Map pe data directories from pefile.PE object
#### [v0.1.0b1][8]  => Create maec xml from pefile output
[4]: https://github.com/MAECProject/pefile/issues/4 "Add ability to print headers from pefile module"
[5]: https://github.com/MAECProject/pefile/issues/5 "Map pe headers from pefile.PE object"
[6]: https://github.com/MAECProject/pefile/issues/6 "Map pe sections from pefile.PE object"
[7]: https://github.com/MAECProject/pefile/issues/7 "Map pe data directories from pefile.PE object"
[8]: https://github.com/MAECProject/pefile/issues/8 "Create maec xml from pefile output"
[11]: https://github.com/MAECProject/pefile/issues/11 "Map pe optional header from pefile.PE object"