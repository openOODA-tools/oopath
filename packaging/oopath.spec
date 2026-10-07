Name:           oopath
Version:        0.1.0
Release:        1%{?dist}
Summary:        Sovereign path syntax sanitizer normalizing relative components and dot segments.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oopath
Source0:        oopath-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oopath is a sovereign, capability-bounded PATH MANIPULATOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oopath
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oopath-uninstall

%files
/usr/bin/oopath
/usr/bin/oopath-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
