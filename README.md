
# Gitpass

*Gitpass is an extension of the Python standard library's [getpass](http://docs.python.org/library/getpass.html), designed for keeping passwords out of your git repository*.


Do you have a password, credentials or other information that you don't
want to commit to your git repository?  Use gitpass as a quick, easy,
insecure way to prevent a password from appearing on your git
repository, while only having to enter it once.


**WARNING**: Passwords are saved in hidden text files at the base
directory of your git repository.  Although they are obfuscated, they
**are not encrpyted** and keep in mind they are vulnerable to other users of your
computer.

## Installation

    pip install gitpass

## Usage

    import gitpass
    aws_pwd = gitpass.gitpass('AWS Password')

The first time you use this in your git repository, it will:

  1. Prompt you for a password in the terminal
  2. Create a file called `.__aws_password` that contains your password
     in [base64 encoding](http://docs.python.org/library/base64.html)
  3. Add `.__aws_password` to your `.gitignore` file.  

The next time you use the password, it will not prompt you again for
your password.

## Optional arguments

`gitpass.gitpass(prompt, passfile=None, force_prompt=False)`

 - `passfile`: the name of the file to store the password.  If this is
   not specified, a default filename will be created from the prompt
(lowercased, removing whitespaces).
 - `force_prompt`: if True, it forces the user to enter the password
   again, ignoring whatever is in the file

Gitpass is covered under the [MIT
License](http://opensource.org/licenses/mit-license.php) and was created
by [Dustin Smith](http://web.media.mit.edu/~dustin/].
