# Modification from: https://gist.github.com/tgarc/7d6901858ef708030c19
# which itself was a 
# modification of config created here: https://gist.github.com/cscorley/9144544
try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2
import os
import sys

# Make this the root of your jekyll site
basedir = '/Users/afq/Documents/Dropbox/afqueiruga.github.io/'

f = None
for arg in sys.argv:
    if arg.endswith('.ipynb'):
        f = arg.split('.ipynb')[0]
        break


c = get_config()
c.NbConvertApp.export_format = 'markdown'
c.MarkdownExporter.template_path = [basedir+'/scripts/jupyterconverter/'] # point this to your jekyll template file
c.MarkdownExporter.template_file = 'jekyll'
#c.Application.verbose_crash=True

# modify this function to point your images to a custom path
# by default this saves all images to a directory 'images' in the root of the blog directory
def path2support(path):
    """Turn a file path into a URL"""
    return '{{ BASE_PATH }}/assets/' + f +'_files/' + os.path.basename(path)

c.MarkdownExporter.filters = {'path2support': path2support}

if f:
    c.NbConvertApp.output_base = f.lower().replace(' ', '-')
    c.FilesWriter.build_directory = basedir+'/assets/' # point this to your build directory

