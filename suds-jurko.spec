#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : suds-jurko
Version  : 0.6
Release  : 28
URL      : https://bitbucket.org/jurko/suds/downloads/suds-jurko-0.6.tar.bz2
Source0  : https://bitbucket.org/jurko/suds/downloads/suds-jurko-0.6.tar.bz2
Summary  : Lightweight SOAP client (Jurko's fork)
Group    : Development/Tools
License  : LGPL-3.0
Requires: suds-jurko-license = %{version}-%{release}
Requires: suds-jurko-python = %{version}-%{release}
Requires: suds-jurko-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
---------------------------------------
        Lightweight SOAP client (Jurko's fork).
        ---------------------------------------
        
          Based on the original 'suds' project by Jeff Ortel (jortel at redhat

%package license
Summary: license components for the suds-jurko package.
Group: Default

%description license
license components for the suds-jurko package.


%package python
Summary: python components for the suds-jurko package.
Group: Default
Requires: suds-jurko-python3 = %{version}-%{release}

%description python
python components for the suds-jurko package.


%package python3
Summary: python3 components for the suds-jurko package.
Group: Default
Requires: python3-core
Provides: pypi(suds_jurko)

%description python3
python3 components for the suds-jurko package.


%prep
%setup -q -n suds-jurko-0.6
cd %{_builddir}/suds-jurko-0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583458054
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/suds-jurko
cp %{_builddir}/suds-jurko-0.6/LICENSE.txt %{buildroot}/usr/share/package-licenses/suds-jurko/adbfde070cbf605aea1261de577ac0d2b2c12d68
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__init__.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__pycache__/__init__.cpython-3*.pyc

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/suds-jurko/adbfde070cbf605aea1261de577ac0d2b2c12d68

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
