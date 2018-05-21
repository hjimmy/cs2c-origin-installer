%define name etcd-allinone

Summary: Cs2c etcd all package dependencies.
Name: %{name}
Version:1.0
Release: 1
Vendor: CS2C
License: GPL
Group: System Environment/Base
BuildRoot: /var/tmp/%{name}-buildroot
Requires: etcd
Requires: iptables-services


%description
This origin etcd all in one

%prep
%build

%install

%files 
%changelog
