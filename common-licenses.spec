Summary:	Contains the various common licenses uses by the distribution
Name:		common-licenses
Version:	1.1
Release:	%mkrel 2
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Base
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
