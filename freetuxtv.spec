Name:		freetuxtv
Summary:	TV player
Version:	0.6.5
Release:1
Group:		Video
License:	GPLv2
Source:		http://freetuxtv.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://freetuxtv.googlecode.com
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libcurl) >= 7.16.4
BuildRequires:	pkgconfig(gdk-2.0) >= 2.22.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:	pkgconfig(libnotify) >= 0.4.0
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libvlc) >= 1.1.0
BuildRequires:	intltool >= 0.35
Requires:	vlc >= 1.1.0


%description
freetuxtv is a player for Television on Internet with french Free
or SFR (ex-Neuf) Internet service providers, and a lot of WebTV in
French languages in the world (Canada, Switzerland, Belgium, etc...).

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x --disable-static --enable-shared
%make

%install
%makeinstall_std
%find_lang %{name}

rm -fr %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/*.la %{buildroot}%{_includedir}


%files -f %{name}.lang
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_libdir}/*.so.*

