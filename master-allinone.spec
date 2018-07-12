%define name master-allinone

Summary: Cs2c Origin Management platform all package dependencies.
Name: %{name}
Version:1.0
Release: 1
Vendor: CS2C
License: GPL
Group: System Environment/Base
BuildRoot: /var/tmp/%{name}-buildroot
Requires: ansible
Requires: apr
Requires: apr-util
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
Requires: httpd-tools
Requires: iptables-services
Requires: libnetfilter_cthelper
Requires: libnetfilter_cttimeout
Requires: libnetfilter_queue
Requires: libtomcrypt
Requires: libtommath
Requires: m4
Requires: oci-register-machine
Requires: oci-systemd-hook
Requires: oci-umount
Requires: openshift-ansible
Requires: openshift-ansible-docs
Requires: openshift-ansible-playbooks
Requires: openshift-ansible-roles
Requires: openvswitch
Requires: origin
Requires: origin-clients
Requires: origin-docker-excluder
Requires: origin-excluder
Requires: origin-master
Requires: origin-node
Requires: origin-sdn-ovs
Requires: ostree
Requires: patch
Requires: perl-Error
Requires: perl-Git
Requires: perl-TermReadKey
Requires: python2-crypto
Requires: python2-cryptography
Requires: python2-jmespath
Requires: python2-pyasn1
Requires: python-babel
Requires: python-cffi
Requires: python-docker-py
Requires: python-docker-pycreds
Requires: python-enum34
Requires: python-httplib2
Requires: python-idna
Requires: python-jinja2
Requires: python-markupsafe
Requires: python-paramiko
Requires: python-passlib
Requires: python-ply
Requires: python-pycparser
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
Requires: sshpass
Requires: PyYAML
Requires: libyaml
Requires: docker >= 1.13
Requires: ansible >= 2.4

%description
This origin master all in one

%prep
%build

%install

%files 
%changelog
