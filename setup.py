from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['ReviewBoard', 'Markdown==2.4', 'docutils'],
			dependency_links = ['https://www.djangoproject.com/download/1.4.5/tarball/#egg=Django-1.4.5',],
     )
