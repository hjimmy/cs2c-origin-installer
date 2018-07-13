%define name node-allinone

Summary: Cs2c node all package dependencies.
Name: %{name}
Version:1.0
Release: 1
Vendor: CS2C
License: GPL
Group: System Environment/Base
BuildRoot: /var/tmp/%{name}-buildroot
Requires: ceph-common
Requires: cifs-utils
Requires: conntrack-tools
Requires: container-selinux
Requires: container-storage-setup
Requires: docker
Requires: docker-client
Requires: docker-common
Requires: git
Requires: glusterfs-fuse
Requires: hdparm
Requires: iptables-services
Requires: libnetfilter_cthelper
Requires: libnetfilter_cttimeout
Requires: libnetfilter_queue
Requires: m4
Requires: oci-register-machine
Requires: oci-systemd-hook
Requires: oci-umount
Requires: openvswitch
Requires: origin
Requires: origin-clients
Requires: origin-docker-excluder
Requires: origin-excluder
Requires: origin-node
Requires: origin-sdn-ovs
Requires: ostree
Requires: patch
Requires: perl-Error
Requires: perl-Git
Requires: perl-TermReadKey
Requires: python-docker-py
Requires: python-docker-pycreds
Requires: python-rados
Requires: python-rbd
Requires: python-requests
Requires: python-urllib3
Requires: python-websocket-client
Requires: redhat-lsb-core
Requires: redhat-lsb-submod-security
Requires: skopeo
Requires: skopeo-containers
Requires: socat
Requires: spax
Requires: PyYAML
Requires: libyaml
Requires: docker >= 1.13
Requires: bind
Requires: ntp
Requires: flannel


%description
This origin node all in one

%prep
%build

%install

%files 
%changelog
