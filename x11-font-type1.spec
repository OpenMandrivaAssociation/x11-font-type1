Name: x11-font-type1
Version: 1.0.0
Release: 16
Summary: X11 fonts type1
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildArch: noarch
Requires: x11-font-bitstream-type1
Requires: x11-font-xfree86-type1
Conflicts: xorg-x11 <= 6.9.0

%description
Type1 fonts for X.org

%files
%defattr(-,root,root)


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.0-10mdv2011.0
+ Revision: 675585
- rebuild
- br fontconfig for fc-query used in new rpm-setup-build

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9
+ Revision: 671220
- mass rebuild

* Thu Jan 21 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-8mdv2011.0
+ Revision: 494706
- Don't require non-free fonts

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-7mdv2009.1
+ Revision: 351265
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 226005
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2008.1
+ Revision: 179645
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2008.0
+ Revision: 75831
- rebuild


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

