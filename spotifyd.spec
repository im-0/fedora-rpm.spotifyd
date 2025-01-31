Name:           spotifyd
Version:        0.3.3
Release:        1%{?dist}
Summary:        An open source Spotify client running as a UNIX daemon.

License:        GPL3
URL:            https://github.com/Spotifyd/spotifyd
Source0:        https://github.com/Spotifyd/spotifyd/archive/v%{version}.zip

# Contains spotifyd-$VERSION/vendor/*.
#     $ cargo vendor
#     $ mkdir spotifyd-X.Y.Z
#     $ mv vendor spotifyd-X.Y.Z/
#     $ tar vcJf spotifyd-X.Y.Z.cargo-vendor.tar.xz spotifyd-X.Y.Z
Source1:        spotifyd-%{version}.cargo-vendor.tar.xz
Source2:        config.toml

BuildRequires:  cargo openssl-devel alsa-lib-devel pulseaudio-libs-devel systemd-rpm-macros dbus-devel
BuildRequires:  rust-packaging

%description


%prep
%autosetup -N -b1 -n spotifyd-%{version}

mkdir .cargo
cp %{SOURCE2} .cargo/

%build
export RUSTFLAGS=-g
%{__cargo} build %{?_smp_mflags} -Z avoid-dev-deps --frozen --release \
        --features "pulseaudio_backend,dbus_keyring,dbus_mpris"

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_userunitdir}

cp target/release/spotifyd %{buildroot}/%{_bindir}/spotifyd
cp contrib/spotifyd.service %{buildroot}/%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%{_bindir}/spotifyd
%{_userunitdir}/%{name}.service
%license LICENSE



%changelog
* Thu Dec 09 2021 Piotr Rogowski <piotrekrogowski@gmail.com> - 0.3.3-1
- new version

* Sat May 01 2021 Piotr Rogowski <piotrekrogowski@gmail.com> - 0.3.2-1
- new version

* Sun Feb 14 2021 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.3.0-1
- new version

* Thu Jan 14 2021 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2.25_1-1
- new version

* Wed Jan 13 2021 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2.25-1
- new version

* Mon Jan 27 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2.24-1
- new version

* Fri Jan 24 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl>
-
