Name:		ql23xx-firmware
Summary: 	Firmware for qlogic 23xx devices
Version:	3.03.27
Release:	3.1%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/ql2300_fw.bin
Source1:	ftp://ftp.qlogic.com/outgoing/linux/firmware/ql2322_fw.bin
Source2:	ftp://ftp.qlogic.com/outgoing/linux/firmware/LICENSE
URL:		ftp://ftp.qlogic.com/outgoing/linux/firmware/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Firmware for qlogic 2300 and 2322 devices.

%prep
%setup -n %{name} -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
# Firmware, do nothing.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware/
install -m0644 ql2300_fw.bin $RPM_BUILD_ROOT/lib/firmware/
install -m0644 ql2322_fw.bin $RPM_BUILD_ROOT/lib/firmware/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
/lib/firmware/ql2300_fw.bin
/lib/firmware/ql2322_fw.bin

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.03.27-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.03.27-1
- update to 3.03.27

* Wed Oct 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.03.20-1
- Initial package for Fedora
