import re

r = re.compile(r"<!-- block {} -->{}<!-- endblock {} -->".format("content", ".*", "content"), \
    re.DOTALL)

chunk = "<!-- block {} -->{}<!-- endblock {} -->".format("content", "\n{}\n", "content")


with open('README.md', 'r+') as f:
    content = f.read()
    f.write(r.sub(chunk, content))