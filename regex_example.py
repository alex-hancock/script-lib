import re

def validateConsonanceUUID(consonance_uuid):
	# Return if consonance uuid only contains hex characters and "-" 
	uuid_pattern = re.compile("[a-f,A-F,0-9,-]+")
	return bool(uuid_pattern.match(consonance_uuid))
