Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		aMule
Version:	1.2.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/amule/%{name}-%{version}.tar.bz2
# Source0-md5:	a6fe7157000efdc5985dfc8774efbccd
Patch0: 	%{name}-po_makefile.patch
URL:		http://developer.berlios.de/projects/amule/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7.3
BuildRequires:	bison
BuildRequires:	curl-devel >= 7.9.7
BuildRequires:	expat-devel
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRequires:	wxBase-devel >= 2.4.0
Requires:	wget
Obsoletes:      xmule
Obsoletes:      lmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aMule is a Linux port of eMule client.

%description -l pl
aMule to linuksowy port klienta eMule.

%prep
%setup  -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=/usr/bin/wxgtk2-2.4-config \
	--enable-optimise

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang amule

%clean
rm -rf $RPM_BUILD_ROOT

%files -f amule.lang
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/README docs/Changelog docs/ED2K-Links.HOWTO docs/TODO docs/eMule-Imports-Status docs/amulesig.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
