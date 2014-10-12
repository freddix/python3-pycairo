Summary:	Python 3.x Cairo bindings
Name:		python3-pycairo
Version:	1.10.0
Release:	2
License:	LGPL v3
Group:		Libraries
Source0:	http://cairographics.org/releases/pycairo-%{version}.tar.bz2
# Source0-md5:	e6fd3f2f1e6a72e0db0868c4985669c5
URL:		http://cairographics.org/
BuildRequires:	cairo-devel
BuildRequires:	pkg-config
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 3.x Cairo bindings.

%package devel
Summary:	Development files for pycairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for pycairo.

%prep
%setup -qn pycairo-%{version}

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CPP="%{__cpp}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export PYTHONDIR="%{py3_sitedir}"
export PYTHON=python3
%{__python3} ./waf %{?_smp_mflags} configure \
	--libdir=%{_libdir} \
	--prefix=%{_prefix}

python3 ./waf build

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} ./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%dir %{py3_sitedir}/cairo
%attr(755,root,root) %{py3_sitedir}/cairo/_cairo.so
%{py3_sitedir}/cairo/*.py
%{py3_sitedir}/cairo/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/pycairo
%{_pkgconfigdir}/py3cairo.pc

