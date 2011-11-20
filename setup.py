from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.piwik.mediaelement',
      version=version,
      description="Analytics support for media elements in Plone using Piwik & MediaElement.js",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='video analytics flowplayer piwik plone',
      author='unweb.me',
      author_email='we@unweb.me',
      url='https://github.com/plumi/collective.piwik.mediaelement',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.piwik'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.piwik.core',
          'collective.mediaelementjs',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
