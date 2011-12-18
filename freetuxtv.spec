Name:		freetuxtv
Summary:	Freetuxtv - TV player
Version:	0.6.1
Release:	%mkrel 1
Group:		Video
License:	GPLv2
Source:		http://freetuxtv.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://freetuxtv.googlecode.com
BuildRequires:	gettext-devel
BuildRequires:	curl-devel >= 7.16.4
BuildRequires:	gtk+2-devel >= 2.22.0
BuildRequires:	glib2-devel >= 2.16.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	sqlite3-devel
BuildRequires:	vlc-devel >= 1.1.0
BuildRequires:	intltool >= 0.35
Requires:	vlc >= 1.1.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
freetuxtv is a player for Television on Internet with french Free
or SFR (ex-Neuf) Internet service providers, and a lot of WebTV in
french languages in the world (Canada, Switzerland, Belgium, etc...).

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x --disable-static --enable-shared
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

rm -fr %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/*.la %{buildroot}%{_includedir}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_libdir}/*.so.*
