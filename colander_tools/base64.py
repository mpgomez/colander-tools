
from __future__ import absolute_import

import base64

from colander import SchemaType, null, Invalid, _


class AbstractEncodedBytes(SchemaType):
    encoder = None
    decoder = None

    def serialize(self, node, appstruct):
        if appstruct is null:
            return null

        if not isinstance(appstruct, str):
            raise Invalid(node, _("must be a byte string"))

        return self.encoder(appstruct)

    def deserialize(self, node, cstruct):
        if cstruct is null:
            return null

        if not isinstance(cstruct, basestring):
            raise Invalid(node, _("must be a string"))

        return self.decoder(cstruct)


class Base16Bytes(AbstractEncodedBytes):
    encoder = base64.b16encode
    decoder = base64.b16decode


class Base32Bytes(AbstractEncodedBytes):
    encoder = base64.b32encode
    decoder = base64.b32decode


class Base64Bytes(AbstractEncodedBytes):
    encoder = base64.standard_b64encode
    decoder = base64.standard_b64decode


class URLSafeBase64Bytes(AbstractEncodedBytes):
    encoder = base64.urlsafe_b64encode
    decoder = base64.urlsafe_b64decode
