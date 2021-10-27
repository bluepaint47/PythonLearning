import platform as p

name = p.system()
version = p.version()
release = p.release()
py_version  = p.python_version()
print(name)
print(version)
print(release)
print("python verion "+ py_version)

