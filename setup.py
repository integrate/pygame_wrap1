import setuptools, glob, sys



# if "develop" in sys.argv:
setuptools.setup(
    packages=["wrap_engine"]
    # package_dir={"wrap_engine":"wrap_engine"}
)
# else:
#
#     extensions = ("*.py", "*.pyx")
#     list = []
#     for extension in extensions:
#         list.extend(glob.glob("wrap_engine/" + extension))
#
#     ext = [setuptools.extension.Extension("wrap_engine", list)]
#
#     setuptools.setup(
#         ext_modules=ext
#     )
