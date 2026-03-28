# Debugging the linker

Sometimes the link step doesn't go as we expect and we need good information to figure out what's wrong. But the problems are on a user's machine, not our own. So when this occurs, walk a user through these instructions to generate a log file which we can examine to figure out what might be wrong with either the linker's code or the user's installation.

1. Open up the user's environment variables and add a new one "SDS2\_LINKER\_LOG\_FILE"
2. Set this to a valid filepath in a directory they can write to, something like "C:\\Users\\theiruser\\linker.log"
3. Run your program like normal
4. Ask them to send you this linker.log file
5. Have them remove that "SDS2\_LINKER\_LOG\_FILE" environment variable and delete linker.log once it's sent.

For developers, you can just set SDS2\_LINKER\_LOG\_FILE to a valid path at the command line and run your program.

If you set SDS2\_LINKER\_LOG\_FILE to "stdout" it will dump to standard out instead of a file. This can be handy for programmers debugging console applications.