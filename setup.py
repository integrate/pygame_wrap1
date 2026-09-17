import setuptools, glob, sys



if "develop" in sys.argv:
    setuptools.setup(
        packages=["wrap_engine"]
    )
else:

    extensions = ("*.py", "*.pyx")
    l = []
    for extension in extensions:
        l.extend(glob.glob("wrap_engine/" + extension))

    ext = [setuptools.extension.Extension("wrap_engine", l)]

    setuptools.setup(
        ext_modules=ext
    )
