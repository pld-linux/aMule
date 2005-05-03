Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		aMule
Version:	2.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/amule/%{name}-%{version}.tar.gz
# Source0-md5:	e6680641e171ddf4236c955168947ba0
Patch0:		%{name}-configure_in.patch
Patch1:		%{name}-desktop.patch
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
BuildRequires:	wxBase-devel >= 2.4.2
BuildRequires:	wxGTK2-devel >= 2.4.2
Requires:	wget
Obsoletes:	lmule
Obsoletes:	xmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aMule is a Linux port of eMule client.

%description -l pl
aMule to linuksowy port klienta eMule.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=/usr/bin/wxgtk2-2.4-config	\
	--enable-optimise				\
	--enable-amulecmd				\
	--enable-amulecmdgui				\
	--enable-webserver				\
	--enable-webservergui

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}%{_rc}	\
    $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang amule

%clean
rm -rf $RPM_BUILD_ROOT

%files -f amule.lang
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/README docs/Changelog docs/ED2K-Links.HOWTO docs/TODO docs/amulesig.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/amuleweb
%{_datadir}/cas
