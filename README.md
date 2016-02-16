# Geohazards platform Documentation

[![Join the chat at https://gitter.im/geohazards-tep/doc-tep-geohazards-nsbas](https://badges.gitter.im/geohazards-tep/doc-tep-geohazards-nsbas.svg)](https://gitter.im/geohazards-tep/doc-tep-geohazards-nsbas?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is the official repository of Tep Geohazards platform's Documentation. This
documentation is live at:
[http://terradue.github.io/doc-tep-geohazards](http://terradue.github.io/doc-tep-geohazards).

You are encouraged to fork this repo and send us pull requests!

## Getting started

Here's the procedure to install the required packages on a CentOS 6.x

```
sudo yum install python-sphinx
sudo yum install python-pip
pip install sphinx_bootstrap_theme
git clone git@github.com:Terradue/doc-tep-geohazards.git
```

If needed, set your github information

```
git config --global user.name <github username>
git config --global user.email <email address>
```

## Building

Build the documentation by running ``make html``.

## Publish the documentation

``make html`` creates a ``build`` folder in the doc-tep-geohazards local repository.

As root, do:

```
cd /var/www/html
ln -s /home/fbrito/doc-tep-geohazards/build/html/ doc-tep-geohazards
chown apache:apache data-tep-geohazards
```
> Replace /home/fbrito with the path to the folder where you have cloned the repository

Open you browser at the address http://127.0.0.1/doc-tep-geohazards

## This documentation is built with sphinx-doc

[More information](http://sphinx-doc.org/).
