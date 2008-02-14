Name: x11-font-type1
Version: 1.0.0
Release: %mkrel 4
Summary: X11 fonts type1
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildArch: noarch
Requires: x11-font-adobe-utopia-type1
Requires: x11-font-bh-type1
Requires: x11-font-bitstream-type1
Requires: x11-font-ibm-type1
Requires: x11-font-xfree86-type1
Conflicts: xorg-x11 <= 6.9.0

%description
Type1 fonts for X.org

%files
%defattr(-,root,root)