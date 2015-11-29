#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define 	module	pyramid_beaker
Summary:	Beaker session factory backend for Pyramid
Name:		python-%{module}
Version:	0.7
Release:	1
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pyramid_beaker/%{module}-%{version}.tar.gz
# Source0-md5:	acb863517a98b90b5f29648ce55dd563
URL:		http://docs.pylonsproject.org/projects/pyramid_beaker/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-Beaker
Requires:	python-pyramid
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a session factory for the Pyramid web framework backed by the
Beaker sessioning system.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests.py*

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
