"""Tests for mdx_bootstrap."""
import markdown
import unittest
import textwrap

from mdx_bootstrap import BootstrapExtension
from mdx_gfm import GithubFlavoredMarkdownExtension

class MDXBootstrap(unittest.TestCase):

    def test_load_extension_as_string(self):
        markdown.markdown('', extensions=['bootstrap'])

    def test_load_extension_as_object(self):
        markdown.markdown('', extensions=[BootstrapExtension()])

    def test_image_addition(self):
        text = textwrap.dedent("""
            # Wow this is a header

            ![abc](http://via.placeholder.com/350x150)
            """)
        html = textwrap.dedent("""\
            <h1>Wow this is a header</h1>
            <p><img alt="abc" class="img-fluid" src="http://via.placeholder.com/350x150" /></p>""")
        output = markdown.markdown(text, extensions=[BootstrapExtension()])
        self.assertEqual(output, html)

    def test_table_addition(self):
        text = textwrap.dedent("""
| Tables        | Cool
| ------------- |:-------------:
| col 3 is      | right-aligned
| col 2 is      | centered
| zebra stripes | are neat
            """)
        html = textwrap.dedent("""<table class="table table-striped">
<thead>
<tr>
<th>Tables</th>
<th align="center">Cool</th>
</tr>
</thead>
<tbody>
<tr>
<td>col 3 is</td>
<td align="center">right-aligned</td>
</tr>
<tr>
<td>col 2 is</td>
<td align="center">centered</td>
</tr>
<tr>
<td>zebra stripes</td>
<td align="center">are neat</td>
</tr>
</tbody>
</table>""")
        output = markdown.markdown(text, extensions=[GithubFlavoredMarkdownExtension(),
                                                     BootstrapExtension()])
        self.assertEqual(output, html)

