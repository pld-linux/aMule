#
# TODO:
# - split into subpackages
# - package %{_libdir}/xchat/plugins/xas.pl
#
Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		aMule
Version:	2.0.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/amule/%{name}-%{version}.tar.gz
# Source0-md5:	e6680641e171ddf4236c955168947ba0
Patch0:		%{name}-configure_in.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-cas-datadir.patch
URL:		http://www.amule.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7.3
BuildRequires:	bison
#BuildRequires:	cryptopp-devel >= 5.1
BuildRequires:	curl-devel >= 7.9.7
BuildRequires:	expat-devel
BuildRequires:	gd-devel
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	wxBase-devel >= 2.6.0
BuildRequires:	wxGTK2-devel >= 2.6.0
Requires:	wget
Obsoletes:	lmule
Obsoletes:	xmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aMule is a Linux port of eMule client.

%description -l pl
aMule to linuksowy port klienta eMule.

%package plugin-xchat
Summary:	Xchat plugin
Summary(pl):	Wtyczka dla xchat
Requires:	%{name} = %{version}-%{release}
Group:		X11/Applications
Provides:	%{name}-plugin-xchat

%description plugin-xchat
Plugin for Xchat IRC client.

%description plugin-xchat -l pl
Wtczka dla klienta IRC xchat.

%package alc
Summary:	Ed2k link creator for aMule
Summary(pl):	Kreator linków ed2k dla aMule
Requires:	%{name} = %{version}-%{release}
Group:		X11/Applications
Provides:	alc

%description alc
Tool for creating ed2k links.

%description -l pl alc
Narzêdzie do tworzenia linków ed2k.

%package cas
Summary:	aMule online stats
Summary(pl):	Statystyki online aMule
Requires:	%{name} = %{version}-%{release}
Group:		X11/Applications
Provides:	cas

%description cas
Tool for generating aMule online stats.

%description -l cas
Narzêdzie do generownia statystyk aMule.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=%{_bindir}/wx-gtk2-ansi-config	\
	--%{?debug:en}%{!?debug:dis}able-debug		\
	--enable-optimise				\
	--enable-amule-daemon				\
	--enable-amulecmd				\
	--enable-amulecmdgui				\
	--enable-webserver				\
	--enable-webservergui				\
	--enable-cas					\
	--enable-wxcas					\
	--enable-alc					\
	--enable-alcc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{et_EE,et}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}

%find_lang amule

%clean
rm -rf $RPM_BUILD_ROOT

%files -f amule.lang
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/README docs/Changelog docs/ED2K-Links.HOWTO docs/TODO docs/amulesig.txt
%attr(755,root,root) %{_bindir}/amule*
%{_bindir}/ed2k
%dir %{_datadir}/amule
%{_datadir}/amule/webserver
%{_desktopdir}/amule.desktop
%{_pixmapsdir}/amule.xpm
%{_mandir}/man1/amule*
%{_mandir}/man1/ed2k*
%{_mandir}/man1/xas*
%lang(de) %{_mandir}/de/man1/amule*
%lang(de) %{_mandir}/de/man1/ed2k*
%lang(de) %{_mandir}/de/man1/xas*
%lang(es) %{_mandir}/es/man1/amule*
%lang(es) %{_mandir}/es/man1/ed2k*
%lang(es) %{_mandir}/es/man1/xas*
%lang(fr) %{_mandir}/fr/man1/amule*
%lang(fr) %{_mandir}/fr/man1/ed2k*
%lang(hu) %{_mandir}/hu/man1/amule*
%lang(hu) %{_mandir}/hu/man1/ed2k*
%lang(hu) %{_mandir}/hu/man1/xas*

%files plugin-xchat
%defattr(644,root,root,755)
%{_libdir}/xchat/plugins/xas.pl

%files alc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/alc*
%{_desktopdir}/alc.desktop
%{_pixmapsdir}/alc.xpm
%{_mandir}/man1/alc*
%lang(de) %{_mandir}/de/man1/alc*
%lang(es) %{_mandir}/es/man1/alc*
%lang(fr) %{_mandir}/fr/man1/alc*
%lang(hu) %{_mandir}/hu/man1/alc*

%files cas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*cas
%{_datadir}/amule/cas
%{_desktopdir}/*cas.desktop
%{_pixmapsdir}/wxcas.xpm
%{_mandir}/man1/*cas*
%lang(de) %{_mandir}/de/man1/*cas*
%lang(es) %{_mandir}/es/man1/*cas*
%lang(hu) %{_mandir}/hu/man1/*cas*
