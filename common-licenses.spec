%define name	common-licenses
%define version	1.0
%define rel	12
%define release	%mkrel %{rel}

Summary:	Contains the various common licenses uses by the distribution
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}.tar.lzma
License:	GPLv2+
Group:		System/Base
BuildArch:	noarch

%description
Contains the various common licenses uses by the distribution. Instead of
including the COPYING file in every package, just refer to this one.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}
cp -a %{name} %{buildroot}%{_datadir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/%{name}


