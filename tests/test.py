from pelican import contents

file_ = None

with open('content/2018-01-21-windows设置防火墙开放特定端口.md') as fp:
    file_ = fp.read()

content = contents.Content(file_)
print(content)
