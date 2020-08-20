from setuptools import setup

# =============================================================================
# PATH TO THIS MODULE
# =============================================================================

PATH = os.path.abspath(os.path.dirname(__file__))


# =============================================================================
# Get the version from the module file itself (not imported)
# =============================================================================

MODULE_PY_PATH = os.path.join(PATH, "simplemath.py")

with open(MODULE_PY_PATH, 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            _, _, MODULE_VERSION = line.replace('"', "").split()
            break


# =============================================================================
# RETRIEVE TE README
# =============================================================================

README_MD_PATH = os.path.join(PATH, "README.md")

with open(README_MD_PATH, 'r') as f:
    LONG_DESCRIPTION = f.read()


setup(name='simplemath',
      version=MODULE_VERSION,
      description='Simple Math Module',
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      author='Martin Beroiz',
      author_email='martinberoiz@gmail.com',
      py_modules=['simplemath', ],
      install_requires=[numpy,],
      test_suite='tests',
     )
