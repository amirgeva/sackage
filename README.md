sackage
=======

Debian packaging tool for interpreted language applications.

This tool assumes that the application does not require any building, 
and can be run simply by invoking the interpreter.

It creates a package that installs as a directory tree under ```/usr/share```
and creates a shell script that installs under /usr/bin and starts the main
application script.

The tool is built as a sort of wizard that asks all the required information,
and then builds all of the control files and runs the appropriate build tools.

