"""
pythonedaeventnixflakes/flake_created.py

This file defines the FlakeCreated event class.

Copyright (C) 2023-today rydnr's pythoneda-event/nix-flakes

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythoneda.value_object import primary_key_attribute, attribute

class FlakeCreated(Event):
    """
    Represents the event when a Nix flake for a Python package has been created.

    Class name: FlakeCreated

    Responsibilities:
        - Represent the event when a Nix flake for a Python package has been created.

    Collaborators:
        - None
    """
    def __init__(self, packageName: str, packageVersion: str, flakeFolder: str):
        """
        Creates a new FlakeCreated instance.
        :param packageName: The name of the package.
        :type packageName: str
        :param packageVersion: The version of the package.
        :type packageVersion: str
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        super().__init__()
        self._package_name = packageName
        self._package_version = packageVersion
        self._flake_folder = flakeFolder

    @property
    @primary_key_attribute
    def package_name(self):
        """
        Retrieves the name of the package.
        :return: The name of the package.
        :rtype: str
        """
        return self._package_name

    @property
    @primary_key_attribute
    def package_version(self):
        """
        Retrieves the version of the package.
        :return: The version of the package.
        :rtype: str
        """
        return self._package_version

    @property
    @attribute
    def flake_folder(self):
        """
        Retrieves the flake folder.
        :return: The flake folder.
        :rtype: str
        """
        return self._flake_folder
