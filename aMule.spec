#
# TODO: ./configure --enable-plasmamule (BR: qt4-build, QtCore 4, KDE 4)
#
Summary:	Unix port of eMule client
Summary(pl.UTF-8):	Uniksowy port klienta eMule
Name:		aMule
Version:	2.3.2
Release:	6
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/amule/%{name}-%{version}.tar.bz2
# Source0-md5:	4516bde73327e6153c140cef59375f38
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-cas-datadir.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-cryptopp.patch
URL:		http://www.amule.org/
BuildRequires:	GeoIP-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7.3
BuildRequires:	binutils-devel
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.47
BuildRequires:	cryptopp-devel >= 5.1
BuildRequires:	curl-devel >= 7.9.7
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	gd-devel >= 2.0.0
BuildRequires:	gettext-tools >= 0.11.5
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libupnp-devel >= 1.6.6
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	readline-devel
BuildRequires:	wxGTK2-unicode-devel >= 2.8.12
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel >= 1.1.4
Requires:	cryptopp >= 5.1
Requires:	gd >= 2.0.0
Requires:	libupnp >= 1.6.6
Requires:	wget
Requires:	zlib >= 1.1.4
Obsoletes:	lmule
Obsoletes:	xmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aMule is a Linux port of eMule client.

%description -l pl.UTF-8
aMule to linuksowy port klienta eMule.

%package plugin-xchat
Summary:	Xchat plugin
Summary(pl.UTF-8):	Wtyczka dla xchat
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-plugin-xchat

%description plugin-xchat
Plugin for Xchat IRC client.

%description plugin-xchat -l pl.UTF-8
Wtyczka dla klienta IRC xchat.

%package alc
Summary:	Ed2k link creator for aMule
Summary(pl.UTF-8):	Kreator linków ed2k dla aMule
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Provides:	alc

%description alc
Tool for creating ed2k links.

%description alc -l pl.UTF-8
Narzędzie do tworzenia linków ed2k.

%package cas
Summary:	aMule online stats
Summary(pl.UTF-8):	Statystyki online aMule
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Provides:	cas

%description cas
Tool for generating aMule online stats.

%description cas -l pl.UTF-8
Narzędzie do generownia statystyk aMule.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-denoise-level=1				\
	--with-libpng-config=/usr/bin/libpng-config	\
	--with-wx-config=wx-gtk2-unicode-config		\
	--enable-alc					\
	--enable-alcc					\
	--enable-amulecmd				\
	--enable-amule-daemon				\
	--enable-amule-gui				\
	--enable-cas					\
	--enable-debug%{!?debug:=no}			\
	--enable-geoip					\
	--enable-optimize%{!?debug:=no}			\
	--enable-webserver				\
	--enable-wxcas					\
	--enable-xas

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/et{_EE,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/ko{_KR,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/amule
%find_lang amule

%clean
rm -rf $RPM_BUILD_ROOT

%files -f amule.lang
%defattr(644,root,root,755)
%doc docs/ABOUT-NLS docs/AUTHORS docs/Changelog docs/EC_Protocol.txt docs/README docs/TODO docs/amulesig.txt
%attr(755,root,root) %{_bindir}/autostart-xas
%attr(755,root,root) %{_bindir}/amule*
%attr(755,root,root) %{_bindir}/ed2k
%dir %{_datadir}/amule
%{_datadir}/amule/webserver
%{_datadir}/amule/skins
%{_desktopdir}/amule.desktop
%{_desktopdir}/amulegui.desktop
%{_pixmapsdir}/amule.xpm
%{_pixmapsdir}/amulegui.xpm
%{_mandir}/man1/amule*.1*
%{_mandir}/man1/ed2k.1*
%lang(de) %{_mandir}/de/man1/amule*.1*
%lang(de) %{_mandir}/de/man1/ed2k.1*
%lang(es) %{_mandir}/es/man1/amule*.1*
%lang(es) %{_mandir}/es/man1/ed2k.1*
%lang(fr) %{_mandir}/fr/man1/amule*.1*
%lang(fr) %{_mandir}/fr/man1/ed2k.1*
%lang(hu) %{_mandir}/hu/man1/amule*.1*
%lang(hu) %{_mandir}/hu/man1/ed2k.1*
%lang(it) %{_mandir}/it/man1/amule*.1*
%lang(it) %{_mandir}/it/man1/ed2k.1*
%lang(ro) %{_mandir}/ro/man1/amule*.1*
%lang(ro) %{_mandir}/ro/man1/ed2k.1*
%lang(ru) %{_mandir}/ru/man1/amule*.1*
%lang(ru) %{_mandir}/ru/man1/ed2k.1*
%lang(tr) %{_mandir}/tr/man1/amule*.1*
%lang(tr) %{_mandir}/tr/man1/ed2k.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/amule*.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/ed2k.1*

%files plugin-xchat
%defattr(644,root,root,755)
%{_libdir}/xchat/plugins/xas.pl
%{_mandir}/man1/xas.1*
%lang(de) %{_mandir}/de/man1/xas.1*
%lang(es) %{_mandir}/es/man1/xas.1*
%lang(fr) %{_mandir}/fr/man1/xas.1*
%lang(hu) %{_mandir}/hu/man1/xas.1*
%lang(it) %{_mandir}/it/man1/xas.1*
%lang(ro) %{_mandir}/ro/man1/xas.1*
%lang(ru) %{_mandir}/ru/man1/xas.1*
%lang(tr) %{_mandir}/tr/man1/xas.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/xas.1*

%files alc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/alc
%attr(755,root,root) %{_bindir}/alcc
%{_desktopdir}/alc.desktop
%{_pixmapsdir}/alc.xpm
%{_mandir}/man1/alc.1*
%{_mandir}/man1/alcc.1*
%lang(de) %{_mandir}/de/man1/alc.1*
%lang(de) %{_mandir}/de/man1/alcc.1*
%lang(es) %{_mandir}/es/man1/alc.1*
%lang(es) %{_mandir}/es/man1/alcc.1*
%lang(fr) %{_mandir}/fr/man1/alc.1*
%lang(fr) %{_mandir}/fr/man1/alcc.1*
%lang(hu) %{_mandir}/hu/man1/alc.1*
%lang(hu) %{_mandir}/hu/man1/alcc.1*
%lang(it) %{_mandir}/it/man1/alc.1*
%lang(it) %{_mandir}/it/man1/alcc.1*
%lang(ro) %{_mandir}/ro/man1/alc.1*
%lang(ro) %{_mandir}/ro/man1/alcc.1*
%lang(ru) %{_mandir}/ru/man1/alc.1*
%lang(ru) %{_mandir}/ru/man1/alcc.1*
%lang(tr) %{_mandir}/tr/man1/alc.1*
%lang(tr) %{_mandir}/tr/man1/alcc.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/alc.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/alcc.1*

%files cas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cas
%attr(755,root,root) %{_bindir}/wxcas
%{_datadir}/amule/cas
%{_desktopdir}/wxcas.desktop
%{_pixmapsdir}/wxcas.xpm
%{_mandir}/man1/cas.1*
%{_mandir}/man1/wxcas.1*
%lang(de) %{_mandir}/de/man1/cas.1*
%lang(de) %{_mandir}/de/man1/wx*cas.1*
%lang(es) %{_mandir}/es/man1/cas.1*
%lang(es) %{_mandir}/es/man1/wxcas.1*
%lang(fr) %{_mandir}/fr/man1/cas.1*
%lang(fr) %{_mandir}/fr/man1/wxcas.1*
%lang(hu) %{_mandir}/hu/man1/cas.1*
%lang(hu) %{_mandir}/hu/man1/wxcas.1*
%lang(it) %{_mandir}/it/man1/cas.1*
%lang(it) %{_mandir}/it/man1/wxcas.1*
%lang(ro) %{_mandir}/ro/man1/cas.1*
%lang(ro) %{_mandir}/ro/man1/wxcas.1*
%lang(ru) %{_mandir}/ru/man1/cas.1*
%lang(ru) %{_mandir}/ru/man1/wxcas.1*
%lang(tr) %{_mandir}/tr/man1/cas.1*
%lang(tr) %{_mandir}/tr/man1/wxcas.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/cas.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/wxcas.1*
