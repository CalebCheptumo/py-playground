#Reading from a file.
#An incredible amount of data is available in text files. Text files can contain weather data, traffic data, socioeconomic data, literary works, and more. Reading from a file is particularly useful in data analysis applications, but it’s also applicable to any situation in which you want to analyze or modify information stored in a text file. For example, you can write a program that reads in the contents of a text file and rewrites the file with formatting that allows a browser to display it.

#reading the context of a file
#pi_digits.txt - contains pi to 30 decimal places with 10 decimal place per line
#path is the exact location of a file or folder on a system.
#python provides a module called pathlib that makes it easy to work with the file system.
#a module that provides specific functionality like this is often called a library. hence, pathlib is a library.



#relative and absolute file paths
#relative  file path tells python to look for a given location relative to the directory where the currently running program file is stored.
#syntax: path = Path("relative_path_to_file")
#example of relative path: path = Path("files-and-exceptions/pi_digits.txt")
#absolute file path tells python exactly where a file is on your computer regardless of where the program that’s being executed is stored. it start from the root directory of the file system.
#absolute path are usually longer than relative paths.
#syntax: path = Path("absolute_path_to_file")
#example of absolute path: path = Path("/home/caleb/Documents/CALEBTHEDEV/py-playground/files-and-exceptions/pi_digits.txt")
#you can use either a relative or an absolute path to open a file. However, it’s important to be consistent in your use of these approaches. If you use relative paths, all the files you reference in your code will be in the same directory, or you’ll need to be aware of the directory structure of your project. If you use absolute paths, your code will only work on your computer, and it will break on anyone else’s computer. It’s also easier to move your project to another computer if you use relative paths. For this reason, we recommend using relative paths when possible.