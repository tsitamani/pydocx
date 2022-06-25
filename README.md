# pydocx
docx parser in python , a midified version from <a href="https://github.com/CenterForOpenScience/pydocx">[pydocx]</a>

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
  
  def docx2txt(fsrc, fdest):
    try:
      print(fsrc) 
      data = pydocx.PyDocX.to_text(fsrc)
      f = open(fdest, 'w')
      f.write(data)
      f.close()
      return (0, fdest)
    except:
      print('fail %s' % fsrc)
      return (1, fsrc)
  </code></pre>

  or

  <pre><code>
  
  from bs4 import BeautifulSoup
  
  def get_html_file_content(html):
    soup = BeautifulSoup(html, features='lxml')
    html_content_tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4']#,'div']
    contents = []
    for child in soup.findAll(html_content_tags):
      inner_text = child.text.strip() if child.text else ""
      if inner_text:
        contents.append(inner_text)
    result = '\n'.join(contents) + '\n'
    return result

  def docx2txt(fsrc, fdest):
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
