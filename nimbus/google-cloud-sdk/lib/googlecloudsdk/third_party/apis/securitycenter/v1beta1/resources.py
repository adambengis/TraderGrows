# -*- coding: utf-8 -*- #
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://securitycenter.googleapis.com/v1beta1/'
DOCS_URL = 'https://console.cloud.google.com/apis/api/securitycenter.googleapis.com/overview'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  ORGANIZATIONS = (
      'organizations',
      'organizations/{organizationsId}',
      {},
      [u'organizationsId'],
      True
  )
  ORGANIZATIONS_ASSETS = (
      'organizations.assets',
      'organizations/{organizationsId}/assets/{assetsId}',
      {},
      [u'organizationsId', u'assetsId'],
      True
  )
  ORGANIZATIONS_OPERATIONS = (
      'organizations.operations',
      '{+name}',
      {
          '':
              'organizations/{organizationsId}/operations/{operationsId}',
      },
      [u'name'],
      True
  )
  ORGANIZATIONS_SOURCES = (
      'organizations.sources',
      '{+name}',
      {
          '':
              'organizations/{organizationsId}/sources/{sourcesId}',
      },
      [u'name'],
      True
  )
  ORGANIZATIONS_SOURCES_FINDINGS = (
      'organizations.sources.findings',
      'organizations/{organizationsId}/sources/{sourcesId}/findings/'
      '{findingId}',
      {},
      [u'organizationsId', u'sourcesId', u'findingId'],
      True
  )

  def __init__(self, collection_name, path, flat_paths, params,
               enable_uri_parsing):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
    self.enable_uri_parsing = enable_uri_parsing
