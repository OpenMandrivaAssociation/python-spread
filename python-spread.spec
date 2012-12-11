Summary:	Python wrapper for Spread client libraries
Name:		python-spread
Version:	1.5
Release:	4
Group:		Development/Python
License:	BSD-style
URL:		http://www.zope.org/Members/tim_one/spread/
Source0:	http://www.zope.org/Members/tim_one/spread/SpreadModule-%{version}/SpreadModule-%{version}.tgz
Patch0:		SpreadModule-1.5-fix-for-spread4.patch
Requires:	spread >= 4.0.0
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
%patch0 -p1

%build

python setup.py build_ext

%install
python setup.py install --root %{buildroot} --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc CHANGES doc.txt LICENSE README TODO.txt



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1:1.5-3mdv2010.0
+ Revision: 442489
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 1:1.5-2mdv2009.1
+ Revision: 323370
- rebuild

* Tue Oct 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.5-1mdv2009.1
+ Revision: 297900
- import python-spread


* Tue Oct 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.5-1mdv2009.0
- initial Mandriva package
