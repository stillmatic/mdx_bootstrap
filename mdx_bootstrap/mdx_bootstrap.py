from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree


class BootstrapExtension(Extension):
    def __init__(self, *args, **kwargs):
        """Merge user and default configuration."""
        # Default settings.
        self.config = {
            'metadata': [
                ['title'],
                'List of metadata keys to which apply Bootstrap classes.'],
        }

        # Override defaults with user settings.
        for key, value in kwargs.items():
            self.setConfig(key, str(value))

        super(BootstrapExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        self.processor = BootstrapTreeprocessor()
        self.processor.md = md
        self.processor.config = self.getConfigs()
        md.treeprocessors.add('bootstrap', self.processor, '_end')


class BootstrapTreeprocessor(Treeprocessor):

    def run(self, node):
        for child in node.getiterator():
            if child.tag == 'img':
                child.set("class", "img-fluid")
            elif child.tag == 'table':
                child.set("class", "table table-striped")

        return node
