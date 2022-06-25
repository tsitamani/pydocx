# pydocx
docx parser in python , a midyfied version from <a href="[http://example.com/](https://github.com/CenterForOpenScience/pydocx)">_[pydocx]_</a>

# install
python setup install

# usage
**command line Usage**: pydocx --html|--markdown|--text input.docx output

  pydocx --text file1.docx file2.txt
  pydocx --html file1.docx file2.html
  pydocx --markdown file1.docx file2.md

**call in python**

  <pre><code>
  import pydocx
  
  def docx2txt(arg):
    fsrc, fdest = arg
    try:
      print(fsrc) 
      html = pydocx.PyDocX.to_html(fsrc)
      data = get_html_file_content(html)
      f = open(fdest, 'w')
      f.write(data)
      f.close()
      return (0, fdest)
    except:
      print('fail %s' % fsrc)
      return (1, fsrc)
</code></pre>
