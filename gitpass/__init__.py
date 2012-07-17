"""
An extension of the Python standard library's 'getpass' module designed for
(not) committing a password to a Git repository

Copyright (C) 2012 Dustin Smith

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
import os
import re
import logging
import getpass
import base64

def find_git_directory(prefix=None):
    """
    Traverses the directory starting from 'prefix' (or this file's path)
    for .git and returns that directory or False if none can be found
    """
    if prefix is None:
        prefix = os.path.dirname(os.path.abspath(os.getcwd()))
    if os.path.isdir(prefix+'/.git'):
        return prefix
    else:
        prefix = os.path.abspath(prefix + "/" + os.path.pardir)
        if prefix == "/":
            return False
        else:
            return find_git_directory(prefix)

def find_in_gitignore(gitdir, entry):
    """
    Returns True iff 'entry' is in the .gitignore file
    in the 'gitdir' git repository
    """
    with open(gitdir + "/.gitignore") as f:
        for line in f:
            if line.strip() == entry:
                return True
    return False


def ensure_in_gitignore(gitdir, entry):
    """
    Stores the file 'entry' in the 'gitdir'/.gitignore file
    """
    try:
        if find_in_gitignore(gitdir, entry):
            return True
    except IOError:
        # .gitignore doesn't exit
        logging.info("Creating %s/.gitignore" % (gitdir,))
    logging.info("Adding %s to .gitignore" % (entry,))
    with open(gitdir + "/.gitignore", 'a') as f:
        f.write("%s\n" % (entry,))
        f.close()

def save_password(passfile, password):
    """
    Creates/overwrites a file 'passfile' to contain contents
    'password'
    """
    with open(passfile, 'w') as f:
        f.write("%s\n" % (base64.b64encode(password),))
        f.close()

def gitpass(prompt, passfile=None, force_new=False):
    """
    This prompts the user with 'prompt' in the terminal and then
    creates a file (named 'passfile' if specified, otherwise based on
    the prompt) to store the password in for the future.

    force_new asks the user for a prompt at each time.
    """
   
    passfile = passfile or re.sub(r'\s', '_', prompt.lower().strip())
    hidden_passfile = ".__%s" % passfile
    gitdir = find_git_directory()
    passpath = gitdir + "/" + hidden_passfile
    try:
        if force_new:
            raise IOError 
        with open(passpath) as pf:
            password = base64.b64decode(pf.read().strip())
            pf.close()
        return password
    except IOError:
        password = getpass.getpass(prompt + ":").strip()
        ensure_in_gitignore(gitdir, hidden_passfile)
        save_password(passpath, password)
        return password

