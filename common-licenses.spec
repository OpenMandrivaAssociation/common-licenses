Summary:	Contains the various common licenses uses by the distribution
Name:		common-licenses
Version:	1.1
Release:	13
License:	GPLv2+
Group:		System/Base
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
Contains the various common licenses uses by the distribution. Instead of
including the COPYING file in every package, just refer to this one.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}
cp -a %{name} %{buildroot}%{_datadir}

%files
%{_datadir}/%{name}

