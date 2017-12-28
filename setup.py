from setuptools import setup, find_packages

setup(
    name ='FB-Spider',
    version ='2.0',
    description = 'accepts the id of a Facebook page and transforms into a table of the latest 5 posts and the respective latest 5 comments per post. The table will be in .html format',
    author = 'Parth Verma',
    author_email = 'vermaparth97@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'facepy',
        'json2html',
        'click',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        fbspider=graph:cli
    ''',
)
