%define name    freetuxtv
%define version 0.3.0
%define release %mkrel 1

Name:		%{name} 
Summary:	Freetuxtv - TV player
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.gz
URL:		http://freetuxtv.googlecode.com
Patch1:		freetuxtv-0.3.0-desktop.patch
Group:          Video
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
License:	GPLv2
Requires:	vlc >= 0.9.8
BuildRequires: gettext-devel
BuildRequires: libcurl-devel >= 7.16.4
BuildRequires: libhal-devel >= 0.5.0
BuildRequires: libgtk+2.0_0-devel >= 2.12.0
BuildRequires: libglib2.0-devel >= 2.16.0
BuildRequires: libglade2.0_0-devel >= 2.6.0
BuildRequires: libdbus-glib-1_2-devel >= 0.74
BuildRequires: libnotify-devel >= 0.4.0
BuildRequires: libsqlite3-devel >= 3.4.0
BuildRequires: libstdc++-devel
BuildRequires: vlc-devel >= 0.9.2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
freetuxtv is a player for Television on Internet with french Free
or SFR (ex-Neuf) Internet service providers, and a lot of WebTV in
french languages in the world (Canada, Switzerland, Belgium, etc...).

%prep
%setup -q
%patch1 -p0 -b .desktop

%build 
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/channel_logos.xml
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/%{name}/images/%{name}.ico
%{_datadir}/%{name}/images/channels/*.png
%{_datadir}/%{name}/sqlite3-create-tables.sql
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
