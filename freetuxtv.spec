Summary:	TV player
Name:		freetuxtv
Version:	0.6.6
Release:	2
License:	GPLv2+
Group:		Video
Url:		http://freetuxtv.googlecode.com
Source0:	http://freetuxtv.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	freetuxtv-ru.po
Source2:	freetuxtv-ru.gmo
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(sqlite3)
Requires:	vlc

%description
freetuxtv is a player for Television on Internet with french Free
or SFR (ex-Neuf) Internet service providers, and a lot of WebTV in
French languages in the world (Canada, Switzerland, Belgium, etc...).

%files -f %{name}.lang
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*

#----------------------------------------------------------------------------

%prep
%setup -q
cp %{SOURCE1} po/ru.po
cp %{SOURCE2} po/ru.gmo

%build
autoreconf -fi
%configure2_5x --with-gtk=3.0
%make

%install
%makeinstall_std

%find_lang %{name}

rm -fr %{buildroot}%{_libdir}/*.a
rm -fr %{buildroot}%{_includedir}

