st-copy
=======
## Plugin

Netbeans automatically copies files on save from 'webapp' folder to 'target' subtree for Glassfish deployment.

This plugin enables using Sublime Text for web related work of a glassfish deployed project. Directory structure is hardcoded for author's specific project, but it should be easy to adapt it for different kind of structure.

from source:
*\src\main\webapp\
to:
*\target\*SNAPSHOT\

For example:
File: root_folder\my_web_project_name\src\main\webapp\some\relative\substructure\hello.html
Gets copied to: root_folder\my_web_project_name\target\my_web_project_name-1.0-SNAPSHOT\some\relative\substructure\hello.html
	
## Installation

Copy cloned/downloaded repo folder to:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`