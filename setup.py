from setuptools import setup, find_packages

setup(name='treqs',
      version='3.0',
      description='Tool Support for Managing Requirements in Large-Scale Agile System Development',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'treqs=_treqs.functions.checkConsistency:check',
              # 'generatepreview=treqs.generatePreview:generate_preview',
              'generatereq=_treqs.functions.generateReq:generate',
              'generatereqdoc=_treqs.functions.generateReqDoc:generate_doc',
          ],
      },
      install_requires=['python-gitlab','gitpython' ,'wheel', 'sphinx', 'html-parser', 'htmltag', 'pandas', 'uuid'],
      zip_safe=False)
