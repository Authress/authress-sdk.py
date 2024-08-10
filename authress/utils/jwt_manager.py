import base64
import json

class JwtManager:
    def decode(self, token):
        try:
            if token:
                # Extract the payload part of the JWT (the second part)
                payload = token.split('.')[1]
                # Decode the base64url-encoded payload
                decoded_bytes = base64.urlsafe_b64decode(self.pad_base64url(payload))
                # Convert the decoded bytes into a JSON object
                return json.loads(decoded_bytes.decode('utf-8'))
            return None
        except Exception:
            return None

    def pad_base64url(self, data):
        """Pads the base64url string with '=' to make its length a multiple of 4."""
        return data + '=' * (4 - len(data) % 4)