%define name    freetuxtv
%define version 0.5.2
%define release %mkrel 1

Name:		%{name} 
Summary:	Freetuxtv - TV player
Version:	%{version}
Release:	%{release}
Source:		http://freetuxtv.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		freetuxtv-0.5.2-libnotify0.7.patch
Patch1:		freetuxtv-0.5.2-gcc46.patch
URL:		http://freetuxtv.googlecode.com

Group:          Video
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
License:	GPLv2
Requires:	vlc >= 1.1.0
BuildRequires: gettext-devel
BuildRequires: curl-devel >= 7.16.4
BuildRequires: gtk+2-devel >= 2.12.0
BuildRequires: glib2-devel >= 2.16.0
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: libnotify-devel >= 0.4.0
BuildRequires: sqlite3-devel
BuildRequires: vlc-devel >= 1.1.0
BuildRequires: intltool >= 0.35

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
freetuxtv is a player for Television on Internet with french Free
or SFR (ex-Neuf) Internet service providers, and a lot of WebTV in
french languages in the world (Canada, Switzerland, Belgium, etc...).

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
%configure2_5x --disable-static --enable-shared
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}

rm -fr %buildroot%_libdir/*.so %buildroot%_libdir/*.la %buildroot%_includedir

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_libdir}/*.so.*
