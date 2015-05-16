
%define name nethserver-linux-dash
%define version 1.0.0
%define release 1
Summary: NethServer integration of linux-dash
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name} 
Group: Neth/addon
Source: %{name}-%{version}.tar.gz

BuildArchitectures: noarch
BuildRequires: perl
BuildRequires: nethserver-devtools 
BuildRoot: /var/tmp/%{name}-%{version}
Requires: git
Requires: nethserver-httpd, nethserver-directory
Requires: mod_authnz_external, pwauth
AutoReqProv: no

%description
NethServer integration of Linux-dash

%prep
%setup
%build
perl ./createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
  > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "
 Hi

 All my development work is done in my free time and from my own expenses. 
 If you consider my work as something helpful, thank you to kindly make 
 a donation to my paypal account and allow me to continue paying my server 
 and all associated costs.

 https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZPK8FKHVT4TY8

 Thank in advance.
 
 Stephane de Labrusse Alias Stephdl
"

%preun

%postun
#remove the git repository
rm -rf /usr/share/linux-dash >/dev/null 2>&1
%changelog
* Sat May 16 2015 stephane de labrusse <stephdl@de-labrusse.fr> 1.0.0-1.ns6
- first release to NethServer
