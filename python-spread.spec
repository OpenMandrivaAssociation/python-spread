Summary:	Python wrapper for Spread client libraries
Name:		python-spread
Version:	1.5
Release:	%mkrel 2
Group:		Development/Python
License:	BSD-style
URL:		http://www.zope.org/Members/tim_one/spread/
Source0:	http://www.zope.org/Members/tim_one/spread/SpreadModule-%{version}/SpreadModule-%{version}.tgz
BuildRequires:	python-devel
BuildRequires:	spread-devel >= 4.0.0
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains a simple Python wrapper module for the Spread toolkit.
The wrapper is known to be compatible with Python 2.3 and 2.4. It may work
with earlier Pythons, but this has not been tested.

%prep

%setup -q -n SpreadModule-%{version}

# instead of a patch...
perl -pi -e "s|/usr/local|%{_prefix}|g" setup.py
perl -pi -e "s|/lib\b|/%{_lib}|g" setup.py
perl -pi -e "s|\'tspread\'|\'tspread-core\'|g" setup.py

%build

python setup.py build_ext

%install
rm -rf %{buildroot}

python setup.py install --root %{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc CHANGES doc.txt LICENSE README TODO.txt

