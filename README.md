# Jinja markdown

### Short description:
This program generates static pages using Jinja, a template engine for Python.

### Instalation:

* Clone the project
* Install the requirements (best inside a virtualenv)
* Run the program:
  ./generate.py test/source output
* Test the program:
 ./test.py 

### Functions:

* generate_site(folder_path, output): 
creates a jinja environment and generates the site from the basic layout of the 
pages and by rendering the data provided
it takes two parameters:
 * folder_path - the folder containing the layout and the data for the website
 * output - the folder in which the pages will be created

* read_file(file_path):
takes a path to a file which contains the data to be rendered
* list_files(folder_path):
takes a path to a folder containing files to be rendered; it returns a generator to iterate over them
* write_output(name, html)
takes a name and the html generated and creates the static page 
