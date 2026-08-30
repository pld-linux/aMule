Summary:	Unix port of eMule client
Summary(pl.UTF-8):	Uniksowy port klienta eMule
Name:		aMule
Version:	3.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://github.com/amule-org/amule/releases/download/%{version}/%{name}-%{version}-src.tar.gz
# Source0-md5:	9dd76690485bf002608ced039294b335
Patch0:		%{name}-desktop.patch
URL:		https://amule-org.github.io/
BuildRequires:	binutils-devel
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.70
BuildRequires:	cmake >= 3.13
BuildRequires:	cryptopp-devel >= 5.6
BuildRequires:	curl-devel
BuildRequires:	flex
BuildRequires:	gd-devel >= 2.0.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libayatana-appindicator-gtk3-devel
BuildRequires:	libmaxminddb-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libupnp-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	readline-devel
BuildRequires:	wxGTK3-unicode-devel >= 3.2.0
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-theme
Requires:	hicolor-icon-theme
Obsoletes:	lmule
Obsoletes:	xmule
Obsoletes:	aMule-plugin-xchat < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aMule is a Linux port of eMule client.

%description -l pl.UTF-8
aMule to linuksowy port klienta eMule.

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
%patch -P0 -p1

# the release tarball ships .git_archival.txt with unexpanded $Format: keywords,
# so cmake falls back to PACKAGE_VERSION="GIT"; hand it the real tag instead
echo "describe-name: %{version}" > .git_archival.txt

%build
%cmake -B build \
	-DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}-%{version} \
	-DBUILD_ALC=ON \
	-DBUILD_ALCC=ON \
	-DBUILD_AMULECMD=ON \
	-DBUILD_CAS=ON \
	-DBUILD_DAEMON=ON \
	-DBUILD_ED2K=ON \
	-DBUILD_FILEVIEW=OFF \
	-DBUILD_MONOLITHIC=ON \
	-DBUILD_REMOTEGUI=ON \
	-DBUILD_WEBSERVER=ON \
	-DBUILD_WXCAS=ON \
	-DDEFAULT_VERSION_CHECK=OFF \
	-DENABLE_BFD=ON \
	-DENABLE_CCACHE=OFF \
	-DENABLE_IP2COUNTRY=ON \
	-DENABLE_NLS=ON \
	-DENABLE_UPNP=ON \
	-DTRANSLATED_MANPAGES=OFF \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk3-unicode-config

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/et{_EE,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/ko{_KR,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
%find_lang amule

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f amule.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/amule*
%attr(755,root,root) %{_bindir}/ed2k
%dir %{_datadir}/amule
%{_datadir}/amule/webserver
%{_datadir}/amule/skins
%{_desktopdir}/org.amule.aMule.desktop
%{_desktopdir}/org.amule.aMule.gui.desktop
%{_datadir}/metainfo/org.amule.aMule.metainfo.xml
%{_iconsdir}/hicolor/128x128/apps/org.amule.aMule.png
%{_iconsdir}/hicolor/256x256/apps/org.amule.aMule.png
%{_pixmapsdir}/org.amule.aMule.png
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
%lang(pt_BR) %{_mandir}/pt_BR/man1/amule*.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/ed2k.1*
%lang(ro) %{_mandir}/ro/man1/amule*.1*
%lang(ro) %{_mandir}/ro/man1/ed2k.1*
%lang(ru) %{_mandir}/ru/man1/amule*.1*
%lang(ru) %{_mandir}/ru/man1/ed2k.1*
%lang(tr) %{_mandir}/tr/man1/amule*.1*
%lang(tr) %{_mandir}/tr/man1/ed2k.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/amule*.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/ed2k.1*

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
%lang(pt_BR) %{_mandir}/pt_BR/man1/alc.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/alcc.1*
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
%{_datadir}/cas
%{_desktopdir}/wxcas.desktop
%{_pixmapsdir}/wxcas.xpm
%{_mandir}/man1/cas.1*
%{_mandir}/man1/wxcas.1*
%lang(de) %{_mandir}/de/man1/cas.1*
%lang(de) %{_mandir}/de/man1/wxcas.1*
%lang(es) %{_mandir}/es/man1/cas.1*
%lang(es) %{_mandir}/es/man1/wxcas.1*
%lang(fr) %{_mandir}/fr/man1/cas.1*
%lang(fr) %{_mandir}/fr/man1/wxcas.1*
%lang(hu) %{_mandir}/hu/man1/cas.1*
%lang(hu) %{_mandir}/hu/man1/wxcas.1*
%lang(it) %{_mandir}/it/man1/cas.1*
%lang(it) %{_mandir}/it/man1/wxcas.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cas.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/wxcas.1*
%lang(ro) %{_mandir}/ro/man1/cas.1*
%lang(ro) %{_mandir}/ro/man1/wxcas.1*
%lang(ru) %{_mandir}/ru/man1/cas.1*
%lang(ru) %{_mandir}/ru/man1/wxcas.1*
%lang(tr) %{_mandir}/tr/man1/cas.1*
%lang(tr) %{_mandir}/tr/man1/wxcas.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/cas.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/wxcas.1*
