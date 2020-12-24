keyword: Shell
	The shell is a program that takes keyboard commands and passes them to the operating system to carry out.
keyword: Terminal Emulators
	A terminal emulator is a program that allows us to communicate with the shell. Popular ones include konsole and gnome-terminal.
command: cal 
	Displays a small calender of the current month in your terminal
command: df 
	Displays the current amount of free space on disk drives
command: free
	Displays the amount of free memory
command: pwd
	Displays the file path for current working directory
command: cd 
	cd shortcuts
	change the current working directory to the home directory of username
		cd ~username
	change the working directory to your home directory 
		cd 
command: ls -l 
		same as ls, but returns it in long format, showing much more detail.
	ls -lt 
		same as ls -l but sorts the output by file's modification time
	ls -lt --reverse 
		same as ls -lt but sorts output in reverse order

command: ls
	Common ls options
	-all, -a
		lists all files including hidden ones
	-A, --almost-all
		same thing as -a except does not list current or parent directories
	-d, --directory
		in conjunction with -l shows details about the directory rather than its contents
	-F, --classify
		appends an indicator character to the end of each listed name
	-h, --human-readable
		pretty prints long format listings
	-S 
		sort results by file size
	-t 
		sort by modification time 
command: file <filename>
	returns information on file such as filetype.
command: less
	displays text in a file similarly to cat
command: type 
	displays a command's type. Can be useful when you are trying to get information on a command.
command: which 
	display's an executable's location. When working with large servers, there may be more than one version of an exe installed on a system.
	Only works for executable programs, not builtins or aliases. 
command: help
	displays a built-in help facility for each of the shell builtins.Syntax is help <command>.
	Note this is different from the --help options that most programs have.
command: man 
	displays a program's manual page. Mainly to be used as a reference for when using a program.
command: apropos 
	display appropriate commands. Syntax is apropos <command>. Searches the list of man pages for possible matches based on search term.
command: whatis
	displays one-line manual page descriptions. Helpful for quick info on a command. 
command: info 
	displays a programs info entry. An alternative to man pages that are displayed with a reader program called info, and are hyperlinked 
	like webpages. Syntax is info <command>
operation: Redirect IO
	You can redirect the standard output of a command to a text if you so choose. This can be useful if you want to save some output 
	information after running a command. You can do this with the > command, followed by where you would like to save the output, like a 
	text file. If you use this command on a not-existant text file, then it will create the text file. Note that if you call this command
	on a already existing text file, the files information will be overwritten. If instead you would like to append the information 
	to the file, run >> instead. 
	Example:
		ls -l /usr/bin > output //will create the file and overwrite if it already exists
		ls -l /usr/bin >> output //Will append the information to a file. If it does not exist it will work like > instead.
	You can also redirect error messages & save the output into a text file. This is harder however because standard error lacks the ease
	of a dedicated redirection operator. Thus you must refer to its file descriptor. 
	The three file streams; standard input, output & error is reffered to internally as file descriptors 0, 1, & 2. 
	Shell provides a notation for redirecting files using the file descriptor number. 
	Example:
		ls -l /bin/usr 2 > ls-error
	The file descriptor 2 is placed immediately before the redirection operator to perform the redirection of standard error. 
	In situations where you want to capture all of the output of a command, you must redirect both standard output and standard 
operation: absolute & relative paths
	Note that when working in directories, You can call the current working directory with . and its parent directory with ..
	file path = /home/user/documents/notes/school/science
	current working directory = science
	cd ./ => returns science
	cd ../ => returns school
	In addition, if a pathname is not specified, the current working directory will automatically be assumed. 
	cd bin is the same thing as cd ./bin
operation: hidden files
	Note that filenames that begin with a period character are hidden and can only be shown with ls -a.
operation: naming files
	It's considered good practice to not put spaces in your file names. Try to stick to programming-style conventions. 
	Also linux has no concept of file extensions, so things like .txt or .mp3 won't matter.
operation: Linux directories
	/bin
		Contains binaries necessary for the system to boot & run
	/boot
		Contains the actual Linux kernel, initial RAM disk image and the boot loader. 
	/dev 
		Contains device nodes, which Linux maintains a list of all the devices on the system
	/etc 
		Contains system-wide configuration files & collections of shell scripts that run at boot time
	/home
		Contains each user's home directory, such as Documents & Downloads
	/lib
		Contains shared library files used by the core system programs. Similar to .dll files in Windows
	/lost+found
		Only used in extremely bad file system corruptions. Should normally be empty
	/media
		Contains mount points for removable media like usb drives and cd-roms
	/mnt 
		Contains mount points for removeable media on older Linux systems
	/opt
		Used to install "optional" software, like commercial software products
	/proc
		A virtual file system maintained by the Linux kernal
	/root
		Contains home directory for the root account
	/sbin
		Contains system binaries, used for vital system tasks generally reserved for super user
	/tmp 
		Contains temporary files created by various programs. Cleaned after each reboot
	/usr 
		Contains all the programs and support files used by regular users
	/usr/bin
		Contains executable programs installed by your distribution. Can hold thousands of programs
	/usr/lib
		Contains shared libraries for the programs in /usr/bin.
	/usr/local
		Contains programs not included with your distribution but are intended for system-wide use
	/usr/sbin
		Contains more system admin programs
	/usr/share
		Contains all shared data used by programs in /usr/bin
	/usr/share/doc
		Contains documention on programs in /usr/share
	/var 
		Contains data likely to change, such as databases, spool files and user email
	/var/log
		Contains log files, records of various system activity
operation: Symbolic Links
	Also known as soft link or symlink. Allows you to reference a file under multiple names. Useful when multiple programs all work with
	the same file. You can almost think of it as storing the information in a variable and having everything reference the variable as 
	opposed to some hard coded link. 
operation: Hard Links
	Hard Links are the original Unix way of creating links. Every file has a single hard link that gives the file it's name. When creating
	a hard link, we create an additional directory entry for a file. Note hard links have the following two limitations:
		- Cannot reference a file outside its own file system, as in they cannot reference a file that is not on the same disk partition
		as the link itself
		- Cannot reference a directory
	Hard link is indistinguishable from the file itself. You will see no special indication of the link either. When a hard link is deleted, 
	the link is removed but the contents of the file itself continue to exist.  
operation: Wildcards
	Similarly to Regex, Wildcards are special characters that can be used with many linux commands to select filenames based on patterns
	of characters. 
	Examples of Wildcards:
		* = Matches any characters
		? = Matches any single character
		[characters] = Matches any character that is a member of the set characters
		[!characters] = Matches any character that is not a member of the set characters. Not its like programming
		[[:class]] = Matches any character that is a member of the specified class
	Most commonly used character classes:
		[:alnum:] = Matches any alphanumeric character
		[:aplha:] = Matches any alphabetic character
		[:digit:] = Matches any numeral
		[:lower:] = Matches any lowercase letter
		[:upper:] = Matches any uppercase letter
	Examples of Wildcard:
		* = All files
		g* = Any file beginning with g
		b*.txt = Any file beginning with b followed by any characters and ending with .txt
		Data??? = Any file beginning with Data followed by exactly three characters
		[abc]* = Any file beginning with either an a, a b, or a c
		BACKUP.[0-9][0-9][0-9] = Any file beginning with BACKUP followed by exactly three numerals
		[[:upper:]]* = Any file beginning wiht an uppercase letter
		[![:digit:]]* = Any file not beginning with a numeral
		*[[:lower:]123] = Any file ending with a lowercase letter or the numerals 1, 2, or 3
	Note that wildcards are not limited simply to the command line; many popular file managers like Nautilus, Dolphin, and Konquerer, can 
	also use wildcards in there search bars. 
operation: Alias
	Alias allows you to define functions within your shell, allowing you to do all kinds of unique operations that Linux would normally 
	not have options for. Note that before you create a alias it is best to call type on its prospective name before actually assinging
	it so that you do not overwrite another function. General notation for this is alias <aliasname> = <string>. Note that your entire 
	function should be inside of a string: 'cd /home/user; mkdir newfolder; cd newfolder'. Also note that you can commit multiple 
	commands in the same line; simply split them with a semicolon. Also note that alias will be deleted once the terminal is closed.
