from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "nlp_dvc_demo"
AUTHOR_USER_NAME = "Lakshman"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [
    'tqdm',
    'dvc',
    'pandas',
    'numpy',
    'pyyaml',
    'Scipy',
    'scikit-learn',
    'lxml'
]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author='Lakshman',
    description="A small package for DVC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/lakshman-luq/nlp_dvc_demo.git",
    author_email="hanumandla14334@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
