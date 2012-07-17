
# Gitpass

An extension of the Python standard library's [getpass](http://docs.python.org/library/getpass.html) module designed for
(not) committing a password to a Git repository.  By Dustin Smith,
covered under the [MIT License](http://opensource.org/licenses/mit-license.php)

## Usage

    import gitpass
    aws_pwd = gitpass.gitpass('AWS Password')

The first time you use this in your git repository, it will:

  1. Prompt you for a password in the terminal
  2. Create a file called `.__aws_password` that contains your password
     in [base64 encoding](http://docs.python.org/library/base64.html)
  3. Add `.__aws_password` to your `.gitignore` file.  

The next time you use the password, it will not prompt you.

## Optional arguments

`gitpass.gitpass(prompt, pass_file=None, force_prompt=False)`

 - `passfile`: the name of the file to store the password in
 - `force_prompt`: if True, it forces the user to enter the password
   again, ignoring whatever is in the file

