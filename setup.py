import setuptools, glob

extensions = ("*.py","*.pyx")
list = []
for extension in extensions:
    list.extend(glob.glob("pygame_wrap1/"+extension))

ext = [setuptools.extension.Extension("pygame_wrap1", list)]

setuptools.setup(
    ext_modules=ext
)
