# The main Makefile.am for srpmtools project.
# Copyright (C) 2016 Red Hat, Inc.
# Written by Pavel Raiskup <praiskup@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

bin_SCRIPTS =
libexec_SCRIPTS =
noinst_SCRIPTS =

libexec_SCRIPTS += \
	libexec/srpm-build

bin_SCRIPTS += \
	bin/srpm-tool-get-sources \
	bin/srpm-generator

docs = \
	README

noinst_SCRIPTS += build-aux/srpm-tools-install-sh
INSTALL_SCRIPT = build-aux/srpm-tools-install-sh
$(INSTALL_SCRIPT): $(INSTALL_SCRIPT).in config.status
	sed -e "s|[@]bindir@|$(bindir)|g" \
	    -e "s|[@]libexecdir@|$(libexecdir)|g" \
	    -e "s|[@]prefix@|$(prefix)|g" \
	    $< > "$@"
	chmod +x "$@"

EXTRA_DIST = \
	$(docs) \
	$(INSTALL_SCRIPT).in \
	$(bin_SCRIPTS) \
	libexec/srpm-build
