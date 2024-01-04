BuildArch:      noarch
Name:           aps-dts-user
Version:        1.2.1
Release:        1
License:        GPLv3
Group:          Unspecified
Summary:        A RPM package containing the APSensing dts user configuration
Distribution:   PhotonPonyOS

URL:            https://github.com/AP-Sensing/aps-dts-user/tree/ppos38
Vendor:         AP Sensing
Packager:       AP Sensing
Provides:       aps-dts-user = %{version}-%{release}

Source0:        %{_sourcedir}/dts_user.conf
Source1:        %{_sourcedir}/dts_home.conf

Requires:       (systemd or systemd-standalone-sysusers)
Requires:       (systemd or systemd-standalone-tmpfiles)

%description
A RPM package containing the APSensing dts user configuration.

%install
install -d -m 755 $RPM_BUILD_ROOT/usr/lib/sysusers.d/
install -m 644 %{_sourcedir}/dts_user.conf $RPM_BUILD_ROOT/usr/lib/sysusers.d/dts.conf

install -d -m 755 $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/
install -m 644 %{_sourcedir}/dts_home.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/dts.conf

%post
# Do not run those commands during post since then ostree user integration will be broken and running sudo commands for the dts user is broken.
# This results in the same issue as described here: https://gitlab.bbn.apsensing.com/infrastructure/ppos/ppos/-/issues/47
# /usr/bin/systemd-sysusers /usr/lib/sysusers.d/dts.conf
# /usr/bin/systemd-tmpfiles --create /usr/lib/tmpfiles.d/dts.conf

%files
%attr(644, root, root) /usr/lib/sysusers.d/dts.conf
%attr(644, root, root) /usr/lib/tmpfiles.d/dts.conf

%changelog
* Thu Jan 04 2024 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.2.1-1
- Not creating user and tmp files during post to prevent sudo issues

* Thu Dec 21 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.2.0-1
- Creating the dts home dir during installation

* Wed Dec 20 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.1.0-1
- Using systemd-sysusers for managing the dts user

* Fri Sep 22 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-2
- Empty ghost file to fix RPM generation

* Fri Sep 22 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-1
- Initial release
