from setuptools import setup, find_packages

setup(name='treqs',
      version='3.0',
      description='Tool Support for Managing Requirements in Large-Scale Agile System Development',
      url='https://github.com/yujhenchen/treqs.git',
      author='Yu-Jhen Chen',
      author_email='yujhen.chen93@gmail.com',
      license='MIT',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'treqs=src.scripts.checkConsistency:check',
              'generatereq=src.scripts.generateReq:generate',
              'generatereqdoc=src.scripts.generateReqDoc:generate_doc',
          ],
      },
      install_requires=['python-gitlab','gitpython' ,'wheel', 'sphinx', 'html-parser', 'htmltag', 'pandas', 'uuid'],
      zip_safe=False)
