Value MAC_ADDRESS (([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})
Value ADDRESS ((\d{1,3}\.){3}\d{1,3})
Value NAME ((\d{1,3}\.){3}\d{1,3})
Value INTERFACE (\S+)

Start
  ^MAC.+Flags.*$$ -> CAPTURE

CAPTURE
  ^${MAC_ADDRESS} +${ADDRESS} +${NAME} +${INTERFACE} -> Record

EOF