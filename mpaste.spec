%define VERSION 0.1
%define RELEASE 1
%define HASH 1a23b45

Name:		mpaste
Version:	%{VERSION}
Release:	%{RELEASE}.%{HASH}%{dist}
Summary:	Lean, mean and clean, pastebinnin' machine.

Group:		Utilities/Misc
License:	AGPL
URL:		https://github.com/firnsy/mpaste
Source0:	%{name}-%{version}-%{HASH}.tar.gz

BuildArch:	noarch
Requires:	perl-Mojolicious
Requires:	perl-DBD-SQLite

%description
Lean, mean and clean, pastebinnin' machine.

%prep
%setup -q

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/%{name} %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/etc/sysconfig
mkdir -p %{buildroot}/etc/profile.d
cp -a %{_builddir}/%{name}-%{version}/{public,mpasted,LICENSE} %{buildroot}/usr/share/%{name}
cp -a %{_builddir}/%{name}-%{version}/tools/%{name} %{buildroot}/usr/bin
cp -a %{_builddir}/%{name}-%{version}/etc/%{name}.service %{buildroot}/usr/lib/systemd/system
cp -a %{_builddir}/%{name}-%{version}/etc/profile.sh %{buildroot}/etc/profile.d/%{name}.sh
cp -a %{_builddir}/%{name}-%{version}/mpaste.conf %{buildroot}/etc/sysconfig/%{name}

%pre
id %{name} &>/dev/null || {
  useradd --home-dir /var/lib/mpaste \
    --create-home --system %{name} \
    --shell /sbin/nologin

  # permissions do not appear to be set correctly by useradd 
  # when invoked during RPM install. The following 
  # corrects that with the subtlety of Mjolnir
  chown mpaste.mpaste /var/lib/mpaste
  chmod 755 /var/lib/mpaste
}

%post
systemctl daemon-reload &>/dev/null

%files
%defattr(-,root,root,-)
%attr(755,root,root) /usr/share/%{name}/mpasted
%attr(644,root,root) /usr/share/%{name}/LICENSE
/usr/share/%{name}/public/*
%config(noreplace) %attr(644,root,root) /etc/sysconfig/%{name}
%attr(644,root,root) /usr/lib/systemd/system/%{name}.service

%package cli
Version:	%{VERSION}
Summary:	Command line mpaste client
Group:		Utilities/Misc
Requires:	curl
%description cli
Command line client for posting data to an mpaste server

%files cli
%attr(755,root,root) /usr/bin/%{name}
%attr(644,root,root) /etc/profile.d/%{name}.sh

%changelog
