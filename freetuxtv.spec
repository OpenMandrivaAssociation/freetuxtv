%define name    freetuxtv
%define version 0.4.1
%define release %mkrel 4

Name:		%{name} 
Summary:	Freetuxtv - TV player
Version:	%{version}
Release:	%{release}
Source:		http://freetuxtv.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://freetuxtv.googlecode.com

Group:          Video
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
License:	GPLv2
Requires:	vlc >= 0.9.8
BuildRequires: gettext-devel
BuildRequires: curl-devel >= 7.16.4
BuildRequires: hal-devel >= 0.5.0
BuildRequires: gtk+2-devel >= 2.12.0
BuildRequires: glib2-devel >= 2.16.0
BuildRequires: libglade2-devel >= 2.6.0
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: libnotify-devel >= 0.4.0
BuildRequires: sqlite3-devel
BuildRequires: libstdc++-devel
BuildRequires: vlc-devel >= 0.9.2
BuildRequires: intltool >= 0.35

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
freetuxtv is a player for Television on Internet with french Free
or SFR (ex-Neuf) Internet service providers, and a lot of WebTV in
french languages in the world (Canada, Switzerland, Belgium, etc...).

%prep
%setup -q -n %{name}-%{version}

%build 
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/*.so.*
%exclude %{_libdir}/*.so
%exclude %{_libdir}/*.la
%exclude %{_includedir}
