Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		aMule
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/amule/%{name}-%{version}.tar.bz2
# Source0-md5:	61c0b03236a740f916d50e83c1fb6bbd
URL:		http://amule.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7.3
BuildRequires:	bison
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	expat-devel
BuildRequires:	wxGTK-devel >= 2.4.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libstdc++-devel
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xMule is a Linux port of eMule client.

%description -l pl
xMule to linuksowy port klienta eMule.

%prep
%setup  -q

%build

%configure \
	--with-wx-config=/usr/bin/wxgtk-2.4-config 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
