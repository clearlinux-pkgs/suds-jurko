#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : suds-jurko
Version  : 0.6
Release  : 5
URL      : https://bitbucket.org/jurko/suds/downloads/suds-jurko-0.6.tar.bz2
Source0  : https://bitbucket.org/jurko/suds/downloads/suds-jurko-0.6.tar.bz2
Summary  : Lightweight SOAP client (Jurko's fork)
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: suds-jurko-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Overview
=================================================
"Suds" is a lightweight SOAP-based web service client for Python licensed under
LGPL (see the ``LICENSE.txt`` file included in the distribution).

%package python
Summary: python components for the suds-jurko package.
Group: Default

%description python
python components for the suds-jurko package.


%prep
%setup -q -n suds-jurko-0.6

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
