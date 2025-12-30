Name:		python-humanize
Version:	4.15.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/humanize/humanize-%{version}.tar.gz
Summary:	Python humanize utilities
URL:		https://pypi.org/project/humanize/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildSystem:	python
BuildArch:	noarch

%description
Python humanize utilities

%files
%{py_sitedir}/humanize
%{py_sitedir}/humanize-*.*-info
