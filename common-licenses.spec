Summary:	Contains the various common licenses uses by the distribution
Name:		common-licenses
Version:	1.1
Release:	%mkrel 3
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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdv2011.0
+ Revision: 663392
- mass rebuild

* Thu Oct 21 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-1mdv2011.0
+ Revision: 587137
- bump version to 1.1:
  	o remove BSD license as the license is specific to the software itself
  	  and requires for the individual licenses to be ccarried
  	o move ZPL license into the right directory so that it gets packaged
  	o change name format from FOO-VERSION to FOOvVERSION for it to be
  	  consistent with naming convention used for rpm License tag, thus
  	  useful for tools such as ie. rpmlint etc. to check against
  	o switch to use xz compression for tarball

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-16mdv2010.1
+ Revision: 522389
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-15mdv2010.0
+ Revision: 413259
- rebuild

* Wed Mar 18 2009 Emmanuel Andry <eandry@mandriva.org> 1.0-14mdv2009.1
+ Revision: 357515
- add ZPL (#24175)

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0-13mdv2009.1
+ Revision: 350731
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-12mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 13 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-12mdv2008.0
+ Revision: 85215
- drop LGPLv2 - LGPLv2 and LGPLv2.1 are identical except for the name, there's no need to have both
- update GFDL to 1.2
- add GPLv3 and LGPLv3
- Fedora license policy


* Thu Dec 14 2006 Eskild Hustvedt <eskild@mandriva.org> 1.0-11mdv2007.0
+ Revision: 97163
- Yearly rebuild
- Import common-licenses

* Wed Aug 24 2005 Eskild Hustvedt <eskild@mandriva.org> 1.0-10mdk
- FSF has changed it address, added updated gpl from http://www.gnu.org/licenses/gpl.txt
- %%mkrel

* Wed Mar 02 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-9mdk
- added the GNU Free Documentation License (GFDL)

* Sat May 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-8mdk
- added the apache v2 license

