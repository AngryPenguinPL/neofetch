%define debug_package		%{nil}

Summary:	Neofetch is a CLI system information tool written in BASH
Name:		neofetch
Version:	5.0.0
Release:	1
License:	MIT
Group:		Shells
Url:		https://github.com/dylanaraps/neofetch
#Source0:	https://github.com/dylanaraps/neofetch/archive/%{version}/%{name}-%{version}.tar.gz
#Source for master with experimental OpenMandriva support.
Source: https://github.com/dylanaraps/neofetch/archive/801760a01ba7cce2d2c0d02f704c75bd36adceae.zip
BuildArch: 	noarch

%description
Neofetch is a CLI system information tool written in BASH. 
Neofetch displays information about your system next to an 
image, your OS logo, or any ascii file of your choice. 

%prep
%setup -qn %{name}-801760a01ba7cce2d2c0d02f704c75bd36adceae

%build
%make

%install
%makeinstall_std

%files
%doc README.md CHANGELOG.md LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
